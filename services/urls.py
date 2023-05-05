from django.urls import path, include
from services.views import home,service

urlpatterns = [
    path('', home, name='home_page'),
    path('service', service, name='service_page'),
]