from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('Veterinaria', views.veter, name='veter'),
    path('servicios', views.serv, name='serv')
]