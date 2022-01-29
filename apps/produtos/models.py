from django.db import models
from apps.fornecedores.models import Fornecedor
# Create your models here.
class Produto(models.Model):
    nome = models.CharField(max_length=100,help_text='Nome do Produto')
    dataCompra = models.DateTimeField()
    precoUnitario = models.DecimalField(max_digits=8, decimal_places=2)
    #imagem =
    fornecedor = models.ForeignKey(Fornecedor, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome