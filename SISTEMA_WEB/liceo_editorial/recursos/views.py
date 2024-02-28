from django.shortcuts import render, redirect
from .forms import RecursoForm

def subir_recurso(request):
    if request.method == 'POST':
        form = RecursoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('lista_recursos')
    else:
        form = RecursoForm()
    return render(request, 'subir_recurso.html', {'form': form})

def lista_recursos(request):
    recursos = Recurso.objects.all()
    return render(request, 'lista_recursos.html', {'recursos': recursos})



from django.http import FileResponse
from django.shortcuts import get_object_or_404
from .models import Recurso

def ver_pdf(request, pdf_id):
    pdf = get_object_or_404(Recurso, pk=pdf_id)
    ruta_archivo = pdf.archivo.path
    return FileResponse(open(ruta_archivo, 'rb'), content_type='application/pdf')

