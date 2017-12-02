from django.db import models

class Estacion(models.Model):
    nombre = models.CharField(max_length=255, unique=True)
    ubicacion = models.CharField(max_length=255, blank=True, null=True)
    region = models.CharField(max_length=255, blank=True, null=True)
    departamento = models.CharField(max_length=255, blank=True, null=True)
    ciudad = models.CharField(max_length=255, blank=True, null=True)
    direccion = models.CharField(max_length=255, blank=True, null=True)
    latitud = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True)
    longitud = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True)
    estructura = models.CharField(max_length=255, blank=True, null=True)
    categoria = models.CharField(max_length=255, blank=True, null=True)

    estado = models.BooleanField(default=True, editable=False)
    subestado = models.BooleanField(default=False, editable=False)
    creado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('creado',)
        verbose_name = 'estacion'
        verbose_name_plural = 'estaciones'

    def __str__(self):
        return self.nombre
