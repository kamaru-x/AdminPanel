from django.urls import path
from banners import views

urlpatterns = [
    path('banner/<int:uid>/',views.banner,name='banner'),
    path('manage_banner/<int:uid>/',views.manage_banner,name='manage_banner'),
    path('edit_banner/<int:uid>/<int:bid>/',views.edit_banner,name='edit_banner'),
    path('remove_banner/<int:uid>/<int:bid>/',views.remove_banner,name='remove_banner'),
]