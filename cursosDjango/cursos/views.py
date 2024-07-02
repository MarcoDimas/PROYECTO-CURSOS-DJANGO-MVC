from django.shortcuts import render
from .models import CursosAlmacenados

# Create your views here.
def cursos(requets):
    nombre = CursosAlmacenados.objects.all()
    return render(requets, "cursos/cursos.html", {'9B':nombre})