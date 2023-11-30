from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.render_wall),

    path('log_off', views.log_off),

    path('post_message', views.post_message),


    path('comment', views.comment),


    path('remove_post/<id>', views.remove),

]
