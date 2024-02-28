from django.db import models

class Contacto(models.Model):
    nombre = models.CharField(max_length=100)
    correo = models.EmailField()
    telefono = models.CharField(max_length=20)
    fecha = models.DateField(auto_now_add=True)
    mensaje = models.TextField()
