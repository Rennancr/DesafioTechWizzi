from django.db import models


# Classe principal para definir os requisistos funcionais do desafio no nosso banco
class DadosCheckout(models.Model):
    data_ida = models.DateField()
    data_volta = models.DateField()
    passageiros_adultos = models.PositiveIntegerField()
    passageiros_criancas = models.PositiveIntegerField()
    origem = models.CharField(max_length=100)
    destino = models.CharField(max_length=100)
    nome_passageiro = models.CharField(max_length=100)
    email_passageiro = models.EmailField()

    def __str__(self):
        return f"Checkout de {self.origem} para {self.destino}"
