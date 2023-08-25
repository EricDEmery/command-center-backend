from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone

class CustomUser(AbstractUser):
    epic_id = models.CharField(null=True, max_length=12)

    def __str__(self):
        return self.username

    class Meta:
        app_label = 'commandcenter'

class Post(models.Model):
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    epic_id = models.CharField(null = True, max_length=12)  # Add epic_id field to the Post model

class Comment(models.Model):
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
