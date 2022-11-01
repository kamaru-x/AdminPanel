from django.shortcuts import render,redirect
from home.models import User,Blog
from django.contrib import messages
# Create your views here.

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
        return redirect('/blog/' %user.id)
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
        #     if len(blog.Image) > 0:
        #         os.remove(blog.Image.path)
            blog.Image = request.FILES['image']
        #     else:
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

def remove_blog(request,uid,bid):
    user = User.objects.get(id=uid)
    blog = Blog.objects.get(id=bid)

    blog.delete()
    messages.error(request,'blog deleted')
    return redirect('/manage_blog/%s' %user.id)

########################################################################

def remove_blog_img(request,uid,bid):
    user = User.objects.get(id=uid)
    blog = Blog.objects.get(id=bid)

    blog.Image.delete(save=True)
    blog.save()

    return redirect('/edit_blog/1/%s' %blog.id)

########################################################################