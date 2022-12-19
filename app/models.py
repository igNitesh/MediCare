from django.db import models
from pyexpat import model

# Create your models here.
class City(models.Model):
    name=models.CharField(max_length=50 ,null=False ,blank= False)
    def __str__(self):
        return self.name

class Hospital(models.Model):
    name=models.CharField(max_length=50 ,null=False ,blank= False)
    phone=models.CharField(max_length=12 ,null=False ,blank= False)
    address=models.CharField(max_length=200 ,null=False ,blank= False)
    # If user select a state then all cities of those state shows then shows name of hospitals
    beds_total = models.IntegerField(default=0)
    beds_avilable = models.IntegerField(default=0)
    oxygen_cylender_total =models.IntegerField(default=0)
    oxygen_cylender_avilable =models.IntegerField(default=0)
    ventilator_total = models.IntegerField(default=0)
    ventilator_avilable = models.IntegerField(default=0)
    city = models.ForeignKey(City,on_delete=models.CASCADE,default = 1)

    def __str__(self):
        return self.name

    @staticmethod
    def get_all_services_by_cityid(city_id):
        if city_id:
            return Hospital.objects.filter(city = city_id)
        else:
            return Hospital.objects.all()
# class Services(models.Model):
#     # If user select a state then all cities of those state shows then shows name of hospitals then shows services of hospital
#     hospital = models.OneToOneField(
#         Hospital, on_delete=models.CASCADE,primary_key=True)
#     beds_total = models.IntegerField(default=0)
#     beds_avilable = models.IntegerField(default=0)
#     oxygen_cylender_total =models.IntegerField(default=0)
#     oxygen_cylender_avilable =models.IntegerField(default=0)
#     ventilator_total = models.IntegerField(default=0)
#     ventilator_avilable = models.IntegerField(default=0)
#     def __str__(self):
#         return self.hospital.name





