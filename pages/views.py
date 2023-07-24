from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def getHakkimizda(req):
    return render(req, 'hakkimizda.html')

def home(Req):
    return HttpResponse('Anasayfa')

def getAsd(req,asd):
    return HttpResponse(asd)

def iletisim(req):
    return render(req, 'iletisim.html')
    