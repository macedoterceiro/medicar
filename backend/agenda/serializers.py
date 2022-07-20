from rest_framework import serializers
from agenda.models import Agenda
from medico.serializers import MedicoSerializer
from config import settings

class AgendaSerializer(serializers.ModelSerializer):
    medico = MedicoSerializer()
    dia = serializers.DateField(format='%d/%m/%Y', input_formats=settings.DATE_INPUT_FORMATS)
    horarios = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='hora'
    )

    class Meta:
        model = Agenda
        fields = ['id', 'dia', 'horarios','medico']