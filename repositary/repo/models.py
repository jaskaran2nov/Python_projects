from django.db import models
from django.utils import timezone
from django.urls import reverse
# Create your models here.

class Post(models.Model):
    titel=models.CharField(max_length=50)
    datetime=models.DateTimeField(default=timezone.now)
    author=models.CharField(max_length=30)
    description=models.TextField()
    code=models.TextField()

    def __str__(self):
        return (self.titel+" | "+self.author)

    def get_absolute_url(self):
        return reverse('posts')

