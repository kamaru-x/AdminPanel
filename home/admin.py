from django.contrib import admin
from home.models import User,Feedback,About,Blog,Album,Album_Image
# Register your models here.

admin.site.register(User)
admin.site.register(Feedback)
admin.site.register(About)
admin.site.register(Blog)
admin.site.register(Album)
admin.site.register(Album_Image)