from django.urls import path
from .views import schedule_home

urlpatterns = [
    path('',schedule_home)
    ]