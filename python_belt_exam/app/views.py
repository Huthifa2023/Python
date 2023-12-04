from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages
import bcrypt


def dashboard(request):
    if 'id' in request.session:
        context = {
            'user' : User.objects.get(id= request.session['id']),
            'all_sightings' : Sight.objects.all().order_by('-date'),
        }
        return render(request, 'dashboard.html', context)
    else:
        return redirect('/')

def login(request):
    return render(request, 'login.html')

def add_user(request):
    errors = User.objects.validator(request.POST)
    if len(errors) > 0:
        for k , v in errors.items():
            messages.error(request, v)
        return redirect('/')
    else:
        User.objects.create(
            first_name = request.POST['first_name'],
            last_name = request.POST['last_name'],
            email = request.POST['email'],
            password = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt()).decode(),
        )
        messages.success(request, 'New user added successfully, please login!')
        return redirect('/')

def login_request(request):
    user = User.objects.filter(email = request.POST['email'])
    if user:
        user = user[0]
        if bcrypt.checkpw(request.POST['password'].encode(), user.password.encode()):
            request.session['id'] = user.id
            return redirect('/dashboard')
        else:
            messages.error(request, 'Wrong Email or Passowrd')
            return redirect('/')
    else:
        messages.error(request, 'Wrong Email or Passowrd')
        return redirect('/')

def logout(request):
    request.session.flush()
    return redirect('/')

###################################################################End login & Registration methods


def sightings_new(request):
    if 'id' in request.session:
        context = {
            'user' : User.objects.get(id= request.session['id']),
        }
        return render(request, 'new_sightings.html', context)
    else:
        return redirect('/')

def report_new_sight(request):
    errors = Sight.objects.validator(request.POST)
    request.session['hold_desc'] = request.POST['desc']
    if len(errors) > 0:
        for k , v in errors.items():
            messages.error(request, v)
        return redirect('/sightings/new')
    else:
        l = Sight.objects.create(
            location = request.POST['location'],
            date = request.POST['date'],
            number_sasquatches = request.POST['number_sasquatches'],
            desc = request.POST['desc'],
            user = User.objects.get(id=request.POST['current_user_id'])
        )
        l.save()
        l.skeptics.add(User.objects.get(id=request.POST['current_user_id']))
    return redirect('/dashboard')

def details(request, id):
    if 'id' in request.session:
        context = {
            'user' : User.objects.get(id= request.session['id']),
            'sight' : Sight.objects.get(id = id),
        }
        return render(request, 'details.html', context)
    else:
        return redirect('/')



def edit(request,id):
    if 'id' in request.session:
        if request.session['id'] == Sight.objects.get(id=id).user.id:
            context = {
                'user' : User.objects.get(id= request.session['id']),
                'sight' : Sight.objects.get(id = id),
                'sight_date' : str(Sight.objects.get(id=id).date),
            }
            return render(request, 'edit.html', context)
    else:
        return redirect('/')
    
def edit_request(request):
    errors = Sight.objects.validator(request.POST)
    if len(errors) > 0:
        for k , v in errors.items():
            messages.error(request, v)
        return redirect(f'/sightings/edit/{request.POST['current_sight_id']}')
    else:
        x = Sight.objects.get(id= request.POST['current_sight_id'])
        x.location = request.POST['location']
        x.date = request.POST['date']
        x.number_sasquatches = request.POST['number_sasquatches']
        x.desc = request.POST['desc']
        x.user = User.objects.get(id = request.POST['current_user_id'])
        x.save()
        return redirect(f'/sightings/{request.POST['current_sight_id']}')
    
def delete_sight(request, id):
    y = Sight.objects.get(id = id)
    y.delete()
    return redirect('/dashboard')


def add_skeptics(request, sight_id, user_id):
    Sight.objects.get(id = sight_id).skeptics.add(User.objects.get(id = user_id))
    return redirect(f'/sightings/{sight_id}')



def remove_skeptics(request, sight_id, user_id):
    Sight.objects.get(id = sight_id).skeptics.remove(User.objects.get(id = user_id))
    return redirect(f'/sightings/{sight_id}')
