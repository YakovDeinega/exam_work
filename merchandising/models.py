from django.db import models

# Create your models here.


class Division(models.Model):
    description = models.CharField(max_length=1000, verbose_name='Описание')
    address = models.CharField(max_length=100, verbose_name='Адрес подразделения')

    class Meta:
        verbose_name = 'Подразделение'
        verbose_name_plural = 'Подразделения'

