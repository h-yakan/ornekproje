from datetime import date
from django.shortcuts import redirect, render
from django.http import HttpResponse, HttpResponseNotFound
from django.urls import reverse



data = {
    "Kurslar":[
        {"title":"Javascript Kursu",
               "description": "js kurs açıklaması",
               "imageUrl":"https://img-c.udemycdn.com/course/100x100/1258436_2dc3_4.jpg",
               "slug":"javascript-kursu",
               "date": date(2022,2,2),
               "isActive":True
               },
        {"title":"Python Kursu",
               "description": "py kurs açıklaması",
               "imageUrl":"https://img-c.udemycdn.com/course/100x100/2463492_8344_3.jpg",
               "slug":"py-kursu",
               "date": date(2022,3,2),
               "isActive":True
               }
        ],
    "kategoriler":
        [{"name":"programlama","id":1,"slug":"programlama"},{"name":"web geliştirme","id":2,"slug":"web-gelistirme"}]
}

def index(req):
   kurslar = []
   kategoriler = data["kategoriler"]
   for kurs in data["Kurslar"]:
       if kurs["isActive"]:
           kurslar.append(kurs) 
   return render(req,'kurs.html',{'Kurslar': kurslar, 'Kategoriler': kategoriler} )

def getByCategoryName(req,category_name):
    try:
        category_text = data[category_name]
        return render(req,'kurslar/kurs.html',{
            'category': category_name,
            'category_text': category_text
        })
    except:
        return HttpResponse('Yanlış Kategori')
    

def getByCategoryNum(req, category_id):
    category_list = list(data["kategoriler"].keys())
    if(category_id>len(category_list)):
        return HttpResponseNotFound("Yanlış Kategori")
    category = category_list[category_id-1]
    redirected_url = reverse('courses_by_category',args=[category])
    return redirect(redirected_url)

def getAsd(req, kurs_adi):
    return HttpResponse(kurs_adi)