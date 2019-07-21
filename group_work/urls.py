from django.urls import path
from .views import group_work_home

urlpatterns = [
    path('',group_work_home)
    ]