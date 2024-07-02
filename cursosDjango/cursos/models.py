from django.db import models
from ckeditor.fields import RichTextField


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
    

class Actividad(models.Model):
    claveActividad = models.AutoField(primary_key=True,verbose_name="Clave")
    nombre = models.ForeignKey(CursosAlmacenados, 
                               on_delete=models.CASCADE,verbose_name="Curso")
    descripcion = RichTextField(verbose_name="Comentario")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Registrado")


    class Meta:
        verbose_name = "Actividade"
        verbose_name_plural = "Actividades"
        ordering = ["-created"]

    def __str__(self):
        return self.descripcion
