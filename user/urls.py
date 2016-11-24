import django
from django.conf.urls import url,include
from django.contrib import admin
from .views import *

urlpatterns = [
    url(r'^$', register),
    url(r'^/active/(?P<auth_id>\w+)$',active),

]