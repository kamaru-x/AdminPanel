from django.urls import path
from home import views

urlpatterns = [
    path('',views.login,name='login'),
    path('<int:uid>',views.index,name='index'),
    path('dashboard/<int:uid>/',views.dashboard,name='dashboard'),
    path('about_us/<int:uid>/',views.about_us,name='about_us'),
    path('blog/<int:uid>/',views.blog,name='blog'),
    path('gallery/<int:uid>/',views.gallery,name='gallery'),

    path('create_album/<int:uid>/',views.create_album,name='create_album'),
    path('view_album/<int:uid>/<int:aid>/',views.view_ablum,name='view_album'),
    path('upload_image/<int:uid>/',views.upload_image,name='upload_image'),
    
    path('contact_us/<int:uid>/',views.contact_us,name='contact_us'),
    path('products/<int:uid>/',views.products,name='products'),
    path('services/<int:uid>/',views.services,name='services'),
    path('feedback/<int:uid>/',views.feedback,name='feedback'),
    path('enquiry/<int:uid>/',views.enquiry,name='enquiry'),
    path('quick_links/<int:uid>/',views.quick_links,name='quick_links'),
    path('add_logo/<int:uid>/',views.add_logo,name='add_logo'),
    path('add_testimonial/<int:uid>/',views.add_testimonial,name='add_testimonial'),
    path('banner/<int:uid>/',views.banner,name='banner'),

    path('manage_blog/<int:uid>/',views.manage_blog,name='manage_blog'),
    path('manage_album/<int:uid>/',views.manage_album,name='manage_album'),
    path('manage_menu/<int:uid>/',views.manage_menu,name='manage_menu'),
    path('manage_product/<int:uid>/',views.manage_product,name='manage_product'),
    path('manage_service/<int:uid>/',views.manage_service,name='manage_service'),
    path('manage_logo/<int:uid>/',views.manage_logo,name='manage_logo'),
    path('manage_testimonial/<int:uid>/',views.manage_testimonial,name='manage_testimonial'),
    path('manage_banner/<int:uid>/',views.manage_banner,name='manage_banner'),

    path('edit_blog/<int:uid>/<int:bid>/',views.edit_blog,name='edit_blog'),
    path('edit_album/<int:uid>/<int:aid>/',views.edit_album,name='edit_album'),
    path('edit_product/<int:uid>/<int:pid>/',views.edit_product,name='edit_product'),
    path('edit_service/<int:uid>/<int:sid>/',views.edit_service,name='edit_service'),
    path('edit_testimonial/<int:uid>/<int:tid>/',views.edit_testimonial,name='edit_testimonial'),
    path('edit_banner/<int:uid>/<int:bid>/',views.edit_banner,name='edit_banner'),

    path('remove/<int:uid>/<int:aid>/',views.remove,name='remove'),
    path('remove_image/<int:uid>/<int:aid>/<int:iid>/',views.remove_image,name='remove_image'),
    path('remove_blog/<int:uid>/<int:bid>/',views.remove_blog,name='remove_blog'),
    path('remove_product/<int:uid>/<int:pid>/',views.remove_product,name='remove_product'),
    path('remove_service/<int:uid>/<int:sid>/',views.remove_service,name='remove_service'),
    path('remove_logo/<int:uid>/<int:lid>/',views.remove_logo,name='remove_logo'),
    path('remove_testimonial/<int:uid>/<int:tid>/',views.remove_testimonial,name='remove_testimonial'),
    path('remove_banner/<int:uid>/<int:bid>/',views.remove_banner,name='remove_banner'),
    path('remove_img/<int:uid>/<int:bid>/',views.remove_img,name='remove_img'),
    path('remove_abt_img/<int:uid>/<int:aid>/',views.remove_abt_img,name='remove_abt_img'),
]