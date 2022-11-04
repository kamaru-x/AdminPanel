from django.shortcuts import render,redirect
from home.models import About,Service,Product,Blog,Album,Album_Image,Contact,Testimonial,Banners,Feedback,Enquiry,Manage_Menu,Quick_Links

# Create your views here.

def indexpage(request):
    about = About.objects.last()
    services = Service.objects.all()
    products = Product.objects.all()
    contact = Contact.objects.last()
    #blogs = Blog.objects.all()
    blogs = Blog.objects.all().order_by('-id')[:3]
    testimonials = Testimonial.objects.all()
    banners = Banners.objects.all()
    quick = Quick_Links.objects.last()
    menu = Manage_Menu.objects.last()

    featured = []

    for p in products :
        if p.Show_Feature :
            featured.append(p)

    feature = []

    for s in services :
        if s.Show_Feature :
            feature.append(s)

    context = {
        'about' : about,
        'services' : services,
        'products' : products,
        'blogs' : blogs,
        'testimonials' : testimonials,
        'banners' : banners,
        'contact' : contact,
        'quick' : quick,
        'menu' : menu,
        'featured' : featured,
        'feature' : feature,
    }
    return render(request,'fp/index.html',context)

########################################################################

def header(request):
    menu = Manage_Menu.objects.last()
    context = {
        'menu' : menu,
    }
    return render(request,'fp/header.html',context)

########################################################################

def aboutpage(request):
    about = About.objects.last()
    contact = Contact.objects.last()
    services = Service.objects.all()
    products = Product.objects.all()
    quick = Quick_Links.objects.last()
    menu = Manage_Menu.objects.last()

    context = {
        'about' : about,
        'services' : services,
        'products' : products,
        'contact' : contact,
        'quick' : quick,
        'menu' : menu,
    }
    return render(request,'fp/about.html',context)

########################################################################

def service(request):
    services = Service.objects.all()
    contact = Contact.objects.last()
    products = Product.objects.all()
    quick = Quick_Links.objects.last()
    menu = Manage_Menu.objects.last()

    context = {
        'services' : services,
        'contact' : contact,
        'products' : products,
        'quick' : quick,
        'menu' : menu,
    }
    return render(request,'fp/service.html',context)

########################################################################

def service_single(request,url):
    service = Service.objects.get(Url=url)
    products = Product.objects.all()
    contact = Contact.objects.last()
    quick = Quick_Links.objects.last()
    menu = Manage_Menu.objects.last()
    services = Service.objects.all()

    if request.method == 'POST' :
        name = request.POST.get('name')
        mobile = request.POST.get('mobile')
        email = request.POST.get('email')

        ser_name = service.Title
        refer = service.Refer_number

        data = Enquiry(Name=name,Mobile_Number=mobile,Email=email,Product_Name=ser_name,Refer_number=refer)
        data.save()

    context = {
        'service' : service,
        'products' : products,
        'contact' : contact,
        'quick' : quick,
        'menu' : menu,
        'services' : services,
    }
    return render(request,'fp/service-single.html',context)

########################################################################

def product(request):
    services = Service.objects.all()
    products = Product.objects.all()
    contact = Contact.objects.last()
    quick = Quick_Links.objects.last()
    menu = Manage_Menu.objects.last()

    context = {
        'products' : products,
        'services' : services,
        'contact' : contact,
        'quick' : quick,
        'menu' : menu,
    }
    return render(request,'fp/products.html',context)

########################################################################

def products_single(request,url):
    product = Product.objects.get(Url=url)
    products = Product.objects.all()
    services = Service.objects.all()
    contact = Contact.objects.last()
    quick = Quick_Links.objects.last()
    menu = Manage_Menu.objects.last()

    if request.method == 'POST' :
        name = request.POST.get('name')
        mobile = request.POST.get('mobile')
        email = request.POST.get('email')

        pro_name = product.Title
        refer = product.Refer_number

        data = Enquiry(Name=name,Mobile_Number=mobile,Email=email,Product_Name=pro_name,Refer_number=refer)
        data.save()

    context = {
        'product' : product,
        'products' : products,
        'services' : services,
        'contact' : contact,
        'quick' : quick,
        'menu' : menu,
    }
    return render(request,'fp/products-single.html',context)

########################################################################

def blog(request):
    blogs = Blog.objects.all()
    product = Product.objects.all()
    services = Service.objects.all()
    contact = Contact.objects.last()
    quick = Quick_Links.objects.last()
    menu = Manage_Menu.objects.last()

    context = {
        'blogs' : blogs,
        'products' : product,
        'services' : services,
        'contact' : contact,
        'quick' : quick,
        'menu' : menu,
    }
    return render(request,'fp/blog.html',context)

########################################################################

def blog_single(request,url):
    blog = Blog.objects.get(Url=url)
    product = Product.objects.all()
    services = Service.objects.all()
    contact = Contact.objects.last()
    quick = Quick_Links.objects.last()
    menu = Manage_Menu.objects.last()

    context = {
        'blog' : blog,
        'products' : product,
        'services' : services,
        'contact' : contact,
        'quick' : quick,
        'menu' : menu,
    }
    return render(request,'fp/blog-single.html',context)

########################################################################

def gallery(request):
    albums = Album.objects.all()
    product = Product.objects.all()
    services = Service.objects.all()
    contact = Contact.objects.last()
    quick = Quick_Links.objects.last()
    menu = Manage_Menu.objects.last()

    context = {
        'albums' : albums,
        'products' : product,
        'services' : services,
        'contact' : contact,
        'quick' : quick,
        'menu' : menu,
    }
    return render(request,'fp/gallery.html',context)

########################################################################

def album_inner(request,id):
    images = Album_Image.objects.filter(Album_Name=id)
    product = Product.objects.all()
    services = Service.objects.all()
    contact = Contact.objects.last()
    quick = Quick_Links.objects.last()
    menu = Manage_Menu.objects.last()

    context = {
        'images' : images,
        'products' : product,
        'services' : services,
        'contact' : contact,
        'quick' : quick,
        'menu' : menu,
    }
    return render(request,'fp/album-inner.html',context)

########################################################################

def contact(request):
    contact = Contact.objects.last()
    product = Product.objects.all()
    services = Service.objects.all()
    quick = Quick_Links.objects.last()
    menu = Manage_Menu.objects.last()

    if request.method == 'POST':
        name = request.POST.get('email')
        email = request.POST.get('email')
        number = request.POST.get('contact')
        message = request.POST.get('message')

        data = Feedback(Name=name,Email=email,Contact=number,Message=message)
        data.save()
        return redirect('.')

    context = {
        'contact' : contact,
        'products' : product,
        'services' : services,
        'quick' : quick,
        'menu' : menu,
    }
    return render(request,'fp/contact.html',context)

########################################################################

def team(request):
    return render(request,'fp/team.html')

########################################################################

def footer(request):
    products = Product.objects.all()
    services = Service.objects.all()
    contact = Contact.objects.last()
    quick = Quick_Links.objects.last()
    
    context = {
        'services' : services,
        'products' : products,
        'contact' : contact,
        'quick' : quick,
    }
    return render(request,'footer.html',context)