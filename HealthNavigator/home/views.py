from django.shortcuts import render,HttpResponse,redirect
from datetime import datetime
from home.models import Contact
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.models import User


# Create your views here.
def index(request):
    #messages.success(request,"This is the test message")
    # if request.user.is_anonymous:
    #     return redirect("/")
    return render(request,'index.html')
    # return HttpResponse("This is the Home Page")

def about(request):
    return render(request,'about.html')

def services(request):
  return HttpResponse("This is the Services Page")

def contact(request):
    if request.method=="POST":
        email=request.POST.get('email')
        contact=request.POST.get('contact')
        address=request.POST.get('address')
        queries=request.POST.get('queries')
        contact=Contact(email=email,contact=contact,address=address,queries=queries)#,date=datetime.today())
        contact.save()
        messages.success(request, "Thanks for Uploading the form")

    # return HttpResponse("This is the Contact Page")
    return render(request,'contact.html')

def consult(request):
    return render(request,'consult.html')

def check(request):
    return render(request,'check.html')

def Usersignup(request):
    if request.method=="POST":
        username=request.POST["username"]
        password=request.POST["password"]
        password=request.POST["password"]
        user = User.objects.create_user(username=username,password=password) 
        user.save()
        messages.success(request,"Account created successfully")
        return redirect("/")
    else:
            # No backend authenticated the credentials
            return HttpResponse("Not Found")

    #return render(request,'login.html')

def Userlogin(request):
    if request.method=="POST":
        username=request.POST["username"]
        password=request.POST["password"]

        user_name=authenticate(username=username,password=password)
        print(user_name)
        if user_name is not None:
            login(request,user_name)
            messages.success(request,"Logged In successfully")
            return redirect("/")
        else:
            messages.error(request,"Wrong email/password")
            return redirect("/")

    return HttpResponse("Userlogin")

def Userlogout(request):
    logout(request)
    messages.success(request,"Logged Out")
    return redirect("/")

    #return HttpResponse("Userlogout")
