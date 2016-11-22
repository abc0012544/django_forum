from django.db import models

class Block(models.Model):
    name=models.CharField("版块名称",max_length=100)
    desc = models.CharField("版块描述", max_length=100)
    manager_name = models.CharField("版块管理员名称", max_length=100)
    status=models.IntegerField("状态",
                               choices=((0,"正常"),(-1,"删除")),default=0)

#返回Block属性名称显示在admin Block模块列表中
    def __str__(self):
        return self.name

    '''
    meta名字是固定的，必须如此写。用于说明Block这个类
    verbose_name显示在adminBlock模块列表表头
    verbose_name_plural是显示版块的复数
    '''

    class Meta:
        verbose_name_plural="版块"
        verbose_name="版块"


