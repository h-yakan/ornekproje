from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
# Create your views here.

def user_login(req):
    if req.user.is_authenticated:
        return redirect('/index')
    if req.method == "POST":
        username = req.POST["username"]
        password = req.POST["password"]
        user = authenticate(username = username, password = password)
        if user is not None:
            login(req,user)
            return redirect('/index')
        else:
            return render(req,"account/login.html",{"error":"Kullanıcı adı veya Parola yanlış"})
    return render(req,'account/login.html')

def user_register(req):
    if req.method == "POST":
        username = req.POST["username"]
        password = req.POST["password"]
        password2 = req.POST["password2"]
        name = req.POST["name"]
        email = req.POST["email"]
        surname = req.POST["surname"]
        if password==password2:
            if User.objects.filter(username = username).exists():
                return render(req,"account/register.html",{"error":"Bu kullanıcı adı zaten kullanılıyor"})
            if User.objects.filter(email = email).exists():
                return render(req,"account/register.html",{"error":"Bu eposta zaten kullanılıyor"})
            else:
                user = User.objects.create_user(username=username, password=password, email=email, first_name= name, last_name = surname)
                user.save()
                return redirect('user_login')
        else:
                return render(req,"account/register.html",{"error":"Şifreler eşleşmiyor"})
    return render(req,'account/register.html')

def user_logout(req):
    logout(req)
    return redirect('/index')
