from django.contrib import admin
from block.models import Block

#告诉admin Block列表中显示哪些字段
class BlockAdmin(admin.ModelAdmin):
    list_display = ("name","desc","manager_name","status")

#admin后台增加block应用
admin.site.register(Block,BlockAdmin)