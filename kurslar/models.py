
import datetime
from django.db import models


    
class Kategoriler(models.Model):
    name = models.CharField(max_length=30)
    slug = models.SlugField(max_length=15)

    def __str__(self):
        return f"{self.name}"

class Kurs(models.Model):
    title = models.CharField(max_length=30)
    description = models.TextField(null=True)
    imageUrl = models.URLField()
    slug = models.SlugField(unique=True,db_index=True,null=False)
    date = models.DateField(default=datetime.datetime.now())
    isActive = models.BooleanField()
    kategori = models.ManyToManyField(Kategoriler,blank = True)

    def __str__(self):
        return f"{self.title}"
