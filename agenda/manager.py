from django.db import models
from datetime import date, datetime
from django.utils import timezone
from django.db.models import  Q

class AgendaManager(models.Manager):
    def disponiveis(self):
        return super().get_queryset().filter(dia__gte=date.today()).order_by('dia')

class HorarioManager(models.Manager):
    def disponiveis(self):
        hora_atual = timezone.localtime(timezone.now()).time()
        hora_padrao = datetime.strptime('00:00', '%H:%M')
        
        return super().get_queryset().filter(
                                (
                                  Q(agenda__dia=date.today(), 
                                   hora__gt= hora_atual) 
                                  | Q(agenda__dia__gt=date.today(),
                                    hora__gte=hora_padrao)
                                ), 
                                marcado=False
                                ).order_by('hora')
                                