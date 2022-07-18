from django.contrib import admin
from medico.models import Medico

class Medicos(admin.ModelAdmin):
    list_display = ('id', 'crm', 'nome', 'email')
    list_display_links = ('id', 'nome')
    search_fields = ('nome', 'crm')
    
admin.site.register(Medico, Medicos)