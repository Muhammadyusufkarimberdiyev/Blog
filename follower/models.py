from django.db import models
from django.contrib.auth.models import User

# from blog.models import Article

# Create your models here.

class Fallower(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    name = models.CharField(verbose_name="Ismi", unique=True, max_length=55,blank=True)
    surname = models.CharField(max_length=55)
    age = models.PositiveIntegerField(default=0)
    liked_articles = models.ManyToManyField('blog.Article',blank=True)
    rating = models.PositiveIntegerField(default=0)
    email = models.EmailField()
    adress = models.CharField(max_length=500)