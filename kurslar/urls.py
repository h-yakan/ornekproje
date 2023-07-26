from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,),
    path('kategori/<int:category_id>',views.getByCategoryNum),
    path('<name>',views.detay,name ='courses'),
    path('kategori/<str:category_name>',views.getByCategoryName,name = 'courses_by_category'),
    
    
]
