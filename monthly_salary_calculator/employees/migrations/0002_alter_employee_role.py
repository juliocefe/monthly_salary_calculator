# Generated by Django 4.0.10 on 2023-03-20 02:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='role',
            field=models.IntegerField(choices=[(1, 'Chofer'), (2, 'Cargador'), (3, 'Auxiliar')], default=1, verbose_name='Rol'),
        ),
    ]
