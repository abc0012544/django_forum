from django.contrib import admin
from django.contrib.auth.models import User
from userprofile.models import UserProfile

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ("user","logo","sex","birthday")

admin.site.register(UserProfile,UserProfileAdmin)
