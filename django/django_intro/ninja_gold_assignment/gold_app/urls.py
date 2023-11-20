from django.urls import path
from . import views

urlpatterns = [
    path('', views.main),
    path('process', views.what_to_do),
    path('gambling', views.gambling),
    path('reset', views.reset),
]