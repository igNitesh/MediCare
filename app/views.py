from django.http import HttpResponse
from django.shortcuts import render
from app.models import City,Hospital
from multiprocessing import context

# Create your views here.
def home(request):
        selected_city_id = request.GET.get('city')
        # services = Services.objects.all()
        cities = City.objects.all()
        print('selected city id ',selected_city_id)
        if selected_city_id:
                hospitals = Hospital.get_all_services_by_cityid(selected_city_id)
                context = {
                'cities' : cities,
                'hospitals' : hospitals,
                }

                return render(request,template_name='index.html',context=context)
        else:
                hospitals = Hospital.objects.all()
                context = {
                'cities' : cities,
                'hospitals' : hospitals,
                }
                print('else part executed ')
                return render(request,template_name='index.html',context=context)