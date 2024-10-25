from django.db import models

# Create your models here.
class Manufactor(models.Model):
    CompanyName=models.CharField(max_length=100,blank=True,null=True)
    Email=models.CharField(max_length=100,blank=True,null=True)
    PhoneNo=models.IntegerField(blank=True,null=True)
    CompanyAddress=models.CharField(max_length=100,blank=True,null=True)
    LoginId=models.CharField(max_length=100,blank=True,null=True)
class User(models.Model):
    Name=models.CharField(max_length=100,blank=True,null=True)
    Email=models.CharField(max_length=100,blank=True,null=True)
    PhoneNo=models.IntegerField(blank=True,null=True)
    LoginId=models.CharField(max_length=100,blank=True,null=True)
class Product(models.Model):
    ProductName=models.CharField(max_length=100,blank=True,null=True)
    BuildDate=models.DateField(blank=True,null=True)
    ExpiryDate=models.DateField(blank=True,null=True)
    UploadPhoto=models.FieldFile(blank=True,null=True)
    ProductPrice=models.FieldFile(blank=True,null=True)
class Feedback(models.Model):
    Feedback=models.CharField(max_length=250,blank=True,null=True)
    Rating=models.FloatField(max_length=20,blank=True,null=True)
    