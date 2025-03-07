from rest_framework import generics
from django.db.models import F
from .models import Price
from .serializers import PriceSerializer

class PriceListView(generics.ListAPIView):
    """
    API для получения истории цен.
    Поддерживает параметр ?symbol=BTCUSDT для фильтрации по паре.
    """
    serializer_class = PriceSerializer

    def get_queryset(self):
        symbol = self.request.query_params.get('symbol', None)
        queryset = Price.objects.all().order_by(F('timestamp').desc())

        if symbol:
            queryset = queryset.filter(symbol=symbol.upper())

        return queryset
