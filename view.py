from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, "index.html")

def fb(request):
    return HttpResponse("Fb")

def home(request):
    return HttpResponse("home")