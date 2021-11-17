from django.db import models
class ContactUs(models.Model):
    name = models.CharField(max_length=20)
    surname = models.CharField(max_length=20)
    middlename = models.CharField(max_length=20)
    phone = models.CharField(max_length=13)
class Product(models.Model):
    image=models.ImageField(null=True, blank=True)
    title=models.CharField(max_length=30)
    description=models.TextField(max_length=400)
class Product_uz(models.Model):
    image = models.ImageField(null=True, blank=True)
    title = models.CharField(max_length=30)
    description = models.TextField(max_length=400)