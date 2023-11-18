from django.shortcuts import render, redirect
def index(request):
    return render(request,"index.html")

def create_user(request):
    # print("Got Post Info..............................................")
    # name_from_form = request.POST['name']
    # email_from_form = request.POST['email']
    # gender_from_form = request.POST['gender']
    # print(name_from_form)
    # print(email_from_form)
    
    context = {
        "name_on_template" : name_from_form,
        "email_on_template" : email_from_form,
        "me"                :   "ok another input coming",
        "gender"            :   gender_from_form
    }
    return redirect("/success")

def success(request):
    return render(request,"success.html")