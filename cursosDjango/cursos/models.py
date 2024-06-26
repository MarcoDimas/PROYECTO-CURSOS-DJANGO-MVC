from django.db import models


class CursosAlmacenados(models.Model) :
    nombre = models.TextField()
    email = models.EmailField(unique=True)
    curso = models.CharField(max_length=10)  
    modulos = models.IntegerField()
    precio = models.FloatField()
    comentario = models.CharField(max_length=500, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name='Crear')
    updated = models.DateTimeField(auto_now_add=True, verbose_name='Editar')

    class Meta:
        verbose_name = "Cursos"
        verbose_name_plural = "Curso"
        ordering = ["-created"]

    def __str__(self):
        return self.nombre