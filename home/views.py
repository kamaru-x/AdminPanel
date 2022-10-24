from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,'index.html')

def about_us(request):
    return render(request,'about_us.html')

def blog(request):
    return render(request,'blog.html')

def gallery(request):
    return render(request,'gallery.html')

def contact_us(request):
    return render(request,'contact_us.html')

def products(request):
    return render(request,'products.html')

def services(request):
    return render(request,'services.html')

def feedback(request):
    return render(request,'feedback.html')

def manage_menu(request):
    return render(request,'manage_menu.html')