from django.urls import path
from . import views

urlpatterns = [
    # http://localhost:8000/group_work
    path('', views.post_list, name='post_list'),
    path('<int:post_pk>', views.post_detail, name="post_detail"),
    path('type/<int:group_type_pk>', views.posts_with_type, name="posts_with_type"),
]