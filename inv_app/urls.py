from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import InvoiceViewSet, InvoiceDetailViewSet

router = DefaultRouter()
router.register(r'invoices', InvoiceViewSet, basename='invoice')
router.register(r'invoicedetails', InvoiceDetailViewSet, basename='invoicedetail')

urlpatterns = [
    path('', include(router.urls)),
]
