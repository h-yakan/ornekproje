from django import forms

from kurslar.models import Kurs

# class KursGirisi(forms.Form):
#     title = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control",}))
#     description= forms.CharField(widget=forms.Textarea(attrs={"class":"form-control",}))
#     imageUrl= forms.URLField(required=False,widget=forms.TextInput(attrs={"class":"form-control",}))

class KursGiris(forms.ModelForm):
    class Meta:
        model = Kurs
        fields = ('title','description','imageUrl')
        labels = {'title':'Kurs Başlığı',
                  'description':'Kurs Açıklaması',
                  'imageUrl':'Kurs Resmi'}
        
        widgets = {'title':forms.TextInput(attrs={"class":"form-control",}),
                   'description':forms.Textarea(attrs={"class":"form-control",}),
                   'imageUrl':forms.TextInput(attrs={"class":"form-control",})}