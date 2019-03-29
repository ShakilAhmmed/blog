from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('login', views.login, name="login"),
    path('post_list', views.post_list, name="post_list"),
    path('update_post/<int:post_id>', views.update_post, name="update_post"),
    path('create_post', views.create_post, name="create_post"),
    path('settings', views.settings, name="settings")
]
