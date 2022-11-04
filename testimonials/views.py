from django.shortcuts import render,redirect
from home.models import Testimonial
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def add_testimonial(request):
    if request.method == 'POST' :
        name = request.POST.get('name')
        designation = request.POST.get('designation')
        cname = request.POST.get('cname')
        image = request.FILES['image']
        testimonial = request.POST.get('testimonial')

        data = Testimonial(Tes_Name=name,Designation=designation,Company_Name=cname,Testimonial=testimonial,Tes_Image=image)
        data.save()
        messages.success(request,'testimonial added')
        return redirect('add_testimonial')
    return render(request,'add_testimonial.html')

########################################################################

@login_required
def manage_testimonial(request):
    testimonials = Testimonial.objects.all()
    context = {
        'testimonials' : testimonials
    }
    return render(request,'manage_testimonial.html',context)

########################################################################

@login_required
def edit_testimonial(request,tid):
    testimonial = Testimonial.objects.get(id=tid)
    if request.method == 'POST':
        if len(request.FILES) != 0:
        #     if len(testimonial.Image) > 0:
        #         os.remove(testimonial.Image.path)
            testimonial.Tes_Image = request.FILES['image']
        testimonial.Tes_Name = request.POST.get('name')
        testimonial.Designation = request.POST.get('designation')
        testimonial.Company_Name = request.POST.get('cname')
        testimonial.Testimonial = request.POST.get('testimonial')
        testimonial.save()
        messages.success(request,'testimonial edited')
        return redirect('.')
    context = {
        'tes' : testimonial,
    }
    return render(request,'edit_testimonial.html',context)

########################################################################

@login_required
def remove_testimonial(request,tid):
    testimonial = Testimonial.objects.get(id=tid)

    testimonial.delete()
    messages.success(request,'testimonial deleted')
    return redirect('manage_testimonial')

########################################################################

@login_required
def remove_tes_img(request,tid):
    testimonial = Testimonial.objects.get(id=tid)

    testimonial.Tes_Image.delete(save=True)
    testimonial.save()

    return redirect('edit_testimonial/%s' %testimonial.id)