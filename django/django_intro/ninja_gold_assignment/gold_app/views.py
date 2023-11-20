from django.shortcuts import render, redirect
import random
import datetime

def main(request):
    if 'user_balance' not in request.session:
        request.session['user_balance'] = 0
        request.session['log'] = []
    
    return render(request, 'main.html')

def what_to_do(request):
    amount = random.randint(10, 20)
    request.session['user_balance'] += amount
    log_statment = (f'user gained {amount} golds, ({datetime.datetime.now()})')
    request.session['log'].append(log_statment) 
    request.session.save() 
    return redirect('/')


def gambling(request):
    if random.randint(0,1) == 1:
        amount = random.randint(0, 50)
        request.session['user_balance'] -= amount
        log_statment = (f'user lost {amount} golds, ({datetime.datetime.now()})')
        request.session['log'].append(log_statment)
        request.session.save() 
    else: 
        amount = random.randint(0, 50)
        request.session['user_balance'] += amount
        log_statment = (f'user gained {amount} golds, ({datetime.datetime.now()})')
        request.session['log'].append(log_statment)
        request.session.save()
    return redirect('/')

def reset(request):
    request.session.flush()
    return redirect('/')

# in this assignment they want us to use forms (with hidden inputs, in order to specify location with it)
# and then use input in url instead of hidden inputs