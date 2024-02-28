from django.db import models

class Informacion(models.Model):
    objetivo = models.CharField(max_length=200)
    mision = models.TextField()
    imagen = models.ImageField(upload_to='informacion_imagenes/', null=True, blank=True)

    def __str__(self):
        return "Información Inicial"

class LGC(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField()

    def __str__(self):
        return "LCG"


class AboutInfo(models.Model):
    titulo = models.CharField(max_length=200)
    contenido = models.TextField()
    imagen = models.ImageField(upload_to='info_about/', null=True, blank=True)