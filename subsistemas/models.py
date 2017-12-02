from django.db import models

class Subsistema(models.Model):
    nombre = models.CharField(max_length=255, unique=True)

    estado = models.BooleanField(default=True, editable=False)
    subestado = models.BooleanField(default=False, editable=False)
    creado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('creado',)
        verbose_name = 'subsistema'
        verbose_name_plural = 'subsistemas'

    def __str__(self):
        return self.nombre
