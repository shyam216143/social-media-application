from django.urls import path
from .consumers import ChatConsumer, MySyncConsumer


websocket_urlpatterns=[
    path('ws/sc/', MySyncConsumer.as_asgi()),
    path('ws/as/', ChatConsumer.as_asgi())
]
