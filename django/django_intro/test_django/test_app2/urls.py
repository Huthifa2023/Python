from django.urls import path     
from . import views
urlpatterns = [
    path('app2_route1', views.serve1),	   
    path('app2_route2', views.serve2),	   
    path('redirect', views.redirect_function),	   
]