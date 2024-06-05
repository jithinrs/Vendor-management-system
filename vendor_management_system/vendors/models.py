from django.db import models
import random, string
from datetime import datetime

def generate_vendor_code():
    while True:
        all_chars = string.ascii_uppercase + string.digits
        vendor_code = ''.join(random.choices(all_chars,k=6))
        return vendor_code


class Vendor(models.Model):
    name = models.CharField(max_length=255)
    contact_details = models.TextField()
    address = models.TextField()
    vendor_code = models.CharField(max_length=50, unique=True, blank=True, default=generate_vendor_code)
    on_time_delivery_rate = models.FloatField(default=0.0)
    quality_rating_avg = models.FloatField(default=0.0)
    average_response_time = models.FloatField(default=0.0)
    fulfillment_rate = models.FloatField(default=0.0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True) 

    def __str__(self):
        return self.name


def generate_po_number():
    while True:
        all_chars = string.ascii_uppercase + string.digits
        vendor_code = ''.join(random.choices(all_chars,k=10))
        return vendor_code



class PurchaseOrder(models.Model):
    STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('completed', 'Completed'),
        ('canceled', 'Canceled'),
    )
    po_number = models.CharField(max_length=50, unique=True, blank=True, default=generate_po_number)
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    order_date = models.DateTimeField(auto_now_add=True)
    delivery_date = models.DateTimeField(blank=True, null=True)
    delivered_date = models.DateTimeField(blank=True, null=True)
    items = models.JSONField()
    quantity = models.PositiveIntegerField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    quality_rating = models.FloatField(blank=True, null=True)
    issue_date = models.DateTimeField(blank=True, null=True)
    acknowledgment_date = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"PO #{self.po_number} - {self.vendor.name}"

    def save(self, *args, **kwargs):
        if self.pk:
            existing_status = PurchaseOrder.objects.filter(pk=self.pk).first()
            if existing_status:
                if existing_status.status != 'completed' and self.status == 'completed':
                    print('time updated')
                    self.delivered_date = datetime.now()
        super().save(*args, **kwargs)


class HistoricalVendorPerformance(models.Model):
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    on_time_delivery_rate = models.FloatField(default=0.00)
    quality_rating_avg = models.FloatField(default=0.00)
    average_response_time = models.FloatField(default=0.00)
    fulfillment_rate = models.FloatField(default=0.00)


    def __str__(self):
        return self.vendor.name