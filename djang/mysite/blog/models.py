from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=150)
    content = models.TextField(blank=True)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
    comments = models.TextField(blank=True)
    published = models.DateTimeField(auto_now_add=True)