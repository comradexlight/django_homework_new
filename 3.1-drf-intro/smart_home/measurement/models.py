from datetime import date
from django.db import models


class Sensor(models.Model):
    name = models.CharField(max_length=100, verbose_name='название датчика')
    description = models.CharField(max_length=250, verbose_name='описание датчика', blank=True)


class Measurement(models.Model):
    temperature = models.DecimalField(max_digits=3, decimal_places=1, verbose_name='температура')
    created_at = models.DateField(default=date.today, verbose_name='дата измерения')
    photo = models.ImageField(upload_to=f'sensors_photo/{date.today()}', null=True)
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE, related_name='measurements')
