from django.shortcuts import render, redirect

from instituciones_colaboradoras.forms import FotosFormulario
from instituciones_colaboradoras.models import FotoInstitucion


def subir_foto(request):
    if request.method == 'POST':
        form = FotosFormulario(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('informacion')
    else:
        form = FotosFormulario()
    return render(request, 'cargar_foto.html', {'form': form})


def mostrar_foto(request):
    fotos = FotoInstitucion.objects.all()
    return render(request, 'mostrar_foto.html',{'fotos':fotos})

