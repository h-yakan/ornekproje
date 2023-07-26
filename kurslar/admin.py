from django.contrib import admin
from .models import Kurs,Kategoriler    
# Register your models here.
@admin.register(Kurs)
class KursAdmin(admin.ModelAdmin):
    list_display = "title","isActive"
    list_editable = "isActive",

admin.site.register(Kategoriler)

