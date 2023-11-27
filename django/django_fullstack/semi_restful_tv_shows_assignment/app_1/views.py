from django.shortcuts import render, redirect
from .models import *

def new(request):
    return render(request, 'new.html')


def create(request):
    created_object = Show.objects.create(
        title = request.POST['title'],
        network = request.POST['network'],
        date = request.POST['date'],
        desc = request.POST['desc'],
    )
    id = created_object.id
    return redirect(f'/shows/{id}')



def showTV(request, id):                    #render current show details
    x = Show.objects.get(id=id)
    context = {
        'id' : x.id,
        'title' : x.title,
        'network' : x.network,
        'date' : x.date,
        'desc' : x.desc,
        'updated_at' : x.updated_at
    }
    return render(request, 'showTV.html', context)


def shows(request):                             #render main page
    all_shows = Show.objects.all()
    context={
        'all_shows' : all_shows
    }
    return render(request, 'shows.html', context)


def edit_show(request, id):
    y = Show.objects.get(id=id)
    correct_date_format = str(y.date)
    print(correct_date_format)
    context = {
        "show" : y,
        'date_as_string' : correct_date_format     
    }
    return render(request, 'edit.html', context)



def update_show(request):
    k = Show.objects.get(id= request.POST['id'])
    k.title = request.POST['title']
    k.network = request.POST['network']
    k.date = request.POST['date']
    k.desc = request.POST['desc']
    k.save()
    print(type(k.date))
    return redirect(f'/shows/{k.id}')



def delete_show(request, id):
    d = Show.objects.get(id=id)
    d.delete()
    return redirect('/shows')