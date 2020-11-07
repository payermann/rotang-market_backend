import json
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async
from .models import Dialog
from django.db.models import F


class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_%s' % self.room_name

        # Join room group
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    # Receive message from WebSocket
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        if message == 'get-room-messages':
            room_messages = await database_sync_to_async(self.get_messages)()
            await self.send(text_data=json.dumps({
                'message': room_messages
            }))
        else:
            room_messages = await self.save_messages(message)
            # await self.send(text_data=json.dumps({
            #     'message': room_messages
            # }))
        # Send message to room group
            await self.channel_layer.group_send(
                self.room_group_name,
                {
                    'type': 'chat_message',
                    'message': message
                }
            )

    def get_messages(self):
        try:
            # if room exists get messages
            room = Dialog.objects.get(dialogmans=self.room_name)
            # data = serializers.serialize("json", room.message)
            return room.message
        except:
            # room doesnt exist, create room
            newDialog = Dialog(dialogmans=self.room_name, message='')
            newDialog.save()
            return ''

    @database_sync_to_async
    def save_messages(self, message):
        try:
            # if room exists get messages
            temp = Dialog.objects.get(dialogmans=self.room_name)
            tempmessage = '\n' + message
            temp.message += tempmessage
            temp.save()
            # data = serializers.serialize("json", room.message)
            return message
        except:
            # room doesnt exist, create room
            newDialog = Dialog(dialogmans=self.room_name, message=message)
            newDialog.save()
            # return message
    # Receive message from room group

    async def chat_message(self, event):
        message = event['message']

        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'message': message
        }))
