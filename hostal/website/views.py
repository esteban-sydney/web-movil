from website.utils import render_to_pdf
from django.contrib.auth import update_session_auth_hash
from django.db import models
from django.shortcuts import render,redirect
from django.http.response import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.views.generic.detail import DetailView
from django.contrib import messages
from django.contrib.auth.models import Group, User
from django.contrib.auth.forms import PasswordChangeForm, UserCreationForm
from django.views.generic import ListView, CreateView, View
from django.http import JsonResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.views import generic
from django.db.models import Q, fields

from .forms import AddHuespedReservaForm, ClienteCreateForm, ClienteUpdateForm, EmpleadoCreateForm, EmpleadoUpdateForm, ProveedorCreateForm, ProveedorUpdateForm, UsuarioCreateForm, UsuarioUpdateForm, ReservaCreateForm, ReservaUpdateForm
from .models import Cliente, Factura, Orden_pedido, Comedor, Proveedor, Producto, Habitacion, ReservaHuesped, Rubro_proveedor, Servicio, Empleado, Ordenesdecompra, Inventario, Huesped, Reserva

# Create your views here.
@login_required(login_url='/accounts/login/')
def home(request):
    return render(request, 'website/home.html')

def index(request):
    return render(request, 'website/index.html')  

def habs(request):
    return render(request, 'website/habs.html')     

def clientes(request):
    busqueda = request.GET.get("buscar")
    cliente = Cliente.objects.all()

    if busqueda:
        cliente = Cliente.objects.filter(
            Q(rut_cliente__icontains = busqueda) |
            Q(nombre__icontains = busqueda)
        ).distinct()

    return render(request, 'website/clientes.html', {'cliente':cliente}) 

def habitaciones(request):
    busqueda = request.GET.get("buscar")
    habitacion = Habitacion.objects.all()

    if busqueda:
        habitacion = Habitacion.objects.filter(
            Q(numero_habitacion__icontains = busqueda)
        ).distinct()

    return render(request, 'website/habitaciones.html', {'habitacion':habitacion})  

def huespedes(request):
    busqueda = request.GET.get("buscar")
    huesped = Huesped.objects.all()

    if busqueda:
        huesped = Huesped.objects.filter(
            Q(rut_huesped__icontains = busqueda)
        ).distinct()

    return render(request, 'website/huespedes.html', {'huesped':huesped})      
      
# vista producto
def producto(request):
    return render(request, 'website/producto.html')

# vista USUARIOS


# vista INVENTARIO 
def inventario(request):
    return render(request, 'website/inventario.html')

# vista PLATO-COMEDOR
def comedor(request):
    busqueda = request.GET.get("buscar")
    comedor = Comedor.objects.all()

    if busqueda:
        comedor = Comedor.objects.filter(
            Q(codigo_plato__icontains = busqueda) |
            Q(nombre__icontains = busqueda)).distinct()
    return render(request, 'website/comedor.html', {'comedor':comedor})

#PLATO-COMEDOR-CRUD
class ComedorCreate(CreateView):
    model = Comedor
    fields = '__all__'
    template_name = 'website/comedor_form.html'
    success_url = reverse_lazy('comedor_list')

class  ComedorUpdate(UpdateView):
    model = Comedor
    fields = '__all__'
    success_url = reverse_lazy('comedor_list')

class ComedorDelete(DeleteView):
    model = Comedor
    success_url = reverse_lazy('comedor_list')

class ComedorDetailView(generic.DetailView):
    model = Comedor    

class ComedorListView(generic.ListView):
    model = Comedor
    template_name = 'website/comedor_list.html'
     

#EMPLEADOS JUAN

def empleados(request):
    busqueda = request.GET.get("buscar")
    empleado = Empleado.objects.all()

    if busqueda:
        empleado = Empleado.objects.filter(
            Q(rut_empleado__icontains = busqueda) |
            Q(nombres__icontains = busqueda) ).distinct()
    return render(request, 'website/empleados.html', {'empleado':empleado})

