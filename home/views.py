import re
from django.shortcuts import render,redirect
from home.models import Album_Image, Contact, Product, Service, User,Feedback,About,Blog,Album
from home.forms import Edit_Blog
from django.contrib import messages
import os

# Create your views here.

########################################################################

def index(request,uid):
    user = User.objects.get(id=uid)
    return render(request,'index.html',{'user':user})

########################################################################

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

########################################################################

def dashboard(request,uid):
    user = User.objects.get(id=uid)
    feedbacks = Feedback.objects.all()

    context = {
        'feedbacks':feedbacks,
        'user':user,
    }
    return render(request,'dashboard.html',context)

########################################################################

def about_us(request,uid):
    user = User.objects.get(id=uid)
    if request.method == 'POST':
        title = request.POST.get('title')
        image = request.FILES['image']
        description = request.POST.get('description')
        url = request.POST.get('url')
        smtitle = request.POST.get('smtitle')
        smkeywords = request.POST.get('smkeywords')
        smdescription = request.POST.get('smdescription')
        
        Data = About(Title=title,Description=description,Image=image,Url=url,SMTitle=smtitle,
        SMDescription=smdescription,SMKeywords=smkeywords)
        Data.save()
        return redirect('.')
    return render(request,'about_us.html',{'user':user})

########################################################################

def blog(request,uid):
    user = User.objects.get(id=uid)
    if request.method == 'POST':
        title = request.POST.get('title')
        image = request.FILES['image']
        description = request.POST.get('description')
        url = request.POST.get('url')
        smtitle = request.POST.get('smtitle')
        smkeywords = request.POST.get('smkeywords')
        smdescription = request.POST.get('smdescription')
        
        Data = Blog(Title=title,Description=description,Image=image,Url=url,SMTitle=smtitle,
        SMDescription=smdescription,SMKeywords=smkeywords)
        Data.save()
        return redirect('.')
    return render(request,'blog.html',{'user':user})

########################################################################

def manage_blog(request,uid):
    user = User.objects.get(id=uid)
    blogs = Blog.objects.all()
    return render(request,'manage_blog.html',{'blogs':blogs,'user':user})

########################################################################

def edit_blog(request,uid,bid):
    user = User.objects.get(id=uid)
    blog = Blog.objects.get(id=bid)
    if request.method == 'POST':
        if len(request.FILES) != 0:
            if len(blog.Image) > 0:
                os.remove(blog.Image.path)
            blog.Image = request.FILES['image']
        blog.Title = request.POST.get('title')
        blog.Description = request.POST.get('description')
        blog.Url = request.POST.get('url')
        blog.SMTitle = request.POST.get('smtitle')
        blog.SMDescription = request.POST.get('smdescription')
        blog.SMKeywords = request.POST.get('smkeywords')
        blog.save()
        return redirect('.')
    context = {
        'user' : user,
        'blog' : blog,
    }
    return render(request,'edit_blog.html',context)

########################################################################

def gallery(request,uid):
    user = User.objects.get(id=uid)
    albums = Album.objects.all()
    context = {
        'user' : user,
        'albums' : albums,
    }
    return render(request,'gallery.html',context)

########################################################################

def create_album(request,uid):
    user = User.objects.get(id=uid)
    if request.method == 'POST':
        title = request.POST.get('title')
        image = request.FILES['image']
        url = request.POST.get('url')
        smtitle = request.POST.get('smtitle')
        smkeywords = request.POST.get('smkeywords')
        smdescription = request.POST.get('smdescription')
        
        Data = Album(Title=title,Thumbnail=image,Url=url,SMTitle=smtitle,
        SMDescription=smdescription,SMKeywords=smkeywords)
        Data.save()
        return redirect('.')
    context = {
        'user' : user
    }
    return render(request,'create_album.html',context)

########################################################################

def view_ablum(request,uid,aid):
    user = User.objects.get(id=uid)
    album = Album.objects.get(id=aid)
    context = {
        'user' : user,
        'album' : album,
    }
    return render(request,'album_view.html',context)

########################################################################

def upload_image(request,uid):
    user = User.objects.get(id=uid)
    albums = Album.objects.all()
    if request.method == 'POST':
        select = request.POST.get('select')
        image = request.FILES['image']

        album = Album.objects.get(id=select)
        
        Data = Album_Image(Album_Name=album,Image=image,)
        Data.save()
        return redirect('.')
    context = {
        'user' : user,
        'albums' : albums
    }
    return render(request,'upload_image.html',context)

########################################################################

def manage_album(request,uid):
    user = User.objects.get(id=uid)
    albums = Album.objects.all()
    context = {
        'user' : user,
        'albums' : albums
    }
    return render(request,'manage_album.html',context)

########################################################################

def edit_album(request,uid,aid):
    user = User.objects.get(id=uid)
    album = Album.objects.get(id=aid)
    images = Album_Image.objects.filter(Album_Name=aid)
    context = {
        'user' : user,
        'album' : album,
        'images' : images,
    }
    return render(request,'edit_album.html',context)

########################################################################

