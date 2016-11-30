from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.http import JsonResponse
import json
from block.models import Block
from .models import Article
import json
from  .forms import CommentForm
from comment.models import Comment
from django.views.generic import View
from django.views.generic import DetailView
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from article.views import *
def comment_create(request):
    parm={}
    to_comment_id=int(request.POST.get("to_comment_id",0))
    print("to_comment_id",to_comment_id)
    parm["content"]=request.POST.get("content")
    parm["article_id"] = request.POST.get("article_id")
    print("parm",parm)
    ok={"status":"ok","msg":"发布成功"}
    err = {"status": "err", "msg": "发布失败"}
    # article_id =64
    # content =request.POST["content"]
    article_id = parm["article_id"]
    content = parm["content"]
    article_id = int(article_id)
    name = request.user
    form = CommentForm(request.POST)
    if to_comment_id!=0:
        to_comment=Comment.objects.get(id=to_comment_id)
    else:
        to_comment =None
    if form.is_valid():
        article = Article.objects.get(id=article_id)
        comment= Comment(article=article, owner=name, content=content,to_comment=to_comment, status=0)
        comment.save()
        return HttpResponse(json.dumps(ok))
    else:
        return HttpResponse(json.dumps(err))


