""" admin blog imports """
from django.contrib import admin
from .models import Post, Comment


class PostAdmin(admin.ModelAdmin):
    """  blog class """
    list_display = ('title', 'slug', 'created_on', 'author', 'image')
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}


class CommentAdmin(admin.ModelAdmin):
    """ for comment model """
    list_display = ('comment', 'date_added')


admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
