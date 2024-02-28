from django.db import models

class MiembroRed(models.Model):
    nombre = models.CharField(max_length=100)
    apellidoPaterno = models.CharField(max_length=100, null=True)
    apellidoMaterno = models.CharField(max_length=100, null=True)
    centroTrabajo = models.CharField(max_length=100, null=True)
    email = models.EmailField(null=True)
    education_degree = models.CharField(max_length=100, null=True)

    def __str__(self):
        return "MIEMBROS RED LICEO"
