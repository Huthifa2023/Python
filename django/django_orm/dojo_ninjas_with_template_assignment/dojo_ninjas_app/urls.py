from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('add_dojo', views.add_dojo),
    path('add_ninja', views.add_ninja),
    path('delete_dojo/<dojo_id>', views.delete_dojo_with_ninjas),
    path('delete_ninja/<ninja_id>', views.delete_ninja),
]