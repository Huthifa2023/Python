from django.shortcuts import render, redirect
from .models import User

def index(request):
    context={
        "user_table" : User.objects.all()       #this will return list of all objects (user records)
    }
    return render(request, 'index.html', context)

def create_user(request):

    age_value =  request.POST['age']  if request.POST['age'] else None
    User.objects.create(first_name=request.POST['first_name'],      #use CRUD OP to create user with att. comes from the POST method (form)
                        last_name=request.POST['last_name'],
                        email_address=request.POST['email_address'],
                        age=age_value
                        )
    
    return redirect('/')
