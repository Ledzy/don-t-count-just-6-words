from django.contrib import admin
from .models import ChatRoom, Message, UserExtension
# Register your models here.

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('sender','receiver','content','chat_room')

@admin.register(ChatRoom)
class ChatRoomAdmin(admin.ModelAdmin):
    list_display = ('room_name','room_type','member_count')

@admin.register(UserExtension)
class UserExtensionAdmin(admin.ModelAdmin):
    list_display = ('user','register_date')