from django.shortcuts import render,redirect
from home.models import User,Group_Of_Companies
from django.contrib import messages
# Create your views here.

def add_logo(request,uid):
    user = User.objects.get(id=uid)
    if request.method == 'POST' :
        image = request.FILES.getlist('image')

        for img in image :
            data = Group_Of_Companies(Logo=img)
            data.save()
        messages.success(request,'logo added')
        return redirect('.')

    context = {
        'user' : user,
    }
    return render(request,'add_logo.html',context)

########################################################################

def manage_logo(request,uid):
    user = User.objects.get(id=uid)
    logos = Group_Of_Companies.objects.all()
    context = {
        'user' : user,
        'logos' : logos,
    }
    return render(request,'manage_logo.html',context)

########################################################################

def remove_logo(request,uid,lid):
    user = User.objects.get(id=uid)
    logo = Group_Of_Companies.objects.get(id=lid)

    logo.delete()
    messages.success(request,'logo deleted')
    return redirect('/manage_logo/%s' %user.id)

########################################################################