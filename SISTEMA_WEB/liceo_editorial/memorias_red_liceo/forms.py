from django import forms
from .models import DocumentoMemoria

class DocumentoMemoriaForm(forms.ModelForm):
    class Meta:
        model = DocumentoMemoria
        fields = ['titulo', 'documento', 'fecha', 'referencia']
