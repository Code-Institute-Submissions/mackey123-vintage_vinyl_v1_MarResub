""" import forms, comment post """
from django import forms
from .models import Comment, Post


class CommentForm(forms.ModelForm):
    """ comment form class """
    class Meta:
        model = Comment
        fields = ['comment']


class PostForm(forms.ModelForm):
    """ comment post form class """
    class Meta:
        model = Post
        fields = ['title', 'image', 'content']
