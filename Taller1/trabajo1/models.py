from django.db import models
import uuid

# Create your models here.
class Trabajo1(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    type = models.CharField(verbose_name='Temperatura', max_length=20)
    value = models.IntegerField(verbose_name='Valor')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)