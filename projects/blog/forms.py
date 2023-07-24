from django import forms
from .models import Post, Comment, HashTag

class PostForm(forms.ModelForm):
    
    class Meta:
        model = Post
        fields = ['title','content', 'imgfile']
        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 10, 'cols':'35'}),
        }
        labels = {
            'title': '제목',
            'content': '내용',
            'imgfile': '이미지'
        }


class CommentForm(forms.ModelForm):
    
    class Meta:
        model = Comment
        fields = ['content']
        widgets = {
            'content' : forms.Textarea(attrs={'rows': '3', 'cols':'35'})
        }
        

class HashTagForm(forms.ModelForm):
    
    class Meta:
        model = HashTag
        fields = ['name']