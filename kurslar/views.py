from django.shortcuts import render
from django.http import HttpResponse

def home(Req):
    return HttpResponse('Anasayfa')

def getByCategoryName(req,category_name):
    return HttpResponse(f'{category_name} yanlış')

def getByCategoryNum(req, category_id):
    return HttpResponse (f'{category_id} doğru')
def getAsd(req, kurs_adi):
    return HttpResponse(kurs_adi)