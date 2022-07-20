# from django.shortcuts import render
from rest_framework import viewsets
from django.db.models import Prefetch, OuterRef, Exists
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from datetime import date, datetime
from agenda.models import Agenda, Horario
from agenda.serializers import AgendaSerializer

class AgendasViewSet(viewsets.ViewSet):
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, ]
    filterset_fields = ['medico']

    def list(self, request):
      horarios_desmarcados = Horario.objects.disponiveis().filter(agenda=OuterRef('pk'))

      search_medico = self.request.query_params.get('medico', None)
      search_crm = self.request.query_params.get('crm', None)
      search_especialidade = self.request.query_params.get('especialidade', None)
      start_date = self.request.query_params.get('start_date', None)
      end_date = self.request.query_params.get('end_date', None)


      queryset = Agenda.objects.disponiveis().prefetch_related(
                                              Prefetch
                                                  ('horarios', 
                                                    queryset=Horario.objects.disponiveis())
                                                  ).filter(Exists(horarios_desmarcados))

      if search_medico:
        queryset=queryset.filter(medico=search_medico)
      if search_crm:
        queryset=queryset.filter(crm=search_crm)
      if search_especialidade:
        queryset=queryset.filter(especialidade=search_especialidade)
      if start_date and end_date:
        date_format='%d/%m/%Y'
        start_date=datetime.strptime(start_date,date_format)
        end_date=datetime.strptime(end_date,date_format)
        queryset=queryset.filter(dia__range=[start_date,end_date])


      serializer = AgendaSerializer(queryset, many=True)
      return Response(serializer.data)