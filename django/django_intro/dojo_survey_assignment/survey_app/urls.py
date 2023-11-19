from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_func),
    path('send_data', views.receive_data),
    path('show', views.results),
]