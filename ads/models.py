from django.db import models


class Ad(models.Model):
    name = models.TextField(max_length=100)
    author = models.TextField(max_length=100)
    price = models.IntegerField()
    description = models.TextField(max_length=1000, null=True)
    address = models.TextField(max_length=200)
    is_published = models.BooleanField()


class Categories(models.Model):
    name = models.TextField(max_length=100)
