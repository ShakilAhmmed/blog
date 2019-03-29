from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('post_details/<int:post_id>', views.post_details, name="post_details")
]
