from django.db import models
from django.core.exceptions import ValidationError

class Especialidade(models.Model):
    nome = models.CharField(max_length=25,unique=True)

    def __str__(self):
        return self.nome

class Medico(models.Model):
    crm = models.IntegerField(unique=True)
    nome = models.CharField(max_length=200)
    email = models.EmailField(max_length=60, unique=True, null=True, blank=True)
    especialidade = models.ForeignKey(Especialidade, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return f'{self.nome} - CRM: {self.crm} - {self.especialidade}'