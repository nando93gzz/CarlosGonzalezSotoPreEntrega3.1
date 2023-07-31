from django.shortcuts import render
from django.http import HttpResponse
from .forms import LibroTextoForm, LibroReferenciaForm, BusquedaForm
from .models import *

# Create your views here.

def index(request):
    return render(request, "aplicacion/base.html") 
#HttpResponse("estoy en la app , seccion index")

def profesores(request):
    return render(request, "aplicacion/profesores.html") 

def estudiantes(request):
    return render(request, "aplicacion/estudiantes.html")

def entregables(request):
    return render(request, "aplicacion/entregables.html")

def cursos(request):
    ctx = {"cursos": Curso.objects.all()}
    return render(request, "aplicacion/cursos.html", ctx)


################################

def formulario_libro_texto(request):
    if request.method == 'POST':
        form = LibroTextoForm(request.POST)
        if form.is_valid():
            form.save()
            # Realizar acciones adicionales después de guardar el formulario
    else:
        form = LibroTextoForm()

    return render(request, 'formulario_libro_texto.html', {'form': form})

def formulario_libro_referencia(request):
    if request.method == 'POST':
        form = LibroReferenciaForm(request.POST)
        if form.is_valid():
            form.save()
            # Realizar acciones adicionales después de guardar el formulario
    else:
        form = LibroReferenciaForm()

    return render(request, 'formulario_libro_referencia.html', {'form': form})

def buscar_libros(request):
    resultados = None

    if request.method == 'POST':
        form = BusquedaForm(request.POST)
        if form.is_valid():
            termino_busqueda = form.cleaned_data['termino_busqueda']
            # Realizar la consulta en la base de datos para buscar libros relacionados con el término de búsqueda
            resultados = LibroTexto.objects.filter(titulo__icontains=termino_busqueda) | LibroReferencia.objects.filter(titulo__icontains=termino_busqueda)
    else:
        form = BusquedaForm()

    return render(request, 'buscar_libros.html', {'form': form, 'resultados': resultados})