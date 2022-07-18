from django.db import models
from rest_framework import serializers
from medico.models import Medico

class Agenda(models.Model):
    dia = models.DateField()
    medico = models.ForeignKey(Medico,on_delete=models.CASCADE,default=None,)
    horarios = serializers.ListField(
        child = serializers.TimeField(default=None)
    )

    def __str__(self):
        return self.nome