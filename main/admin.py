# main/admin.py
from django.contrib import admin
from .models import Vehiculo

@admin.register(Vehiculo)
class VehiculoAdmin(admin.ModelAdmin):
    list_display = ('tipo', 'modelo', 'precio')
    search_fields = ('tipo', 'modelo')
    list_filter = ('tipo',)

