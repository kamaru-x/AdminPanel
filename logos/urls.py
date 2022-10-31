from django.urls import path
from logos import views

urlpatterns = [
    path('add_logo/<int:uid>/',views.add_logo,name='add_logo'),
    path('manage_logo/<int:uid>/',views.manage_logo,name='manage_logo'),
    path('remove_logo/<int:uid>/<int:lid>/',views.remove_logo,name='remove_logo'),
]