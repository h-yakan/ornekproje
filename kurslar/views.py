from django.shortcuts import redirect, render
from django.http import HttpResponse, HttpResponseNotFound
from django.urls import reverse

def home(Req):
    return HttpResponse('Anasayfa')

data = {
    'programlama':'programlama kurslarının listesi',
    'mobil':'mobil kurslarının listesi',
    'web': 'web kurslarının listesi'
}

def kurslar(req):
    list_items = ""
    category_list = list(data.keys())
    for category in category_list:
        redirected_url = reverse('courses_by_category',args=[category])
        list_items += f"<li><a href='{redirected_url}'>{category}</a></li>"

    html = f"<h1>kurs listesi</h1><br><ul>{list_items}</ul>"
    return HttpResponse(html)

def getByCategoryName(req,category_name):
    try:
        return HttpResponse(f'{data[category_name]}')
    except:
        return HttpResponse('Yanlış Kategori')
    

def getByCategoryNum(req, category_id):
    category_list = list(data.keys())
    if(category_id>len(category_list)):
        return HttpResponseNotFound("Yanlış Kategori")
    category = category_list[category_id-1]
    redirected_url = reverse('courses_by_category',args=[category])
    return redirect(redirected_url)

def getAsd(req, kurs_adi):
    return HttpResponse(kurs_adi)