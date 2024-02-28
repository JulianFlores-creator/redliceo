from django.db import models

class FotoInstitucion(models.Model):
    title = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='photos/')
