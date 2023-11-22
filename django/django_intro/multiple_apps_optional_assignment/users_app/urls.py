from django.urls import path
from . import views

from blog_app.views import index       # to solve optional root route utilize the same method as the /blogs route

urlpatterns = [
    path('', index),                    #invoke index method located in blogs_app in views
    path('register', views.register),
    path('login', views.login),
    path('users/new', views.register),
    path('users', views.users),
]