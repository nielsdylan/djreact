from django.shortcuts import render

from django.shortcuts import render,redirect
from .forms import PersonaForm
from .models import Persona
from django.contrib.auth.forms import AuthenticationForm
# Create your views here.


def index(request):
    return render(request, "index.html")

def RegistrarPersona(request):
    if request.method == 'POST':
        print(request.POST)
        persona_form = PersonaForm(request.POST)
        print(persona_form)
        if persona_form.is_valid():
            persona_form.save()
            return redirect('menu')
        #verifica si es valido con el sigiente if de los campos asignados
    else:
        persona_form = PersonaForm()
    return render(request,'idioma/registrar.html', {'persona_form':persona_form})
    