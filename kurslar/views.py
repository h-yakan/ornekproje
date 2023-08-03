
from django.shortcuts import get_object_or_404, redirect, render
from django.http import Http404
from kurslar.forms import KursGiris
from .models import Kurs, Slider, Kategoriler
from django.core.paginator import Paginator
from django.contrib.auth.decorators import user_passes_test


def isAdmin(user):
    return user.is_superuser

def index(req):
   kurslar = Kurs.objects.filter(isActive = 1)
   kursp = Paginator(kurslar,2)
   sayfa_sayi = req.GET.get('page',1)
   paged_kurs = kursp.get_page(sayfa_sayi)
   kategoriler = Kategoriler.objects.all()
   slider = Slider.objects.filter(isActive = True)

   return render(req,'kurs.html',{'Kurslar': paged_kurs, 'sliders':slider, 'Kategoriler': kategoriler} )

def detay(req,name):
    try:
        kurs= Kurs.objects.filter(slug = name)
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

@user_passes_test(isAdmin)
def kursGir(req):
    if req.method =='POST':
        form = KursGiris(req.POST,req.FILES)
        if form.is_valid():
            kurs = Kurs(title=form.cleaned_data["title"],
                        description = form.cleaned_data["description"],
                        image=req.FILES["image"],
                        isActive = True)
            kurs.save()
            return redirect('/kurslar/')
    else:
        form = KursGiris()
    return render(req, 'kursKayit.html',{'form':form})

def getByCategoryName(req,slug):
    kurs = Kurs.objects.filter(kategori__slug=slug,isActive=True)
    kategori=Kategoriler.objects.all()
    kursp = Paginator(kurs,2)
    sayfa_sayi = req.GET.get('page',1)
    paged_kurs = kursp.get_page(sayfa_sayi)
    return render(req,'kurs.html',{'Kurslar': paged_kurs, 'Kategoriler':kategori,'seciliKategori':slug})

@user_passes_test(isAdmin)
def kursListesi(req):
    kurslar = Kurs.objects.all()
    return render(req,'kursListesi.html',{'Kurslar': kurslar})


@user_passes_test(isAdmin)
def kursDuzenle(req,slug):

    kurs = get_object_or_404(Kurs,slug = slug)
    if req.method == "POST":
        form = KursGiris(req.POST, req.FILES, instance=kurs)
        form.save()
        return redirect("/kurslar/kursListesi")
    form = KursGiris(instance=kurs)

    return render(req,'kursDuzenle.html',{'form':form}) 

@user_passes_test(isAdmin)
def kursSil(req,slug):
    kurs = get_object_or_404(Kurs,slug = slug)
    if req.method == "POST":
        kurs.delete()
        return redirect("kursListesi")
    return render(req,'kursSil.html',{'kurs':kurs})

    


        
    