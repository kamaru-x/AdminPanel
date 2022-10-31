from django.urls import path
from testimonials import views

urlpatterns = [
    path('add_testimonial/<int:uid>/',views.add_testimonial,name='add_testimonial'),
    path('manage_testimonial/<int:uid>/',views.manage_testimonial,name='manage_testimonial'),
    path('edit_testimonial/<int:uid>/<int:tid>/',views.edit_testimonial,name='edit_testimonial'),
    path('remove_testimonial/<int:uid>/<int:tid>/',views.remove_testimonial,name='remove_testimonial'),
]