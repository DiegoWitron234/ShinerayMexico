from django.db import models

class Vehiculo(models.Model):
    marca = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)
    año = models.PositiveIntegerField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    imagen = models.ImageField(upload_to='vehiculos/', null=True, blank=True)
    descripcion = models.TextField(blank=True)

    def __str__(self):
        return f"{self.marca} {self.modelo} ({self.año})"
