from django.urls import path
from . import views

urlpatterns = [
    path('', views.shows),      #render main page showing all TV shows in DB


    path('new', views.new),         #render a form to create new record
    path('create', views.create),   #post request to add new record     , redirect to main page

    path('<int:id>', views.showTV),     #render the show for indivadual 

    path('<int:id>/edit', views.edit_show), #render the edit page
    path('Update', views.update_show),      #post request to edit a record , reidrect to main page

    path('delete/<id>', views.delete_show), #redirect after delete record to main page

]