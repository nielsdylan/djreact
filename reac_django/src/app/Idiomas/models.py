from django.db import models

# Create your models here.
class Persona(models.Model):
    PersonaId =models.AutoField(primary_key = True)
    dni = models.CharField( max_length = 200, blank = False, null = False)
    apellidoPaterno = models.CharField( max_length = 200, blank = False, null = False)
    apellidoMaterno = models.CharField( max_length = 200, blank = False, null = False)
    nombres = models.CharField( max_length = 200, blank = False, null = False)
    direccion = models.CharField( max_length = 200, blank = False, null = False)
    telefono = models.CharField( max_length = 200, blank = False, null = False)
    FechaCreacion = models.DateField('fecha de creacion', auto_now_add=False, auto_now=True)
    estado = models.BooleanField('Estado', default = True)

    class Meta:
        verbose_name = 'Persona'
        verbose_name_plural = 'Personas'
        ordering = ['dni'] #esta linea es para el orden alfabetico
    #eeste def es para no visualizrlo como objeto y verlo por su nombre
    def __str__(self):
        return self.apellidoPaterno