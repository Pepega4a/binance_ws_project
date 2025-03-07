from django.apps import AppConfig
import os


class BinanceAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'binance_app'
    path = os.path.dirname(os.path.abspath(__file__))
