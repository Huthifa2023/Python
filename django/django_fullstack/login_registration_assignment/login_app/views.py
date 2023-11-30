from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages
import bcrypt
from datetime import date   

def index(request):
    return render(request, 'index.html')


def register(request):
    errors = User.objects.validator(request.POST)
    if len(errors) > 0:
        for k , v in errors.items():
            messages.error(request, v)
        return redirect('/')
    else:
        user = User.objects.create(
            first_name = request.POST['first_name'],
            last_name = request.POST['last_name'],
            email = request.POST['email'],
            password = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt()).decode(),
            birth_day = request.POST['birth_day'],
        )
        user.save()
        return redirect(f'/success')


def success(request):
    if 'id' in request.session:             #Don't allow a user who is not logged in to reach the /success route (i.e. by making a GET request in the address bar)
        user = User.objects.get(id =request.session['id'])
        request.session['first_name'] = user.first_name
        request.session['last_name'] = user.last_name
        request.session['email'] = user.email
        request.session['age'] = int(str(date.today())[0:4]) - int(str(user.birth_day)[0:4])
        return render(request, 'success.html')
    else:
        messages.error(request,'please sign in to show this profile ')
        return redirect('/')



def login(request):
    x = User.objects.filter(email = request.POST['email'])
    if x:
        logged_user = x[0]
        if bcrypt.checkpw(request.POST['password'].encode() , logged_user.password.encode()):
            request.session['id'] = logged_user.id     #Don't allow a user who is not logged in to reach the /success route (i.e. by making a GET request in the address bar)
            return redirect(f'/success')
        else:
            messages.error(request, 'wrong email or password!')
            return redirect('/')
    else:
        messages.error(request, 'wrong email or password!')
        return redirect('/')


def logout(request):
    request.session.flush()
    return redirect('/')