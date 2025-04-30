from django.db import models
from django.contrib.auth.models import User

class Producto(models.Model):
    codigo_barras = models.CharField(max_length=100, unique=True)
    referencia = models.CharField(max_length=100)
    departamento = models.CharField(max_length=100)
    seccion = models.CharField(max_length=100)
    descripcion = models.TextField()
    tipo = models.CharField(max_length=50)
    stock = models.IntegerField()

    creado = models.DateTimeField(auto_now_add=True)
    modificado = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.descripcion} ({self.codigo_barras})"

class MovimientoInventario(models.Model):
    TIPO_CHOICES = (
        ('entrada', 'Entrada'),
        ('salida', 'Salida'),
    )

    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    tipo = models.CharField(max_length=10, choices=TIPO_CHOICES)
    cantidad = models.PositiveIntegerField()
    usuario = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.tipo.capitalize()} - {self.producto.descripcion} ({self.cantidad})"

class ConteoInventario(models.Model):
    nombre = models.CharField(max_length=100)
    creado_por = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    fecha_creado = models.DateTimeField(auto_now_add=True)
    cerrado = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.nombre} ({'Cerrado' if self.cerrado else 'Activo'})"

class ItemConteo(models.Model):
    conteo = models.ForeignKey(ConteoInventario, on_delete=models.CASCADE, related_name="items")
    producto = models.ForeignKey('Producto', on_delete=models.CASCADE)
    cantidad_contada = models.PositiveIntegerField()
    fecha = models.DateTimeField(auto_now_add=True)
    usuario = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.producto.descripcion} - {self.cantidad_contada}"
