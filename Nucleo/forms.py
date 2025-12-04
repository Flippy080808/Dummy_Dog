from django import forms
from .models import Producto

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'marca', 'precio', 'inventario', 'categoria', 'id_veter']