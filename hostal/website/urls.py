
from django.urls import path
from django.views.generic.base import View
from . import views
 


urlpatterns = [
    path('home', views.home, name='home'),
    path('index', views.index, name='index'),
    path('habs', views.habs, name='habs'),
    path('cambiar_clave', views.ChangePasswordView, name='cambiar_clave'),

    path('clientes', views.clientes, name='clientes'),
    path('clientes/list', views.ClienteListView.as_view(), name='clientes_list'),
    path('cliente/<int:pk>', views.ClienteDetailView.as_view(), name='cliente-detail'),
    path('cliente/create', views.ClienteCreate.as_view(), name='cliente_create'),
    path('cliente/<int:pk>/update', views.ClienteUpdate.as_view(), name='cliente_update'),
    path('cliente/<int:pk>/delete', views.ClienteDelete.as_view(), name='cliente_delete'),

    path('habitaciones', views.habitaciones, name='habitaciones'),
    path('habitacion/create', views.HabitacionCreate.as_view(), name='habitacion_create'),
    path('habitaciones/list', views.HabitacionListView.as_view(), name='habitaciones_list'),
    path('habitacion/<int:pk>/update', views.HabitacionUpdate.as_view(), name='habitacion_update'),
    path('habitacion/<int:pk>/delete', views.HabitacionDelete.as_view(), name='habitacion_delete'),
    path('habitaciones/pdf', views.ListHabitacionesPdf.as_view(), name='habitaciones_pdf'),

    path('proveedor',views.ProveedorListView.as_view(), name='proveedores'),
    path('proveedor/create', views.ProveedorCreate.as_view(), name='proveedor_create'),
    #path('proveedor/<int:pk>', views.ProveedorDetailView.as_view(), name='proveedor_detail'),
    path('proveedor/<int:pk>/delete',views.ProveedorDelete.as_view(), name='proveedor_delete'),
    path('proveedor/<int:pk>/update',views.ProveedorUpdate.as_view(), name='proveedor_update'),

    path('proveedor/rubro', views.RubroProveedorListView.as_view(), name='rubros_proveedor'),
    path('proveedor/rubro/create', views.RubroProveedorCreateView.as_view(), name='rubro_create'),
    path('proveedor/rubro/<int:pk>/update', views.RubroProveedorUpdateView.as_view(), name='rubro_update'),
    path('proveedor/rubro/<int:pk>/delete', views.RubroProveedorDeleteView.as_view(), name='rubro_delete'),

    path('orden_pedido',views.Orden_pedidoListView.as_view(), name='orden_pedido'),
    path('orden_pedido/create', views.Orden_pedidoCreate.as_view(), name='orden_pedido_create'),
    path('orden_pedido/<int:pk>/delete', views.Orden_pedidoDelete.as_view(), name='orden_pedido_delete'),
    path('orden_pedido/<int:pk>/update',views.Orden_pedidoUpdate.as_view(), name='orden_pedido_update'),

    #Producto, Listar, Detalles, Crear, Actualizar, Eliminar PRODUCTO
    path('producto', views.producto, name='producto'),
    path('producto/list', views.ProductoListView.as_view(), name='producto_list'),
    path('producto/<int:pk>', views.ProductoDetailView.as_view(), name='producto-detail'),
    path('producto/create', views.ProductoCreate.as_view(), name='producto_create'),
    path('producto/<int:pk>/update', views.ProductoUpdate.as_view(), name='producto_update'),
    path('producto/<int:pk>/delete', views.ProductoDelete.as_view(), name='producto_delete'),


    #Listar, Detalles, Crear, Actualizar, Eliminar  USUARIO
    path('usuario', views.UsuarioListView.as_view(), name= 'usuario_list'),
    path('usuario/create', views.UsuarioCreate,name='usuario_create'),
    path('usuario/<int:user_id>/update', views.UsuarioUpdate,name='usuario_update'),
    path('usuario/<int:user_id>/deactivate', views.UsuarioDeactivate,name='usuario_deactivate'),
    path('usuario/<int:user_id>/activate', views.UsuarioActivate,name='usuario_activate'),

    path('usuario/grupo', views.GrupoListView.as_view(), name='groups_list'),
    path('usuario/grupo/create', views.GrupoCreateView.as_view(), name='group_create'),
    path('usuario/grupo/<int:pk>/update', views.GrupoUpdateView.as_view(), name='group_update'),
    path('usuario/grupo/<int:pk>/delete', views.GrupoDeleteView.as_view(), name='group_delete'),
    
    #JUAN
    path('empleados',views.empleados,name='empleados'),
    path('empleados/list', views.EmpleadoListView.as_view(), name='empleados_list'),
    path('empleado/<int:pk>', views.EmpleadoDetailView.as_view(), name='empleado-detail'),
    path('empleado/create', views.EmpleadoCreate.as_view(), name='empleado_create'),
    path('empleado/<int:pk>/update', views.EmpleadoUpdate.as_view(), name='empleado_update'),
    path('empleado/<int:pk>/delete', views.EmpleadoDelete.as_view(), name='empleado_delete'),

    path('ordenesdecompras',views.ordenesdecompra,name='ordenesdecompras'),
    path('ordenesdecompras/list', views.OrdenesdecompraListView.as_view(), name='ordenesdecompras_list'),
    path('ordenesdecompra/<int:pk>', views.OrdenesdecompraDetailView.as_view(), name='ordenesdecompra-detail'),
    path('ordenesdecompra/create', views.OrdenesdecompraCreate.as_view(), name='ordenesdecompra_create'),
    path('ordenesdecompra/<int:pk>/update', views.OrdenesdecompraUpdate.as_view(), name='ordenesdecompra_update'),
    path('ordenesdecompra/<int:pk>/delete', views.OrdenesdecompraDelete.as_view(), name='ordenesdecompra_delete'),

    #PLATO-COMEDOR
    path('comedor',views.comedor,name='comedor'),
    path('comedor/list', views.ComedorListView.as_view(), name='comedor_list'),
    path('comedor/<int:pk>', views.ComedorDetailView.as_view(), name='comedor-detail'),
    path('comedor/create', views.ComedorCreate.as_view(), name='comedor_create'),
    path('comedor/<int:pk>/update', views.ComedorUpdate.as_view(), name='comedor_update'),
    path('comedor/<int:pk>/delete', views.ComedorDelete.as_view(), name='comedor_delete'),

    #FACTURA
    path('facturas',views.factura,name='facturas'),
    path('facturas/list', views.FacturaListView.as_view(), name='facturas_list'),
    path('factura/<int:pk>', views.FacturaDetailView.as_view(), name='factura-detail'),
    path('factura/create', views.FacturaCreate.as_view(), name='factura_create'),
    path('factura/<int:pk>/update', views.FacturaUpdate.as_view(), name='factura_update'),
    path('factura/<int:pk>/delete', views.FacturaDelete.as_view(), name='factura_delete'),

     #INVENTARIO
    path('inventario',views.inventario,name='inventario'),
    path('inventario/list', views.InventarioListView.as_view(), name='inventario_list'),
    path('inventario/<int:pk>', views.InventarioDetailView.as_view(), name='inventario-detail'),
    path('inventario/create', views.InventarioCreate.as_view(), name='inventario_create'),
    path('inventario/<int:pk>/update', views.InventarioUpdate.as_view(), name='inventario_update'),
    path('inventario/<int:pk>/delete', views.InventarioDelete.as_view(), name='inventario_delete'),

    path('huesped', views.huespedes, name='huespedes'),
    path('huesped',views.HuespedListView.as_view(),name='huesped_list'),
    path('huesped/create', views.HuespedCreate.as_view(), name='huesped_create'),
    path('huesped/<int:pk>/delete',views.HuespedDelete.as_view(), name='huesped_delete'),
    path('huesped/<int:pk>/update',views.HuespedUpdate.as_view(), name='huesped_update'),
    path('huespedes/pdf', views.ListHuespedesPdf.as_view(), name='huespedes_pdf'),

    path('reserva',views.ReservaListView.as_view(),name='reservas'),
    path('reserva/create', views.ReservaCreate.as_view(), name='reserva_create'),
    path('reserva/<int:pk>/detail',views.DetalleReserva.as_view(), name='reserva_detail'),
    path('reserva/<int:pk>/anular',views.AnularReserva, name='reserva_anular'),
    path('reserva/<int:pk>/update',views.ReservaUpdate.as_view(), name='reserva_update'),
    path('reserva/<int:pk>/add_huesped', views.AddHuespedReserva.as_view(),name='add-huesped'),
    path('reserva/<int:pk>/<int:pk2>/<int:pk3>/rem_huesped', views.RemHuespedReserva,name='rem-huesped'),
]
    
