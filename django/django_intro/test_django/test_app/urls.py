from django.urls import path     
from . import views
urlpatterns = [
    path('app1_route1/', views.serve1),	   
    path('app1_route2/', views.serve2),	   
    path('print/<int:value>/', views.print_value),	   
]