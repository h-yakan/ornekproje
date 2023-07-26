from datetime import date
from django.shortcuts import redirect, render
from django.http import Http404, HttpResponse, HttpResponseNotFound
from django.urls import reverse
from .models import Kurs
from .models import Kategoriler


def index(req):
   kurslar = Kurs.objects.filter(isActive = 1)
   kategoriler = Kategoriler.objects.all()
   return render(req,'kurs.html',{'Kurslar': kurslar, 'Kategoriler': kategoriler} )

def detay(req,name):
    try:
        kurs= Kurs.objects.filter(slug__startswith = name)
        return render(req,'detay.html',{
            'Kurs': kurs
        })
    except:
        return Http404

def getByCategoryName(req,category_name):
    try:
        category_text = Kategoriler.objects.filter(name= category_name)
        return render(req,'kurs.html',{
            'Kategori': category_text,
        })
    except:
        return HttpResponse('Yanlış Kategori')
    
    

def getByCategoryNum(req, category_id):
    category_list = Kategoriler.objects.all()
    if(category_id>len(category_list)):
        return HttpResponseNotFound("Yanlış Kategori")
    category = category_list[category_id-1]
    redirected_url = reverse('courses_by_category',args=[category.slug])
    return redirect(redirected_url)
