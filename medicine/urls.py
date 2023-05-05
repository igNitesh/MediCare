from django.urls import path, include
from medicine.views import medicine

urlpatterns = [
    path('', medicine, name='medicine_page'),
]