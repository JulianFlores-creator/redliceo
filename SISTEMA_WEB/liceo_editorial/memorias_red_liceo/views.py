from django.http import FileResponse
from django.shortcuts import render, get_object_or_404
from .forms import DocumentoMemoriaForm
from .models import DocumentoMemoria


def capturarMemoria(request):
    if request.method == 'POST':
        form = DocumentoMemoriaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # Aquí puedes agregar cualquier lógica adicional, como redireccionar a otra página
    else:
        form = DocumentoMemoriaForm()
    return render(request, 'capturar_documento.html', {'form': form})

def mostrarMemorias(request):
    memorias = DocumentoMemoria.objects.all()
    return render(request, 'encuentros.html',{'encuentros':memorias})

def verMemorias(request, m_id):
    memoriaPdf = get_object_or_404(DocumentoMemoria, m_id)
    ruta_archivo = memoriaPdf.archivo.path
    return FileResponse(ruta_archivo,'rb', content_type='application/pdf')

