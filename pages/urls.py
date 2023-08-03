from django.shortcuts import render
from django.urls import path
from . import views

urlpatterns = [
path('',views.index),
path('index',views.index,name="index"),
path('hakkimizda',views.getHakkimizda),
path('iletisim',views.iletisim),
path('<asd>',views.getAsd),
]
