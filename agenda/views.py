# from django.shortcuts import render
from rest_framework import viewsets
from agenda.models import Agenda
from agenda.serializers import AgendaSerializer

class AgendasViewSet(viewsets.ModelViewSet):
    queryset = Agenda.objects.all()
    serializer_class = AgendaSerializer