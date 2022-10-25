from re import U
from tkinter import Image
from django.shortcuts import render,redirect
from home.models import Album_Image, Contact, User,Feedback,About,Blog,Album
from django.contrib import messages

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
    return render(request,'products.html',{'user':user})

########################################################################

def services(request,uid):
    user = User.objects.get(id=uid)
    return render(request,'services.html',{'user':user})

########################################################################

def feedback(request,uid):
    user = User.objects.get(id=uid)
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