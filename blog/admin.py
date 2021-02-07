from django.contrib import admin
from django.contrib.admin.decorators import register
from django.db import models
from .models import Blogger, Blogpost, Comment, Tag
# Register your models here.
admin.site.register(Tag)
admin.site.register(Comment)
admin.site.register(Blogpost)


class CommentInline(admin.ModelAdmin):
    model = Comment
    list_display = ['commenter', 'comment_date', 'post']

class BlogPostInline(admin.TabularInline):
    model = Blogpost
    list_display = ['title', 'post_date']
    extra = 0
    inlines = [CommentInline]


@register(Blogger)
class BloggerAdmin(admin.ModelAdmin):
    model = Blogger
    list_display = ['first_name', 'last_name', 'bio']
    inlines = [BlogPostInline]


class TagAdmin(admin.ModelAdmin):
    model = Tag
    inlines = [BlogPostInline]


class BlogpostAdmin(admin.ModelAdmin):
    model = Blogpost
    inlines = [CommentInline]

# class CommentAdmin(admin.ModelAdmin):
#     list_display = ['commenter', ]