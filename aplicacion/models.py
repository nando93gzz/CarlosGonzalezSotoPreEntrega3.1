from django.db import models

class Libro(models.Model):
    titulo = models.CharField(max_length=200)
    autor = models.CharField(max_length=100)
    contenido = models.TextField()
    

    def __str__(self):
        return self.titulo

class LibroTexto(Libro):
    tema = models.CharField(max_length=100)
    nivel = models.CharField(max_length=50)

class LibroReferencia(Libro):
    isbn = models.CharField(max_length=13)
