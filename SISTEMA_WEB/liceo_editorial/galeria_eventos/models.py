from django.db import models

class EventosGaleria(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    date = models.DateField()
    image = models.ImageField(upload_to='galeria_eventos/')
