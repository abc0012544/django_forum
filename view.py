from django.http import HttpResponse
from django.shortcuts import render
from block.models import Block

def index(request):
    block_infos=Block.objects.filter(status=0).order_by("-id")

    return render(request, "index3.html",{"blocks":block_infos})

def index2(request):
    return render(request, "index2.html")

def fb(request):
    return HttpResponse("Fb")

def home(request):
    return HttpResponse("home")