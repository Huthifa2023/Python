from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages
import bcrypt


def main(request):
    if 'id' in request.session:
        user = User.objects.get(id = request.session['id'])
        context = {
            'user' : user,
            'all_books' : Book.objects.all(),
            'liked_books' : user.liked_books.all(),
        }
        return render(request, 'main.html', context)
    else:
        return redirect('/login/')


def login(request):
    return render(request, 'login.html')


def add_user(request):
    errors = User.objects.validator(request.POST)
    if len(errors) > 0:
        for k, v in errors.items():
            messages.error(request, v)
        return redirect('/login/')
    else:
        hashed_password = bcrypt.hashpw(request.POST['password'].encode() , bcrypt.gensalt()).decode()
        User.objects.create(
            first_name = request.POST['first_name'],
            last_name = request.POST['last_name'],
            email = request.POST['email'],
            password = hashed_password,
        )
        messages.success(request, 'User Added Succesfuly, sign in to see the books!')
        return redirect('/login/')
    


def login_request(request):
    user = User.objects.filter(email = request.POST['email'])
    if user:
        user = user[0]
        if bcrypt.checkpw(request.POST['password'].encode(), user.password.encode()):
            request.session['id'] = user.id
            return redirect('/books/')
        else:
            messages.error(request, 'wrong email or password')
            return redirect('/login/')
    else:
        messages.error(request, 'wrong email or password')
        return redirect('/login/')


def LogOut(request):
    request.session.flush()
    return redirect('/login/')


def add_book(request):
    errors = Book.objects.validator(request.POST)
    if len(errors) > 0:
        for k , v in errors:
            messages.error(request, v)
        return redirect('/books/')
    else:
        session_user = User.objects.get(id = request.session['id'])
        book = Book.objects.create(
            title = request.POST['title'],
            desc = request.POST['desc'],
            created_by = session_user,
        )
        book.save()
        session_user.liked_books.add(book)
        return redirect('/books/')
    

def like_book(request, book_id):
    session_user = User.objects.get(id = request.session['id'])
    session_user.liked_books.add(Book.objects.get(id = book_id))
    return redirect(f'/view_book/{book_id}/')


def unlike_book(request, book_id):
    session_user = User.objects.get(id = request.session['id'])
    session_user.liked_books.remove(Book.objects.get(id = book_id))
    return redirect(f'/view_book/{book_id}/')

def view_book(request, book_id):
    the_book = Book.objects.get(id = book_id)
    user = User.objects.get(id = request.session['id'])
    context = {
        'user' : user,
        'the_book' : the_book,

    }
    return render(request, 'view_book.html', context)

def update_desc(request):
    book = Book.objects.get(id=request.POST['book_id'])
    book.desc = request.POST['desc']
    book.save()
    return redirect(f'/view_book/{book.id}/')


def delete_book(request, book_id):
    book = Book.objects.get(id = book_id)
    book.delete()
    return redirect('/books/')