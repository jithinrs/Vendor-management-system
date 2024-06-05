from django.db.models.signals import post_save
from django.dispatch import receiver
from datetime import datetime
from django.db.models import Avg, Sum, F

from .models import PurchaseOrder, HistoricalVendorPerformance, Vendor


@receiver(post_save, sender=PurchaseOrder)
def update_vendor_performance(sender, instance, **kwargs):
    vendor_performance,created = HistoricalVendorPerformance.objects.get_or_create(vendor=instance.vendor)
    if not vendor_performance:
        return
    vendor_data = Vendor.objects.filter(id=instance.vendor.id).first()
    if instance.status == 'completed':
        vendor_performance.on_time_delivery_rate = get_on_time_delivery_rate(instance)
        vendor_data.on_time_delivery_rate = vendor_performance.on_time_delivery_rate
        vendor_performance.quality_rating_avg = get_quality_rating_avg(instance)
        vendor_data.quality_rating_avg = vendor_performance.quality_rating_avg

    elif instance.status == 'pending' and instance.acknowledgment_date:
        vendor_performance.average_response_time = get_average_response_time(instance)
        vendor_data.average_response_time = vendor_performance.average_response_time

    vendor_performance.fulfillment_rate = get_fulfillment_rate(instance)
    vendor_data.fulfillment_rate = vendor_performance.fulfillment_rate
    vendor_data.save()
    vendor_performance.save()


def get_on_time_delivery_rate(instance):
    completed_po = PurchaseOrder.objects.filter(vendor=instance.vendor, status='completed').count()
    completed_po_ontime = PurchaseOrder.objects.filter(vendor=instance.vendor, status='completed',delivered_date__lte=instance.delivery_date).count()
    delivery_rate = (completed_po_ontime/completed_po) * 100 if completed_po > 0 else 0.00
    return delivery_rate

def get_quality_rating_avg(instance):
    avg_quality_rating = PurchaseOrder.objects.filter(vendor=instance.vendor, status='completed').aggregate(Avg('quality_rating'))['quality_rating__avg'] or 0.0
    return avg_quality_rating

def get_average_response_time(instance):
    total_response_time = PurchaseOrder.objects.filter(vendor=instance.vendor, acknowledgment_date__isnull=False).\
        annotate(response_time=F('acknowledgment_date') - F('issue_date')).aggregate(total_response_time=Sum('response_time'))['total_response_time'] or 0
    total_acknowledged_pos = PurchaseOrder.objects.filter(vendor=instance.vendor, acknowledgment_date__isnull=False).count()
    average_response_time = (total_response_time / total_acknowledged_pos).total_seconds() / 3600 if total_acknowledged_pos > 0 else 0.0
    return average_response_time


def get_fulfillment_rate(instance):
    total_pos = PurchaseOrder.objects.filter(vendor=instance.vendor).count()
    fulfilled_pos = PurchaseOrder.objects.filter(vendor=instance.vendor, status='completed').count()
    fulfillment_rate = (fulfilled_pos / total_pos) * 100 if total_pos > 0 else 0.0
    return fulfillment_rate