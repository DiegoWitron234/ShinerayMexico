from django.db import models

class Vehiculo(models.Model):
    modelo = models.CharField(max_length=50)
    tipo = models.CharField(max_length=50)
    carga = models.PositiveIntegerField(default=0)
    motor = models.PositiveIntegerField(default=0)
    rendimiento = models.PositiveIntegerField(default=0)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    imagen = models.ImageField(upload_to='vehiculos/', null=True, blank=True)
    descripcion = models.TextField(blank=True)

    def __str__(self):
        return f"{self.tipo} {self.modelo}"
