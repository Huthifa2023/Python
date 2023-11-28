from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages

def new(request):
    return render(request, 'new.html')


def create(request):                   #called by POST form, validations all is required(title>=2, network>=3, desc optional, date:must be before now)

    errors = Show.objects.validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)    #why request is needed in messages.error?????????
        return redirect('/shows/new')
    else:
        created_object = Show.objects.create(
            title = request.POST['title'],
            network = request.POST['network'],
            date = request.POST['date'],
            desc = request.POST['desc'],
        )
        # messages.success(request, "New movie added Succesfully updated")
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
    context = {
        "show" : y,
        'date_as_string' : correct_date_format     
    }
    return render(request, 'edit.html', context)



def update_show(request):
    errors = Show.objects.validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)    #why request is needed in messages.error?????????
        return redirect(f'/{request.POST['id']}/edit')
    else:
        k = Show.objects.get(id= request.POST['id'])
        k.title = request.POST['title']
        k.network = request.POST['network']
        k.date = request.POST['date']
        k.desc = request.POST['desc']
        k.save()
    return redirect(f'/shows/{k.id}')



def delete_show(request, id):
    d = Show.objects.get(id=id)
    d.delete()
    return redirect('/shows')