from django.shortcuts import render, redirect, get_object_or_404
import requests #type: ignore
from .forms import ProductoForm
from .models import Producto

def index(request):    
    url = "https://mocki.io/v1/294fd412-661e-46d1-a0bf-647e1f59fa53"
    try:
        response = requests.get(url)
        data = response.json()
        products = data.get("products", [])
    except:
        products = []

    return render(request, "index.html", {"products": products})

def veter(request):
    return render(request, 'veter.html')

def serv(request):
    return render(request, 'serv.html')

def producto(request):
    return render(request, 'producto.html')

def cuidador(request):
    return render(request, 'cuidador.html')

def adopcion(request):
    return render(request, 'adopcion.html')

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