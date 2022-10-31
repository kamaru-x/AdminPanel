from django.shortcuts import render,redirect
from home.models import User,Banners
from django.contrib import messages

# Create your views here.

def banner(request,uid):
    user = User.objects.get(id=uid)
    if request.method == 'POST' :
        caption = request.POST.get('caption')
        scaption = request.POST.get('scaption')
        label = request.POST.get('label')
        link = request.POST.get('link')
        image = request.FILES['image']

        data = Banners (Caption=caption,Sub_Caption=scaption,Button_Label=label,Link=link,Banner_Image=image)
        data.save()
        messages.success(request,'banner added')
        return redirect('/banner/%s' %user.id)

    context = {
        'user' : user,
    }
    return render(request,'banner.html',context)

########################################################################

def manage_banner(request,uid):
    user = User.objects.get(id=uid)
    banners = Banners.objects.all()
    context = {
        'user' : user,
        'banners' : banners,
    }
    return render(request,'manage_banner.html',context)

########################################################################

def edit_banner(request,uid,bid):
    user = User.objects.get(id=uid)
    banner = Banners.objects.get(id=bid)
    if request.method == 'POST':
        if len(request.FILES) != 0:
        #     if len(banner.Banner_Image) > 0:
        #         os.remove(banner.Banner_Image.path)
            banner.Banner_Image = request.FILES['image']
        banner.Caption = request.POST.get('caption')
        banner.Sub_Caption = request.POST.get('scaption')
        banner.Button_Label = request.POST.get('label')
        banner.Link = request.POST.get('link')
        banner.save()
        messages.success(request,'banner edited')
        return redirect('.')
    context = {
        'user' : user,
        'banner' : banner,
    }
    return render(request,'edit_banner.html',context)

########################################################################

def remove_banner(request,uid,bid):
    user = User.objects.get(id=uid)
    banner = Banners.objects.get(id=bid)

    banner.delete()
    messages.success(request,'banner deleted')
    return redirect('/manage_banner/%s' %user.id)

########################################################################