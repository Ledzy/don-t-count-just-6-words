from django.urls import path
from .views import slide_home

urlpatterns = [
    path('',slide_home)
    ]