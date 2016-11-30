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
# from article.views import *
from message.models import Message

def comment_create(request):
    parm={}
    to_comment_id=int(request.POST.get("to_comment_id",0))
    print("to_comment_id",to_comment_id)
    parm["content"]=request.POST.get("content")
    parm["article_id"] = request.POST.get("article_id")
    parm["b_id"]=request.POST.get("b_id")
    parm["page_no"] = request.POST.get("page_no")
    ok={"status":"ok","msg":"发布成功"}
    err = {"status": "err", "msg": "发布失败"}
    # article_id =64
    # content =request.POST["content"]
    article_id = parm["article_id"]
    content = parm["content"]
    article_id = int(article_id)
    article = Article.objects.get(id=article_id)
    name = request.user
    link="http://%s/article/%s/%s/detail?page_no=%s" %(request.get_host() ,parm["b_id"],parm["article_id"],parm["page_no"])
    form = CommentForm(request.POST)

    if to_comment_id!=0:
        to_comment=Comment.objects.get(id=to_comment_id)
        owner =to_comment.owner

    else:
        to_comment =None
        owner =article.owner
    if form.is_valid():
        comment= Comment(article=article, owner=name, content=content,to_comment=to_comment, status=0)
        comment.save()
        message=Message(owner=owner,content=content,link=link,status=0)
        message.save()

        return HttpResponse(json.dumps(ok))
    else:
        return HttpResponse(json.dumps(err))


