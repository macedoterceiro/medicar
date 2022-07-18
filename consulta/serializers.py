from rest_framework import serializers
from consulta.models import Consulta

class ConsultaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Consulta
        fields = ('id', 'dia', 'hora', 'data_agendamento', 'medico')
        depth = 1