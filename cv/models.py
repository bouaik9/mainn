from django.db import models

# Create your models here.

class Person(models.Model):
    name = models.CharField(max_length=100)  # Assuming name length won't exceed 100 characters
   
    email = models.EmailField(blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)

    skills = models.CharField(max_length=300, null=True, blank=True)

    experience = models.CharField(max_length=300, null=True, blank=True)
    education = models.CharField(max_length=300, null=True, blank=True)

  




class UploadedFile(models.Model):
    file = models.FileField(upload_to='uploads/')
    uploaded_at = models.DateTimeField(auto_now_add=True)