from django.shortcuts import render,redirect
from home.models import User,Album,Album_Image
from home.forms import AboutForm
from django.contrib import messages

# Create your views here.

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
        return redirect('/create_album/%s' %user.id)
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
        return redirect('/upload_image/%s' %user.id)
    context = {
        'user' : user,
        'albums' : albums
    }
    return render(request,'upload_image.html',context)

########################################################################

def manage_album(request,uid):
    user = User.objects.get(id=uid)
    albums = Album.objects.all()
    image_count = []
    for album in albums :
        images = Album_Image.objects.filter(Album_Name=album)
        total = len(images)
        image_count.append(total)
        print(image_count)
    context = {
        'user' : user,
        'albums' : albums,
        'count' : image_count
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
    return redirect('/edit_album/1/%s' %album.id)

########################################################################