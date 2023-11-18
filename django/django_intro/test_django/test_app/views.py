from django.shortcuts import render, HttpResponse
def serve1(request):
    return HttpResponse("this is test_app first route")

def serve2(request):
    return HttpResponse("this is test_app second route")

def print_value(request, value):
    return HttpResponse(f"this value {value} is generated from route parameter")