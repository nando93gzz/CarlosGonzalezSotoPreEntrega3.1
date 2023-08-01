from django import forms
from .models import LibroTexto, LibroReferencia, Libro


class LibroTextoForm(forms.ModelForm):
    class Meta:
        model = LibroTexto
        fields = '__all__'

class LibroReferenciaForm(forms.ModelForm):
    class Meta:
        model = LibroReferencia
        fields = '__all__'

class LibroForm(forms.ModelForm):
    termino_busqueda = forms.CharField(max_length=100)

    class Meta:
        model = Libro
        fields = ['titulo', 'autor', 'contenido']  # Eliminar 'genero' si no es necesario

    # Opcionalmente, si deseas agregar los campos de LibroTexto y LibroReferencia:
    tema = forms.CharField(max_length=100, required=False)
    nivel = forms.CharField(max_length=50, required=False)
    isbn = forms.CharField(max_length=13, required=False)

