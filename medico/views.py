# from django.shortcuts import render
from rest_framework import viewsets
from medico.models import Medico
from medico.serializers import MedicoSerializer

class MedicosViewSet(viewsets.ModelViewSet):
    queryset = Medico.objects.all()
    serializer_class = MedicoSerializer