from django.contrib import admin
from .models import DadosCheckout


class CheckoutAdmin(admin.ModelAdmin):
    # Definindo o que visualizar na parte de admin e a funcao para registrar
    list_display = ['nome_passageiro', 'origem', 'destino', 'data_ida', 'data_volta']
    search_fields = ['nome_passageiro']


admin.site.register(DadosCheckout, CheckoutAdmin)
