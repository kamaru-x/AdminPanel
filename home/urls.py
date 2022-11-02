from django.urls import path
from home import views

urlpatterns = [
    path('',views.user_login,name='login'),
    path('',views.index,name='index'),
    path('test-area/',views.test_area,name='test-area'),
    path('profile/',views.user_profile,name='profile'),
    path('dashboard/',views.dashboard,name='dashboard'),
    path('about_us/',views.about_us,name='about_us'), 
    path('contact_us/',views.contact_us,name='contact_us'), 
    path('feedback/',views.feedback,name='feedback'),
    path('remove_feedback/<int:fid>/',views.remove_feedback,name='remove_feedback'),
    path('enquiry/',views.enquiry,name='enquiry'),
    path('remove_enquiry/<int:eid>/',views.remove_enquiry,name='remove_enquiry'),
    path('quick_links/',views.quick_links,name='quick_links'),
    path('manage_menu/',views.manage_menu,name='manage_menu'),
    path('remove_abt_img/<int:aid>/',views.remove_abt_img,name='remove_abt_img'),
]