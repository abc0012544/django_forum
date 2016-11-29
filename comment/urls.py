from django.conf.urls import url
from .views import *
from django.contrib.auth.decorators import login_required
'''
（?P<name>\pattern)符合pattern模式的一个值，把这个值赋值给名
为name的变量，传入后面的处理函数
'''
urlpatterns=[
    url(r'^list/(?P<block_id>\d+)$',article_list),
    #url(r'^create/(?P<blockid>)$',article_content),
    url(r'^create',login_required(article_create.as_view())),
    url(r'^(?P<block_id>\d+)/(?P<article_id>\d+)/detail',detail),
    #url(r'^(?P<pk>\d+)/detail',Article_detail.as_view()),
]