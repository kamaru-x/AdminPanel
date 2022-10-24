from django.shortcuts import render,redirect
from home.models import User,Feedback
from django.contrib import messages

# Create your views here.

def index(request,uid):
    user = User.objects.get(id=uid)
    return render(request,'index.html',{'user':user})

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = User.objects.filter(Username=username).exists()

        if not user:
            messages.warning(request,'invalid Username')
            return redirect('login')
        elif password != (User.objects.get(Username=username)).Password:
            messages.warning(request,'incorrect password')
            return redirect('login')
        else:
            userdata = User.objects.get(Username=username)
            return redirect('dashboard/%s' %userdata.id)
    return render(request,'login.html')

def dashboard(request,uid):
    user = User.objects.get(id=uid)
    feedbacks = Feedback.objects.all()
    context = {
        'feedbacks':feedbacks,
        'user':user,
    }
    return render(request,'dashboard.html',context)

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