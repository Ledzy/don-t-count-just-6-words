# Generated by Django 2.2.3 on 2019-07-25 05:53

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('chat', '0007_auto_20190725_1236'),
    ]

    operations = [
        migrations.AddField(
            model_name='chatroom',
            name='members',
            field=models.ManyToManyField(null=True, related_name='in_room', to=settings.AUTH_USER_MODEL),
        ),
        migrations.RemoveField(
            model_name='userextension',
            name='rooms',
        ),
        migrations.AddField(
            model_name='userextension',
            name='rooms',
            field=models.ManyToManyField(null=True, related_name='group_member', to='chat.ChatRoom'),
        ),
    ]
