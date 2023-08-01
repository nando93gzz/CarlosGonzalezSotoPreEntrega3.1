from django.shortcuts import render, redirect, get_object_or_404
from .forms import LibroForm
from .models import *

def index(request):
    return render(request, "aplicacion/base.html")

def agregar_libro(request):
    if request.method == 'POST':
        form = LibroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('agregar_libro')
    else:
        form = LibroForm()
    return render(request, 'aplicacion/agregar_libro.html', {'form': form})

def buscar_libro(request):
    if request.method == 'POST':
        buscar = request.POST.get('buscar')
        libros = Libro.objects.filter(titulo__icontains=buscar)
        return render(request, 'aplicacion/resultado_busqueda.html', {'libros': libros})
    return render(request, 'aplicacion/buscar_libro.html')

def eliminar_libro(request, libro_id):
    libro = get_object_or_404(Libro, id=libro_id)
    libro.delete()
    return redirect('aplicacion/buscar_libro')



