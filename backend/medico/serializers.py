from rest_framework import serializers
from medico.models import Medico, Especialidade

class EspecialidadeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Especialidade
        fields = ('id', 'nome')

class MedicoSerializer(serializers.ModelSerializer):
    especialidade = EspecialidadeSerializer()
    
    class Meta:
        model = Medico
        fields = ('id', 'crm', 'nome', 'email', 'especialidade')