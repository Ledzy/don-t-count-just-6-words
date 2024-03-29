# Generated by Django 2.2.3 on 2019-07-24 14:15

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
        ('chat', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ChatRoom',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room_name', models.TextField(max_length=20)),
                ('room_type', models.TextField(max_length=20)),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('member_count', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='UserExtension',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, related_name='extension', serialize=False, to=settings.AUTH_USER_MODEL)),
                ('register_date', models.DateTimeField(auto_now_add=True)),
                ('last_active', models.DateTimeField(auto_now=True)),
                ('portait', models.ImageField(upload_to='')),
                ('rooms', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='group_member', to='chat.ChatRoom')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
