from django.contrib import admin
from django.contrib.auth.models import User
from user.models import Active

class ArticleAdmin(admin.ModelAdmin):
    list_display = ("user","auth","create_timestamp")

admin.site.register(Active,ArticleAdmin)
