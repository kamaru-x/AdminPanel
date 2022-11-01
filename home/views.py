from django.shortcuts import render,redirect
from home.models import Contact,Enquiry,Manage_Menu,Product,Quick_Links,Service,User,Feedback,About,Blog,Album
from home.forms import AboutForm
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

    sl = []
    for i in range(1,len(products)+1):
        sl.append(i)
        print(sl)

    context = {
        'feedbacks':feedbacks,
        'user':user,
        'pro' : product_count,
        'ser' : service_count,
        'blg' : blog_count,
        'alb' : album_count,
        'sl' : sl
    }
    return render(request,'dashboard.html',context,)

########################################################################

def about_us(request,uid):
    user = User.objects.get(id=uid)
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
            return redirect('/about_us/%s' %user.id)
    form = AboutForm(instance=about)
    context = {
        'user' : user,
        'about' : about,
        'form' : form
    }
    return render(request,'about_us.html',context)

########################################################################

def contact_us(request,uid):
    user = User.objects.get(id=uid)
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
            return redirect('/contact_us/%s' %user.id)
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

            data = Contact(Company_Name=title,Adress=address,Telephone=address,
            Mobile=mobile,Whatsapp=whatsapp,Email=email,Website=website,Longitude=longitude,
            Latitude=latitude,Facebook=facebook,Instagram=instagram,Linkedin=linkedin,
            Twitter=twitter,Image=image,Url=url,SMTitle=smtitle,SMDescription=smdescription,SMKeywords=smkeywords)
            data.save()
            return redirect('/contact_us/%s' %user.id)
    return render(request,'contact_us.html',{'user':user,'data':contact})

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
        return redirect('/manage_menu/%s' %user.id)
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
        quick.Optional_Products = request.POST.get('op-products')
        quick.Optional_Service = request.POST.get('op-services')
        quick.save()
        messages.success(request,'quick links edited successfully ...!')
        return redirect('/quick_links/%s' %user.id)
    context = {
        'user' : user,
        'quick' : quick,
    }
    return render(request,'quick_links.html',context)

########################################################################

def remove_abt_img(request,uid,aid):
    user = User.objects.get(id=uid)
    about = About.objects.get(id=aid)

    about.Image.delete(save=True)
    about.save()

    return redirect('/about_us/%s' %user.id)

########################################################################

def remove_feedback(request,uid,fid):
    user = User.objects.get(id=uid)
    feedback = Feedback.objects.get(id=fid)
    feedback.delete()
    return redirect('/feedback/%s' %user.id)

########################################################################

def remove_enquiry(request,uid,eid):
    user = User.objects.get(id=uid)
    enquiry = Enquiry.objects.get(id=eid)
    enquiry.delete()
    return redirect('/enquiry/%s' %user.id)

########################################################################

def user_profile(request,uid):
    user = User.objects.get(id=uid)
    if request.method == 'POST' :
        user.Username = request.POST.get('username')
        user.Password = request.POST.get('password')

        user.save()

        return redirect('/dashboard/%s' %user.id)
    return render(request,'profile.html',{'user':user})