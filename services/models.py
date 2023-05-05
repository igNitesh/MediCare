from django.db import models

# Create your models here.
class state(models.Model):
    name = models.CharField(max_length=20, null=False, blank=False)

    def __str__(self):
        return self.name


class city(models.Model):
    name = models.CharField(max_length=20, null=False, blank=False)
    state = models.ForeignKey(state, on_delete=models.CASCADE, default=0)

    def __str__(self):
        return self.name


class hospital(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    contact = models.CharField(max_length=35, null=False, blank=False)
    address = models.CharField(max_length=200, null=False, blank=False)
    # Services
    ambulance = models.CharField(max_length=10, null=False, blank=False, default=0)
    total_beds = models.IntegerField(default=0)
    available_beds = models.IntegerField(default=0)
    total_oxygen_cylinder = models.IntegerField(default=0)
    available_oxygen_cylinder = models.IntegerField(default=0)
    total_ventilator = models.IntegerField(default=0)
    available_ventilator = models.IntegerField(default=0)
    city = models.ForeignKey(city, on_delete=models.CASCADE, default=0)

    def __str__(self):
        return self.name