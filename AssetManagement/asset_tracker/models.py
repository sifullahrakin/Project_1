from django.db import models

class Company(models.Model):
    name = models.CharField(max_length=100)
    # Add other fields as needed

class Employee(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    # Add other fields as needed

class Device(models.Model):
    name = models.CharField(max_length=100)
    condition = models.TextField()
    checked_out = models.DateTimeField(null=True, blank=True)
    checked_in = models.DateTimeField(null=True, blank=True)
    employee = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True, blank=True)