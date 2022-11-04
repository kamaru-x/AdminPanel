from django.shortcuts import render,redirect
from home.models import Banners
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def banner(request):
    if request.method == 'POST' :
        caption = request.POST.get('caption')
        scaption = request.POST.get('scaption')
        label = request.POST.get('label')
        link = request.POST.get('link')
        image = request.FILES['image']

        data = Banners (Caption=caption,Sub_Caption=scaption,Button_Label=label,Link=link,Banner_Image=image)
        data.save()
        messages.success(request,'banner added')
        return redirect('banner')

    return render(request,'banner.html')

########################################################################

@login_required
def manage_banner(request):
    banners = Banners.objects.all()
    context = {
        'banners' : banners,
    }
    return render(request,'manage_banner.html',context)

########################################################################

@login_required
def edit_banner(request,bid):
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
        'banner' : banner,
    }
    return render(request,'edit_banner.html',context)

########################################################################

@login_required
def remove_banner(request,bid):
    banner = Banners.objects.get(id=bid)

    banner.delete()
    messages.success(request,'banner deleted')
    return redirect('manage_banner')

########################################################################

@login_required
def remove_ban_img(request,bid):
    banner = Banners.objects.get(id=bid)

    banner.Banner_Image.delete(save=True)
    banner.save()

    return redirect('edit_banner/%s' %banner.id)