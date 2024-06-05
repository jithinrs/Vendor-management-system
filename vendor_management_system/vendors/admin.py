from django.contrib import admin
from .models import Vendor, PurchaseOrder, HistoricalVendorPerformance


admin.site.register(Vendor)
admin.site.register(PurchaseOrder)
admin.site.register(HistoricalVendorPerformance)