from django.contrib import admin
from .models import LibroTexto,Libro,LibroReferencia

# Register your models here.


admin.site.register(Libro)
admin.site.register(LibroTexto)
admin.site.register(LibroReferencia)



