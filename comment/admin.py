from django.contrib import admin
from comment.models import Comment

class CommentAdmin(admin.ModelAdmin):
    list_display = ("id","owner","article","to_comment","to_comment_id","content","status","create_timestamp","last_update_timestamp")

admin.site.register(Comment,CommentAdmin)