from django.db import models

class Producto(models.Model):
    id_product = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=200)
    marca = models.CharField(max_length=100, blank=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    inventario = models.IntegerField(default=0)
    categoria = models.CharField(max_length=100, blank=True)
    id_veter = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return f"{self.nombre} ({self.marca})"
