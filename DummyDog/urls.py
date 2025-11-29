from django.contrib import admin
from django.urls import path
from Nucleo import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('Veterinaria', views.veter, name='veter'),
    path('servicios',views.serv,name='serv')
]