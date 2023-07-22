from django.db import models

class User(models.Model):
    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.usuario


class Item(models.Model):
    data = models.DateField(null=True, blank=True)
    modelo = models.CharField(max_length=100)
    cor = models.CharField(max_length=50)
    tamanho = models.CharField(max_length=20)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    valor_venda = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    quantidade = models.PositiveIntegerField()

    def __str__(self):
        return self.model


