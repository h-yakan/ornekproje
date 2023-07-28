from django.contrib import admin
from .models import Kurs,Kategoriler    
# Register your models here.
@admin.register(Kurs)
class KursAdmin(admin.ModelAdmin):
    list_display = "title","isActive","category_list"
    list_editable = "isActive",
    prepopulated_fields={"slug":("title",),}
    def category_list(self,obj):
        html=""
        for kategori in obj.kategori.all():
            html +=kategori.name
        return html


@admin.register(Kategoriler)
class KategorilerAdmin(admin.ModelAdmin):
    prepopulated_fields={"slug":("name",),}

