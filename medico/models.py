from django.db import models

class Medico(models.Model):
    crm = models.CharField(max_length=8,unique=True)
    nome = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)

    def __str__(self):
        return self.nome