from django.shortcuts import render, redirect
from login_app.models import User
from .models import Message, Comment

def render_wall(request):
    if 'id' in request.session:
        user = User.objects.get(id = request.session['id'])
        messages = Message.objects.all()
        context = {
            'user' : user,
            'messages' : messages,
        }
        return render(request, 'wall.html', context)
    else:
        return redirect('/login')



def log_off(request):
    request.session.flush()
    return redirect('/login')


def post_message(request):
    Message.objects.create(
        message = request.POST['message'],
        user = User.objects.get(id=request.session['id']),
    )
    return redirect('/')


def comment(request):
    Comment.objects.create(
        user = User.objects.get(id = request.session['id']),
        message = Message.objects.get(id = request.POST['message_id']),
        comment = request.POST['comment'],
    )
    return redirect('/')


def remove(request, id):
    message = Message.objects.get(id = id)
    message.delete()
    return redirect('/')
