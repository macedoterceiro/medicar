from django.db import models
from medico.models import Medico

class Consulta(models.Model):
    dia = models.DateField()
    hora = models.TimeField()
    data_agendamento = models.DateTimeField(auto_now_add=True, blank=True)
    medico = models.ForeignKey(Medico,on_delete=models.CASCADE,default=None,)

    def __str__(self):
        return self.medico