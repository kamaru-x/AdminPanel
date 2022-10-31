from django.urls import path
from blog import views

urlpatterns = [
    path('blog/<int:uid>/',views.blog,name='blog'),
    path('manage_blog/<int:uid>/',views.manage_blog,name='manage_blog'),
    path('edit_blog/<int:uid>/<int:bid>/',views.edit_blog,name='edit_blog'),
    path('remove_blog/<int:uid>/<int:bid>/',views.remove_blog,name='remove_blog'),
    path('remove_blog_img/<int:uid>/<int:bid>/',views.remove_blog_img,name='remove_img'),
]