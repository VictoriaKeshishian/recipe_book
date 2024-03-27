from django.db import models
from django.contrib.auth.models import User


class Recipe(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    cooking = models.TextField()
    time_cooking = models.CharField(max_length=50)
    img = models.ImageField(upload_to='products/')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    ingredients = models.TextField()
    categories = models.ManyToManyField('Categories', related_name='recipes')


class Categories(models.Model):
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='products/', blank=True, null=True)
    keywords = models.CharField(max_length=100)





