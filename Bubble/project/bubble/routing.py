from django.urls import re_path
from .consumers import Myconsumer

websocket_urlpatterns = [
    re_path(r'ws/Chatroom/(?P<pk>\d+)/$', Myconsumer.as_asgi()),
]

