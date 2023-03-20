from django.db import models


class Employee(models.Model):

    class Role(models.IntegerChoices):
        DRIVER = 1, "Chofer"
        LOADER = 2, "Cargador"
        ASSITANT = 3, "Auxiliar"

    name = models.CharField(max_length=100, unique=True)
    role = models.IntegerField(
        "Rol", choices=Role.choices, default=Role.DRIVER
    )

    def __str__(self):
        return self.name