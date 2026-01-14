from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'), # La ruta vacía aquí es la raíz de la app
]