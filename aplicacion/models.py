from django.db import models

# Create your models here.
class Curso(models.Model):
    nombre = models.CharField(max_length=50)
    comision = models.IntegerField()

class Estudiante(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.EmailField()

class Profesor(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.EmailField()
    profesion = models.CharField(max_length=50)

class Entregable(models.Model):
    nombre = models.CharField(max_length=50)
    fechaEntrega = models.DateField()
    entregado = models.BooleanField()   

##############################
class Libro(models.Model):
    titulo = models.CharField(max_length=100)
    autor = models.CharField(max_length=100)
    # Otros campos relacionados con libros

    class Meta:
        abstract = True

class LibroTexto(Libro):
    asignatura = models.CharField(max_length=100)
    nivel = models.CharField(max_length=50)
    # Otros campos específicos de libros de texto

class LibroReferencia(Libro):
    editorial = models.CharField(max_length=100)
    # Otros campos específicos de libros de referencia