from django.shortcuts import render, redirect
from time import gmtime, strftime


def current_time(request):
    time_now = strftime("%Y-%m-%d %H-%M-%p", gmtime())

    context = {
        "time" : time_now,
    }
    return render(request, 'index.html', context)


