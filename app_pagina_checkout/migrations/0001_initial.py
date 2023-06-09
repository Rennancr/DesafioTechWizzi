# Generated by Django 4.2.1 on 2023-05-13 04:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DadosCheckout',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_ida', models.DateField()),
                ('data_volta', models.DateField()),
                ('passageiros_adultos', models.PositiveIntegerField()),
                ('passageiros_criancas', models.PositiveIntegerField()),
                ('origem', models.CharField(max_length=100)),
                ('destino', models.CharField(max_length=100)),
                ('nome_passageiro', models.CharField(max_length=100)),
                ('email_passageiro', models.EmailField(max_length=254)),
            ],
        ),
    ]
