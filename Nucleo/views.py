from django.shortcuts import render, redirect
import requests #type: ignore
from .forms import ProductoForm

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

def crear_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('agregar_producto')  # recarga el formulario vacío; cambiar destino si se desea
    else:
        form = ProductoForm()
    return render(request, 'agregar_productos.html', {'form': form})