from django.db import models
from django.contrib.auth.models import User
import datetime

class Active(models.Model):
    user = models.ForeignKey(User, verbose_name="用户")
    auth = models.CharField("激活码", max_length=100)
    create_timestamp = models.DateTimeField("创建时间", auto_now_add=True)

    def __str__(self):
        return self.auth

    class Meta:
        verbose_name_plural = "激活信息"
        verbose_name = "激活信息"