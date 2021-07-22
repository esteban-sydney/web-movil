import datetime
from django.db import models
from django.db.models.enums import Choices
from django.utils import timezone
from django.db.models.fields import EmailField, IntegerField, BigAutoField, DateField, DateTimeField, DateTimeCheckMixin
from django.urls import reverse
from django.contrib.auth.models import User
import uuid
import datetime

# Create your models here.

class Rubro_proveedor(models.Model):
    id_rubro = models.BigAutoField(primary_key=True)
    rubro = models.CharField(max_length=25,null=False)
    descripcion = models.CharField(max_length=50)

    def __str__(self):
        return self.rubro

    def get_absolute_url(self):
        return reverse('rubros_proveedor')

class Proveedor(models.Model):
    rut_proveedor = models.IntegerField(primary_key=True)
    dv = models.CharField(max_length=1, null=False)
    nombre = models.CharField(max_length=50,null=False)
    telefono = models.IntegerField(null=False)
    email = models.EmailField(null=False)
    direccion = models.CharField(max_length=100,null=False)
    id_rubro = models.ForeignKey(Rubro_proveedor,on_delete=models.CASCADE)
    usuario = models.OneToOneField(User,on_delete=models.CASCADE, null=True)

    def get_absolute_url(self):
        return reverse('proveedores')
    
    def __str__(self):
        return self.nombre

class Orden_pedido(models.Model):
    numero_orden_p=models.BigAutoField(primary_key=True)
    fecha=models.DateField(null=False)
    neto=models.IntegerField(null=False)
    iva=models.IntegerField(null=False)
    total=models.IntegerField(null=False)
    rut_proveedor=models.ForeignKey(Proveedor,on_delete=models.CASCADE)
    #rut_empleado=models.IntegerField(primary_key=True)

    def get_absolute_url(self):
        return reverse('orden_pedido')

    def __str__(self):
        return '%s' % (self.numero_orden_p)

class Cliente(models.Model):

    rut_cliente = models.IntegerField(primary_key=True, help_text='')
    dv = models.CharField(max_length=1)
    nombre = models.CharField(max_length=100)
    telefono = models.IntegerField()
    email = models.CharField(max_length=100)
    direccion = models.CharField(max_length=100)
    usuario = models.OneToOneField(User,on_delete=models.CASCADE, null=True)

    def get_absolute_url(self):
        return reverse('clientes_list')

    def __str__(self):
        return self.nombre


#Opciones de habitaciones
habitacion_estado = [
    ('Disponible', 'Disponible'),
    ('Asignada', 'Asignada'),
    ('En Mantención', 'En Mantención')
]  

habitacion_tipo_cama = [
    ('Individual', 'Individual'),
    ('Queen', 'Queen'),
    ('King', 'King')
]

habitacion_tipo= [
    ('Individual', 'Individual'),
    ('Individual Premium', 'Individual Premium'),
    ('Doble', 'Doble'),
    ('Loft', 'Loft')
]

class Habitacion(models.Model):

    numero_habitacion = models.IntegerField(primary_key=True, help_text='')
    tipo = models.CharField(max_length=25,
    null=False, blank=False,
    choices=habitacion_tipo,
    #default=1
    )    
    estado = models.CharField(max_length=25,null=False, blank=False, choices=habitacion_estado,
    #default=1
    )
    tipo_cama = models.CharField(max_length=25,
    null=False, blank=False,
    choices=habitacion_tipo_cama,
    #default=1
    )
    accesorios = models.CharField(max_length=50)
    precio = models.IntegerField()

    def get_absolute_url(self):
        return reverse('habitacion-detail', args=[str(self.id)])

    def __str__(self):
        return str(self.numero_habitacion)
#fin de Opciones de habitaciones


# modelo base de datos producto
class Producto(models.Model):

    codigo_producto = models.IntegerField(primary_key=True, help_text='')
    nombre = models.CharField(max_length=100)
    familia=models.CharField(max_length=50)
    descripcion = models.CharField(max_length=250)
    fecha_elaboracion =models.DateField(default=timezone.now)
    fecha_vencimineto =models.DateField(default=timezone.now)
    stock= models.IntegerField()
    stock_critico=models.IntegerField()
    precio_unitario=models.IntegerField()
    item= models.CharField(max_length=100)

    def get_absolute_url(self):
        return reverse('producto-detail', args=[str(self.id)])

    def __str__(self):
        return self.nombre

tipo_perfil= [
    ('cambiar', 'cambiar'),
    ('agregar', 'agregar')
]

 
   

