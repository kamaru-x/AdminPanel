from django.urls import path
from FrontPage import views

urlpatterns = [
    path('',views.indexpage,name='indexpage'),

    path('about/',views.aboutpage,name='about'),
    path('contact/',views.contact,name='contactpage'),

    path('service/',views.service,name='servicepage'),
    path('service-details/<int:sid>',views.service_single,name='single-service'),

    path('products/',views.product,name='productspage'),
    path('single-product/<int:pid>',views.products_single,name='single-product'),

    path('blog/',views.blog,name='blogspage'),
    path('blog-single/<int:bid>',views.blog_single,name='blog-single'),

    path('album/<int:aid>/',views.album_inner,name='album'),
    path('gallery/',views.gallery,name='gallerypage'),

    path('team/',views.team,name='team'),
]