from django.db import models

# Create your models here.

class User(models.Model):
    Username = models.CharField(max_length=25)
    Password = models.CharField(max_length=25)

    def __str__(self):
        return self.Username

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

class Blog(models.Model):
    Title = models.CharField(max_length=50)
    Description = models.TextField()
    Image = models.ImageField(blank=True,null=True,upload_to='about_us')
    Url = models.CharField(max_length=20000)
    SMTitle = models.CharField(max_length=2000)
    SMDescription = models.TextField()
    SMKeywords = models.CharField(max_length=2000)

    def __str__(self):
        return self.Title