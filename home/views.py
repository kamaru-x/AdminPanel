import re
from django.shortcuts import render,redirect
from home.models import Album_Image, Banners, Contact, Enquiry, Group_Of_Companies, Manage_Menu, Product, Quick_Links, Service, Testimonial, User,Feedback,About,Blog,Album
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
    products = Product.objects.all()
    services = Service.objects.all()
    blogs = Blog.objects.all()
    albums = Album.objects.all()

    product_count = len(products)
    service_count = len(services)
    blog_count = len(blogs)
    album_count = len(albums)

    context = {
        'feedbacks':feedbacks,
        'user':user,
        'pro' : product_count,
        'ser' : service_count,
        'blg' : blog_count,
        'alb' : album_count,
    }
    return render(request,'dashboard.html',context,)

########################################################################

def about_us(request,uid):
    user = User.objects.get(id=uid)
    about = About.objects.last()
    if request.method == 'POST':
        if len(request.FILES) != 0:
            if len(about.Image) > 0:
                os.remove(about.Image.path)
            about.Image = request.FILES['image']
        about.Title = request.POST.get('title')
        about.Description = request.POST.get('description')
        about.Url = request.POST.get('url')
        about.SMTitle = request.POST.get('smtitle')
        about.SMDescription = request.POST.get('smdescription')
        about.SMKeywords = request.POST.get('smkeywords')
        about.save()
        messages.success(request,'about page edited')
        return redirect('.')
    
    context = {
        'user':user,
        'data':about
    }
    return render(request,'about_us.html',context)

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
        messages.success(request,'new blog added successfully.....!')
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
        messages.success(request,'blog edited successfull...!')
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
        messages.success(request,'album created successfully...!')
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
        image = request.FILES.getlist('image')

        album = Album.objects.get(id=select)

        for img in image: 
            Data = Album_Image(Album_Name=album,Image=img,)
            Data.save()
        messages.success(request,'image uploaded successfully ...!')
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
    contact = Contact.objects.last()
    if request.method == 'POST':
        if len(request.FILES) != 0:
            if len(contact.Image) > 0:
                os.remove(contact.Image.path)
            contact.Image = request.FILES['image']
        contact.Company_Name = request.POST.get('name')
        contact.Mobile = request.POST.get('mobile')
        contact.Telephone = request.POST.get('telephone')
        contact.Email = request.POST.get('email')
        contact.Website = request.POST.get('website')
        contact.Adress = request.POST.get('address')
        contact.Latitude = request.POST.get('latitude')
        contact.Longitude = request.POST.get('longitude')
        contact.Whatsapp = request.POST.get('whatsapp')
        contact.Facebook = request.POST.get('facebook')
        contact.Url = request.POST.get('url')
        contact.Instagram = request.POST.get('instagram')
        contact.Twitter = request.POST.get('twitter')
        contact.Linkedin = request.POST.get('linkedin')
        contact.SMTitle = request.POST.get('smtitle')
        contact.SMDescription = request.POST.get('smdescription')
        contact.SMKeywords = request.POST.get('smkeywords')
        contact.save()
        messages.success(request,'contact details edited successfully ...!')
        return redirect('.')
    return render(request,'contact_us.html',{'user':user,'data':contact})

########################################################################

def products(request,uid):
    user = User.objects.get(id=uid)

    if request.method == 'POST':
        title = request.POST.get('title')
        image = request.FILES['image']
        refer = request.POST.get('rfr')
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

        Data = Product(Title=title,Image=image,Refer_number=refer,Description=description,Show_Price=show_price,
        Actual_Price=actual_price,Offer_Price=offer_price,Show_Whatsapp=whatsapp,Whatsapp_Number=number,
        Show_Enquiry=show_enquiry,SMTitle=smtitle,SMDescription=smdescription,SMKeywords=smkeywords)
        Data.save()
        messages.success(request,'added new product succesfully')
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
        product.Show_Enquiry = request.POST.get('check3')
        product.SMTitle = request.POST.get('smtitle')
        product.SMDescription = request.POST.get('smdescription')
        product.SMKeywords = request.POST.get('smkeywords')
        product.save()
        messages.success(request,'product details edited successfully')
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
        refer = request.POST.get('rfr')
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

        Data = Service(Title=title,Image=image,Refer_number=refer,Description=description,Show_Price=show_price,
        Actual_Price=actual_price,Offer_Price=offer_price,Show_Whatsapp=whatsapp,Whatsapp_Number=number,
        Show_Enquiry=show_enquiry,SMTitle=smtitle,SMDescription=smdescription,SMKeywords=smkeywords)
        Data.save()
        messages.success(request,'new services added successfully')
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
        messages.success(request,'service details edited successfully ...!')
        return redirect('.')
    context = {
        'user' : user,
        'service' : service,
    }
    return render(request,'edit_service.html',context)

########################################################################

def feedback(request,uid):
    user = User.objects.get(id=uid)
    feedbacks = Feedback.objects.all()
    context = {
        'user' : user,
        'feedbacks' : feedbacks
    }
    return render(request,'feedback.html',context)

########################################################################

def enquiry(request,uid):
    user = User.objects.get(id=uid)
    enquiries = Enquiry.objects.all()
    context = {
        'user' : user,
        'enquiries' : enquiries,
    }
    return render(request,'enquiry.html',context)

########################################################################

