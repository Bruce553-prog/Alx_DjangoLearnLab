from django.shortcuts import render
from rest_framework import viewsets, permissions, filters
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.views import APIView
from django_filters.rest_framework import DjangoFilterBackend
from .models import Post, Comment
from .serializers import PostListSerializer, PostDetailSerializer, CommentSerializer
from .permissions import IsOwnerOrReadOnly


class StandardResultsSetPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.select_related('author').prefetch_related('comments')
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    pagination_class = StandardResultsSetPagination
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    search_fields = ['title', 'content']
    filterset_fields = ['author__username']

    def get_serializer_class(self):
        if self.action in ['list']:
            return PostListSerializer
        return PostDetailSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.select_related('author', 'post')
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    pagination_class = StandardResultsSetPagination
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    search_fields = ['content']
    filterset_fields = ['post', 'author__username']

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)



class FeedView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        # Get all users the current user is following
        following_users = request.user.following.all() 

        # Filter posts by followed users and order by most recent
        posts = Post.objects.filter(author__in=following_users).order_by('-created_at')  

        serializer = PostListSerializer(posts, many=True)
        return Response(serializer.data)
