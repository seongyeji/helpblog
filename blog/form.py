from django import forms
from .models import Blog, Comment

class NewBlog(forms.ModelForm):
# models를 기반으로 만드는거라서 Form이 아니라 ModelForm
    class Meta:
        model = Blog
        fields = ['title', 'body']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ( 'author', 'text', ) 
        # fields라는 리스트에 author과 text만 입력받겠다.