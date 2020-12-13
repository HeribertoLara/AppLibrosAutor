#from django.urls import path
#from libros.views import views_libros

from libros.views import LibroViewSet
from rest_framework.routers import DefaultRouter

router=DefaultRouter()
router.register(r'',LibroViewSet)

urlpatterns=router.urls

#app_name= 'Libros'
#urlpatterns = [
 #   path('lista/',views_libros, name= 'views_libros')
#]