from pyexpat import model
from rest_framework import serializers
from .models import vehicle

class VehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model=vehicle
        fields=['name','static_map','speed','average_speed','Temprature','Fuel_level','Engine_status']
        