from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return render(request, "hi/index.html")
    # return HttpResponse("Hi, world!")

def cory(request):
    return HttpResponse("Hello, Cory!")

def greet(request, name):
    return render(request, "hi/greet.html", {
        "name": name.capitalize()
    })
    # return HttpResponse(f"Hello, {name}!")
