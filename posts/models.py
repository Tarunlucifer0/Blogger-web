from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    title=models.CharField(max_length=75)
    body=models.TextField()
    slug=models.SlugField()
    date=models.DateTimeField(default=timezone.now)
    banner=models.ImageField(default='fallback.png', blank=True)
    auther=models.ForeignKey(User, on_delete=models.CASCADE, default=None)

    def __str__(self) -> str:
        return self.title 

