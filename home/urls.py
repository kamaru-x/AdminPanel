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
    
    path('manage_blog/<int:uid>/',views.manage_blog,name='manage_blog'),
    path('manage_album/<int:uid>/',views.manage_album,name='manage_album'),
    path('manage_menu/<int:uid>/',views.manage_menu,name='manage_menu'),
    path('manage_product/<int:uid>/',views.manage_product,name='manage_product'),

    path('edit_blog/<int:uid>/<int:bid>/',views.edit_blog,name='edit_blog'),
    path('edit_album/<int:uid>/<int:aid>/',views.edit_album,name='edit_album'),

    path('remove/<int:uid>/<int:aid>/',views.remove,name='remove'),
    path('remove_image/<int:uid>/<int:aid>/<int:iid>/',views.remove_image,name='remove_image'),
    path('remove_blog/<int:uid>/<int:bid>/',views.remove_blog,name='remove_blog'),
]