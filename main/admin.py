# main/admin.py
from django.contrib import admin
from .models import Vehiculo

@admin.register(Vehiculo)
class VehiculoAdmin(admin.ModelAdmin):
    list_display = ('marca', 'modelo', 'año', 'precio')
    search_fields = ('marca', 'modelo')
    list_filter = ('marca', 'año')
