from django.shortcuts import render
from .models import MiembroRed

def miembrosRedLiceo(request):
    miembros = MiembroRed.objects.all()
    return render(request, 'lista_miembros.html', {'miembros': miembros})
