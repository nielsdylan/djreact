from django import forms
from .models import Persona

class PersonaForm(forms.ModelForm):
    class Meta:
        model = Persona
        fields = ['dni','apellidoPaterno','apellidoMaterno','nombres','direccion','telefono']