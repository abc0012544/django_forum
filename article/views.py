from django.shortcuts import render,redirect
from block.models import Block
from .models import Article
from  .forms import AricleForm
from comment.models import Comment
from django.views.generic import View
from django.views.generic import DetailView
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db.models import Q
from userprofile.models import UserProfile

blockid2=[]

def fenye(request,article_all,cnt_1page):
    page_links = []
    previous_link=0
    next_link=0
    ARTICLE_CNT_1PAGE =cnt_1page
    p = Paginator(article_all, ARTICLE_CNT_1PAGE)
    page_num=p.num_pages
    page_no = int(request.GET.get("page_no", 1))
    if page_no > p.num_pages:
        page_no = p.num_pages
    if page_no < 1:
        page_no = 1


    page = p.page(page_no)
    for i in range(page_no - 3, page_no + 4):
        if i > 0 and i <= p.num_pages:
            page_links.append(i)

    if page_links[-1] + 1 <= p.num_pages:
        raquo = 1
        next_link = page_links[-1] + 1
    else:
        raquo = 0
    if page_links[0] - 1 > 0:
        laquo = 1
        previous_link = page_links[0] - 1
    else:
        laquo = 0
        # 上面是计算最大页，最小页逻辑，如果符合，标示为1，并且记录最大页，最小页数值
    article_objs = page.object_list
    fenye_data={
        "raquo":raquo,
        "laquo":laquo,
        "previous_link":previous_link,
        "next_link":next_link,
        "page_num":p.num_pages,
        "page_links":page_links,
        "page_no":page_no
    }
    # return raquo,laquo,previous_link,next_link,page_num,article_objs,page_links
    return (article_objs,fenye_data)

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
    article_all=Article.objects.filter(block=block,status=0).order_by("-id")
    article_objs,fenye_data=fenye(request, article_all,6)
    print("fenye_data",fenye_data)
    # return render(request,"article_list.html",{"articles":article_objs,"b":block,"p":p,"page_links":page_links,"page_no":page_no,
    #                                            "raquo":raquo,"laquo":laquo,"previous_link":previous_link,"next_link":next_link})
    return  render(request,"article_list.html",{"b":block,"article_objs":article_objs,"fenye_data":fenye_data})


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
        # title = request.POST["title"].strip()
        # content = request.POST["content"].strip()

        # if not title or not content:
        #     return render(request, "article_content.html", {"article": article_objs, "b": block,"error":"标题或者内容不能为空"})
        # if len(content)>10000 or len(title)>100:
        #     return render(request, "article_content.html", {"article": article_objs, "b": block,"error":"标题或者内容过长！",
        #                                                     "title":title,"content":content})
        # article=Article(block=block,title=title,content=content,status=0)
        # article.save()
        # return  redirect("/article/list/%d" %blockid)
        # 冗余写法，下面是更好的写法
        form=AricleForm(request.POST)
        if form.is_valid():
            article=form.save(commit=False)
            article.block=block
            article.owner="admin"
            article.status=0
            article.save()
            return  redirect("/article/list/%d" %blockid)
        else:
            return render(request, "article_content.html", {"article": article_objs, "b": block, "form": form})

class article_create(View):
    def init_data(self,request):
        if len(blockid2):
            self.blockid = blockid2[0]
            print("打印1" ,self.blockid)
        else:
            bt = Block.objects.filter(status=0)[:1]
            if bt:
                self.blockid = bt[0].id
                print("打印2", self.blockid)
            else:
                return render(request, "index.html")
        self.block = Block.objects.get(id=self.blockid)
        self.article_objs=Article.objects.filter(block__id=self.blockid, status=0).order_by("-id")
        self.name=request.user
        self.owner=User.objects.get(username=self.name)

    def get(self,request):
        self.init_data(request)
        return render(request, "article_content.html", {"article": self.article_objs, "b": self.block})

    def post(self,request):
        self.init_data(request)
        form = AricleForm(request.POST)
        if form.is_valid():
            article = form.save(commit=False)
            article.owner = self.owner
            article.block=self.block
            article.status = 0
            article.save()
            return redirect("/article/list/%d" % self.blockid)
        else:
            return render(request, "article_content.html", {"article": self.article_objs, "b": self.block, "form": form})

def detail(request,block_id,article_id):
    article_id=int(article_id)
    block_id = int(block_id)
    name=request.user
    user = User.objects.filter(username=name)
    if user:
        u= UserProfile.objects.filter(user=user)

    article=Article.objects.get(id=article_id)
    block = Block.objects.get(id=block_id)
    #name=article.owner
    comment_all=Comment.objects.filter(article=article,status=0).order_by("-id")
    comment_tocomment=Comment.objects.filter(Q(article=article) & Q(status=0) & ~Q(to_comment=0)).order_by("-id")
    comment_objs, fenye_data = fenye(request, comment_all, 3)
    #article_objs=Article.objects.filter(block=block,status=0).order_by("-id")
    return render(request, "article_detail.html",{"b":block,"a":article,"name":name,"fenye_data":fenye_data,
                                                  "comment_objs":comment_objs,"comment_tocomment":comment_tocomment,"u":u})

class Article_detail(DetailView):
    model = Article
    template_name ="article_detail.html"
    context_object_name = "a"

