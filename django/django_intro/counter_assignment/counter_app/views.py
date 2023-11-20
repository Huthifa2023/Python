from django.shortcuts import render,redirect

def index(request):
    if 'counter' in request.session:
        request.session['counter'] +=1
    else:
        request.session['counter'] =1

    return render(request,'index.html')

def clear_func(request):
    del request.session['counter']
    return redirect('/')

def add_2(request):
    request.session['counter'] += 1
    return redirect('/')


def add_num(request):
    numnum = int(request.POST['num'])
    request.session['counter'] += numnum-1
    return redirect('/')