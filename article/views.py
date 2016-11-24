from django.shortcuts import render,redirect
from block.models import Block
from .models import Article
from  .forms import AricleForm
from django.views.generic import View
from django.views.generic import DetailView
from django.core.paginator import Paginator

blockid2=[]



def article_list(request,block_id):
    global raquo
    global laquo
    global previous_link
    global next_link
    global page_links
    global p
    raquo = 0
    laquo=0
    previous_link=0
    next_link=0
    page_links=[]
    ARTICLE_CNT_1PAGE=6
    page_no=int(request.GET.get("page_no","1"))
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
    p=Paginator(article_all,ARTICLE_CNT_1PAGE)
    page=p.page(page_no)
    for i in range(page_no - 3, page_no + 4):
        if i > 0 and i <= p.num_pages:
            page_links.append(i)

    if page_links[-1] + 1 <= p.num_pages:
        raquo=1
        next_link=page_links[-1] + 1
    else:
        raquo=0
    if page_links[0]-1 >0:
        laquo=1
        previous_link=page_links[0]-1
    else:
        laquo=0
    print("page_links", page_links)
    print("p.num_pages",p.num_pages)
    print("page_links[-1]",page_links[-1])
    print("raquo",raquo)
    print("laquo",laquo)
    print("next_link",next_link)
    print("previous_link",previous_link)
    article_objs=page.object_list
    return render(request,"article_list.html",{"articles":article_objs,"b":block,"p":p,"page_links":page_links,"page_no":page_no,
                                               "raquo":raquo,"laquo":laquo,"previous_link":previous_link,"next_link":next_link})


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

    def get(self,request):
        self.init_data(request)
        return render(request, "article_content.html", {"article": self.article_objs, "b": self.block})

    def post(self,request):
        self.init_data(request)
        form = AricleForm(request.POST)
        if form.is_valid():
            article = form.save(commit=False)
            article.block = self.block
            article.status = 0
            article.save()
            return redirect("/article/list/%d" % self.blockid)
        else:
            return render(request, "article_content.html", {"article": self.article_objs, "b": self.block, "form": form})

def detail(request,block_id,article_id):
    article_id=int(article_id)
    block_id = int(block_id)
    article=Article.objects.get(id=article_id)
    block = Block.objects.get(id=block_id)
    #article_objs=Article.objects.filter(block=block,status=0).order_by("-id")
    return render(request, "article_detail.html",{"b":block,"a":article})

class Article_detail(DetailView):
    model = Article
    template_name ="article_detail.html"
    context_object_name = "a"

