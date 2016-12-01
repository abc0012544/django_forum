import os
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render,redirect
from  user.forms import AricleForm
from .models import UserProfile




def logo(request):
    if request.method=="GET":
        return render(request, "index.html")

    else:
        msg="无法上传"
        err="选择不能为空"
        profile=request.user.userprofile
        logo_file=request.FILES.get('logo')
        if logo_file:
            print("logo_file",logo_file)
            if logo_file.size >= 3000000:
                return redirect('/',{"msg":msg})
            else:
                file_path=os.path.join("D:/project/DJ/django_forum/userprofile/logo/",logo_file.name)
                with open(file_path,'wb+') as f:
                    for chunk in logo_file.chunks():
                        f.write(chunk)
                url="http://dj.com:8000/userprofile/logo/%s" %logo_file.name
                print ("url:",url)
                profile.logo=url
                profile.save()
                return redirect('/')
        else:
            return redirect('/')
