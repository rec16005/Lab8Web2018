from django.db import models

# Create your models here.

class Users(models.Model):
  name = models.CharField(max_length=25)
  last_name = models.CharField(max_length=25)
  email = models.CharField(max_length=25)
  user_name = models.CharField(max_length=25)

class Posts(models.Model):
  title = models.CharField(max_length=50)
  post_body = models.CharField(max_length=125)
  number_likes = models.ManyToManyField(Users, through='Likes')
  date = models.DateField(auto_now=True)

class Likes(models.Model):
  user = models.ForeignKey(Users, on_delete=models.CASCADE)
  post = models.ForeignKey(Posts, on_delete=models.CASCADE)
  datetime = models.DateTimeField(auto_now=True)