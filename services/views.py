from django.shortcuts import render, HttpResponse
from services.models import *

# Create your views here


def home(request):
    return render(request, 'index.html')


def service(request):

    state_id = request.GET.get('state')
    city_id = request.GET.get('city')

    if state_id:
        city_list = city.objects.filter(state=state_id)

    else:
        city_list = city.objects.all()

    if city_id:
        hospital_obj = hospital.objects.filter(city=city_id)
    else:
        hospital_obj = hospital.objects.all()

    states_list = state.objects.all()
    context = {'hospital_services': hospital_obj,
               'states': states_list,
               'cities': city_list,
               'selected_state_id': state_id,
               'selected_city_id': city_id
               }
    return render(request, template_name='service.html', context=context)
