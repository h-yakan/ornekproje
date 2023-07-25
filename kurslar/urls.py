from django.urls import path
from . import views

urlpatterns = [
    path('',views.index),
    path('<kurs_adi>',views.getAsd),
    path('kategori/<int:category_id>',views.getByCategoryNum),
    path('kategori/<str:category_name>',views.getByCategoryName,name = 'courses_by_category'),
]
