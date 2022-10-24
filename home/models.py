from django.db import models

# Create your models here.

class User(models.Model):
    Username = models.CharField(max_length=25)
    Password = models.CharField(max_length=25)

    def __str__(self):
        return self.Username