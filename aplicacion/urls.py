
from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name="inicio" ),
    path('profesores/', profesores, name="profesores" ),
    path('cursos/', cursos, name="cursos" ),
    path('entregables/', entregables, name="entregables" ),
    path('estudiantes/', estudiantes, name="estudiantes" ),
   
]
