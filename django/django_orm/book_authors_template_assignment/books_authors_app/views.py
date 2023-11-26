from django.shortcuts import render, redirect
from .models import *

def add_book(request):
    context = {
        "all_books" : Book.objects.all()
    }
    return render(request, 'add_book.html', context)


def add_this_book(request):
    Book.objects.create(
        title = request.POST['title'],
        desc = request.POST['desc'],
    )
    return redirect('/')

def display_books(request, number):
    author_without_book = []            #bonus display only authors with no associated books
    for j in Author.objects.all():
        if j.books.all():
            pass
        else: author_without_book.append(j)
        
    context = {
        "book_from_main" : Book.objects.get(id=int(number)),
        'Athors_for_this_book' : Book.objects.get(id=int(number)).authors.all(),
        'all_authors' : author_without_book,
    }
    return render(request, 'display_books.html', context)


def add_author_to_this_book(request):
    x = Book.objects.get(id=request.POST['book_id'])
    x.authors.add(Author.objects.get(id=request.POST['author']))
    return redirect('/')    

def add_this_author(request):
    context = {
        "all_authors" : Author.objects.all()
    }
    return render(request, 'add_author.html', context)


def add_author_object(request):
    Author.objects.create(first_name = request.POST['first_name'],
                        last_name = request.POST['last_name'],
                        note = request.POST['note'],
)
    return redirect('/add_this_author')

def display_author(request, number):
    context = {
        "author_from_main" : Author.objects.get(id=int(number)),
        'books_for_this_author' : Author.objects.get(id=int(number)).books.all(),
        'all_books' : Book.objects.all(),
    }
    return render(request, 'display_author.html', context)


def add_book_to_this_author(request):
    y = Author.objects.get(id=request.POST['author_id'])
    y.books.add(Book.objects.get(id = request.POST['author']))
    return redirect('/add_this_author')