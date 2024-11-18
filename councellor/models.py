from django.db import models

# Create your models here.

class Councellor(models.Model):
    name=models.CharField(max_length=30, blank=True, null= True)
    age=models.IntegerField(blank=True, null= True)
    gender=models.CharField(max_length=30, blank=True, null= True)
    address=models.CharField(max_length=30, blank=True, null= True)
    phone=models.IntegerField(blank=True, null= True)
    email=models.CharField(max_length=30, blank=True, null= True)
    qualification=models.CharField(max_length=30, blank=True, null= True)

class feedback(models.Model):
    userid=models.CharField(max_length=30, blank=True, null= True)
    rating=models.CharField(max_length=30,blank=True, null= True)
    feedback=models.CharField(max_length=30, blank=True, null= True)
     
class rating(models.Model):
    userid=models.CharField(max_length=30, blank=True, null= True)
    councellorid=models.IntegerField(blank=True, null= True)
    review=models.CharField(max_length=30, blank=True, null= True)
    rating=models.CharField(max_length=30, blank=True, null= True)

class complaint(models.Model):
    userid=models.CharField(max_length=30, blank=True, null= True)
    compalint=models.CharField(max_length=100, blank=True, null= True)
    replay=models.CharField(max_length=100, blank=True, null= True)
    complaintdate=models.DateField(blank=True, null= True)
