from django.shortcuts import render, HttpResponse, redirect
def serve1(request):
    return HttpResponse("this is test_app2 first route")

def serve2(request):
    return HttpResponse("this is test_app2 second route")

def redirect_function(request):
    return redirect("/test_app/app1_route1")


