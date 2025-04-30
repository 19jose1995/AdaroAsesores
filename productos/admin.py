from django.contrib import admin
from .models import Producto
from .models import MovimientoInventario

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('codigo_barras', 'referencia', 'departamento', 'seccion', 'descripcion', 'tipo', 'stock')
    search_fields = ('codigo_barras', 'descripcion', 'referencia')
    list_filter = ('departamento', 'seccion', 'tipo')

@admin.register(MovimientoInventario)
class MovimientoAdmin(admin.ModelAdmin):
    list_display = ('producto', 'tipo', 'cantidad', 'usuario', 'fecha')
    list_filter = ('tipo', 'fecha', 'usuario')