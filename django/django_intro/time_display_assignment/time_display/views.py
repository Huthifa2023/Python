from django.shortcuts import render, redirect
from time import gmtime, strftime
from datetime import datetime

def current_time(request):
    time_GMT = datetime.utcnow()
    time_GMT_2 = datetime.now()
    context = {
        "time_GMT" : time_GMT,
        "time_GMT_2" : time_GMT_2,
    }
    return render(request, 'index.html', context)


def redirect_to_root(requset):
    return redirect(requset, '/')