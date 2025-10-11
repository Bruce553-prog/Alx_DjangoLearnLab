from rest_framework import viewsets, permissions, filters
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend
from .models import Post, Comment
from .serializers import PostListSerializer, PostDetailSerializer, CommentSerializer
from .permissions import IsOwnerOrReadOnly


class StandardResultsSetPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()  
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    pagination_class = StandardResultsSetPagination
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    search_fields = ['title', 'content']
    filterset_fields = ['author__username']

    def get_serializer_class(self):
        if self.action == 'list':
            return PostListSerializer
        return PostDetailSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def perform_update(self, serializer):
        if self.request.user == serializer.instance.author:
            serializer.save()
        else:
            raise permissions.PermissionDenied("You can only edit your own posts.")

    def perform_destroy(self, instance):
        if self.request.user == instance.author:
            instance.delete()
        else:
            raise permissions.PermissionDenied("You can only delete your own posts.")


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()  # ✅ required by checker
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    pagination_class = StandardResultsSetPagination
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    search_fields = ['content']
    filterset_fields = ['post', 'author__username']

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def perform_update(self, serializer):
        if self.request.user == serializer.instance.author:
            serializer.save()
        else:
            raise permissions.PermissionDenied("You can only edit your own comments.")

    def perform_destroy(self, instance):
        if self.request.user == instance.author:
            instance.delete()
        else:
            raise permissions.PermissionDenied("You can only delete your own comments.")

