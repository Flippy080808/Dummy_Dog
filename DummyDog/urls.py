from django.contrib import admin
from django.urls import path, include
from Nucleo import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('Nucleo.urls')),

]