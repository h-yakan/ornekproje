from datetime import date
from django.shortcuts import redirect, render
from django.http import Http404
from .models import Kurs
from .models import Kategoriler
from django.core.paginator import Paginator

def index(req):
   kurslar = Kurs.objects.filter(isActive = 1)
   kursp = Paginator(kurslar,2)
   sayfa_sayi = req.GET.get('page',1)
   paged_kurs = kursp.get_page(sayfa_sayi)
   kategoriler = Kategoriler.objects.all()
   return render(req,'kurs.html',{'Kurslar': paged_kurs, 'Kategoriler': kategoriler} )

def detay(req,name):
    try:
        kurs= Kurs.objects.filter(slug__startswith = name)
        return render(req,'detay.html',{
            'Kurs': kurs
        })
    except:
        return Http404
    
def search(req):
    if "q" in req.GET and req.GET["q"] !="":
        q = req.GET["q"]
        kurslar = Kurs.objects.filter(isActive=True, title__contains=q)
        kategoriler=  Kategoriler.objects.all()
    else:
        return redirect("/kurslar")
    kursp = Paginator(kurslar,2)
    sayfa_sayi = req.GET.get('page',1)
    paged_kurs = kursp.get_page(sayfa_sayi)
     
    return render(req,'kurs.html',{'Kurslar': paged_kurs, 'Kategoriler': kategoriler} )

def getByCategoryName(req,slug):
    kurs = Kurs.objects.filter(kategori__slug=slug,isActive=True)
    kategori=Kategoriler.objects.all()
    kursp = Paginator(kurs,2)
    sayfa_sayi = req.GET.get('page',1)
    paged_kurs = kursp.get_page(sayfa_sayi)
    return render(req,'kurs.html',{'Kurslar': paged_kurs, 'Kategoriler':kategori,'seciliKategori':slug})
