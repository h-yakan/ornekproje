
import datetime
from django.db import models
from django.utils.text import slugify

    
class Kategoriler(models.Model):
    name = models.CharField(max_length=30)
    slug = models.SlugField(max_length=15)

    def __str__(self):
        return f"{self.name}"

class Kurs(models.Model):
    title = models.CharField(max_length=30)
    description = models.TextField(null=True)
    image = models.ImageField(upload_to="images",default="",blank=True)
    slug = models.SlugField(unique=True,db_index=True,null=False)
    date = models.DateField(default=datetime.datetime.now())
    isActive = models.BooleanField()
    kategori = models.ManyToManyField(Kategoriler,blank = True)

    def __str__(self):
        return f"{self.title}"
    
    def save(self,*args,**kwargs):
        self.slug=slugify(self.title)
        super().save(args,kwargs)
    
class Slider(models.Model):
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to="images")
    kurs = models.ForeignKey(Kurs,on_delete=models.SET_NULL,null=True,blank=True)
    isActive = models.BooleanField(default=False)   
    
    def __str__(self):
        return f"{self.title}"