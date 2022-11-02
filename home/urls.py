from django.urls import path
from home import views

urlpatterns = [
    path('',views.login,name='login'),
    path('<int:uid>',views.index,name='index'),
    path('test-area/',views.test_area,name='test-area'),
    path('profile/<int:uid>/',views.user_profile,name='profile'),
    path('dashboard/<int:uid>/',views.dashboard,name='dashboard'),
    path('about_us/<int:uid>/',views.about_us,name='about_us'), 
    path('contact_us/<int:uid>/',views.contact_us,name='contact_us'), 
    path('feedback/<int:uid>/',views.feedback,name='feedback'),
    path('remove_feedback/<int:uid>/<int:fid>/',views.remove_feedback,name='remove_feedback'),
    path('enquiry/<int:uid>/',views.enquiry,name='enquiry'),
    path('remove_enquiry/<int:uid>/<int:eid>/',views.remove_enquiry,name='remove_enquiry'),
    path('quick_links/<int:uid>/',views.quick_links,name='quick_links'),
    path('manage_menu/<int:uid>/',views.manage_menu,name='manage_menu'),
    path('remove_abt_img/<int:uid>/<int:aid>/',views.remove_abt_img,name='remove_abt_img'),
]