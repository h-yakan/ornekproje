from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,),
    path('search',views.search,name='search'),
    path('<name>',views.detay,name ='courses'),
    path('kategori/<slug:slug>',views.getByCategoryName,name = 'courses_by_category'),
    
    
]
