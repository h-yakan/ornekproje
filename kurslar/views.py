from django.shortcuts import render
from django.http import HttpResponse

def home(Req):
    return HttpResponse('Anasayfa')

# Create your views here.
