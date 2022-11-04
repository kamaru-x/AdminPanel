from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.

########################################################################

class User(models.Model):
    Username = models.CharField(max_length=25)
    Password = models.CharField(max_length=25)

    def __str__(self):
        return self.Username

########################################################################

class Feedback(models.Model):
    Date = models.DateField(auto_now_add=True)
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
    #Description = models.TextField()
    Mission = models.TextField()
    Vision = models.TextField(null=True,blank=True)
    Description = RichTextField(null=True,blank=True)
    Image = models.ImageField(blank=True,null=True,upload_to='about_us')
    Url = models.CharField(max_length=20000,null=True,unique=True)
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
    Url = models.CharField(max_length=20000,unique=True)
    SMTitle = models.CharField(max_length=2000)
    SMDescription = models.TextField()
    SMKeywords = models.CharField(max_length=2000)

    def __str__(self):
        return self.Title

########################################################################

class Album(models.Model):
    Title = models.CharField(max_length=50)
    Thumbnail = models.ImageField(blank=True,null=True,upload_to='album')
    Images = models.IntegerField(default=0,)
    Url = models.CharField(max_length=20000,null=True,unique=True)
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
    Company_Name = models.CharField(max_length=50,null=True)
    Adress = models.TextField(null=True)
    Telephone = models.CharField(max_length=15,null=True)
    Mobile = models.CharField(max_length=15,null=True)
    Whatsapp = models.CharField(max_length=15,null=True)
    Email = models.CharField(max_length=100,null=True)
    Website = models.CharField(max_length=250,null=True)
    Longitude = models.CharField(max_length=30,null=True)
    Latitude = models.CharField(max_length=30,null=True)
    Facebook = models.CharField(max_length=50,null=True)
    Instagram = models.CharField(max_length=50,null=True)
    Linkedin = models.CharField(max_length=50,null=True)
    Twitter = models.CharField(max_length=50,null=True)
    Image = models.ImageField(blank=True,null=True,upload_to='Company')
    Url = models.CharField(max_length=20000,null=True,unique=True)
    SMTitle = models.CharField(max_length=2000,null=True)
    SMDescription = models.TextField(null=True)
    SMKeywords = models.CharField(max_length=2000,null=True)

    def __str__(self):
        return self.Company_Name
    
########################################################################

class Product(models.Model):
    Title = models.CharField(max_length=50, null=True, default=None, blank=True)
    Description = models.TextField()
    Image = models.ImageField(blank=True,null=True,upload_to='Product')
    Refer_number = models.CharField(max_length=6)
    Show_Price = models.BooleanField(default=False, null=True, blank=True)
    Actual_Price = models.CharField(max_length=15, null=True, default=None, blank=True)
    Offer_Price = models.CharField(max_length=15, null=True, default=None, blank=True)
    Show_Whatsapp = models.BooleanField(default=False, null=True, blank=True)
    Whatsapp_Number = models.CharField(max_length=15, null=True, default=None, blank=True)
    Show_Enquiry = models.BooleanField(default=False, null=True, blank=True)
    Show_Feature = models.BooleanField(default=False, null=True, blank=True)
    Url = models.CharField(max_length=20000,unique=True ,null=True,)
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
    Refer_number = models.CharField(max_length=6)
    Show_Price = models.BooleanField(default=False, null=True, blank=True)
    Actual_Price = models.CharField(max_length=15, null=True, default=None, blank=True)
    Offer_Price = models.CharField(max_length=15, null=True, default=None, blank=True)
    Show_Whatsapp = models.BooleanField(default=False, null=True, blank=True)
    Whatsapp_Number = models.CharField(max_length=15, null=True, default=None, blank=True)
    Show_Enquiry = models.BooleanField(default=False, null=True, blank=True)
    Show_Feature = models.BooleanField(default=False, null=True, blank=True)
    Url = models.CharField(max_length=20000,null=True,unique=True)
    SMTitle = models.CharField(max_length=2000, null=True, default=None, blank=True)
    SMDescription = models.TextField()
    SMKeywords = models.CharField(max_length=2000, null=True, default=None, blank=True)

    def __str__(self):
        return self.Title

########################################################################

class Enquiry(models.Model):
    Date = models.DateField(auto_now_add=True)
    Name = models.CharField(max_length=50)
    Mobile_Number = models.CharField(max_length=15,null=True, default=None, blank=True)
    Email = models.EmailField(null=True, default=None, blank=True)
    Product_Name = models.CharField(max_length=50,null=True, default=None, blank=True)
    Refer_number = models.CharField(max_length=6,null=True, default=None, blank=True)

    def __str__(self):
        return self.Name

########################################################################

class Manage_Menu(models.Model):
    About_Page = models.BooleanField(default=False, null=True, blank=True)
    Blog_Page = models.BooleanField(default=False, null=True, blank=True)
    Image_Gallery = models.BooleanField(default=False, null=True, blank=True)
    Contact_Page = models.BooleanField(default=False, null=True, blank=True)
    Products_Page = models.BooleanField(default=False, null=True, blank=True)
    Service_Page = models.BooleanField(default=False, null=True, blank=True)
    Feedback_Page = models.BooleanField(default=False, null=True, blank=True)
    Enquiry_Page = models.BooleanField(default=False, null=True, blank=True)
    Group_Company = models.BooleanField(default=False, null=True, blank=True)
    Testimonials = models.BooleanField(default=False, null=True, blank=True)

########################################################################

class Quick_Links(models.Model):
    About_Page = models.BooleanField(default=False, null=True, blank=True)
    Blog_Page = models.BooleanField(default=False, null=True, blank=True)
    Image_Gallery = models.BooleanField(default=False, null=True, blank=True)
    Contact_Page = models.BooleanField(default=False, null=True, blank=True)
    Optional_Service = models.BooleanField(default=False, null=True, blank=True)
    Optional_Products = models.BooleanField(default=False, null=True, blank=True)
    Products_Page = models.BooleanField(default=False, null=True, blank=True)
    Service_Page = models.BooleanField(default=False, null=True, blank=True)
    Testimonials = models.BooleanField(default=False, null=True, blank=True)

########################################################################

class Group_Of_Companies(models.Model):
    Logo = models.ImageField(blank=True,null=True,upload_to='CompanyLogo')

########################################################################

class Testimonial(models.Model):
    Tes_Name = models.CharField(max_length=50)
    Designation = models.CharField(max_length=50)
    Company_Name = models.CharField(max_length=50)
    Testimonial = models.TextField()
    Tes_Image = models.ImageField(blank=True,null=True,upload_to='TestimonialImage')

    def __str__(self):
        return self.Tes_Name

########################################################################

class Banners(models.Model):
    Caption = models.CharField(max_length=100)
    Sub_Caption = models.CharField(max_length=100)
    Button_Label = models.CharField(max_length=30)
    Link = models.CharField(max_length=1000)
    Banner_Image = models.ImageField(blank=True,null=True,upload_to='BannerImage')

    def __str__(self):
        return self.Caption