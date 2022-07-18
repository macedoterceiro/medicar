from django.contrib import admin
from medico.models import Medico, Especialidade

class Medicos(admin.ModelAdmin):
    list_display = ('crm', 'nome', 'email', 'especialidade')
    # list_display_links = ('id', 'nome')
    search_fields = ('nome', 'especialidade')
    
admin.site.register(Medico, Medicos)
admin.site.register(Especialidade)