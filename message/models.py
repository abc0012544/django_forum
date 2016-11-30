from django.db import models
from django.contrib.auth.models import User


class Message(models.Model):
    owner= models.ForeignKey(User, verbose_name="用户")
    content = models.CharField("评论", max_length=10000)
    link = models.CharField("链接", max_length=10000)
    status = models.IntegerField("状态", choices=((0, "正常"), (-1, "删除")), default=0)


    def __str__(self):
        return self.content

    class Meta:
        verbose_name_plural = "消息"
        verbose_name = "消息"