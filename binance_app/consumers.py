import json
import asyncio
import websockets
from channels.generic.websocket import AsyncWebsocketConsumer
from django.utils.timezone import now
from asgiref.sync import sync_to_async
from .models import Price

class BinanceConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()
        self.pairs = ["btcusdt", "ethusdt", "ltcusdt", "bnbusdt"]
        self.binance_ws_task = asyncio.create_task(self.fetch_binance_data())

    async def disconnect(self, close_code):
        if hasattr(self, 'binance_ws_task'):
            self.binance_ws_task.cancel()

    async def fetch_binance_data(self):
        """Подключается к Binance WebSocket API и получает данные для всех пар"""
        url = f"wss://stream.binance.com:9443/stream?streams={'/'.join([f'{pair}@trade' for pair in self.pairs])}"
        async with websockets.connect(url) as ws:
            while True:
                try:
                    message = await ws.recv()
                    data = json.loads(message)
                    stream = data.get("stream")

                    if stream:
                        symbol = stream.split("@")[0].upper()
                        price = data["data"]["p"]
                        print(f"🟢 Получена цена: {symbol} - {price}")

                        await self.save_price(symbol, price)

                        await self.send(text_data=json.dumps({"symbol": symbol, "price": price}))

                except Exception as e:
                    print(f"🔴 Ошибка WebSocket Binance: {e}")
                    break

    async def save_price(self, symbol, price):
        """Асинхронно сохраняет цену в БД"""
        await sync_to_async(Price.objects.create)(symbol=symbol, price=price, timestamp=now())
