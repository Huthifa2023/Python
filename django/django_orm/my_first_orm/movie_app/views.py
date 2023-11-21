from django.shortcuts import render

from .models import Movie


def index(request):
    context = {
    "all_the_movies": Movie.objects.all()
    }
    return render(request, "index.html", context)