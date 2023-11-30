from django.urls import path
from . import views



urlpatterns = [
    path('', views.render_login),


    path('add_user', views.add_user),


    path('login_request', views.login_request),


]