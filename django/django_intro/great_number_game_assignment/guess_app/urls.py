from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_page),
    path('send_num', views.take_it),
    path('reset', views.reset),
]