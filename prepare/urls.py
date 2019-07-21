from django.urls import path
from .views import prepare_home

urlpatterns = [
    path('',prepare_home)
    ]