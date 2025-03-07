# Binance WebSocket Django API

## Описание
Проект представляет собой Django-приложение с интеграцией WebSocket для получения данных о ценах криптовалют с Binance API.  
Данные сохраняются в PostgreSQL, а REST API предоставляет доступ к истории изменений.

## Технологии
- Django + Django Channels (WebSocket)
- PostgreSQL
- Docker + Docker Compose
- pytest (тестирование)

## Установка и запуск

### 1. Клонирование репозитория
```bash
git clone https://github.com/your-repo/binance_ws_project.git
cd binance_ws_project
```

### 2. Запуск проекта в Docker
```bash
docker-compose up --build
```

### 3. Проверка API
- Все сохранённые цены: [`http://127.0.0.1:8000/api/prices/`](http://127.0.0.1:8000/api/prices/)
- Фильтр по валютной паре BTC/USDT: [`http://127.0.0.1:8000/api/prices/?symbol=BTCUSDT`](http://127.0.0.1:8000/api/prices/?symbol=BTCUSDT)

### 4. Проверка WebSocket
Подключение к WebSocket:

```bash
wscat -c ws://127.0.0.1:8001/ws/binance/
```

Пример получаемых данных:
```
{"symbol": "BTCUSDT", "price": "63500.00"}
{"symbol": "ETHUSDT", "price": "3500.50"}
```

### 5. Запуск тестов
```bash
pytest
```

## Основные файлы
- `Dockerfile` – описание сборки контейнера
- `docker-compose.yml` – конфигурация сервисов
- `binance_app/consumers.py` – обработка WebSocket-соединений
- `binance_app/views.py` – реализация REST API
- `config/asgi.py` – конфигурация WebSocket маршрутов
