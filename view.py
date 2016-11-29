from django.http import HttpResponse
from django.shortcuts import render

from block.models import Block


def index(request):
    block_infos=Block.objects.filter(status=0).order_by("-id")

    return render(request, "index.html", {"blocks":block_infos})

# def index2(request):
#     return render(request, "index.html")

def fb(request):
    return render(request, "create_comment.html")

def home(request):
    return HttpResponse("home")



