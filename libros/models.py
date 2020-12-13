from django.db import models
from editoriales.models import Editorial
from autores.models import Autor
# Create your models here.
class Libro(models.Model):
    titulo = models.CharField(max_length=200)
    fecha_publicacion = models.DateField()
    paginas = models.IntegerField()

    editorial = models.ForeignKey(Editorial, on_delete=models.CASCADE)
    autores = models.ManyToManyField(Autor, related_name='libros')

    def __str__(self):
        return self.titulo