from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
from django.contrib import admin

class Register(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    location = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=500)
    
class Mobile_Information(models.Model):   
    types = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    manufacturer = models.CharField(max_length=100)
    make = models.CharField(max_length=100)
    os = models.CharField(max_length=100)
    device_id = models.IntegerField(max_length=100)
    serial_number = models.IntegerField(max_length=100)
    ip_address = models.CharField(max_length=100)
    location_of_hosting = models.CharField(max_length=100)
    date_of_purchase = models.DateField()
    server_device_id = models.IntegerField(max_length=100)
    phone_number = models.CharField(max_length=100) 
    updated_date = models.DateField()
    

class Hosting_Information(models.Model): 
    location = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    device_id = models.IntegerField(max_length=100)

class Server_Information(models.Model):    
    types = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    manufacturer = models.CharField(max_length=100)
    make = models.CharField(max_length=100)
    device_id = models.IntegerField(max_length=100)
    serial_number = models.IntegerField(max_length=100)
    server_capacity = models.IntegerField(max_length=100)
    ip_address = models.CharField(max_length=100)
    location_of_hosting = models.CharField(max_length=100)
    date_of_purchase = models.DateField()
    updated_date = models.DateField()
    
class Mapping_Server_Mobile(models.Model):
    server_information_id = models.IntegerField(max_length=100)    
    mobile_information_id = models.IntegerField(max_length=100)
    
class Device_Status(models.Model):
    device_information_id = models.IntegerField(max_length=100)
    category = models.CharField(max_length=100)
    user_id = models.IntegerField(max_length=100)
    status = models.CharField(max_length=100)
    
class Procurement_Request(models.Model):
    user_id = models.IntegerField(max_length=100)
    device_type = models.CharField(max_length=100)
    types = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    os = models.CharField(max_length=100)
    device_id = models.IntegerField(max_length=100)
    number_days = models.IntegerField(max_length=100)
    request_date = models.DateField()
    request_status = models.CharField(max_length=100)

class Allotment(models.Model):
    user_id = models.IntegerField(max_length=100)
    device_type = models.CharField(max_length=100)
    device_information_id = models.IntegerField(max_length=100)
    allot_date = models.DateField()
    expired_date = models.DateField()
    
        
    
    
    
    
    
    

# Create your models here.
