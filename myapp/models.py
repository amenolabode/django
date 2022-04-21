from turtle import title
from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=250)
    body = models.TextField()
    photo = models.CharField(max_length=2000, default='', blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add = True)

class Comment(models.Model):
    post = models.ForeignKey(Post, related_name="my_post", on_delete=models.CASCADE)
    comment = models.TextField()
    date_created = models.DateTimeField(auto_now_add = True)


class User(models.Model):
    user_name = models.CharField(max_length=250)
    