from django.shortcuts import render, HttpResponse
from doctors.models import doctor, department
from services.models import state, city, hospital

# Create your views here.


def doctors(request):
    
    state_id = request.GET.get('state')
    city_id = request.GET.get('city')
    department_id = request.GET.get('department')
    
    if state_id:
        city_list = city.objects.filter(state=state_id)
    else:
        city_list = city.objects.all()
        
    if city_id:
        doctor_list = doctor.objects.filter(city=city_id)
        if department_id:
            doctor_list = doctor.objects.filter(department=department_id,city=city_id)
        else:
            doctor_list = doctor.objects.filter(city=city_id)
    else:
        doctor_list = doctor.objects.all()
    
    # doctor_list = doctor.objects.all()
    states_list = state.objects.all()
    # city_list = city.objects.all()
    department_list = department.objects.all()
    context = {
        'doctors': doctor_list,
        'states': states_list,
        'cities': city_list,
        'departments': department_list,
        'selected_state_id': state_id,
        'selected_city_id': city_id,
        'selected_department_id': department_id
    }
    return render(request, 'doctor.html', context=context)
