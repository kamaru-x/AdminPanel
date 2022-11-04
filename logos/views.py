from django.shortcuts import render,redirect
from home.models import Group_Of_Companies
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def add_logo(request):
    if request.method == 'POST' :
        image = request.FILES.getlist('image')

        for img in image :
            data = Group_Of_Companies(Logo=img)
            data.save()
        messages.success(request,'logo added')
        return redirect('add_logo')

    return render(request,'add_logo.html')

########################################################################

@login_required
def manage_logo(request):
    logos = Group_Of_Companies.objects.all()
    context = {
        'logos' : logos,
    }
    return render(request,'manage_logo.html',context)

########################################################################

@login_required
def remove_logo(request,lid):
    logo = Group_Of_Companies.objects.get(id=lid)

    logo.delete()
    messages.success(request,'logo deleted')
    return redirect('manage_logo')

########################################################################