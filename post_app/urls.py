from django.urls import path
from .views import * 


urlpatterns = [
    path('post/', ListCreatePost.as_view()),
    path('post/<int:pk>', RetrieveUpdateDestroyPost.as_view),
    path('like/', ListCreateLike.as_view()),
    path('comment/', ListCreateComment.as_view()),
    path('follow/', ListCreateFollow.as_view()),
    path('unfollw/', RetrieveUpdateDestroyFollow.as_view()),
]