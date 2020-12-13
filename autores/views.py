from django.shortcuts import render
from django.http import HttpResponse
from autores.models import Autor
from django.views import View
from rest_framework import viewsets, status
#import rest_framework.response import Response
from autores.serializers import AutorSerializer
from rest_framework.decorators import action
from rest_framework.response import Response


# Create your views here.

class AutorViewSet(viewsets.ModelViewSet):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer

    @action(methods=['GET'],detail=True)
    def autores(self,request,pk=None):
        libro= self.get_object()
        serialized=AutorSerializer(libro.autores, many=True)
        return Response(status=status.HTTP_200_OK,data=serialized.data)

    #@action(methods=['GET'])




#def views_autores(request):
 #   autores = Autor.objects.all()
  #  return render(request,'autores_templates/autores.html',{'autores':autores})

#class AutorView(View):
 #   http_method_names = ['get', 'post']
  #  template_name = 'autores_templates/autores.html'

   # def get(self,request):
    #    autores = Autor.objects.all()
     #   return render(request,
      #                self.template_name,
       #               {'autores':autores}
        #              )
    #def post(self,request):
     #   autor_data= {
      #      'nombre': request.POST['nombre'],
       #     'telefono': request.POST['telefono'],
        #    'correo': request.POST['correo'],
         #   'edad': int(request.POST['edad'])
        #}
        #print(autor_data)
        #return render(request, self.template_name,{})



