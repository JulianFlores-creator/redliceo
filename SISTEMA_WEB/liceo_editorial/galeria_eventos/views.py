from django.shortcuts import render
from .models import EventosGaleria

def event_list(request):
    eventos = EventosGaleria.objects.all()
    return render(request, 'listar_evento.html', {'eventos': eventos})

def event_detail(request, event_id):
    evento = EventosGaleria.objects.get(id=event_id)
    return render(request, 'detalle_evento.html', {'evento': evento})
