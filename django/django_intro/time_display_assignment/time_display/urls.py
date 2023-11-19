from django.urls import path
from . import views
urlpatterns = [
    path('', views.current_time),
    path('time_display', views.redirect_to_root),
]
