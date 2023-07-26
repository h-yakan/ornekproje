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
    imageUrl = models.URLField()
    slug = models.SlugField(max_length=15,unique=True,db_index=True,null=False)
    date = models.DateField()
    isActive = models.BooleanField()
    kategori = models.ForeignKey(Kategoriler,null = True,blank = True,on_delete=models.PROTECT)
    def save(self,*args,**kwargs):
        self.slug = slugify(self.title)
        super().save(args,kwargs)
    def __str__(self):
        return f"{self.title}"
