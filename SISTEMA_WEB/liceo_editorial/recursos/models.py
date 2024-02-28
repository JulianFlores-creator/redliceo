from django.db import models

class Recurso(models.Model):
    titulo = models.CharField(max_length=200)
    archivo = models.FileField(upload_to='recursos/libros/')
    coordinadores = models.CharField(max_length=200, null=True)
    ISBN = models.CharField(max_length=20, null=True)
    fecha = models.DateField(null=True)
    edicion = models.CharField(max_length=50, null=True)
    autor = models.CharField(max_length=200, null=True)
    fotoPortada = models.ImageField(upload_to='recursos/fotos/', null=True, blank=True)

    def __str__(self):
        return self.titulo

