from django import forms
from .models import Producto

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'marca', 'precio', 'inventario', 'categoria', 'id_veter', 'imagen_url']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre del producto'}),
            'marca': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Marca (ej: Pedigri, Purina)'}),
            'precio': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': '0.00', 'step': '0.01'}),
            'inventario': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': '0'}),
            'categoria': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Categoría (ej: Alimento, Juguete)'}),
            'id_veter': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'ID del veterinario (opcional)'}),
            'imagen_url': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'https://ejemplo.com/imagen.jpg'}),
        }