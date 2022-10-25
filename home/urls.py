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
    path('upload_image/<int:uid>/',views.upload_image,name='upload_image'),
    path('view_album/<int:uid>/<int:aid>/',views.view_ablum,name='view_album'),
    path('contact_us/<int:uid>/',views.contact_us,name='contact_us'),
    path('products/<int:uid>/',views.products,name='products'),
    path('services/<int:uid>/',views.services,name='services'),
    path('feedback/<int:uid>/',views.feedback,name='feedback'),
    path('manage_menu/<int:uid>/',views.manage_menu,name='manage_menu'),
]