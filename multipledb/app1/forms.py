from django import forms
from app1.models import Student_details,Student_images

class Model1Form(forms.ModelForm):
    class Meta:
        model=Student_details
        fields=['username','password','phonenumber','address']

class Model2Form(forms.ModelForm):
    class Meta:
        model=Student_images
        fields=['image']
