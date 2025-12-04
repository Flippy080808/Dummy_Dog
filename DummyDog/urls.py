from django.contrib import admin
from django.urls import path
from Nucleo import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('Veterinaria', views.veter, name='veter'),
    path('servicios',views.serv,name='serv'),
    path('producto', views.producto, name='producto'),
    path('cuidador', views.cuidador, name='cuidador'),
    path('adopcion', views.adopcion, name='adopcion'),
    path('agregar_producto/', views.crear_producto, name='agregar_producto'),
]