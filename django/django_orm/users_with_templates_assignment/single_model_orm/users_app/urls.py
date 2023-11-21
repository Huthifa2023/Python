from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index),
    path('add_user_DB', views.create_user),
]