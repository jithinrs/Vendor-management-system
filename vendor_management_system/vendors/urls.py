from django.urls import path, include
from rest_framework import routers

from .views import VendorViews, PurchaseOrderViews,VendorPerformanceViews,UpdateAcknowledgementViews

router = routers.DefaultRouter()
router.register('vendors', VendorViews)
router.register('purchase_orders', PurchaseOrderViews)

urlpatterns = [
    path('', include(router.urls)),
    path('vendors/<int:id>/performance', VendorPerformanceViews.as_view()),
    path('purchase_orders/<str:po_id>/acknowledge', UpdateAcknowledgementViews.as_view())
]