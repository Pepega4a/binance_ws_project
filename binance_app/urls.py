from django.urls import path
from .views import PriceListView

urlpatterns = [
    path('api/prices/', PriceListView.as_view(), name='price-list'),
]
