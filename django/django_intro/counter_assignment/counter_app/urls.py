from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('destroy', views.clear_func),
    path('add_2', views.add_2),
    path('add_num', views.add_num)
]
