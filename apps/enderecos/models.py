from django.db import models

# Create your models here.

class Endereco(models.Model):
    nome = models.CharField(max_length=100,help_text='Nome do Produto')
    logradouro = models.DateTimeField()
    bairro = models.CharField(max_length=200)
    cidade = models.CharField(max_length=200)
    estado = models.CharField(max_length=200)
    pais = models.CharField(max_length=200)
    CEP = models.CharField(max_length=10)
    def __str__(self):
        return self.nome + ' ' + self.logradouro
