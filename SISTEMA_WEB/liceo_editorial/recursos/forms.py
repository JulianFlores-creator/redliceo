from django import forms
from .models import Recurso


class RecursoForm(forms.ModelForm):
    class Meta:
        model = Recurso
        fields = ['titulo', 'archivo','coordinadores','ISBN','fecha','edicion','autor','fotoPortada']


