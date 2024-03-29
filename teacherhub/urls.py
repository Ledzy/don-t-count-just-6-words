"""teacherhub URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home_page, name='home'),
    path('admin/', admin.site.urls),
    path('schedule/', include('schedule.urls')),
    path('group_work/', include('group_work.urls')),
    path('prepare/', include('prepare.urls')),
    path('assignment/', include('assignment.urls')),
    path('chat/', include('chat.urls', namespace='chat')),
    path('login/',views.login_, name='login'),
    path('signup/',views.signup_, name='signup'),
    path('login-post', views.login_post),
    path('signup-post',views.signup_post)
]