from django.db import models
import uuid

# Create your models here.
class Trabajo1(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    #type = models.CharField(verbose_name='Temperatura', max_length=20)
    #value = models.IntegerField(verbose_name='value')
    fecha = models.CharField(max_length=90, verbose_name='fecha',default="")
    origen = models.CharField(max_length=90, verbose_name='origen',default="")
    valor = models.IntegerField(verbose_name='valor',default=-1)
    codigoSensor = models.CharField(max_length=90, verbose_name='codigoSensor',default="")
    observacion = models.CharField(max_length=90, verbose_name='observacion',default="")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)