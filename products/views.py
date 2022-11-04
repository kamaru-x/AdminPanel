from django.shortcuts import render,redirect
from home.models import Product
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def products(request):
    product = Product.objects.last()

    if product :
        refer_id = ('PR-00%s' %str(product.id+1))
    else :
        refer_id = ('PR-001')


    if request.method == 'POST':
        title = request.POST.get('title')
        image = request.FILES['image']
        description = request.POST.get('description')
        show_price = request.POST.get('check1')
        whatsapp = request.POST.get('check2')
        show_enquiry = request.POST.get('check3')
        show_feature = request.POST.get('check4')
        actual_price = request.POST.get('actual_price')
        offer_price = request.POST.get('offer_price')
        number = request.POST.get('number')
        url = request.POST.get('url')
        smtitle = request.POST.get('smtitle')
        smkeywords = request.POST.get('smkeywords')
        smdescription = request.POST.get('smdescription')

        Data = Product(Title=title,Image=image,Refer_number=refer_id,Description=description,Show_Price=show_price,
        Actual_Price=actual_price,Offer_Price=offer_price,Show_Whatsapp=whatsapp,Whatsapp_Number=number,
        Show_Enquiry=show_enquiry,Show_Feature=show_feature,Url=url,SMTitle=smtitle,SMDescription=smdescription,SMKeywords=smkeywords)
        Data.save()
        messages.success(request,'added new product succesfully')
        return redirect('products')

    context = {
        'refer_id' : refer_id
    }

    return render(request,'products.html',context)

########################################################################

@login_required
def manage_product(request):
    products = Product.objects.all()
    context = {
        'products' : products
    }
    return render(request,'manage_product.html',context)

########################################################################

@login_required
def edit_product(request,pid):
    product = Product.objects.get(id=pid)
    if request.method == 'POST':
        if len(request.FILES) != 0:
        #     if len(product.Image) > 0:
        #         os.remove(product.Image.path)
            product.Image = request.FILES['image']
        product.Title = request.POST.get('title')
        product.Description = request.POST.get('description')
        product.Show_Price = request.POST.get('check1')
        product.Actual_Price = request.POST.get('actual_price')
        product.Offer_Price = request.POST.get('offer_price')
        product.Show_Whatsapp = request.POST.get('check2')
        product.Whatsapp_Number = request.POST.get('number')
        product.Show_Enquiry = request.POST.get('check3')
        product.Show_Feature = request.POST.get('check4')
        product.Url = request.POST.get('url')
        product.SMTitle = request.POST.get('smtitle')
        product.SMDescription = request.POST.get('smdescription')
        product.SMKeywords = request.POST.get('smkeywords')
        product.save()
        messages.success(request,'product details edited successfully')
        return redirect('.')
    context = {
        'product' : product,
    }
    return render(request,'edit_product.html',context)

########################################################################

@login_required
def remove_product(request,pid):
    product = Product.objects.get(id=pid)

    product.delete()
    messages.success(request,'product deleted successfully')
    return redirect('manage_product')

########################################################################

@login_required
def remove_pro_img(request,pid):
    product = Product.objects.get(id=pid)

    product.Image.delete(save=True)
    product.save()

    return redirect('edit_product/%s' %product.id)