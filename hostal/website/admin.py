from django.contrib import admin
from .models import Comedor, Empleado, Huesped, Inventario, Proveedor, Reserva,Rubro_proveedor, Cliente, Producto, Ordenesdecompra, Orden_pedido, Servicio

# Register your models here.
admin.site.register(Proveedor)
admin.site.register(Rubro_proveedor)
admin.site.register(Cliente)
admin.site.register(Producto)
admin.site.register(Empleado)
admin.site.register(Ordenesdecompra)
admin.site.register(Orden_pedido)
admin.site.register(Comedor)
admin.site.register(Inventario)
admin.site.register(Servicio)
admin.site.register(Huesped)
admin.site.register(Reserva)