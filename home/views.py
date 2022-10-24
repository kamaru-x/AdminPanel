from django.shortcuts import render
from home.models import User

# Create your views here.

def index(request,uid):
    user = User.objects.get(id=uid)
    return render(request,'index.html',{'user':user})

def login(request):
    return render(request,'login.html')

def dashboard(request,uid):
    user = User.objects.get(id=uid)
    return render(request,'dashboard.html',{'user':user})

def about_us(request,uid):
    user = User.objects.get(id=uid)
    return render(request,'about_us.html',{'user':user})

def blog(request,uid):
    user = User.objects.get(id=uid)
    return render(request,'blog.html',{'user':user})

def gallery(request,uid):
    user = User.objects.get(id=uid)
    return render(request,'gallery.html',{'user':user})

def contact_us(request,uid):
    user = User.objects.get(id=uid)
    return render(request,'contact_us.html',{'user':user})

def products(request,uid):
    user = User.objects.get(id=uid)
    return render(request,'products.html',{'user':user})

def services(request,uid):
    user = User.objects.get(id=uid)
    return render(request,'services.html',{'user':user})

def feedback(request,uid):
    user = User.objects.get(id=uid)
    return render(request,'feedback.html',{'user':user})

def manage_menu(request,uid):
    user = User.objects.get(id=uid)
    return render(request,'manage_menu.html',{'user':user})