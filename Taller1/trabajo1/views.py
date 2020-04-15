from django.shortcuts import render
from rest_framework import viewsets
from .models import Trabajo1
from .serializers import MeasureSerializer

class MeasureViewSet(viewsets.ModelViewSet):
    queryset = Trabajo1.objects.all().order_by('-created')
    serializer_class = MeasureSerializer