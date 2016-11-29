from django.shortcuts import render,redirect
from django.http import HttpResponse
import json
from block.models import Block
from .models import Article
from  .forms import CommentForm
from comment.models import Comment
from django.views.generic import View
from django.views.generic import DetailView
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
# **parm
def comment_create(request,parm):
    ok={"status":"ok","msg":"发布成功"}
    err = {"status": "err", "msg": "发布失败"}
    # article_id =64
    # content =request.POST["content"]
    article_id = parm["article_id"]
    content = parm["content"]
    article_id = int(article_id)
    name = request.user
    form = CommentForm(request.POST)
    if form.is_valid():

        article = Article.objects.get(id=article_id)
        comment= Comment(article=article, owner=name, content=content, status=0)
        comment.save()
        return HttpResponse(json.dumps(ok))
    else:
        return HttpResponse(json.dumps(err))
