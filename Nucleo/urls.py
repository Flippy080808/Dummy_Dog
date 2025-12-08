from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('Veterinaria', views.veter, name='veter'),
    path('servicios', views.serv, name='serv'),
    path('producto', views.producto, name='producto'),
    path('cuidador', views.cuidador, name='cuidador'),
    path('adopcion', views.adopcion, name='adopcion'),
    path('agregar_producto/', views.crear_producto, name='agregar_producto'),
    path('buscar/', views.buscar_productos, name='buscar_productos'),

    # CRUD - Read / Update / Delete
    path('productos/', views.lista_productos, name='productos_list'),
    path('productos/<int:pk>/', views.detalle_producto, name='producto_detail'),
    path('productos/<int:pk>/editar/', views.editar_producto, name='editar_producto'),
    path('productos/<int:pk>/eliminar/', views.eliminar_producto, name='eliminar_producto'),
]