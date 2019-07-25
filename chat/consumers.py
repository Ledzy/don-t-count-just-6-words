from django.contrib.auth import get_user_model
from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
import json
from .models import Message, ChatRoom, UserExtension

User = get_user_model()

class ChatConsumer(WebsocketConsumer):

    def fetch_rooms(self, data):
        user = User.objects.filter(username=data['from'])[0]
        user = UserExtension.objects.filter(user=user)[0]
        rooms = user.rooms.all()
        content = {
            'command': 'show_rooms',
            'messages': [{'room_name':room.room_name} for room in rooms]
        }
        self.send_message(content)

    def fetch_messages(self, data):
        room_name = data['room_name']
        room = ChatRoom.objects.filter(room_name=room_name)[0]
        messages = room.room_messages.all()
        content = {
            'command': 'messages',
            'messages': self.messages_to_json(messages)
        }
        print("send the message")
        self.send_message(content)

    def add_room(self,data):
        username = data['from']
        user = User.objects.filter(username=username)[0]
        user = UserExtension.objects.filter(user=user)[0]
        target_room = ChatRoom.objects.filter(room_name=data['room_name'])[0]
        user.rooms.add(target_room)
        self.fetch_messages(data)

        rooms = user.rooms.all()
        data['messages'] = [{'room_name':room.room_name} for room in rooms]
        self.fetch_rooms(data)

    def create_room(self,data):
        target_room = ChatRoom.objects.create(room_name=data['room_name'],room_type='A', member_count=2)
        self.add_room(data)

    def new_message(self, data):
        author = data['from']
        author_user = User.objects.filter(username=author)[0]
        room = ChatRoom.objects.filter(room_name=data['room_name'])[0]
        message = Message.objects.create(
            author=author_user, 
            content=data['message'],
            chat_room=room)
        content = {
            'command': 'new_message',
            'message': self.message_to_json(message)
        }
        return self.send_chat_message(content)

    def messages_to_json(self, messages):
        result = []
        for message in messages:
            result.append(self.message_to_json(message))
        return result

    def message_to_json(self, message):
        return {
            'author': message.author.username,
            'content': message.content,
            'timestamp': str(message.timestamp)
        }

    commands = {
        'fetch_messages': fetch_messages,
        'new_message': new_message,
        'fetch_rooms': fetch_rooms,
        'add_room': add_room,
        'create_room': create_room
    }

    def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_%s' % self.room_name
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )
        self.accept()

    def disconnect(self, close_code):
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name
        )

    def receive(self, text_data):
        data = json.loads(text_data)
        self.commands[data['command']](self, data)
        

    def send_chat_message(self, message):
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message
            }
        )

    def send_message(self, message):
        self.send(text_data=json.dumps(message))

    def chat_message(self, event):
        message = event['message']
        self.send(text_data=json.dumps(message))