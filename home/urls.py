from django.urls import path
from home import views

urlpatterns = [
    path('',views.index,name='index'),
    path('dashboard/',views.dashboard,name='dashboard'),
    path('about_us/',views.about_us,name='about_us'),
    path('blog/',views.blog,name='blog'),
    path('gallery/',views.gallery,name='gallery'),
    path('contact_us/',views.contact_us,name='contact_us'),
    path('products/',views.products,name='products'),
    path('services/',views.services,name='services'),
    path('feedback/',views.feedback,name='feedback'),
    path('manage_menu/',views.manage_menu,name='manage_menu'),
]