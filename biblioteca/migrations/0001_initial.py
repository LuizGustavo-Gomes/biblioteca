# Generated by Django 5.1 on 2024-08-27 16:32

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bibliotecario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('estado', models.CharField(max_length=200)),
                ('cidade', models.CharField(max_length=100)),
                ('logradouro', models.CharField(max_length=100)),
                ('numero', models.CharField(max_length=100)),
                ('cep', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Livro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=200)),
                ('autor', models.CharField(max_length=200)),
                ('ano_publicacao', models.CharField(max_length=4)),
                ('isbn', models.CharField(max_length=13, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('estado', models.CharField(max_length=200)),
                ('cidade', models.CharField(max_length=100)),
                ('logradouro', models.CharField(max_length=100)),
                ('numero', models.CharField(max_length=100)),
                ('cep', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Reserva',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_reserva', models.DateField(auto_now_add=True)),
                ('ativa', models.BooleanField(default=True)),
                ('livro', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='biblioteca.livro')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='biblioteca.usuario')),
            ],
        ),
        migrations.CreateModel(
            name='Emprestimo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_emprestimo', models.DateField(auto_now_add=True)),
                ('data_devolucao', models.DateField(blank=True, null=True)),
                ('livro', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='biblioteca.livro')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='biblioteca.usuario')),
            ],
        ),
    ]
