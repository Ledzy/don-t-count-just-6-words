from django.urls import path
from .views import assignment_home

urlpatterns = [
    path('',assignment_home)
    ]