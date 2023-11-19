from django.shortcuts import render, redirect

def main_func(request):
    return render(request, 'main.html')

def receive_data(request):
    request.session['name'] = request.POST['name']
    request.session['location'] = request.POST['location']
    request.session['language'] = request.POST['language']
    request.session['comment'] = request.POST['comment']
    
    return redirect ('/show')


def results(request):
    return render(request, 'show.html')
