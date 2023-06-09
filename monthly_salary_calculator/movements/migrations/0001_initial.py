# Generated by Django 4.0.10 on 2023-03-20 04:48

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('employees', '0002_alter_employee_role'),
    ]

    operations = [
        migrations.CreateModel(
            name='Movement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deliveries', models.IntegerField(verbose_name='Entregas')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, help_text='Fecha en la que el recurso fue creado.', verbose_name='Fecha de creación')),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employees.employee', verbose_name='Empleado')),
            ],
        ),
    ]
