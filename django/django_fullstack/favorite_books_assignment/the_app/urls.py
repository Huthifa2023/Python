from django.urls import path
from . import views

urlpatterns = [
    path('books/', views.main),
    path('', views.main),

    path('login/', views.login),


    path('add_user/', views.add_user),

    path('login_request/', views.login_request),

    path('LogOut/', views.LogOut),

    path('add_book/', views.add_book),


    path('like_book/<book_id>/', views.like_book),

    path('view_book/<book_id>/', views.view_book),


    path('unlike_book/<book_id>/', views.unlike_book),


    path('update_desc/', views.update_desc),



    path('delete_book/<book_id>/', views.delete_book),
]