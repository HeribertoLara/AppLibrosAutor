from django.db import models

# Create your models here.
class Editorial(models.Model):
    nombre = models.CharField(max_length=200)
    datos_contacto = models.CharField(max_length=20)

    def __str__(self):
        return self.nombre