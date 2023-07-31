from django import forms
from .models import LibroTexto, LibroReferencia

class LibroTextoForm(forms.ModelForm):
    class Meta:
        model = LibroTexto
        fields = '__all__'

class LibroReferenciaForm(forms.ModelForm):
    class Meta:
        model = LibroReferencia
        fields = '__all__'

class BusquedaForm(forms.Form):
    termino_busqueda = forms.CharField(max_length=100)