# JUAN
class Empleado(models.Model):

    rut_empleado = models.IntegerField(primary_key=True, help_text='')
    dv = models.CharField(max_length=1)
    nombres = models.CharField(max_length=100)
    a_paterno = models.CharField(max_length=100)
    a_materno = models.CharField(max_length=100)
    telefono = models.IntegerField()
    email = models.CharField(max_length=100)
    direccion = models.CharField(max_length=100)
    administrador = models.BooleanField(default=False,null=False)
    usuario = models.OneToOneField(User,on_delete=models.CASCADE, null=True)

    def get_absolute_url(self):
        return reverse('empleados_list')

    def __str__(self):
        return self.nombres


#juan
class Ordenesdecompra(models.Model):
    numero_orden_c = models.IntegerField(primary_key=True, help_text='')
    fecha_llegada = models.DateField(default=timezone.now)
    fecha_salida = models.DateField(default=timezone.now)
    total_dias = models.IntegerField()
    total_huespedes = models.IntegerField()
    rut_cliente = models.ForeignKey(Cliente,on_delete=models.CASCADE)
    #codigo_servicio = models.ForeignKey(Servicio,on_delete=models.CASCADE)
    #numero_factura = models.ForeignKey(Factura,on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('ordenesdecompra-detail', args=[str(self.id)])

    def __str__(self):
        return str(self.numero_orden_c)

#modelo servicio (sin vista, solo para llaves foraneas )
class Servicio(models.Model):
    codigo_servicio = models.IntegerField(primary_key=True, help_text='')
    tipo = models.CharField(max_length=100)
    precio = models.IntegerField()

    def get_absolute_url(self):
        return reverse('servicio-detail', args=[str(self.id)])

    def __str__(self):
        return "%s - %s" % (self.codigo_servicio, self.tipo)

class Comedor(models.Model):
    codigo_plato = models.IntegerField(primary_key=True, help_text='')
    nombre = models.CharField(max_length=25)
    descripcion = models.CharField(max_length=150)
    tipo_comida = models.CharField(max_length=25)
    dia = models.DateField(default=timezone.now)  # cambiar para que salga nombre el dia....
    precio = models.IntegerField()
    codigo_servicio = models.ForeignKey(Servicio,on_delete=models.CASCADE)
    
    
    def get_absolute_url(self):
        return reverse('plato-detail', args=[str(self.id)])

    def __str__(self):
        return self.nombre

class Factura(models.Model):
    numero_factura = models.IntegerField(primary_key=True, help_text='')
    fecha = models.DateField(default=timezone.now)
    nombre = models.CharField(max_length=25)
    neto = models.IntegerField()
    iva = models.IntegerField()
    total = models.IntegerField()  # cambiar para que salga nombre el dia....
    #numero_orden_c = models.ForeignKey(Ordenesdecompra,on_delete=models.CASCADE)
    
    
    def get_absolute_url(self):
        return reverse('factura-detail', args=[str(self.id)])

    def __str__(self):
        return str(self.numero_factura)


#CRUD inventario
class Inventario(models.Model):
    codigo = models.IntegerField(primary_key=True, help_text='')
    nombre = models.CharField(max_length=100)
    fecha_actual = models.DateField(default=timezone.now)
    fecha_elaboracion = models.DateField(default=timezone.now)
    fecha_vencimiento = models.DateField(default=timezone.now)
    total_cantidad = models.CharField(max_length=100)
    responsable = models.CharField(max_length=100, blank=True)

    
    def get_absolute_url(self):
        return reverse('inventario-detail', args=[str(self.id)])

    def __str__(self):
        return str(self.codigo)

class Huesped(models.Model):
    rut_huesped = models.IntegerField(primary_key=True)
    dv = models.CharField(max_length=1)
    nombre = models.CharField(max_length=100)
    telefono = models.IntegerField()
    email = models.EmailField()

    def get_absolute_url(self):
        return reverse('huespedes')
    
    def __str__(self):
        return self.nombre
    
class Reserva(models.Model):
    id_reserva = models.BigAutoField(primary_key=True)
    fecha_desde = models.DateField(default=datetime.date.today)
    fecha_hasta = models.DateField(default=datetime.date.today)
    vigente = models.BooleanField(default=True)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('reservas')

    def __str__(self):
        return str(self.id_reserva)

class ReservaHuesped(models.Model):
    id_reserva = models.ForeignKey(Reserva, on_delete=models.CASCADE)
    rut_huesped = models.ForeignKey(Huesped, null=True, on_delete=models.SET_NULL)
    habitacion = models.ForeignKey(Habitacion, null=True, on_delete=models.SET_NULL)

    def get_absolute_url(self):
        return reverse('reservas')

