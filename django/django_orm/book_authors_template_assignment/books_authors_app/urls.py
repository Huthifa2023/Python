from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.add_book),
    path('add_this_book', views.add_this_book),
    path('display_books/<number>', views.display_books),
    path('add_author_to_this_book', views.add_author_to_this_book),


    path('add_this_author', views.add_this_author),
    path('add_author_object', views.add_author_object),
    path('display_Authors/<number>', views.display_author),
    path('add_book_to_this_author', views.add_book_to_this_author),


]