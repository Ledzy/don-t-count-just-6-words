from django.contrib import admin
from .models import GroupType, Post

# Register your models here.
@admin.register(GroupType)
class GroupTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'type_name')

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'group_type', 'author', 'created_time', 'last_updated_time')