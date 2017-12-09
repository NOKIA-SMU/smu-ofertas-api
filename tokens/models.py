from django.db import models

class Token(models.Model):
    uid = models.CharField(max_length=255, unique=True)
    credential = models.TextField(unique=True)

    estado = models.BooleanField(default=True, editable=False)
    subestado = models.BooleanField(default=False, editable=False)
    creado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('creado',)
        verbose_name = 'token'
        verbose_name_plural = 'tokens'

    def __str__(self):
        return self.uid
