from django import forms

from contacto_info.models import Contacto


class ContactoForm(forms.ModelForm):
    class Meta:
        model = Contacto
        fields = ['nombre', 'correo', 'telefono', 'mensaje']
