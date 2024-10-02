from django.db import models

# Create your models here.

class Student_details(models.Model):
    username=models.CharField(max_length=100)
    password=models.CharField(max_length=100)
    phonenumber=models.CharField(max_length=15)
    address=models.TextField()

    def __str__(self):
        return self.username
    
class Student_images(models.Model):
    image=models.ImageField(upload_to='images/')

    def __str__(self):
        return f"image{self.id}"
