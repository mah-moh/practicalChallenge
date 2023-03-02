from django.db import models
from django.contrib.auth.models import User

class Company(models.Model):
    name = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

class Device(models.Model):
    name = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    condition = models.CharField(max_length=100)

class DeviceCheckoutLog(models.Model):
    device = models.ForeignKey(Device, on_delete=models.CASCADE)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    checkout_condition = models.CharField(max_length=100)
    return_condition = models.CharField(max_length=100)