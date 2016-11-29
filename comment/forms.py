from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    # title=forms.CharField(label="标题",max_length=1)
    # content=forms.CharField(label="内容", max_length=1)
    # 上面是自定义规则写法

    class Meta:
        model=Comment
        fields=['content']