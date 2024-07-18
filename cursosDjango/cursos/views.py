from django.shortcuts import render
from .models import CursosAlmacenados

def cursos(requets):
    nombre = CursosAlmacenados.objects.all()
    return render(requets, "cursos/cursos.html", {'9B':nombre})


def cursosPorPrecio(request):
    nombre = CursosAlmacenados.objects.filter(precio__gte=100)
    return render(request, "cursos/consultas.html", {'9B':nombre})


def cursosPorModulos(request, modulos):
    nombre = CursosAlmacenados.objects.filter(modulos=modulos)
    return render(request, "cursos/consultas.html", {'9B':nombre})

