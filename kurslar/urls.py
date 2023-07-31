from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,),
    path('search',views.search,name='search'),
    path('kursKayit',views.kursGir,name='kursKayit'),
    path('upload',views.imgUpload,name='imgUpload'),
    path('kursDuzenle/<slug:slug>',views.kursDuzenle,name='kursDuzenle'),
    path('kursSil/<slug:slug>',views.kursSil,name='kursSil'),
    path('kursListesi',views.kursListesi,name="kursListesi"),
    path('<name>',views.detay,name ='courses'),
    path('kategori/<slug:slug>',views.getByCategoryName,name = 'courses_by_category'),
    
    
]
