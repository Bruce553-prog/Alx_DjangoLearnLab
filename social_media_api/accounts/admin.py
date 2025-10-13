from django.contrib import admin
from posts.models import Post, Comment

from .models import CustomUser

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id','title','author','created_at')
    search_fields = ('title','content','author__username')

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('id','post','author','created_at')
    search_fields = ('content','author__username')


