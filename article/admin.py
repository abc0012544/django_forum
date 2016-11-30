from django.contrib import admin
from article.models import Article

class ArticleAdmin(admin.ModelAdmin):
    list_display = ("block","title","content","owner","status","create_timestamp","last_update_timestamp")

admin.site.register(Article,ArticleAdmin)
