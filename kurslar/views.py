from datetime import date
from django.shortcuts import redirect, render
from django.http import HttpResponse, HttpResponseNotFound
from django.urls import reverse



data = {
    "Kurslar":[
        {"title":"Javascript Kursu",
               "description": "js kurs açıklaması",
               "imageUrl":"",
               "slug":"javascript-kursu",
               "date": date(2022,2,2),
               "isActive":True
               },
        {"title":"Python Kursu",
               "description": "py kurs açıklaması",
               "imageUrl":"",
               "slug":"py-kursu",
               "date": date(2022,3,2),
               "isActive":False
               }
        ],
    "kategoriler":
        [{"name":"programlama","id":1,"slug":"programlama"},{"name":"web geliştirme","id":2,"slug":"web-gelistirme"}]
}

def index(req):
   kurslar = data["Kurslar"]
   kategoriler = data["kategoriler"]

   return render(req,'courses/index.html',{'Kurslar': kurslar, 'Kategoriler': kategoriler} )

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