from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import *
from .serializers import *
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters


class ListCreatePost(ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    ordering_fields = ['date']


class RetrieveUpdateDestroyPost(RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class ListCreateLike(ListCreateAPIView):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer


class ListCreateComment(ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class ListCreateFollow(ListCreateAPIView):
    queryset = Follow.objects.all()
    serializer_class = FollowSerializer


class RetrieveUpdateDestroyFollow(RetrieveUpdateDestroyAPIView):
    queryset = Follow.objects.all()
    serializer_class = FollowSerializer