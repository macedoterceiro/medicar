from rest_framework import serializers
from medico.models import Medico

class MedicoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medico
        fields = ('id', 'crm', 'nome', 'email')