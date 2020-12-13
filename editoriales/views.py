from django.shortcuts import render
from editoriales.models import Editorial
from editoriales.serialaizers import EditorialSerializer
from rest_framework import viewsets
# Create your views here.

class EditorialViewSet(viewsets.ModelViewSet):
    queryset = Editorial.objects.all()
    serializer_class = EditorialSerializer

#def views_editoriales(request):
 #   editoriales = Editorial.objects.all()
  #  return render(request,'editorial/editorial.html',{'editoriales':editoriales})

