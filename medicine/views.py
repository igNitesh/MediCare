from django.shortcuts import render
from .medi_scrap.scrap import get_medicine_data

# Create your views here.

def medicine(request):
    
    if request.method == "POST":
        medicine_name = request.POST.get('medicine_name')
        context = get_medicine_data(medicine_name)
        return render(request, template_name='medicine.html', context=context)
    else:
        return render(request, template_name='medicine.html')
