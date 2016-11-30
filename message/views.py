import smtplib
import uuid
from email.header import Header
from email.mime.text import MIMEText

from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render,redirect
from  user.forms import AricleForm
from .models import Message
import json


def message_info(request):
    name = request.user
    message = Message.objects.filter(owner=name, status=0)
    return render(request, "message.html", {"message": message})

def message_read(request):
    parm = {}
    parm["id"] = request.POST.get("toread_id")
    message=Message.objects.get(id=parm["id"])
    message.status=1
    parm["link"] = message.link
    message.save()
    return HttpResponse(json.dumps(parm))

def message_read1(request,message_id):
    message_id=message_id
    message=Message.objects.get(id=message_id)
    message.status=1
    link=message.link
    message.save()
    return redirect(link)