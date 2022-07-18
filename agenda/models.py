from django.db import models
from django.utils import timezone
from django.core.exceptions import ValidationError
from datetime import date
from medico.models import Medico
from agenda.manager import AgendaManager, HorarioManager

def format_date(date):
    return date.strftime('%d-%m-%Y')
    
class Agenda(models.Model):
    dia = models.DateField(auto_now=False, auto_now_add=False, default=timezone.now)
    medico = models.ForeignKey(Medico,on_delete=models.CASCADE,default=None,)

    objects = AgendaManager()

    def __str__(self):
        return f"Agenda {self.id} - {format_date(self.dia)} | Médico: {self.medico}"
    
    def clean(self):
        def validate_data():
            if self.dia < date.today():
                raise ValidationError({'dia':'Data inválida. A data informada deve ser maior que data atual.'})
        
        def validate_agenda_medico():
            try:
                agenda = Agenda.objects.filter(medico=self.medico, dia=self.dia).get()
                raise ValidationError({'medico':'Já existe uma agenda para esse médico nessa data.'})
            except Agenda.DoesNotExist:
                pass

        validate_data()
        validate_agenda_medico()

class Horario(models.Model):
    agenda = models.ForeignKey(Agenda, related_name='horarios', on_delete=models.CASCADE)
    hora = models.TimeField(auto_now=False, auto_now_add=False)
    marcado = models.BooleanField(default=False)
    objects = HorarioManager()

    def clean(self):
        def validate_horario_exists():
            try:
                horario = Horario.objects.filter(agenda=self.agenda, hora=self.hora).get()
                raise ValidationError({'hora':'Agenda já contém hora informada.'})
            except Horario.DoesNotExist:
                pass

        def validate_horario_dia_atual():
            if self.agenda.dia == date.today():
                if self.hora < timezone.localtime(timezone.now()).time():
                    print(timezone.now())
                    raise ValidationError({'hora':'Horario inválido. A hora informada deve ser maior que a hora atual.'})

        validate_horario_dia_atual()
        validate_horario_exists()
        

    def __str__(self):
        return f"(Agenda {self.agenda.id}) Horario: {self.hora} - ({format_date(self.agenda.dia)} - Médico: {self.agenda.medico.nome})"