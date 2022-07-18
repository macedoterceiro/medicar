from django.contrib import admin
from consulta.models import Consulta

class Consultas(admin.ModelAdmin):
    list_display = ('id', 'dia', 'hora', 'medico')
    list_display_links = ('id', 'dia', 'hora', 'medico')
    search_fields = ('dia', 'hora', 'medico')
    
admin.site.register(Consulta, Consultas)