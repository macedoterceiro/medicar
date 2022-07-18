from django.contrib import admin
from agenda.models import Agenda

class Agendas(admin.ModelAdmin):
    list_display = ('id', 'dia', 'horarios', 'medico')
    list_display_links = ('id', 'dia', 'horarios', 'medico')
    search_fields = ('dia', 'horarios', 'medico')
    
admin.site.register(Agenda, Agendas)