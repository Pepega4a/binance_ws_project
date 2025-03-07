import pytest
from django.urls import reverse
from rest_framework.test import APIClient
from binance_app.models import Price

@pytest.mark.django_db
def test_price_list():
    """Проверяем, что API возвращает сохранённые данные"""
    Price.objects.create(symbol="BTCUSDT", price=50000.0)
    Price.objects.create(symbol="ETHUSDT", price=3500.0)

    client = APIClient()
    response = client.get(reverse('price-list'))
    
    assert response.status_code == 200
    assert len(response.data) == 2

@pytest.mark.django_db
def test_price_list_filter():
    """Проверяем фильтр по символу"""
    Price.objects.create(symbol="BTCUSDT", price=50000.0)
    Price.objects.create(symbol="ETHUSDT", price=3500.0)

    client = APIClient()
    response = client.get(reverse('price-list') + "?symbol=BTCUSDT")
    
    assert response.status_code == 200
    assert len(response.data) == 1
    assert response.data[0]['symbol'] == "BTCUSDT"
