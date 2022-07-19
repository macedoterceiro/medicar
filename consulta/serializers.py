from rest_framework import serializers
from django.utils import timezone
from datetime import date, datetime

from medico.serializers import MedicoSerializer
from consulta.models import Consulta
from agenda.models import Agenda, Horario
from usuario.models import User

class ConsultaSerializer(serializers.ModelSerializer):
    agenda_id = serializers.IntegerField(required=False)
    medico = MedicoSerializer(required=False)
    dia =  serializers.DateField(source='agenda.dia', format='%d/%m/%Y', required=False)
    horario = serializers.TimeField(source='horario.hora')
    data_agendamento = serializers.DateField(format='%d/%m/%Y', required=False)
    
    def validate_agenda_id(self, value):
        try:
            agenda = Agenda.objects.get(id=value)
            if agenda.dia < date.today():
                raise serializers.ValidationError({'agenda':'Data Inválida. Data deve ser posterior a data atual.'})

        except Agenda.DoesNotExist:
            raise serializers.ValidationError({'agenda':'Agenda solicitada inexistente!'})
        
        return value

    def validate(self, data):
        try:
            agenda = Agenda.objects.get(id=data['agenda_id'])
            horario = Horario.objects.get(agenda__id=data['agenda_id'], hora=data['horario']['hora'])
            
            if (agenda.dia == date.today()) & (horario.hora < timezone.localtime(timezone.now()).time()):
                raise serializers.ValidationError({'horario':'Horário Inválido. Horário deve ser anterior ao tempo atual.'})    
            if horario.marcado == True:
                raise serializers.ValidationError({'horario':'Horário Indisponível. Horário solicitado já foi marcado!'})    
        except Horario.DoesNotExist:
            raise serializers.ValidationError({'horario':'Horário solicitado não existe!'})
        
        return data
    
    def save(self):
        agenda_id = self.validated_data['agenda_id']
        horario_req = self.validated_data['horario']['hora']
        
        agenda = Agenda.objects.get(id=agenda_id)
        medico = agenda.medico
        
        horario = Horario.objects.get(agenda__id=agenda_id, hora=horario_req)
        usuario = User.objects.get(username=self.context['request'].user)

        consulta= Consulta(agenda=agenda, horario=horario, medico=medico, usuario=usuario)
        up = Horario.objects.filter(pk=horario.id).update(marcado=True)
        consulta.save()
        
        return consulta
     
    class Meta:
        model = Consulta
        fields = ['id','dia','horario','data_agendamento','medico','agenda_id']
        # depth = 1