from email.policy import default
from django.db import models

# Create your models here.

########################################################################

class User(models.Model):
    Username = models.CharField(max_length=25)
    Password = models.CharField(max_length=25)

    def __str__(self):
        return self.Username

########################################################################

class Feedback(models.Model):
    Date = models.DateField()
    Name = models.CharField(max_length=100)
    Email = models.EmailField()
    Contact = models.CharField(max_length=15)
    Message = models.TextField()

    class Meta:
        ordering =('-id',)

    def __str__(self):
        return self.Name

########################################################################

class About(models.Model):
    Title = models.CharField(max_length=50)
    Description = models.TextField()
    Image = models.ImageField(blank=True,null=True,upload_to='about_us')
    Url = models.CharField(max_length=20000)
    SMTitle = models.CharField(max_length=2000)
    SMDescription = models.TextField()
    SMKeywords = models.CharField(max_length=2000)

    def __str__(self):
        return self.Title

########################################################################

class Blog(models.Model):
    Title = models.CharField(max_length=50)
    Description = models.TextField()
    Image = models.ImageField(blank=True,null=True,upload_to='blog')
    Url = models.CharField(max_length=20000)
    SMTitle = models.CharField(max_length=2000)
    SMDescription = models.TextField()
    SMKeywords = models.CharField(max_length=2000)

    def __str__(self):
        return self.Title

########################################################################

class Album(models.Model):
    Title = models.CharField(max_length=50)
    Thumbnail = models.ImageField(blank=True,null=True,upload_to='album')
    Url = models.CharField(max_length=20000)
    SMTitle = models.CharField(max_length=2000)
    SMDescription = models.TextField()
    SMKeywords = models.CharField(max_length=2000)

    def __str__(self):
        return self.Title

########################################################################

class Album_Image(models.Model):
    Album_Name = models.ForeignKey(Album, on_delete=models.CASCADE)
    Image = models.ImageField(blank=True,null=True,upload_to='album-image')

    def __str__(self):
        return self.Album_Name.Title

########################################################################

class Contact(models.Model):
    Company_Name = models.CharField(max_length=50)
    Adress = models.TextField()
    Telephone = models.CharField(max_length=15)
    Mobile = models.CharField(max_length=15)
    Whatsapp = models.CharField(max_length=15)
    Email = models.CharField(max_length=100)
    Website = models.CharField(max_length=250)
    Longitude = models.CharField(max_length=30)
    Latitude = models.CharField(max_length=30)
    Facebook = models.CharField(max_length=50)
    Instagram = models.CharField(max_length=50)
    Linkedin = models.CharField(max_length=50)
    Image = models.ImageField(blank=True,null=True,upload_to='Company')
    Url = models.CharField(max_length=20000)
    SMTitle = models.CharField(max_length=2000)
    SMDescription = models.TextField()
    SMKeywords = models.CharField(max_length=2000)

    def __str__(self):
        return self.Company_Name
    
########################################################################

class Product(models.Model):
    Title = models.CharField(max_length=50, null=True, default=None, blank=True)
    Description = models.TextField()
    Image = models.ImageField(blank=True,null=True,upload_to='Product')
    Show_Price = models.BooleanField(default=False, null=True, blank=True)
    Actual_Price = models.CharField(max_length=15, null=True, default=None, blank=True)
    Offer_Price = models.CharField(max_length=15, null=True, default=None, blank=True)
    Show_Whatsapp = models.BooleanField(default=False, null=True, blank=True)
    Whatsapp_Number = models.CharField(max_length=15, null=True, default=None, blank=True)
    Show_Enquiry = models.BooleanField(default=False, null=True, blank=True)
    SMTitle = models.CharField(max_length=2000, null=True, default=None, blank=True)
    SMDescription = models.TextField()
    SMKeywords = models.CharField(max_length=2000, null=True, default=None, blank=True)

    def __str__(self):
        return self.Title

########################################################################

class Service(models.Model):
    Title = models.CharField(max_length=50, null=True, default=None, blank=True)
    Description = models.TextField()
    Image = models.ImageField(blank=True,null=True,upload_to='Product')
    Show_Price = models.BooleanField(default=False, null=True, blank=True)
    Actual_Price = models.CharField(max_length=15, null=True, default=None, blank=True)
    Offer_Price = models.CharField(max_length=15, null=True, default=None, blank=True)
    Show_Whatsapp = models.BooleanField(default=False, null=True, blank=True)
    Whatsapp_Number = models.CharField(max_length=15, null=True, default=None, blank=True)
    Show_Enquiry = models.BooleanField(default=False, null=True, blank=True)
    SMTitle = models.CharField(max_length=2000, null=True, default=None, blank=True)
    SMDescription = models.TextField()
    SMKeywords = models.CharField(max_length=2000, null=True, default=None, blank=True)

    def __str__(self):
        return self.Title