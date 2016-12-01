from django.db import models
from django.contrib.auth.models import User
import datetime

class UserProfile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    sex = models.IntegerField("性别", choices=((0, "男"), (-1, "女")), default=0)
    birthday = models.DateTimeField("生日", null=True,blank=True)
    logo = models.CharField("头像", max_length=300, blank=True)

    def __str__(self):
        return str(self.sex)

    class Meta:
        verbose_name_plural = "用户相关信息"
        verbose_name = "用户相关信息"