from django.db import models
from services.models import *

# Create your models here.


class department(models.Model):
    name = models.CharField(max_length=20, null=False, blank=False)

    def __str__(self):
        return self.name
    


class doctor(models.Model):
    name = models.CharField(max_length=35, null=False, blank=False)
    contact = models.CharField(max_length=35, null=False, blank=False)
    specialization = models.CharField(max_length=40, null=False, blank=False)
    degree = models.CharField(max_length=30, null=False, blank=False)
    experience = models.CharField(max_length=30, null=False, blank=False)
    availability_time = models.CharField(max_length=20, null=False, blank=False)
    availability_on = models.CharField(max_length=35, null=False, blank=False)
    fee = models.CharField(max_length=30)
    department = models.ForeignKey(department, on_delete=models.CASCADE, default=1)
    hospital = models.ForeignKey(hospital, on_delete=models.CASCADE, default=1)
    city = models.ForeignKey(city, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return f'{self.name} - {self.department}'
