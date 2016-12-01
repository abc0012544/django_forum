from django.http import HttpResponse
from django.shortcuts import render
from message.models import Message
from block.models import Block
from django.contrib.auth.models import User


def index(request):
    block_infos = Block.objects.filter(status=0).order_by("-id")
    name = request.user
    owner=User.objects.filter(username=name)
    if owner:
        msg_num = Message.objects.filter(owner=owner,status=0).count()
    else:
        msg_num =0
    return render(request, "index.html", {"blocks":block_infos,"msg_num":msg_num})

# def index2(request):
#     return render(request, "index.html")

def fb(request):
    return render(request, "create_comment.html")

def home(request):
    return HttpResponse("home")



