from django.urls import path
from . import views

urlpatterns = [
    path('dashboard', views.dashboard),   #default route to main page, only if there is a logged in user(if not redirect to login page)


    path('', views.login),     #render login and registration page


    path('add_user', views.add_user),   #POST request to add new user


    path('login_request', views.login_request),   #POST request to login , success will redirect to main page


    path('logout', views.logout),   #logout anchor request, clear the session redirct to login page

    path('sightings/new', views.sightings_new),

    path('report_new_sight', views.report_new_sight),


    path('sightings/<id>', views.details),  #details page

    path('sightings/edit/<id>', views.edit),    #edit_page

    path('edit_sight', views.edit_request),  #edit request

    path('delete_sight/<id>', views.delete_sight),

    path('add_skeptics/<sight_id>/<user_id>', views.add_skeptics),

    path('remove_skeptics/<sight_id>/<user_id>', views.remove_skeptics),
]