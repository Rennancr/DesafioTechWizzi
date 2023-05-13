from django.shortcuts import render
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from .models import DadosCheckout


def checkout(request):
    # Adicionando metodo Post para inserir nossos dados no banco.
    if request.method == 'POST':
        data_ida = request.POST['data_ida']
        data_volta = request.POST['data_volta']
        passageiros_adultos = request.POST['passageiros_adultos']
        passageiros_criancas = request.POST['passageiros_criancas']
        origem = request.POST['origem']
        destino = request.POST['destino']
        nome_passageiro = request.POST['nome_passageiro']
        email_passageiro = request.POST['email_passageiro']

        #validacoes:

        try:
            validate_email(email_passageiro)
        except ValidationError:
            error_message = '* O e-mail do passageiro principal está inválido!'
            return render(request, 'core/formulario.html', {'error_message': error_message})

        if not data_ida or not data_volta or not passageiros_adultos or not passageiros_criancas or not origem or not destino or not nome_passageiro or not email_passageiro:
            error_message = '* Todos os campos devem ser preenchidos!'
            return render(request, 'core/formulario.html', {'error_message': error_message})

        if data_volta < data_ida:
            error_message = '* A data de volta deve ser maior ou igual a data de ida.'
            return render(request, 'core/formulario.html', {'error_message': error_message})

        if passageiros_adultos == 0 and passageiros_criancas == 0:
            error_message = '* A quantidade de passageiros não pode ser zero.'
            return render(request, 'core/formulario.html', {'error_message': error_message})

        try:
            checkout = DadosCheckout(
                data_ida=data_ida,
                data_volta=data_volta,
                passageiros_adultos=passageiros_adultos,
                passageiros_criancas=passageiros_criancas,
                origem=origem,
                destino=destino,
                nome_passageiro=nome_passageiro,
                email_passageiro=email_passageiro
            )
            checkout.save()
        except Exception as e:
            error_message = f'Ocorreu um erro ao salvar os dados: {str(e)}'
            return render(request, 'core/formulario.html', {'error_message': error_message})

        return render(request, 'confirmacao.html')
    else:
        return render(request, 'core/formulario.html')