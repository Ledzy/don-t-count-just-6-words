from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.db import models

User = get_user_model()

class ChatRoom(models.Model):
    room_name = models.TextField(max_length=20,primary_key=True)
    room_type = models.TextField(max_length=20,null=True)
    create_date = models.DateTimeField(auto_now_add=True)
    member_count = models.IntegerField()
    members = models.ManyToManyField(User,related_name="in_room",null=True)

    def __str__(self):
        return self.room_name
    
    def newest_rooms(count):
        return ChatRoom.objects.order_by('-create_date').all()[:count]

    def hotest_rooms(count):
        return ChatRoom.objects.order_by('member_count').all()[:count]


class Message(models.Model):
    author = models.ForeignKey(User, related_name='author_messages', on_delete=models.CASCADE, default="Jonery")
    sender = models.TextField(default="Jonery")
    receiver = models.TextField(default="luoqijun")
    chat_room = models.ForeignKey(ChatRoom,on_delete=models.CASCADE,related_name="room_messages")
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.author.username

    def last_10_messages():
        # messages = Message.objects.filter(author=user)
        # messages = messages.order_by('-timestamp').all()[:10]
        # return messages
        return Message.objects.order_by('-timestamp').all()[:10]
        


class UserExtension(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,related_name="extension",parent_link=True,primary_key=True)
    rooms = models.ManyToManyField(ChatRoom,related_name="group_member",null=True)
    register_date = models.DateTimeField(auto_now_add=True)
    last_active = models.DateTimeField(auto_now=True)
    portrait = models.ImageField(null=True)


@receiver(post_save,sender=User)
def handler_user_extension(sender,instance,created,**kwargs):
    if created:
        # UserExtension.objects.create(user=instance)
        pass
    else:
        print('not created')
        instance.extension.save()
