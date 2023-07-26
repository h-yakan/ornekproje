from django.db import models

class Kategoriler(models.Model):
    name = models.CharField(max_length=30)
    slug = models.SlugField(max_length=15)

class Kurs(models.Model):
    title = models.CharField(max_length=30)
    description = models.TextField(null=True)
    imageUrl = models.URLField()
    slug = models.SlugField(max_length=15)
    date = models.DateField()
    isActive = models.BooleanField()
