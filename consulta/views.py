# from django.shortcuts import render
from rest_framework import viewsets
from consulta.models import Consulta
from consulta.serializers import ConsultaSerializer

class ConsultasViewSet(viewsets.ModelViewSet):
    queryset = Consulta.objects.all()
    serializer_class = ConsultaSerializer
