import smtplib
import uuid
from email.header import Header
from email.mime.text import MIMEText

from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render

from  user.forms import AricleForm
from .models import Active


def auth():
    pk=str(uuid.uuid4()).replace("-","")
    return pk


def register(request):
    if request.method=="GET":
        return render(request, "register.html")

    else:

        form=AricleForm(request.POST)

        if form.is_valid():
            reg=form.save(commit=False)
            reg.save()
            pk=auth()
            user=request.POST['username']
            u=User.objects.get(username=user)
            u.is_active=False
            u.save()
            print("pk=%s user=%s" %(pk,user))
            user=User.objects.get(username=user)
            active=Active(user=user,auth=pk)
            active.save()
            print('request.get_host()',request.get_host())
            text="http://%s/register/active/%s" %(request.get_host() ,pk)
            #text = "http://127.0.0.1/register/active/%s" % pk
            print("text",text)
            #sendemail(w)
            return  HttpResponse(text)
        else:
            return render(request, "register.html", {"form": form})

def sendemail(text):
    sender = 'hehao@szzbmy.com'
    receiver = 'hehao@szzbmy.com'
    subject = '激活码验证'
    smtpserver = 'smtp.ym.163.com'
    username = 'hehao@szzbmy.com'
    password = 'hehao123'
    msg1="点击链接验证激活!            "+text
    msg =MIMEText(msg1,'plain', 'utf-8')   # 中文需参数‘utf-8’，单字节字符不需要
    msg['Subject'] = Header(subject, 'utf-8')
    smtp = smtplib.SMTP()
    smtp.connect('smtp.ym.163.com')
    smtp.login(username, password)
    smtp.sendmail(sender, receiver, msg.as_string())
    smtp.quit()

def active(request,auth_id):
    p=Active.objects.filter(auth=auth_id)

    print("p:",p)
    if p:
        au = Active.objects.get(auth=auth_id)
        uu= User.objects.get(username=au.user)
        if uu.is_active==True:
            return HttpResponse("已经激活过，无需重复激活！")
        else:
            uu.is_active = True
            uu.save()
            return HttpResponse("验证激活成功")


    else:
        return HttpResponse("激活失败")

