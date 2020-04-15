from rest_framework import serializers
from .models import Trabajo1

class MeasureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trabajo1
        fields = ('id', 'type', 'value')