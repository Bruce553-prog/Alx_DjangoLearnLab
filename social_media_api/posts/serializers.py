from rest_framework import serializers
from django.conf import settings
from .models import Post, Comment
from django.contrib.auth import get_user_model

User = get_user_model()

class CommentSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(read_only=True)  # shows username/string
    author_id = serializers.PrimaryKeyRelatedField(source='author', read_only=True)

    class Meta:
        model = Comment
        fields = ['id', 'post', 'author', 'author_id', 'content', 'created_at', 'updated_at']
        read_only_fields = ['id', 'author', 'author_id', 'created_at', 'updated_at']


class PostListSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(read_only=True)
    comments_count = serializers.IntegerField(source='comments.count', read_only=True)

    class Meta:
        model = Post
        fields = ['id', 'title', 'author', 'comments_count', 'created_at', 'updated_at']


class PostDetailSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(read_only=True)
    comments = CommentSerializer(many=True, read_only=True)  # nested read-only

    class Meta:
        model = Post
        fields = ['id', 'title', 'content', 'author', 'comments', 'created_at', 'updated_at']
        read_only_fields = ['id', 'author', 'comments', 'created_at', 'updated_at']
