from django.db import models

# Create your models here.
class Contact(models.Model):

    name=models.CharField(max_length=77)
    email=models.TextField(max_length=77)
    address=models.TextField(max_length=100)
    contact=models.CharField(max_length=77)
    password=models.CharField(max_length=77)
    def __str__(self):
       return self.name