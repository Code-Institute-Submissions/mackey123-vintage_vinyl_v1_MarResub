""" import forms, comment post """
from django import forms
from .models import Comment, Post


class CommentForm(forms.ModelForm):
    """ comment form class """
    class Meta:
        """ comment model class """
        model = Comment
        fields = ['comment']


class PostForm(forms.ModelForm):
    """ comment post form class """
    class Meta:
        """ post model fields"""
        model = Post
        fields = ['title', 'image', 'content']
