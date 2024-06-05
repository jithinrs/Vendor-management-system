from rest_framework.serializers import ModelSerializer

from .models import Vendor, PurchaseOrder, HistoricalVendorPerformance




class VendorSerializer(ModelSerializer):
  
  class Meta:
    model = Vendor
    fields = '__all__' 

class PuchaseOrderSerializer(ModelSerializer):
  
  class Meta:
    model = PurchaseOrder
    fields = '__all__'

class HistoricalVendorPerformanceSerializer(ModelSerializer):
  
  class Meta:
    model = HistoricalVendorPerformance
    fields = '__all__'