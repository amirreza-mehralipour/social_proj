from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

class Post(models.Model):
    user =models.ForeignKey(User, on_delete= models.CASCADE)
    text = models.TextField(blank= True, null= True)
    image = models.ImageField(blank= True, null= True)
    date = models.DateTimeField(auto_now_add=True)

    def clean(self):
        super().clean()
        if not self.text and not self.image:
            raise ValidationError("must have image or text")

    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)


class Like(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete= models.CASCADE)


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, models.CASCADE)
    text = models.TextField()


class Follow(models.Model):
    follower = models.ForeignKey(User, on_delete= models.CASCADE, related_name= "follower")
    following = models.ForeignKey(User, on_delete= models.CASCADE, related_name= 'following')