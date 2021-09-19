from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.
from courses.models import Course

def index(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("users:login"))
        
    return render(request, "users/index.html")


def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(username=username, password=password)
        
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("users:index"))
        else:
            return render(request, "users/login.html", {
                "message": "Invalid credential."
            })
    
    return render(request, "users/login.html")


def logout_view(request):
    logout(request)
    
    return render(request, "users/login.html", {
        "message": "Logged out."
    })
    

def check_courses(request):
    return render(request, "courses/course.html")