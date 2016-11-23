from django.shortcuts import render,redirect
from block.models import Block
from .models import Article
blockid2=[]

def article_list(request,block_id):
    block_id=int(block_id)
    if len(blockid2):
        # blockid2.pop()
        # blockid2.append(block_id)
        blockid2[0]=block_id
    else:
        blockid2.append(block_id)
        # 外面定义一个数组，每次执行这个函数，就判断下，如果数组有值，就删除原来的值，再将当前id追加进去，如果没有，就直接追加，这样
        # 就保存了当前id，在当前页点击发布文章按钮进入article_content.html，就可以带进当前id值
    block=Block.objects.get(id=block_id)
    article_objs=Article.objects.filter(block=block,status=0).order_by("-id")
    return render(request,"article_list.html",{"articles":article_objs,"b":block})


def article_content(request):
    #blockid = int(block_id)
    if len(blockid2):
        blockid= blockid2[0]
    else:
        bt=Block.objects.filter(status=0)[:1]
        if bt:
            blockid =bt[0].id
        else:
            return render(request,"index.html")
# 上面这段判断代码是，先判断数组是否还有值，如果有就赋给bockid，如果没有了，比如重启django服务，就直接读取数据库的其中一条，如果读取到了就
# 赋给bockid，没有读取到说明可能没有创建或者删除了版块，导致没有id信息，就返回首页。

    block = Block.objects.get(id=blockid)
    article_objs = Article.objects.filter(block__id=blockid, status=0).order_by("-id")
    if request.method=="GET":
        return render(request, "article_content.html", {"article": article_objs, "b": block})

    else:
        title = request.POST["title"].strip()
        content = request.POST["content"].strip()
        if not title or not content:
            return render(request, "article_content.html", {"article": article_objs, "b": block,"error":"标题或者内容不能为空"})
        if len(content)>10000 or len(title)>100:
            return render(request, "article_content.html", {"article": article_objs, "b": block,"error":"标题或者内容过长！",
                                                            "title":title,"content":content})
        article=Article(block=block,title=title,content=content,status=0)
        article.save()
        return  redirect("/article/list/%d" %blockid)


