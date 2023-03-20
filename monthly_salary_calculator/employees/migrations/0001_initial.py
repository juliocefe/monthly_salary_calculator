# Generated by Django 4.0.10 on 2023-03-20 02:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('role', models.IntegerField(choices=[(1, 'Chofer'), (2, 'Cargador'), (3, 'Auxiliar')], verbose_name='Rol')),
            ],
        ),
    ]