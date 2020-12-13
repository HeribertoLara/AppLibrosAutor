from django.urls import path
from autores.views import AutorViewSet#views_autores, AutorView
from rest_framework.routers import DefaultRouter

router=DefaultRouter()
router.register(r'',AutorViewSet)

urlpatterns=router.urls
#app_name= 'autores'
#urlpatterns = [
    #path('lista/',views_autores, name= 'views_autores'),
 #   path('vista/',AutorView.as_view(), name='vista')
#]