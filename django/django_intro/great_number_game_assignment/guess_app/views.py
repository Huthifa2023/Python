from django.shortcuts import render, redirect
import random

def main_page(request):
    if 'random_number' not in request.session:
        request.session['random_number'] = int(random.random()*100)
        request.session['attempts'] = 0
    return render (request, 'index.html')


def take_it(request):
    gussed_number = int(request.POST['num_from_user'])
    if gussed_number > request.session['random_number']:
        request.session['status'] = 'less'
    elif gussed_number < request.session['random_number']:
        request.session['status'] = 'more'
    else: request.session['status'] = 'stop'
    request.session['attempts'] += 1
    if request.session['attempts'] > 5:
        request.session['status'] = 'none'
    return redirect('/')


def reset(request):
    if 'status' in request.session:
        del request.session['status']
        del request.session['random_number']
        del request.session['attempts']
    return redirect('/')