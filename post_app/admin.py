from django.contrib.admin import ModelAdmin, register
from .models import *

@register(Post)
class PostAdmin(ModelAdmin):
    pass


@register(Like)
class LikeAdmin(ModelAdmin):
    pass


@register(Comment)
class CommentAdmin(ModelAdmin):
    pass


@register(Follow)
class FollowAdmin(ModelAdmin):
    pass