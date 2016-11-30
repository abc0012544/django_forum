import django
from django.conf.urls import url,include
from django.contrib import admin
import view
from comment.views import *
from message.views import *




urlpatterns = [

    url(r'^info/', message_info),
    url(r'^read/(?P<message_id>\d+)/',message_read1),
    url(r'^read/', message_read),
    # url(r'^accounts/login/$',  login, {'template_name': 'registration/login.html'}),   # 指定登录页面模板
    # url(r'^accounts/logout/$', logout_then_login),


]