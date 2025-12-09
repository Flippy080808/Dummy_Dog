from django.shortcuts import render, redirect, get_object_or_404
import requests #type: ignore
from .forms import ProductoForm
from .models import Producto

def index(request):
    # Obtener productos de la base de datos
    productos = Producto.objects.all().order_by('-id_product')[:8]  # Últimos 8 productos
    return render(request, "index.html", {"productos": productos})

def veter(request):
    return render(request, 'veter.html')

def serv(request):
    return render(request, 'serv.html')

def producto(request, pk=None):
    if pk:
        producto = get_object_or_404(Producto, pk=pk)
        # Obtener productos relacionados (otros productos, excluir el actual)
        productos_relacionados = Producto.objects.exclude(pk=pk)[:4]
        return render(request, 'producto.html', {
            'producto': producto,
            'productos_relacionados': productos_relacionados
        })
    else:
        # Si no hay pk, mostrar el último producto agregado
        producto = Producto.objects.order_by('-id_product').first()
        if producto:
            productos_relacionados = Producto.objects.exclude(pk=producto.pk)[:4]
            return render(request, 'producto.html', {
                'producto': producto,
                'productos_relacionados': productos_relacionados
            })
        else:
            return render(request, 'producto.html', {'producto': None})

def cuidador(request):
    return render(request, 'cuidador.html')

def adopcion(request):
    return render(request, 'adopcion.html')

def carrito(request):
    return render(request, 'carrito.html')

# Autor Alberto GJ
def crear_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('productos_list')
    else:
        form = ProductoForm()
    return render(request, 'agregar_productos.html', {'form': form})

# READ - Lista de productos
def lista_productos(request):
    productos = Producto.objects.all().order_by('nombre')
    return render(request, 'productos_list.html', {'productos': productos})

# READ - Detalle de producto
def detalle_producto(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    return render(request, 'producto_detail.html', {'producto': producto})

# UPDATE - Editar producto
def editar_producto(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    if request.method == 'POST':
        form = ProductoForm(request.POST, instance=producto)
        if form.is_valid():
            form.save()
            return redirect('productos_list')
    else:
        form = ProductoForm(instance=producto)
    return render(request, 'editar_producto.html', {'form': form, 'producto': producto})

# DELETE - Eliminar producto
def eliminar_producto(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    if request.method == 'POST':
        producto.delete()
        return redirect('productos_list')
    return render(request, 'confirmar_eliminar.html', {'producto': producto})

#Autor Jose FDA
def buscar_productos(request):
    q = request.GET.get('consulta_de_productos', '')
    resultados = []
    if q:
        resultados = Producto.objects.filter(
            nombre__icontains=q
        ) | Producto.objects.filter(
            marca__icontains=q
        )
    return render(request, 'buscar.html', {'resultados': resultados})