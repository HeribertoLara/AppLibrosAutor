from libros.models import Libro
from libros.serializers import LibroSerializer
from rest_framework import viewsets
# Create your views here.

class LibroViewSet(viewsets.ModelViewSet):
    queryset = Libro.objects.all()
    serializer_class = LibroSerializer


#from django.shortcuts import render
#from libros.models import Libro
# Create your views here.
#def views_libros(request):
 #   libros = Libro.objects.all()
  #  return render(request,'libros/libros.html',{'libros':libros})