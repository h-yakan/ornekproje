from django.urls import path
from . import views

urlpatterns = [
    path('',views.home),
    path('anasayfa',views.home),
    path('<kurs_adi>',views.getAsd),
    path('kategori/<int:category_id>',views.getByCategoryNum),
    path('kategori/<str:category_name>',views.getByCategoryName),
]
