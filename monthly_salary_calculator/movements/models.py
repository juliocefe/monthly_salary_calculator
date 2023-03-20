from django.db import models
from django.utils import timezone

# Create your models here.

class Movement(models.Model):
    employee = models.ForeignKey(
        "employees.Employee",
        verbose_name="Empleado",
        on_delete=models.CASCADE,
    )
    deliveries = models.IntegerField("Entregas")
    created_at = models.DateTimeField(
        verbose_name="Fecha de creación",
        default=timezone.now,
        help_text="Fecha en la que el recurso fue creado.",
    )