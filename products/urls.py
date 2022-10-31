from django.urls import path
from products import views

urlpatterns = [
    path('products/<int:uid>/',views.products,name='products'),
    path('manage_product/<int:uid>/',views.manage_product,name='manage_product'),
    path('edit_product/<int:uid>/<int:pid>/',views.edit_product,name='edit_product'),
    path('remove_product/<int:uid>/<int:pid>/',views.remove_product,name='remove_product'),
    path('remove_pro_img/<int:uid>/<int:pid>/',views.remove_pro_img,name='remove_pro_img')
]