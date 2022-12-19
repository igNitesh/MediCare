from django.contrib import admin
from django.dispatch import receiver
from app.models import City,Hospital
from django.db.models.signals import post_save
# when admin add hospitals then atomatic name of hospitial and services automatic add in services section
# @receiver(post_save, sender=Hospital)
# def afterHospitalSave(signal,instance,**kwargs):
#     # service = Services(hospital=instance)
#     service.save()
class ServiceAdmin(admin.ModelAdmin):
    model=Hospital
    list_display =[
            'hospital',
            'beds',
            'oxygen_cylender',
            'ventilator'

                ]
    def beds(self,object):
        return f'{object.beds_avilable}/{object.beds_total}'
    def oxygen_cylender(self,object):
        return f'{object.oxygen_cylender_avilable}/{object.oxygen_cylender_total}'
    def ventilator(self,object):
        return f'{object.ventilator_avilable}/{object.ventilator_total}'

class HospitalAdmin(admin.ModelAdmin):
    model = Hospital
    list_display = ['name','phone','address','city']
class CityAdmin(admin.ModelAdmin):
    model = City
    list_display = ['name']
# Register your models here.
admin.site.register(City,CityAdmin)
admin.site.register(Hospital,HospitalAdmin)
# admin.site.register(Services,ServiceAdmin)