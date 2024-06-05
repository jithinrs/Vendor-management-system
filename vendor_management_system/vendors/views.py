from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
from datetime import datetime


from .serializers import VendorSerializer, PuchaseOrderSerializer, HistoricalVendorPerformanceSerializer
from .models import Vendor, PurchaseOrder, HistoricalVendorPerformance



class VendorViews(ModelViewSet):
    serializer_class = VendorSerializer
    queryset = Vendor.objects.all()

class PurchaseOrderViews(ModelViewSet):
    serializer_class = PuchaseOrderSerializer
    queryset = PurchaseOrder.objects.all()

class VendorPerformanceViews(APIView):
    permission_classes = [AllowAny]

    def get(self, request, id):
        vendor_metrics = HistoricalVendorPerformance.objects.filter(vendor=id).first()
        if vendor_metrics:
            serializer = HistoricalVendorPerformanceSerializer(vendor_metrics)
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        else:
            return Response('Vendor id is not found', status=status.HTTP_404_NOT_FOUND)

class UpdateAcknowledgementViews(APIView):
    permission_classes = [AllowAny]

    def put(self, request, po_id):
        purchase_order = PurchaseOrder.objects.filter(po_number=po_id).first()
        if purchase_order:
            purchase_order.acknowledgment_date = datetime.now()
            purchase_order.save()

            return Response('Purchase order acknowledged' , status=status.HTTP_200_OK)
        else:
            return Response('Purchase is not found' ,  status=status.HTTP_404_NOT_FOUND)