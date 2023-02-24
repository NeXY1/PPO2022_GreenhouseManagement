from django.contrib import admin
from .models import Day, Time, TemperatureValue, AirHudimityValue, SoilHudimityValue

registredModels = [
    Day,
    Time,
    TemperatureValue,
    AirHudimityValue,
    SoilHudimityValue
]

for model in registredModels:
    admin.site.register(model)
