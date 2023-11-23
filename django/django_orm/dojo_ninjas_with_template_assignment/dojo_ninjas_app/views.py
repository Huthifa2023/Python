from django.shortcuts import render, redirect
from .models import Dojo,Ninja

def index(request):
    context={
        "dojos" : Dojo.objects.all()
    }
    return render(request, 'index.html', context)


def add_dojo(request):
    Dojo.objects.create(name=request.POST['dojo_name'], city=request.POST['city_name'], state=request.POST['state-code'])
    return redirect('/')


def add_ninja(request):
    Ninja.objects.create(dojo=Dojo.objects.get(id=request.POST['ninjas_dojo']),     #dojo= expected object , but you cannot get object directly from frontend cuz form returns only strings!!!
                        first_name=request.POST['ninja_first_name'],
                        last_name=request.POST['ninja_last_name'],
                        )
    return redirect('/')

def delete_dojo_with_ninjas(request, dojo_id):
    # Dojo.objects.get(id=dojo_id).ninjas.all().delete()    #remove dojo only, will remove all associated ninjas also? why?? cuz all ninjas have att. CASCADE on delete
    Dojo.objects.get(id=dojo_id).delete()
    return redirect('/')

def delete_ninja(request, ninja_id):
    Ninja.objects.get(id=ninja_id).delete()
    return redirect('/')