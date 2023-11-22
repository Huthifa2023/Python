from django.urls import path
from . import views

urlpatterns = [
    path('register', views.register),
    path('login', views.login),
    path('users/new', views.register),
    path('users', views.users),
]