class EmpleadoCreate(CreateView):    
    template_name = 'website/empleado_form.html'
    form_class = EmpleadoCreateForm
    form_user = UserCreationForm    
    success_url = reverse_lazy('empleados_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if 'form' not in context:
            context['form'] = self.form_class(self.request.GET)
        if 'form2' not in context:
            context['form2'] = self.form_user(self.request.GET)
        return context
    
    def post(self, request, *args, **kwargs):
        self.object = self.get_object

        form = self.form_class(request.POST)
        form2 = self.form_user(request.POST)

        if form.is_valid() and form2.is_valid():

            form2.save() #Grabar Usuario
            username = form2.cleaned_data['username']
            user = User.objects.get(username=username)
            user.is_staff = True
            user.save()

            administrador = form.cleaned_data['administrador']

            if administrador == True:
                #Agregar usuario a grupo Administrador
                group = Group.objects.get(name='Administrador')
            else:
                #Agregar usuario a grupo Empleado
                group = Group.objects.get(name='Empleado')
            
            user.groups.add(group)            

            rut_empleado = form.cleaned_data['rut_empleado']
            dv = form.cleaned_data['dv']
            nombres = form.cleaned_data['nombres']
            a_paterno = form.cleaned_data['a_paterno']
            a_materno = form.cleaned_data['a_materno']
            telefono = form.cleaned_data['telefono']
            email = form.cleaned_data['email']
            direccion = form.cleaned_data['direccion']
            
            
            empleado = Empleado(
                rut_empleado=rut_empleado,
                dv=dv,
                nombres=nombres,
                a_paterno=a_paterno,
                a_materno=a_materno,
                telefono=telefono,
                email=email,
                direccion=direccion,
                administrador=administrador,
                usuario=user)
            
            empleado.save()

            return redirect('empleados_list')
        
        else:
            args = {'form':form,'form2':form2}
            return render(request, 'website/empleado_form.html',args)

class EmpleadoUpdate(UpdateView):
    template_name = 'website/empleado_update.html'
    form_class = EmpleadoUpdateForm
    model = Empleado
    
    def get_context_data(self, **kwargs):
        context = super(EmpleadoUpdate, self).get_context_data(**kwargs)
        pk = self.kwargs.get('pk',0)
        empleado = Empleado.objects.get(rut_empleado=pk)
        if 'form' not in context:
            context['form'] = self.form_class(instance=empleado)
        context['id'] = pk
        return context


class EmpleadoDelete(DeleteView):
    model = Empleado
    success_url = reverse_lazy('empleados_list')

class EmpleadoDetailView(generic.DetailView):
    model = Empleado    

class EmpleadoListView(generic.ListView):
    model = Empleado
    template_name = 'website/empleados_list.html'
     
#juan Ordenes de compra

def ordenesdecompra(request):
    busqueda = request.GET.get("buscar")
    ordenesdecompra = Ordenesdecompra.objects.all()

    if busqueda:
        ordenesdecompra = Ordenesdecompra.objects.filter(
            Q(numero_orden_c__icontains = busqueda)
        ).distinct()

    return render(request, 'website/ordenesdecompras.html', {'ordenesdecompra':ordenesdecompra})

class OrdenesdecompraCreate(CreateView):
    model = Ordenesdecompra
    fields = '__all__'
    template_name = 'website/ordenesdecompra_form.html'
    success_url = reverse_lazy('ordenesdecompras_list')

class OrdenesdecompraUpdate(UpdateView):
    model = Ordenesdecompra
    #fields = ['nombres','a.paterno','a.materno','telefono','email','direccion','usuario','contrasenia']    
    fields = '__all__'
    success_url = reverse_lazy('ordenesdecompras_list')

class OrdenesdecompraDelete(DeleteView):
    model = Ordenesdecompra
    success_url = reverse_lazy('ordenesdecompras_list')

class OrdenesdecompraDetailView(generic.DetailView):
    model = Ordenesdecompra    

class OrdenesdecompraListView(generic.ListView):
    model = Ordenesdecompra
    template_name = 'website/ordenesdecompras_list.html'

#juan factura
def factura(request):
    busqueda = request.GET.get("buscar")
    factura = Factura.objects.all()

    if busqueda:
        factura = Factura.objects.filter(
            Q(numero_factura__icontains = busqueda)
        ).distinct()

    return render(request, 'website/facturas.html', {'factura':factura})

class FacturaCreate(CreateView):
    model = Factura
    fields = '__all__'
    template_name = 'website/factura_form.html'
    success_url = reverse_lazy('facturas_list')

class FacturaUpdate(UpdateView):
    model = Factura
    #fields = ['nombres','a.paterno','a.materno','telefono','email','direccion','usuario','contrasenia']    
    fields = '__all__'
    success_url = reverse_lazy('facturas_list')

class FacturaDelete(DeleteView):
    model = Factura
    success_url = reverse_lazy('facturas_list')

class FacturaDetailView(generic.DetailView):
    model = Factura    

class FacturaListView(generic.ListView):
    model = Factura
    template_name = 'website/facturas_list.html'


#sonia
class Orden_pedidoCreate(CreateView):
    model = Orden_pedido
    fields = '__all__'

class Orden_pedidoDetailView(generic.DetailView):
    model = Orden_pedido

class Orden_pedidoDelete(DeleteView):
    model = Orden_pedido
    success_url = reverse_lazy('orden_pedido')

class Orden_pedidoUpdate(UpdateView):
    model = Orden_pedido
    fields = '__all__'

class Orden_pedidoListView(generic.ListView):
    model = Orden_pedido
    template_name = 'website/orden_pedido_list.html'




class ClienteCreate(CreateView):    
    template_name = 'website/cliente_form.html'
    form_class = ClienteCreateForm
    form_user = UserCreationForm    
    success_url = reverse_lazy('clientes_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if 'form' not in context:
            context['form'] = self.form_class(self.request.GET)
        if 'form2' not in context:
            context['form2'] = self.form_user(self.request.GET)
        return context
    
    def post(self, request, *args, **kwargs):
        self.object = self.get_object

        form = self.form_class(request.POST)
        form2 = self.form_user(request.POST)

        if form.is_valid() and form2.is_valid():

            form2.save() #Grabar Usuario
            username = form2.cleaned_data['username']
            user = User.objects.get(username=username)

            #Agregar usuario a grupo Cliente
            group = Group.objects.get(name='Cliente')
            user.groups.add(group)

            rut_cliente = form.cleaned_data['rut_cliente']
            dv = form.cleaned_data['dv']
            nombre = form.cleaned_data['nombre']
            telefono = form.cleaned_data['telefono']
            email = form.cleaned_data['email']
            direccion = form.cleaned_data['direccion']

            cliente = Cliente(
                rut_cliente=rut_cliente,
                dv=dv,
                nombre=nombre,
                telefono=telefono,
                email=email,
                direccion=direccion,
                usuario=user)
            
            cliente.save()            

            return redirect('clientes_list')
        
        else:
            args = {'form':form,'form2':form2}
            return render(request, 'website/cliente_form.html',args)

class ClienteUpdate(UpdateView):
    template_name = 'website/cliente_update.html'
    form_class = ClienteUpdateForm
    model = Cliente

    def get_context_data(self, **kwargs):
        context = super(ClienteUpdate, self).get_context_data(**kwargs)
        pk = self.kwargs.get('pk',0)
        cliente = Cliente.objects.get(rut_cliente=pk)
        if 'form' not in context:
            context['form'] = self.form_class(instance=cliente)
        context['id'] = pk
        return context

class ClienteDelete(DeleteView):
    model = Cliente
    success_url = reverse_lazy('clientes_list')

class ClienteDetailView(generic.DetailView):
    model = Cliente    

class ClienteListView(generic.ListView):
    model = Cliente
    template_name = 'website/clientes_list.html'
    ordering = 'rut_cliente' 


class HabitacionCreate(CreateView):
    model = Habitacion
    fields = '__all__'
    template_name = 'website/habitacion_form.html'
    success_url = reverse_lazy('habitaciones_list')

class HabitacionListView(generic.ListView):
    model = Habitacion
    template_name = 'website/habitaciones_list.html'  
    ordering = 'numero_habitacion'  

class HabitacionUpdate(UpdateView):
    model = Habitacion
    fields = '__all__'
    success_url = reverse_lazy('habitaciones_list')  

class HabitacionDelete(DeleteView):
    model = Habitacion
    success_url = reverse_lazy('habitaciones_list')      
    
class ListHabitacionesPdf(View):
    def get(self, request, *args, **kwargs):
        habitaciones = Habitacion.objects.all()
        data = {
            'habitaciones': habitaciones,
            'cantidad': habitaciones.count()
        }
        pdf = render_to_pdf('website/lista_hab.html', data)
        return HttpResponse(pdf, content_type='aplications/pdf')   


class ProveedorCreate(CreateView):    
    template_name = 'website/proveedor_form.html'
    form_class = ProveedorCreateForm
    form_user = UserCreationForm    
    success_url = reverse_lazy('proveedores')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if 'form' not in context:
            context['form'] = self.form_class(self.request.GET)
        if 'form2' not in context:
            context['form2'] = self.form_user(self.request.GET)
        return context
    
    def post(self, request, *args, **kwargs):
        self.object = self.get_object

        form = self.form_class(request.POST)
        form2 = self.form_user(request.POST)

        if form.is_valid() and form2.is_valid():

            form2.save() #Grabar Usuario
            username = form2.cleaned_data['username']
            user = User.objects.get(username=username)

            #Agregar usuario a grupo Cliente
            group = Group.objects.get(name='Proveedor')
            user.groups.add(group)

            rut_proveedor = form.cleaned_data['rut_proveedor']
            dv = form.cleaned_data['dv']
            nombre = form.cleaned_data['nombre']
            telefono = form.cleaned_data['telefono']
            email = form.cleaned_data['email']
            direccion = form.cleaned_data['direccion']
            id_rubro = form.cleaned_data['id_rubro']

            proveedor = Proveedor(
                rut_proveedor=rut_proveedor,
                dv=dv,
                nombre=nombre,
                telefono=telefono,
                email=email,
                direccion=direccion,
                id_rubro=id_rubro,
                usuario=user)
            
            proveedor.save()            

            return redirect('proveedores')
        
        else:
            print('no valid')
            print(form.errors)
            print(form2.errors)
            args = {'form':form,'form2':form2}
            return render(request, 'website/proveedor_form.html',args)

class ProveedorUpdate(UpdateView):
    template_name = 'website/proveedor_update.html'
    form_class = ProveedorUpdateForm
    model = Proveedor
    
    def get_context_data(self, **kwargs):
        context = super(ProveedorUpdate, self).get_context_data(**kwargs)
        pk = self.kwargs.get('pk',0)
        proveedor = Proveedor.objects.get(rut_proveedor=pk)
        if 'form' not in context:
            context['form'] = self.form_class(instance=proveedor)
        context['id'] = pk
        return context    

class ProveedorDetailView(generic.DetailView):
    model = Proveedor

class ProveedorDelete(DeleteView):
    model = Proveedor
    success_url = reverse_lazy('proveedores')

class ProveedorListView(generic.ListView):
    model = Proveedor
    template_name = 'website/proveedor_list.html'

#Rubro Proveedor
class RubroProveedorListView(generic.ListView):
    model = Rubro_proveedor
    template_name = 'website/rubro_proveedor_list.html'

class RubroProveedorCreateView(CreateView):
    model = Rubro_proveedor
    fields = ['rubro','descripcion']

class RubroProveedorUpdateView(UpdateView):
    model = Rubro_proveedor
    fields = ['rubro','descripcion']
    success_url = reverse_lazy('rubros_proveedor')

class RubroProveedorDeleteView(DeleteView):
    model = Rubro_proveedor
    success_url = reverse_lazy('rubros_proveedor')

#Producto CRUD
class ProductoCreate(CreateView):
    model = Producto
    fields = '__all__'
    template_name = 'website/producto_form.html'
    success_url = reverse_lazy('producto_list')

class ProductoUpdate(UpdateView):
    model = Producto
    #fields = ['nombre','telefono','email','direccion','usuario','contrasenia']    
    fields = '__all__'
    success_url = reverse_lazy('producto_list')

class ProductoDelete(DeleteView):
    model = Producto
    success_url = reverse_lazy('producto_list')

class ProductoDetailView(generic.DetailView):
    model = Producto    

class ProductoListView(generic.ListView):
    model = Producto
    template_name = 'website/producto_list.html'

#USUARIO CRUD


#INVENTARIO CRUD
class InventarioCreate(CreateView):
    model = Inventario
    fields = '__all__'
    template_name = 'website/inventario_form.html'
    success_url = reverse_lazy('inventario_list')

class InventarioUpdate(UpdateView):
    model = Inventario  
    fields = '__all__'
    success_url = reverse_lazy('inventario_list')

class InventarioDelete(DeleteView):
    model = Inventario
    success_url = reverse_lazy('inventario_list')

class InventarioDetailView(generic.DetailView):
    model = Inventario    

class InventarioListView(generic.ListView):
    model = Inventario
    template_name = 'website/inventario_list.html'


class UsuarioListView(generic.ListView):
    model = User
    template_name = 'website/usuario_list.html'

def UsuarioCreate(request):
    if request.method == 'POST':
        if not User.objects.filter(username = request.POST['username']).exists():
            form = UsuarioCreateForm(request.POST)
            if form.is_valid():
                grupo = int(request.POST['grupo_usuario'])
                if form.save(commit=False):
                    form.save(commit=True, grupo_usuario=grupo)

        return redirect('usuario_list')
                
    else:
        form = UsuarioCreateForm()
        return render(request, 'website/usuario_form.html', {'form':form})

def UsuarioUpdate(request, user_id):
    user = User.objects.get(id=user_id)
    if request.method == 'POST':
        form = UsuarioUpdateForm(request.POST)
        username = request.POST['username']
        grupo_usuario = request.POST['grupo_usuario']
        form.save(commit=True,user=user,username=username,grupo_usuario_i=grupo_usuario)

        return redirect('usuario_list')
                
    else:        
        
        group = user.groups.all()[0]
        grupo_usuario = group.id

        form = UsuarioUpdateForm(
            initial={
                'username': user.username , 
                'grupo_usuario': grupo_usuario })

        return render(request, 'website/usuario_update.html', {'form':form})

def UsuarioDeactivate(request, user_id):
    user = User.objects.get(id=user_id)
    if request.method == 'POST':
        user.is_active = False
        user.save()        
        return redirect('usuario_list')
    else:
        return render(request,'website/usuario_deactivate.html', {'user':user})
    

def UsuarioActivate(request, user_id):
    user = User.objects.get(id=user_id)
    if request.method == 'POST':
        user.is_active = True
        user.save()
        return redirect('usuario_list')
    else:
        return render(request,'website/usuario_activate.html', {'user':user})

#Huespedes
class HuespedCreate(CreateView):
    model = Huesped
    fields = '__all__'

class HuespedDelete(DeleteView):
    model = Huesped
    success_url = reverse_lazy('huespedes')

class HuespedUpdate(UpdateView):
    model= Huesped
    fields = '__all__'

class HuespedListView(generic.ListView):
    model = Huesped
    template_name = 'website/huesped_list.html'

class ListHuespedesPdf(View):
    def get(self, request, *args, **kwargs):
        huespedes = Huesped.objects.all()
        data = {
            'huespedes': huespedes,
            'cantidad': huespedes.count()
        }
        pdf = render_to_pdf('website/lista_hue.html', data)

        if pdf:
            response = HttpResponse(pdf, content_type='aplications/pdf')
            filename = "lista_huespedes.pdf"
            content  = "inline; filename=%s" %(filename)
            response['Content-Disposition'] = content
            return response

        return HttpResponse("Not Found")

#Reservas
class ReservaListView(generic.ListView):
    model = Reserva
    template_name = 'website/reserva_list.html'

class ReservaCreate(CreateView):
    template_name = 'website/reserva_create.html'
    form_class = ReservaCreateForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if 'form' not in context:
            context['form'] = self.form_class(self.request.GET)
        return context
    
    def post(self, request, *args, **kwargs):
        self.object = self.get_object

        form = self.form_class(request.POST)

        if form.is_valid():
            cliente = form.cleaned_data['cliente']
            fecha_desde = form.cleaned_data['fecha_desde']
            fecha_hasta = form.cleaned_data['fecha_hasta']
            reserva = Reserva(cliente=cliente,fecha_desde=fecha_desde,fecha_hasta=fecha_hasta)
            reserva.vigente = True

            reserva.save()
            print(reserva.pk)
            return redirect('add-huesped', reserva.pk)

class ReservaUpdate(UpdateView):
    template_name = 'website/reserva_update.html'
    form_class = ReservaUpdateForm
    model = Reserva

    def get_context_data(self, **kwargs):
        context = super(ReservaUpdate, self).get_context_data(**kwargs)
        pk = self.kwargs.get('pk', 0)
        reserva = Reserva.objects.get(id_reserva=pk)
        if 'form' not in context:
            context['form'] = self.form_class(instance=reserva)
        context['id'] = pk
        return context
    
    def post(self, request, *args, **kwargs):
        self.object = self.get_object

        form = self.form_class(request.POST)

        if form.is_valid():
            pk = self.kwargs.get('pk', 0)

            reserva = Reserva.objects.get(id_reserva=pk)

            reserva.cliente = form.cleaned_data['cliente']
            reserva.fecha_desde = form.cleaned_data['fecha_desde']
            reserva.fecha_hasta = form.cleaned_data['fecha_hasta']            

            reserva.save()
            print(reserva.pk)
            return redirect('add-huesped', reserva.pk)

class DetalleReserva(DetailView):
    model = Reserva
    template_name = 'website/reserva_detail.html'
    form_class = ReservaUpdateForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk = self.kwargs.get('pk', 0)
        reserva = Reserva.objects.get(id_reserva=pk)
        huespedes=ReservaHuesped.objects.all().filter(id_reserva=reserva.pk)
        if 'form' not in context:
            context['form'] = self.form_class(instance=reserva)
        if 'reserva' not in context:
            context['reserva'] = reserva
        if 'huespedes' not in context:
            context['huespedes'] = huespedes        
        context['id'] = pk
        
        return context


def AnularReserva(request, pk):
    reserva = Reserva.objects.get(id_reserva=pk)
    if request.method == 'POST':
        reserva.vigente = False
        reserva.save()
        return redirect('reservas')
    else:
        return render(request,'website/reserva_anular.html', {'reserva':reserva})

class AddHuespedReserva(CreateView):
    model=Reserva
    second_model=ReservaHuesped
    template_name = 'website/reserva_add_huesped.html'
    form_class = AddHuespedReservaForm  
    success_url = reverse_lazy('reservas')

    def get_context_data(self,**kwargs):
        context = super(AddHuespedReserva, self).get_context_data(**kwargs)
        pk = self.kwargs.get('pk',0)
        reserva=self.model.objects.get(id_reserva=pk)
        huespedes=self.second_model.objects.all().filter(id_reserva=reserva.pk)
        if 'form' not in context:
            context['form'] = self.form_class(self.request.GET)
        if 'huespedes' not in context:
            context['huespedes'] = huespedes
        return context
    
    def post(self, request, *args, **kwargs):
        self.object = self.get_object

        form = self.form_class(request.POST)

        if form.is_valid():
            pk = self.kwargs.get('pk',0)
            id_reserva = self.model.objects.get(id_reserva=pk)
            rut_huesped = form.cleaned_data['rut_huesped']
            habitacion = form.cleaned_data['habitacion']

            add_huesped = ReservaHuesped(
                id_reserva=id_reserva, 
                rut_huesped=rut_huesped, 
                habitacion=habitacion)

            add_huesped.save()

            return redirect('add-huesped', id_reserva.pk)
        else:
            return redirect('reservas')

def RemHuespedReserva(request,**kwargs):  
    reserva_id = kwargs.get('pk')
    rut_huesped = kwargs.get('pk2')
    habitacion = kwargs.get('pk3')

    reserva_huesped = ReservaHuesped.objects.get(
        id_reserva=reserva_id,
        rut_huesped=rut_huesped,
        habitacion=habitacion)
    reserva_huesped.delete()

    return redirect('add-huesped', reserva_id)

def ChangePasswordView(request):
    if request.method == 'POST':
        form=PasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect('home')
        else:
            return redirect('cambiar_clave')
    else:
        form = PasswordChangeForm(user=request.user)
        args = {'form':form}
        return render(request, 'accounts/change_password.html',args)

class GrupoListView(ListView):
    model = Group
    template_name = 'website/group_list.html'

class GrupoCreateView(CreateView):
    model = Group
    fields = ['name']
    template_name = 'website/group_create.html'
    success_url = reverse_lazy('groups_list')

class GrupoUpdateView(UpdateView):
    model = Group
    fields = ['name']
    template_name = 'website/group_create.html'
    success_url = reverse_lazy('groups_list')

class GrupoDeleteView(DeleteView):
    model = Group
    template_name = 'website/group_confirm_delete.html'
    success_url = reverse_lazy('groups_list')
