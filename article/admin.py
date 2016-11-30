from django.contrib import admin
from article.models import Article
from comment.models import Comment

class Commentinline(admin.TabularInline):
    model = Comment

class ArticleAdmin(admin.ModelAdmin):
    list_display = ("title","content","block","owner","status","create_timestamp","last_update_timestamp")
    actions = ["make_good"]
    inlines = [Commentinline]

    # fieldsets = (
    #     ("基本",{"classes":('collapse',),"fields":("title","content")}),
    #     ("高级",{"classes":('collapse',),"fields":("status",)})
    # )
    #
    # readonly_fields = ("create_timestamp","last_update_timestamp","title","content","status")
    def make_good(ModelAdmin,request,queryset):
        for i in queryset:
            i.status=10
            i.save()
    make_good.short_description = "精华"





admin.site.register(Article,ArticleAdmin)
