from pickle import TRUE
from unicodedata import name
from django.db import models

# Create your models here.
class vehicle(models.Model):
    name=models.CharField(max_length=50)
    static_map=models.ImageField(upload_to='imgs', null=True,blank=True)
    speed=models.IntegerField()
    average_speed=models.IntegerField()
    Temprature=models.IntegerField()
    Fuel_level=models.IntegerField()
    Engine_status=models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.name
