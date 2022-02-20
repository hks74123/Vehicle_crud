import json
from unicodedata import name
from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import sync_to_async
from channels.exceptions import StopConsumer
import datetime
from datetime import timezone
from hks.models import vehicle
from channels.db import database_sync_to_async
from asgiref.sync import async_to_sync

class NotificationConsumer(WebsocketConsumer):
    def connect(self):
        self.group_name = str('hks')  # Setting the group name as the pk of the user primary key as it is unique to each user. The group name is used to communicate with the user.
        async_to_sync(self.channel_layer.group_add)(self.group_name, self.channel_name)
        self.accept()
        channel_layer = self.channel_layer
        data = "notification"+ "...." + str("Working is here...")
        # Trigger message sent to group
        async_to_sync(channel_layer.group_send)(
            str('hks'),      
            {
                "type": "notify",   
                "text": data,
            },
        )  

    def disconnect(self, close_code):
        self.close()
         
    def notify(self, event):
        self.send(text_data=json.dumps(event["text"]))