import json
from channels.generic.websocket import WebsocketConsumer
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async
from .models import Chatroom, Messages
from django.utils import timezone
from django.utils.dateformat import format as django_format
from django.utils.timezone import localtime


class Myconsumer(AsyncWebsocketConsumer):
   
   async def connect(self):
       
        self.user = self.scope ['user']
        self.room_pk = self.scope ['url_route']['kwargs']['pk']
        self.room_channel_name = f'Chatroom_{self.room_pk}'
        print(f'connecterd to {self.room_channel_name}')

        await self.channel_layer.group_add(
            self.room_channel_name,
            self.channel_name
        )
        
        await self.accept()


   async def receive(self, text_data):
        user = self.scope["user"].username
        text_data_json = json.loads(text_data)
        message = text_data_json["message"]
        timestamp = timezone.now()
        timestamp_before_format = localtime(timestamp)
        timestamp_format = django_format(timestamp_before_format, "F j, Y, P")


        print('message:', message,
              'user:', user,
              'timestamp:', timestamp)
        
        room = await database_sync_to_async(Chatroom.objects.get)(pk = self.room_pk)
        Chatroom_content = Messages(
          content = message,
          user= self.scope["user"],
          chat_room = room,
          create_dt = timestamp)
        
        await database_sync_to_async(Chatroom_content.save)()
        
        await self.channel_layer.group_send(
            self.room_channel_name,
            {'type': 'send_message',
            'message': message,
            'user': user,
            'timestamp': timestamp_format})
        
   async def send_message(self, event):
             
        message = event["message"]
        user = event["user"]
        timestamp = event["timestamp"]

        print(f'message sent: {message}')

        await self.send(text_data= json.dumps({
             'user':  user,
             'timestamp': f'Time: {timestamp}',
             'type': 'chat_message',
             'message': f' {user}: {message}'
        }))
    
   async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
             self.room_channel_name, 
             self.channel_name)    
