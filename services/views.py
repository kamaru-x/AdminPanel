from django.shortcuts import render,redirect
from home.models import User,Service
from django.contrib import messages
# Create your views here.

def services(request,uid):
    user = User.objects.get(id=uid)
    service = Service.objects.last()

    refer_id = ('SE-00%s' %str(service.id+1))
    if request.method == 'POST':
        title = request.POST.get('title')
        image = request.FILES['image']
        description = request.POST.get('description')
        show_price = request.POST.get('check1')
        whatsapp = request.POST.get('check2')
        show_enquiry = request.POST.get('check3')
        actual_price = request.POST.get('actual_price')
        offer_price = request.POST.get('offer_price')
        number = request.POST.get('number')
        smtitle = request.POST.get('smtitle')
        smkeywords = request.POST.get('smkeywords')
        smdescription = request.POST.get('smdescription')

        Data = Service(Title=title,Image=image,Refer_number=refer_id,Description=description,Show_Price=show_price,
        Actual_Price=actual_price,Offer_Price=offer_price,Show_Whatsapp=whatsapp,Whatsapp_Number=number,
        Show_Enquiry=show_enquiry,SMTitle=smtitle,SMDescription=smdescription,SMKeywords=smkeywords)
        Data.save()
        messages.success(request,'new services added successfully')
        return redirect('/services/%s' %user.id)
    
    context = {
        'user' : user,
        'refer_id' : refer_id
    }
    return render(request,'services.html',context)

########################################################################

def manage_service(request,uid):
    user = User.objects.get(id=uid)
    services = Service.objects.all()
    context = {
        'user' : user,
        'services' : services,
    }
    return render(request,'manage_service.html',context)

########################################################################

def edit_service(request,uid,sid):
    user = User.objects.get(id=uid)
    service = Service.objects.get(id=sid)
    if request.method == 'POST':
        if len(request.FILES) != 0:
        #     if len(service.Image) > 0:
        #         os.remove(service.Image.path)
            service.Image = request.FILES['image']
        service.Title = request.POST.get('title')
        service.Description = request.POST.get('description')
        service.Show_Price = request.POST.get('check1')
        service.Actual_Price = request.POST.get('actual_price')
        service.Offer_Price = request.POST.get('offer_price')
        service.Show_Whatsapp = request.POST.get('check2')
        service.Whatsapp_Number = request.POST.get('number')
        service.Show_Enquiry = request.POST.get('check3')
        service.SMTitle = request.POST.get('smtitle')
        service.SMDescription = request.POST.get('smdescription')
        service.SMKeywords = request.POST.get('smkeywords')
        service.save()
        messages.success(request,'service details edited successfully ...!')
        return redirect('.')
    context = {
        'user' : user,
        'service' : service,
    }
    return render(request,'edit_service.html',context)

########################################################################

def remove_service(request,uid,sid):
    user = User.objects.get(id=uid)
    service = Service.objects.get(id=sid)

    service.delete()
    messages.success(request,'service deleted')
    return redirect('/manage_service/%s' %user.id)

########################################################################