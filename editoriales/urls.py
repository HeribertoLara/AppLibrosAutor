#from django.urls import path
#from editoriales.views import views_editoriales

from autores.views import AutorViewSet#views_autores, AutorView
from rest_framework.routers import DefaultRouter

router=DefaultRouter()
router.register(r'',AutorViewSet)

urlpatterns=router.urls

#app_name= 'editoriales'
#urlpatterns = [
 #   path('lista/',views_editoriales, name= 'views_editoriales')
#]