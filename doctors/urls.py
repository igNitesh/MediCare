from django.urls import path, include
from doctors.views import doctors

urlpatterns = [
    path('', doctors, name='doctors_page'),
]