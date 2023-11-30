from django.shortcuts import render, redirect
from .models import User
import bcrypt
from django.contrib import messages

def render_login(request):
    return render(request, 'login.html')



def add_user(request):
    encrypted_password = bcrypt.hashpw(request.POST['password'].encode() , bcrypt.gensalt()).decode()
    User.objects.create(
        email = request.POST['email'],
        password = encrypted_password,
        first_name = request.POST['first_name'],
        last_name = request.POST['last_name'],
    )
    return redirect('/login')


def login_request(request):
    user = User.objects.filter(email = request.POST['email'])
    if user:
        logged_user = user[0]
        if bcrypt.checkpw(request.POST['password'].encode(), logged_user.password.encode()):
            request.session['id'] = logged_user.id
            return redirect('/')
        else:
            # messages.error['wrong_passowrd'] = 'wrong email or password'
            return redirect('/login')
    else:
        # messages.error['wrong_email_or_user_not_exist'] = 'wrong email or password'
        return redirect('/login')
