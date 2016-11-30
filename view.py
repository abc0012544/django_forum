from django.http import HttpResponse
from django.shortcuts import render
from message.models import Message
from block.models import Block


def index(request):
    name = request.user
    block_infos=Block.objects.filter(status=0).order_by("-id")
    msg_num = Message.objects.filter(owner=name,status=0).count()
    return render(request, "index.html", {"blocks":block_infos,"msg_num":msg_num})

# def index2(request):
#     return render(request, "index.html")

def fb(request):
    return render(request, "create_comment.html")

def home(request):
    return HttpResponse("home")



