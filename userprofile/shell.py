import os
os.environ['DJANGO_SETTINGS_MODULE']='django_forum.settings'

import django
django.setup()

from userprofile.models import UserProfile
from django.contrib.auth.models import User

for i in User.objects.all():
    p=UserProfile(user=i)
    p.save()