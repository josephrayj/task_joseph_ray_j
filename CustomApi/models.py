from django.db import models
from stdimage import StdImageField

class Address(models.Model):
    hno = models.CharField(max_length=10)
    street = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)

class WorkExperience(models.Model):
    companyName = models.CharField(max_length=100)
    fromDate = models.DateField()
    toDate = models.DateField()
    address = models.CharField(max_length=100)

class Qualification(models.Model):
    qualificationName = models.CharField(max_length=100)
    fromDate = models.DateField()
    toDate = models.DateField()
    percentage = models.DecimalField(max_digits=5, decimal_places=2)

class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()

class Employee(models.Model):
    regid = models.CharField(max_length=50, unique=True)
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    age = models.PositiveIntegerField()
    gender = models.CharField(max_length=10)
    phoneNo = models.CharField(max_length=20,blank=True)
    addressDetails = models.OneToOneField(Address, on_delete=models.CASCADE)
    workExperience = models.ManyToManyField(WorkExperience)
    qualifications = models.ManyToManyField(Qualification)
    projects = models.ManyToManyField(Project)
    photo = StdImageField(upload_to='photos/', variations={'thumbnail': {"width": 100, "height": 100, "crop": True}}, blank=True)
