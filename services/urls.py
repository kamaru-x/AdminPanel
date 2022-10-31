from django.urls import path
from services import views

urlpatterns = [
    path('services/<int:uid>/',views.services,name='services'),
    path('manage_service/<int:uid>/',views.manage_service,name='manage_service'),
    path('edit_service/<int:uid>/<int:sid>/',views.edit_service,name='edit_service'),
    path('remove_service/<int:uid>/<int:sid>/',views.remove_service,name='remove_service'),
]