def contact_us(request,uid):
    user = User.objects.get(id=uid)
    if request.method == 'POST':
        name = request.POST.get('name')
        mobile = request.POST.get('mobile')
        telephone = request.POST.get('telephone')
        email = request.POST.get('email')
        website = request.POST.get('website')
        address = request.POST.get('address')
        latitude = request.POST.get('latitude')
        longitude = request.POST.get('longitude')
        whatsapp = request.POST.get('whatsapp')
        facebook = request.POST.get('facebook')
        instagram = request.POST.get('instagram')
        twitter = request.POST.get('twitter')
        linkedin = request.POST.get('linkedin')
        image = request.FILES['image']
        url = request.POST.get('url')
        smtitle = request.POST.get('smtitle')
        smkeywords = request.POST.get('smkeywords')
        smdescription = request.POST.get('smdescription') 

        Data = Contact(Company_Name=name,Adress=address,Telephone=telephone,Mobile=mobile,
        Whatsapp=whatsapp,Email=email,Website=website,Longitude=longitude,Latitude=latitude,
        Facebook=facebook,Instagram=instagram,Linkedin=linkedin,Image=image,Url=url,
        SMTitle=smtitle,SMDescription=smdescription,SMKeywords=smkeywords)

        Data.save()
        return redirect('.')
    return render(request,'contact_us.html',{'user':user})

########################################################################

def products(request,uid):
    user = User.objects.get(id=uid)

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

        Data = Product(Title=title,Image=image,Description=description,Show_Price=show_price,
        Actual_Price=actual_price,Offer_Price=offer_price,Show_Whatsapp=whatsapp,Whatsapp_Number=number,
        Show_Enquiry=show_enquiry,SMTitle=smtitle,SMDescription=smdescription,SMKeywords=smkeywords)
        Data.save()
        return redirect('.')

    return render(request,'products.html',{'user':user})

########################################################################

def manage_product(request,uid):
    user = User.objects.get(id=uid)
    products = Product.objects.all()
    context = {
        'user' : user,
        'products' : products
    }
    return render(request,'manage_product.html',context)

########################################################################

def edit_product(request,uid,pid):
    user = User.objects.get(id=uid)
    product = Product.objects.get(id=pid)
    if request.method == 'POST':
        if len(request.FILES) != 0:
            if len(product.Image) > 0:
                os.remove(product.Image.path)
            product.Image = request.FILES['image']
        product.Title = request.POST.get('title')
        product.Description = request.POST.get('description')
        product.Show_Price = request.POST.get('check1')
        product.Actual_Price = request.POST.get('actual_price')
        product.Offer_Price = request.POST.get('offer_price')
        product.Show_Whatsapp = request.POST.get('check2')
        product.Whatsapp_Number = request.POST.get('number')
        #product.Show_Enquiry = request.POST.get('check3')
        product.SMTitle = request.POST.get('smtitle')
        product.SMDescription = request.POST.get('smdescription')
        product.SMKeywords = request.POST.get('smkeywords')
        product.save()
        return redirect('.')
    context = {
        'user' : user,
        'product' : product,
    }
    return render(request,'edit_product.html',context)

########################################################################

def services(request,uid):
    user = User.objects.get(id=uid)
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

        Data = Service(Title=title,Image=image,Description=description,Show_Price=show_price,
        Actual_Price=actual_price,Offer_Price=offer_price,Show_Whatsapp=whatsapp,Whatsapp_Number=number,
        Show_Enquiry=show_enquiry,SMTitle=smtitle,SMDescription=smdescription,SMKeywords=smkeywords)
        Data.save()
        return redirect('.')
    return render(request,'services.html',{'user':user})

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
            if len(service.Image) > 0:
                os.remove(service.Image.path)
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
        return redirect('.')
    context = {
        'user' : user,
        'service' : service,
    }
    return render(request,'edit_service.html',context)

########################################################################

def feedback(request,uid):
    user = User.objects.get(id=uid)
    if request.method == "POST":
        date = request.POST.get('date')
        name = request.POST.get('name')
        email = request.POST.get('email')
        contact = request.POST.get('contact')
        message = request.POST.get('message')

        data = Feedback(Date=date,Name=name,Email=email,Contact=contact,Message=message)
        data.save()
        return redirect('.')

    return render(request,'feedback.html',{'user':user})

########################################################################

def manage_menu(request,uid):
    user = User.objects.get(id=uid)
    return render(request,'manage_menu.html',{'user':user})

########################################################################

def remove(request,uid,aid):
    album = Album.objects.get(id=aid)
    user = User.objects.get(id=uid)
    album.delete()
    return redirect('/manage_album/%s' %user.id)

########################################################################

def remove_image(request,uid,aid,iid):
    user = User.objects.get(id=uid)
    album = Album.objects.get(id=aid) 
    image = Album_Image.objects.get(id=iid)
    
    image.delete()
    return redirect('/manage_album/%s' %user.id)

########################################################################

def remove_blog(request,uid,bid):
    user = User.objects.get(id=uid)
    blog = Blog.objects.get(id=bid)

    blog.delete()
    return redirect('/manage_blog/%s' %user.id)

########################################################################

def remove_product(request,uid,pid):
    user = User.objects.get(id=uid)
    product = Product.objects.get(id=pid)

    product.delete()
    return redirect('/manage_product/%s' %user.id)

########################################################################

def remove_service(request,uid,sid):
    user = User.objects.get(id=uid)
    service = Service.objects.get(id=sid)

    service.delete()
    return redirect('/manage_service/%s' %user.id)

########################################################################