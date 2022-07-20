from django.contrib import admin
from agenda.models import Agenda, Horario

class Agendas(admin.ModelAdmin):
    list_display = ('dia', 'medico')
    list_filter = ('dia', 'medico') 

class Horarios(admin.ModelAdmin):
    list_display = ('agenda', 'hora', 'marcado')
    list_filter = ('agenda', 'marcado') 
       
admin.site.register(Agenda, Agendas)
admin.site.register(Horario, Horarios)