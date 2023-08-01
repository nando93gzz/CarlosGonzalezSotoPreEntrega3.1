from django.urls import path, include
from .views import *

urlpatterns = [
    
    path('', index, name="inicio"),
    path('agregar_libro/', agregar_libro, name='agregar_libro'),
    path('buscar_libro/', buscar_libro, name='buscar_libro'),
    path('eliminar_libro/', eliminar_libro, name='eliminar_libro'),
]


