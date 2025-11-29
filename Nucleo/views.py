from django.shortcuts import render
import requests #type: ignore

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