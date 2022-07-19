# from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.http import HttpResponse
from django.core.exceptions import BadRequest
from datetime import date, datetime

from consulta.models import Consulta, Horario
from consulta.serializers import ConsultaSerializer

class ConsultasViewSet(viewsets.ViewSet):
    permission_classes=[IsAuthenticated]

    def list(self, request):    
        queryset = Consulta.objects.filter(usuario__username=request.user).order_by('-id')
        serializer = ConsultaSerializer(queryset, many=True)
        return Response(serializer.data)
    
    def create(self, request):
        serializer = ConsultaSerializer(data=request.data, context={'request': request})
        data={}
        if serializer.is_valid(raise_exception=True):
            consulta = serializer.save()
            consulta_qs = Consulta.objects.get(id=consulta.id)
            consulta_serializer = ConsultaSerializer(consulta_qs)

            data = consulta_serializer.data
        else:
            data = serializer.errors

        return Response(data=data, status= status.HTTP_201_CREATED)

    def destroy(self, request, pk):
        try:
            horario_atual = datetime.now().time()
            consulta = Consulta.objects.get(pk=pk, usuario__username=request.user)

            if consulta.agenda.dia == date.today():
                if consulta.horario.hora < horario_atual:
                    return Response({'consulta':['Erro. Não é possível desmarcar uma consulta que já aconteceu!']}, status= status.HTTP_400_BAD_REQUEST)
            elif  consulta.agenda.dia < date.today():
                return Response({'consulta':['Erro. Não é possível desmarcar uma consulta que já aconteceu!']}, status= status.HTTP_400_BAD_REQUEST)
        
            up = Horario.objects.filter(pk=consulta.horario.id).update(marcado=False)
            consulta.delete()

        except Consulta.DoesNotExist:
            return Response({'consulta':['Consulta inexistente ou não cadastrada para este usuário!']}, status= status.HTTP_400_BAD_REQUEST)
        
        return Response({}, status= status.HTTP_204_NO_CONTENT)