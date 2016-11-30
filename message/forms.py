from django import forms
from django.contrib.auth.models import User

class AricleForm(forms.ModelForm):
    password = forms.CharField(label="密码", max_length=8)
    password2 = forms.CharField(label="密码", max_length=8)
    class Meta:
        model=User
        fields=['username','email']
