from django.urls import path
from . import consumers
websocket_urlpatterns=[
    path('ws/sc/notifications/',consumers.NotificationConsumer.as_asgi()),
]