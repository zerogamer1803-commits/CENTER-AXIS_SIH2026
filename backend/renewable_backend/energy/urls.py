from django.urls import path
from . import views

urlpatterns = [
    path('', views.energy_list, name='energy-list'),
    path('history/', views.energy_history, name='energy-history'),
    path('solar-voltage/', views.solar_voltage_update, name='solar-voltage-update'),
]