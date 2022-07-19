from django.db import models
from medico.models import Medico
from usuario.models import User
from agenda.models import Agenda, Horario

class Consulta(models.Model):
    agenda = models.ForeignKey(Agenda, on_delete=models.CASCADE)
    horario = models.ForeignKey(Horario, on_delete=models.CASCADE)
    data_agendamento = models.DateField(auto_now_add=True)
    medico = models.ForeignKey(Medico, on_delete=models.CASCADE)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)

    # def __str__(self):
    #     return self.medico