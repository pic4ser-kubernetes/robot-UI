from django.urls import path

from . import consumers

websocket_urlpatterns = [
    path('controller/', consumers.ControllerConsumer.as_asgi()),
    path('controller', consumers.ControllerConsumer.as_asgi()),
    path('robot/', consumers.RobotConsumer.as_asgi()),
    path('robot', consumers.RobotConsumer.as_asgi()),
]
