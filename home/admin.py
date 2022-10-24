from django.contrib import admin
from home.models import User,Feedback,About
# Register your models here.

admin.site.register(User)
admin.site.register(Feedback)
admin.site.register(About)