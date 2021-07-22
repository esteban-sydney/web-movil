# Generated by Django 3.1.2 on 2021-07-15 19:02

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('rut_cliente', models.IntegerField(primary_key=True, serialize=False)),
                ('dv', models.CharField(max_length=1)),
                ('nombre', models.CharField(max_length=25)),
                ('telefono', models.IntegerField()),
                ('email', models.CharField(max_length=25)),
                ('direccion', models.CharField(max_length=25)),
                ('usuario', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Factura',
            fields=[
                ('numero_factura', models.IntegerField(primary_key=True, serialize=False)),
                ('fecha', models.DateField(default=django.utils.timezone.now)),
                ('nombre', models.CharField(max_length=25)),
                ('neto', models.IntegerField()),
                ('iva', models.IntegerField()),
                ('total', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Habitacion',
            fields=[
                ('numero_habitacion', models.IntegerField(primary_key=True, serialize=False)),
                ('tipo', models.CharField(choices=[('Individual', 'Individual'), ('Individual Premium', 'Individual Premium'), ('Doble', 'Doble'), ('Loft', 'Loft')], max_length=25)),
                ('estado', models.CharField(choices=[('Disponible', 'Disponible'), ('Asignada', 'Asignada'), ('En Mantención', 'En Mantención')], max_length=25)),
                ('tipo_cama', models.CharField(choices=[('Individual', 'Individual'), ('Queen', 'Queen'), ('King', 'King')], max_length=25)),
                ('accesorios', models.CharField(max_length=50)),
                ('precio', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Huesped',
            fields=[
                ('rut_huesped', models.IntegerField(primary_key=True, serialize=False)),
                ('dv', models.CharField(max_length=1)),
                ('nombre', models.CharField(max_length=100)),
                ('telefono', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Inventario',
            fields=[
                ('codigo', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
                ('fecha_actual', models.DateField(default=django.utils.timezone.now)),
                ('fecha_elaboracion', models.DateField(default=django.utils.timezone.now)),
                ('fecha_vencimiento', models.DateField(default=django.utils.timezone.now)),
                ('total_cantidad', models.CharField(max_length=100)),
                ('responsable', models.CharField(blank=True, max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('codigo_producto', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=25)),
                ('familia', models.CharField(max_length=50)),
                ('descripcion', models.CharField(max_length=250)),
                ('fecha_elaboracion', models.DateField(default=django.utils.timezone.now)),
                ('fecha_vencimineto', models.DateField(default=django.utils.timezone.now)),
                ('stock', models.IntegerField()),
                ('stock_critico', models.IntegerField()),
                ('precio_unitario', models.IntegerField()),
                ('item', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Reserva',
            fields=[
                ('id_reserva', models.BigAutoField(primary_key=True, serialize=False)),
                ('fecha_desde', models.DateField(default=datetime.date.today)),
                ('fecha_hasta', models.DateField(default=datetime.date.today)),
                ('vigente', models.BooleanField(default=True)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.cliente')),
            ],
        ),
        migrations.CreateModel(
            name='Rubro_proveedor',
            fields=[
                ('id_rubro', models.BigAutoField(primary_key=True, serialize=False)),
                ('rubro', models.CharField(max_length=25)),
                ('descripcion', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Servicio',
            fields=[
                ('codigo_servicio', models.IntegerField(primary_key=True, serialize=False)),
                ('tipo', models.CharField(max_length=100)),
                ('precio', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='ReservaHuesped',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('habitacion', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='website.habitacion')),
                ('id_reserva', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.reserva')),
                ('rut_huesped', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='website.huesped')),
            ],
        ),
        migrations.CreateModel(
            name='Proveedor',
            fields=[
                ('rut_proveedor', models.IntegerField(primary_key=True, serialize=False)),
                ('dv', models.CharField(max_length=1)),
                ('nombre', models.CharField(max_length=50)),
                ('telefono', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('direccion', models.CharField(max_length=100)),
                ('id_rubro', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.rubro_proveedor')),
                ('usuario', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Ordenesdecompra',
            fields=[
                ('numero_orden_c', models.IntegerField(primary_key=True, serialize=False)),
                ('fecha_llegada', models.DateField(default=django.utils.timezone.now)),
                ('fecha_salida', models.DateField(default=django.utils.timezone.now)),
                ('total_dias', models.IntegerField()),
                ('total_huespedes', models.IntegerField()),
                ('rut_cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.cliente')),
            ],
        ),
        migrations.CreateModel(
            name='Orden_pedido',
            fields=[
                ('numero_orden_p', models.BigAutoField(primary_key=True, serialize=False)),
                ('fecha', models.DateField()),
                ('neto', models.IntegerField()),
                ('iva', models.IntegerField()),
                ('total', models.IntegerField()),
                ('rut_proveedor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.proveedor')),
            ],
        ),
        migrations.CreateModel(
            name='Empleado',
            fields=[
                ('rut_empleado', models.IntegerField(primary_key=True, serialize=False)),
                ('dv', models.CharField(max_length=1)),
                ('nombres', models.CharField(max_length=25)),
                ('a_paterno', models.CharField(max_length=25)),
                ('a_materno', models.CharField(max_length=25)),
                ('telefono', models.IntegerField()),
                ('email', models.CharField(max_length=25)),
                ('direccion', models.CharField(max_length=50)),
                ('administrador', models.BooleanField(default=False)),
                ('usuario', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Comedor',
            fields=[
                ('codigo_plato', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=25)),
                ('descripcion', models.CharField(max_length=150)),
                ('tipo_comida', models.CharField(max_length=25)),
                ('dia', models.DateField(default=django.utils.timezone.now)),
                ('precio', models.IntegerField()),
                ('codigo_servicio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.servicio')),
            ],
        ),
    ]