from django.db import models

from apps.enderecos.models import Endereco

# Create your models here.
class Fornecedor(models.Model):
    nome = models.CharField(max_length=100, help_text='Nome do Fornecedor')
    endereco = models.ForeignKey(Endereco, on_delete=models.CASCADE, blank=True)
    def __str__(self):
        return self.nome