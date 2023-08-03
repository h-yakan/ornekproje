from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, PasswordChangeForm 
from account.forms import CreateUserForm
from django.contrib.auth.decorators import login_required

# Create your views here.

def user_login(req):
    if req.user.is_authenticated and "next" in req.GET:
            messages.add_message(req,messages.ERROR,"Yetkiniz olmayan bir sayfaya erişmeye çalıştınız")
            return redirect('index')
        
    if req.method == "POST":
        form = AuthenticationForm(req,req.POST)    
        if form.is_valid():
            user = authenticate(username = form.cleaned_data.get("username"), password = form.cleaned_data.get("password"))
            if user is not None:
                login(req,user)
                # messages.add_message(req,messages.SUCCESS,"Giriş başarılı")
                return redirect('/index')
            else:
                # messages.add_message(req,messages.ERROR,"Kullanıcı adı veya şifre yanlış")
                return render(req,'account/login.html',{'form':form})
        # messages.add_message(req,messages.ERROR,"Kullanıcı adı veya şifre yanlış")
        return render(req,'account/login.html',{'form':form})
    
    form = AuthenticationForm()
    return render(req,'account/login.html',{'form':form})

def user_register(req):
    if req.method == "POST":
        form = CreateUserForm(req.POST)
        if form.is_valid():
            user = User.objects.create_user(username=form.cleaned_data["username"], password
                                            =form.cleaned_data["password1"], first_name=form.cleaned_data["first_name"], last_name =form.cleaned_data["last_name"])
            user.save()
            return redirect('user_login')
        
        return render(req,'account/register.html',{'form':form})
    form = CreateUserForm()
    return render(req,'account/register.html',{'form':form})

@login_required
def changePassword(req):
    if req.method == "POST":
        form = PasswordChangeForm(req.user,req.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(req,user)
            messages.add_message(req,messages.INFO,"Şifreniz başarıyla değiştirildi")
            return redirect('index')
        else:
            return render(req,'account/changePassword.html',{'form':form})
    form = PasswordChangeForm(req.user)
    return render(req,"account/changePassword.html",{"form":form})

def user_logout(req):
    logout(req)
    messages.add_message(req,messages.INFO,"Çıkış başarılı")
    return redirect('/index')
