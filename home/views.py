from django.shortcuts import render,redirect
from home.models import Contact,Enquiry,Manage_Menu,Product,Quick_Links,Service,Feedback,About,Blog,Album
from home.forms import AboutForm
from django.contrib import messages
import os
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.decorators import login_required

# Create your views here.

########################################################################

def index(request):
    return render(request,'index.html')

########################################################################

def test_area(request):
    blogs = Blog.objects.all()
    return render(request,'test-area.html',{'blogs':blogs})

########################################################################

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request,'incorrect email or password')
            return redirect('.')
    return render(request,'login.html')

########################################################################

@login_required
def dashboard(request):
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
        'pro' : product_count,
        'ser' : service_count,
        'blg' : blog_count,
        'alb' : album_count,
    }
    return render(request,'dashboard.html',context,)

########################################################################

@login_required
def about_us(request):
    about = About.objects.last()
    form = AboutForm
    if request.method == "POST":
        if about :
            form = AboutForm(request.POST , request.FILES , instance=about)
        else:
            form = AboutForm(request.POST , request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request,'about edited successfully')
            return redirect('about_us')
    form = AboutForm(instance=about)
    context = {
        'about' : about,
        'form' : form
    }
    return render(request,'about_us.html',context)

########################################################################

@login_required
def contact_us(request):
    contact = Contact.objects.last()
    if request.method == 'POST':
        if contact:
            if len(request.FILES) != 0:
        #         if len(contact.Image) > 0:
        #             os.remove(contact.Image.path)
                contact.Image = request.FILES['image']
            contact.Company_Name = request.POST.get('title')
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
            return redirect('contact_us')
        else:
            image = request.FILES['image']
            title = request.POST.get('title')
            mobile = request.POST.get('mobile')
            telephone = request.POST.get('telephone')
            email = request.POST.get('email')
            website = request.POST.get('website')
            address = request.POST.get('address')
            latitude = request.POST.get('latitude')
            longitude = request.POST.get('longitude')
            whatsapp = request.POST.get('whatsapp')
            facebook = request.POST.get('fecebook')
            url = request.POST.get('url')
            instagram = request.POST.get('instagram')
            twitter = request.POST.get('twitter')
            linkedin = request.POST.get('linkedin')
            smtitle = request.POST.get('smtitle')
            smdescription = request.POST.get('smdescription')
            smkeywords = request.POST.get('smkeywords')

            data = Contact(Company_Name=title,Adress=address,Telephone=telephone,
            Mobile=mobile,Whatsapp=whatsapp,Email=email,Website=website,Longitude=longitude,
            Latitude=latitude,Facebook=facebook,Instagram=instagram,Linkedin=linkedin,
            Twitter=twitter,Image=image,Url=url,SMTitle=smtitle,SMDescription=smdescription,SMKeywords=smkeywords)
            data.save()
            return redirect('contact_us')
    return render(request,'contact_us.html',{'data':contact})

########################################################################

@login_required
def feedback(request):
    feedbacks = Feedback.objects.all()
    context = {
        'feedbacks' : feedbacks
    }
    return render(request,'feedback.html',context)

########################################################################

@login_required
def enquiry(request):
    enquiries = Enquiry.objects.all()
    context = {
        'enquiries' : enquiries,
    }
    return render(request,'enquiry.html',context)

########################################################################

@login_required
def manage_menu(request):
    manage = Manage_Menu.objects.last()
    if request.method == 'POST':
        if manage:
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
            return redirect('manage_menu')
        else:
            about = request.POST.get('about')
            blog = request.POST.get('blog')
            gallery = request.POST.get('gallery')
            contact = request.POST.get('contact')
            products = request.POST.get('products')
            services = request.POST.get('services')
            testimonials = request.POST.get('testimonials')
            feedback = request.POST.get('feedback')
            enquiry = request.POST.get('enquiry')
            gop = request.POST.get('gop')
            
            data = Manage_Menu(About_Page=about,Blog_Page=blog,Image_Gallery=gallery,Contact_Page=contact,
            Products_Page=products,Service_Page=services,Testimonials=testimonials,Feedback_Page=feedback,
            Enquiry_Page=enquiry,Group_Company=gop)
            data.save()
            
            messages.success(request,'manage manu edited successfully ...!')
            return redirect('manage_menu')
    context = {
        'manage' : manage,
    }
    return render(request,'manage_menu.html',context)

########################################################################

@login_required
def quick_links(request):
    quick = Quick_Links.objects.last()
    if request.method == 'POST':
        if quick :
            quick.About_Page = request.POST.get('about')
            quick.Blog_Page = request.POST.get('blog')
            quick.Image_Gallery = request.POST.get('gallery')
            quick.Contact_Page = request.POST.get('contact')
            quick.Products_Page = request.POST.get('products')
            quick.Service_Page = request.POST.get('services')
            quick.Testimonials = request.POST.get('testimonials')
            quick.Optional_Products = request.POST.get('op-products')
            quick.Optional_Service = request.POST.get('op-services')
            quick.save()
            messages.success(request,'quick links edited successfully ...!')
            return redirect('quick_links')
        else:
            about = request.POST.get('about')
            blog = request.POST.get('blog')
            gallery = request.POST.get('gallery')
            contact = request.POST.get('contact')
            products = request.POST.get('products')
            services = request.POST.get('services')
            testimonials = request.POST.get('testimonials')
            op_products = request.POST.get('op-products')
            op_services = request.POST.get('op-services')
            data = Quick_Links(About_Page=about,Blog_Page=blog,Image_Gallery=gallery,Contact_Page=contact,
            Products_Page=products,Service_Page=services,Testimonials=testimonials,Optional_Products=op_products,Optional_Service=op_services)
            data.save()
            messages.success(request,'quick links edited successfully ...!')
            return redirect('quick_links')
    context = {
        'quick' : quick,
    }
    return render(request,'quick_links.html',context)

########################################################################

@login_required
def remove_abt_img(request,aid):
    about = About.objects.get(id=aid)

    about.Image.delete(save=True)
    about.save()

    return redirect('about_us')

########################################################################

@login_required
def remove_feedback(request,fid):
    feedback = Feedback.objects.get(id=fid)
    feedback.delete()
    return redirect('feedback')

########################################################################

@login_required
def remove_enquiry(request,eid):
    enquiry = Enquiry.objects.get(id=eid)
    enquiry.delete()
    return redirect('enquiry')

########################################################################

@login_required
def user_profile(request):
    form = UserChangeForm
    if request.method == "POST":
        form = AboutForm(request.POST , request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request,'about edited successfully')
            return redirect('about_us')
    form = UserChangeForm()
    context = {
        'form' : form
    }
    return render(request,'change-password.html',context)

########################################################################

@login_required
def signout(request):
    logout(request)
    return redirect('/')