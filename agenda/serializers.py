from rest_framework import serializers
from agenda.models import Agenda

class AgendaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Agenda
        fields = ('id', 'dia', 'horarios','medico')