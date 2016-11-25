import django
from django.conf.urls import url,include
from django.contrib import admin
from .views import *
from django.contrib.auth.views import login, logout_then_login

urlpatterns = [
    url(r'^$', register),
    url(r'^active/(?P<auth_id>\w+)$',active),
    # url(r'^/login/$',  login, {'template_name': 'registration/login.html'}),   # 指定登录页面模板
    # url(r'^/logout/$', logout_then_login),

]