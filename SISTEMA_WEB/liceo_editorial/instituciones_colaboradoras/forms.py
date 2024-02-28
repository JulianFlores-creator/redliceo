from django import forms
from .models import FotoInstitucion

class FotosFormulario(forms.ModelForm):
    class Meta:
        model = FotoInstitucion
        fields = ['title', 'photo']
