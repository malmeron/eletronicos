from django.db import models

# Create your models here.
class Fornecedor(models.Model):
    nome = models.CharField(max_length=100, help_text='Nome do Fornecedor')

    def __str__(self):
        return self.nome