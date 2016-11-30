from django.contrib import admin
from django.contrib.auth.models import User
from message.models import Message

class MessageAdmin(admin.ModelAdmin):
    list_display = ("owner","content","link","status")

admin.site.register(Message,MessageAdmin)
