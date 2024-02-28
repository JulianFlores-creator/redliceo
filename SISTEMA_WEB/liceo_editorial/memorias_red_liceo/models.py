from django.db import models

class DocumentoMemoria(models.Model):
    titulo = models.CharField(max_length=100)
    documento = models.FileField(upload_to='memorias_red_liceo/encuentros/')
    fecha = models.DateField()
    referencia = models.IntegerField()

    def __str__(self):
        return self.titulo
