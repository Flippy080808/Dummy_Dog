from django.shortcuts import render, redirect
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
            return redirect('agregar_producto')  # recarga el formulario vacío; cambiar destino si se desea
    else:
        form = ProductoForm()
    return render(request, 'agregar_productos.html', {'form': form})



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


def editar_producto(request, producto_id):
    producto = Producto.objects.get(pk=producto_id)
    if request.method == 'POST':
        form = ProductoForm(request.POST, instance=producto)
        if form.is_valid():
            form.save()
            return redirect('buscar_productos')
    else:
        form = ProductoForm(instance=producto)
    return render(request, 'editar_producto.html', {'form': form, 'producto': producto})


def eliminar_producto(request, producto_id):
    producto = Producto.objects.get(pk=producto_id)
    if request.method == 'POST':
        producto.delete()
        return redirect('buscar_productos')
    return render(request, 'eliminar_producto.html', {'producto': producto})