from django.db import models
from block.models import Block

class Article(models.Model):
    block=models.ForeignKey(Block,verbose_name="版块ID")
    title= models.CharField("标题", max_length=100)
    content= models.CharField("内容",max_length=10000)
    status=models.IntegerField("状态",((0,"正常"),(-1,"删除")),default=0)
    create_timestamp=models.DateField("创建时间",auto_now_add=True)
    last_update_timestamp=models.DateField("最后更新时间",auto_now=True)

    def __str__(self):
        return str(self.title)


    class Meta:
        verbose_name_plural="文章"
        verbose_name="文章"