def manage_menu(request,uid):
    user = User.objects.get(id=uid)
    manage = Manage_Menu.objects.last()
    if request.method == 'POST':
        manage.About_Page = request.POST.get('about')
        manage.Blog_Page = request.POST.get('blog')
        manage.Image_Gallery = request.POST.get('gallery')
        manage.Contact_Page = request.POST.get('contact')
        manage.Products_Page = request.POST.get('products')
        manage.Service_Page = request.POST.get('services')
        manage.Testimonials = request.POST.get('testimonials')
        manage.Feedback_Page = request.POST.get('feedback')
        manage.Enquiry_Page = request.POST.get('enquiry')
        manage.Group_Company = request.POST.get('gop')
        manage.save()
        messages.success(request,'manage manu edited successfully ...!')
        return redirect('.')
    context = {
        'user' : user,
        'manage' : manage,
    }
    return render(request,'manage_menu.html',context)

########################################################################

def quick_links(request,uid):
    user = User.objects.get(id=uid)
    quick = Quick_Links.objects.last()
    if request.method == 'POST':
        quick.About_Page = request.POST.get('about')
        quick.Blog_Page = request.POST.get('blog')
        quick.Image_Gallery = request.POST.get('gallery')
        quick.Contact_Page = request.POST.get('contact')
        quick.Products_Page = request.POST.get('products')
        quick.Service_Page = request.POST.get('services')
        quick.Testimonials = request.POST.get('testimonials')
        quick.save()
        messages.success(request,'quick links edited successfully ...!')
        return redirect('.')
    context = {
        'user' : user,
        'quick' : quick,
    }
    return render(request,'quick_links.html',context)

########################################################################

def remove(request,uid,aid):
    album = Album.objects.get(id=aid)
    user = User.objects.get(id=uid)
    album.delete()
    messages.success(request,'album deleted successfully')
    return redirect('/manage_album/%s' %user.id)

########################################################################

def remove_image(request,uid,aid,iid):
    user = User.objects.get(id=uid)
    album = Album.objects.get(id=aid) 
    image = Album_Image.objects.get(id=iid)
    image.delete()
    messages.success(request,'image deleted successfully')
    return redirect('/manage_album/%s' %user.id)

########################################################################

def remove_blog(request,uid,bid):
    user = User.objects.get(id=uid)
    blog = Blog.objects.get(id=bid)

    blog.delete()
    messages.error(request,'blog deleted')
    return redirect('/manage_blog/%s' %user.id)

########################################################################

def remove_product(request,uid,pid):
    user = User.objects.get(id=uid)
    product = Product.objects.get(id=pid)

    product.delete()
    messages.success(request,'product deleted successfully')
    return redirect('/manage_product/%s' %user.id)

########################################################################

def remove_service(request,uid,sid):
    user = User.objects.get(id=uid)
    service = Service.objects.get(id=sid)

    service.delete()
    messages.success(request,'service deleted')
    return redirect('/manage_service/%s' %user.id)

########################################################################

def remove_logo(request,uid,lid):
    user = User.objects.get(id=uid)
    logo = Group_Of_Companies.objects.get(id=lid)

    logo.delete()
    messages.success(request,'logo deleted')
    return redirect('/manage_logo/%s' %user.id)

########################################################################

def add_logo(request,uid):
    user = User.objects.get(id=uid)
    if request.method == 'POST' :
        image = request.FILES['image']

        data = Group_Of_Companies(Logo=image)
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

def add_testimonial(request,uid):
    user = User.objects.get(id=uid)
    if request.method == 'POST' :
        name = request.POST.get('name')
        designation = request.POST.get('designation')
        cname = request.POST.get('cname')
        image = request.FILES['image']
        testimonial = request.POST.get('testimonial')

        data = Testimonial(Tes_Name=name,Designation=designation,Company_Name=cname,Testimonial=testimonial,Tes_Image=image)
        data.save()
        messages.success(request,'testimonial added')
        return redirect('.')
    context = {
        'user' : user,
    }
    return render(request,'add_testimonial.html',context)

########################################################################

def manage_testimonial(request,uid):
    user = User.objects.get(id=uid)
    testimonials = Testimonial.objects.all()
    context = {
        'user' : user,
        'testimonials' : testimonials
    }
    return render(request,'manage_testimonial.html',context)

########################################################################

def remove_testimonial(request,uid,tid):
    user = User.objects.get(id=uid)
    testimonial = Testimonial.objects.get(id=tid)

    testimonial.delete()
    messages.success(request,'testimonial deleted')
    return redirect('/manage_testimonial/%s' %user.id)

########################################################################

def edit_testimonial(request,uid,tid):
    user = User.objects.get(id=uid)
    testimonial = Testimonial.objects.get(id=tid)
    if request.method == 'POST':
        if len(request.FILES) != 0:
            if len(testimonial.Image) > 0:
                os.remove(testimonial.Image.path)
            testimonial.Tes_Image = request.FILES['image']
        testimonial.Tes_Name = request.POST.get('name')
        testimonial.Designation = request.POST.get('designation')
        testimonial.Company_Name = request.POST.get('cname')
        testimonial.Testimonial = request.POST.get('testimonial')
        testimonial.save()
        messages.success(request,'testimonial edited')
        return redirect('.')
    context = {
        'user' : user,
        'tes' : testimonial,
    }
    return render(request,'edit_testimonial.html',context)

########################################################################

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
        return redirect('.')

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
            if len(banner.Banner_Image) > 0:
                os.remove(banner.Banner_Image.path)
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