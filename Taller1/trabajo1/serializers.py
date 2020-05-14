from rest_framework import serializers
from .models import Trabajo1

"""""
,'fecha','origen','valor','codigoSensor','observacion'
"""""
class MeasureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trabajo1
        fields = ('id','fecha','origen','valor','codigoSensor','observacion')