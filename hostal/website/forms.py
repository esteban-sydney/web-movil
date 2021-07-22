from typing import AbstractSet, Text
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import Group, User
from django.forms.widgets import TextInput
from .models import Cliente, Empleado, Habitacion, Huesped, Proveedor, Reserva, ReservaHuesped, Rubro_proveedor

class UsuarioCreateForm(UserCreationForm):

    grupo_usuario = forms.ModelChoiceField(
        queryset=Group.objects.all(),
        required=True,
    )
    
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                 'class': 'form-control'
            }
        )        
    )

    grupo_usuario.widget.attrs.update({'class':'form-control'})

    def save(self, commit=True,grupo_usuario=None):
        user = super().save(commit=False)
        if commit:
            if super().save(commit=True):
                group = Group.objects.get(id=grupo_usuario)

                user.groups.add(group)

        else:
            return user
        

class UsuarioUpdateForm(forms.ModelForm):

    username = forms.CharField(
        label='Usuario',
        required=False,
        widget=forms.TextInput(
            attrs={
                 'class': 'form-control'
            }
        )        
    )

    grupo_usuario = forms.ModelChoiceField(
        queryset=Group.objects.all(),
        required=True,
    )    

    grupo_usuario.widget.attrs.update({'class':'form-control'})

    class Meta:
        model = User
        fields = ('username',)

    def save(self,commit=True,user=None,username=None,grupo_usuario_i=None):
        
        if commit:
            if username != user.username:
                User.objects.filter(id=user.id).update(username=username)

            if grupo_usuario_i != None:
                grupo_usuario = int(grupo_usuario_i)
                
                user.groups.clear()

                group = Group.objects.get(id=grupo_usuario)

                user.groups.add(group)

class ReservaCreateForm(forms.ModelForm):

    cliente = forms.ModelChoiceField(
        label='Cliente',
        queryset=Cliente.objects.all(),
        required=True
    )

    fecha_desde = forms.DateField(
        input_formats=['%d/%m/%Y'],
        label='Fecha Desde',
        widget=forms.DateInput(
            attrs={
                'class':'form-control',
            }
        )
    )

    fecha_hasta = forms.DateField(
        input_formats=['%d/%m/%Y'],
        label='Fecha Hasta',
        widget=forms.DateInput(
            attrs={
                'class':'form-control'
            }
        )
    )

    cliente.widget.attrs.update({'class':'form-control'})
    
    class Meta:
        model = Reserva 
        fields = ['cliente','fecha_desde','fecha_hasta']

class ReservaUpdateForm(forms.ModelForm):

    id_reserva = forms.IntegerField(
        label = 'ID Reserva',
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'readonly':True,
            }
        )
    )

    cliente = forms.ModelChoiceField(
        label='Cliente',
        queryset=Cliente.objects.all(),
        required=True
    )

    fecha_desde = forms.DateField(
        input_formats=['%d/%m/%Y'],
        label='Fecha Desde',
        widget=forms.DateInput(
            attrs={
                'class':'form-control',
            }
        )
    )

    fecha_hasta = forms.DateField(
        input_formats=['%d/%m/%Y'],
        label='Fecha Hasta',
        widget=forms.DateInput(
            attrs={
                'class':'form-control'
            }
        )
    )

    cliente.widget.attrs.update({'class':'form-control'})
    
    class Meta:
        model = Reserva 
        fields = ['id_reserva','cliente','fecha_desde','fecha_hasta']

class AddHuespedReservaForm(forms.ModelForm):

    class Meta:
        model = ReservaHuesped
        fields = ['rut_huesped','habitacion']

    rut_huesped = forms.ModelChoiceField(
        label = 'Huésped',
        queryset = Huesped.objects.all(),
        required  =True
    )

    habitacion = forms.ModelChoiceField(
        label = 'Habitación',
        queryset = Habitacion.objects.all(),
        required = True
    )

    rut_huesped.widget.attrs.update({'class':'form-control mb-2 mr-sm-2'})
    habitacion.widget.attrs.update({'class':'form-control mb-2 mr-sm-2'})

class ClienteCreateForm(forms.ModelForm):    

    rut_cliente = forms.IntegerField(
        label = 'Rut',
        widget=forms.TextInput(
            attrs={
                'class':'form-control'
            }
        )
    )

    dv = forms.CharField(
        label = 'Dígito Verificador',
        widget=forms.TextInput(
            attrs={
                'class':'form-control'
            }
        )
    )

    nombre = forms.CharField(
        label = 'Nombre',
        widget=forms.TextInput(
            attrs={
                'class':'form-control'
            }
        )
    )

    telefono = forms.IntegerField(
        label = 'Teléfono',
        widget=forms.TextInput(
            attrs={
                'class':'form-control'
            }
        )
    )

    email = forms.EmailField(
        label = 'E-mail',
        widget=forms.TextInput(
            attrs={
                'class':'form-control'
            }
        )
    )

    direccion = forms.CharField(
        label = 'Dirección',
        widget=forms.TextInput(
            attrs={
                'class':'form-control'
            }
        )
    )

    class Meta:
        model  = Cliente
        fields = ['rut_cliente','dv','nombre','telefono','email','direccion']

class ClienteUpdateForm(forms.ModelForm):    

    rut_cliente = forms.IntegerField(
        label = 'Rut',
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'readonly':True,
            }
        )
    )

    dv = forms.CharField(
        label = 'Dígito Verificador',
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'readonly':True,
            }
        )
    )

    nombre = forms.CharField(
        label = 'Nombre',
        widget=forms.TextInput(
            attrs={
                'class':'form-control'
            }
        )
    )

    telefono = forms.IntegerField(
        label = 'Teléfono',
        widget=forms.TextInput(
            attrs={
                'class':'form-control'
            }
        )
    )

    email = forms.EmailField(
        label = 'E-mail',
        widget=forms.TextInput(
            attrs={
                'class':'form-control'
            }
        )
    )

    direccion = forms.CharField(
        label = 'Dirección',
        widget=forms.TextInput(
            attrs={
                'class':'form-control'
            }
        )
    )

    class Meta:
        model  = Cliente
        fields = ['rut_cliente','dv','nombre','telefono','email','direccion']

class ProveedorCreateForm(forms.ModelForm):    

    rut_proveedor = forms.IntegerField(
        label = 'Rut',
        widget=forms.TextInput(
            attrs={
                'class':'form-control'
            }
        )
    )

    dv = forms.CharField(
        label = 'Dígito Verificador',
        widget=forms.TextInput(
            attrs={
                'class':'form-control'
            }
        )
    )

    nombre = forms.CharField(
        label = 'Nombre',
        widget=forms.TextInput(
            attrs={
                'class':'form-control'
            }
        )
    )

    telefono = forms.IntegerField(
        label = 'Teléfono',
        widget=forms.TextInput(
            attrs={
                'class':'form-control'
            }
        )
    )

    email = forms.EmailField(
        label = 'E-mail',
        widget=forms.TextInput(
            attrs={
                'class':'form-control'
            }
        )
    )

    direccion = forms.CharField(
        label = 'Dirección',
        widget=forms.TextInput(
            attrs={
                'class':'form-control'
            }
        )
    )

    id_rubro = forms.ModelChoiceField(
        label = 'Rubro Proveedor',
        queryset = Rubro_proveedor.objects.all(),
        required  =True
    )

    id_rubro.widget.attrs.update({'class':'form-control mb-2 mr-sm-2'})

    class Meta:
        model  = Proveedor
        fields = ['rut_proveedor','dv','nombre','telefono','email','direccion','id_rubro']

class ProveedorUpdateForm(forms.ModelForm):    

    rut_proveedor = forms.IntegerField(
        label = 'Rut',
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'readonly':True,
            }
        )
    )

    dv = forms.CharField(
        label = 'Dígito Verificador',
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'readonly':True,
            }
        )
    )

    nombre = forms.CharField(
        label = 'Nombre',
        widget=forms.TextInput(
            attrs={
                'class':'form-control'
            }
        )
    )

    telefono = forms.IntegerField(
        label = 'Teléfono',
        widget=forms.TextInput(
            attrs={
                'class':'form-control'
            }
        )
    )

    email = forms.EmailField(
        label = 'E-mail',
        widget=forms.TextInput(
            attrs={
                'class':'form-control'
            }
        )
    )

    direccion = forms.CharField(
        label = 'Dirección',
        widget=forms.TextInput(
            attrs={
                'class':'form-control'
            }
        )
    )

    id_rubro = forms.ModelChoiceField(
        label = 'Rubro Proveedor',
        queryset = Rubro_proveedor.objects.all(),
        required  =True
    )

    id_rubro.widget.attrs.update({'class':'form-control mb-2 mr-sm-2'})

    class Meta:
        model  = Proveedor
        fields = ['rut_proveedor','dv','nombre','telefono','email','direccion','id_rubro']

class EmpleadoCreateForm(forms.ModelForm):    

    rut_empleado = forms.IntegerField(
        label = 'Rut',
        widget=forms.TextInput(
            attrs={
                'class':'form-control'
            }
        )
    )

    dv = forms.CharField(
        label = 'Dígito Verificador',
        widget=forms.TextInput(
            attrs={
                'class':'form-control'
            }
        )
    )

    nombres = forms.CharField(
        label = 'Nombre',
        widget=forms.TextInput(
            attrs={
                'class':'form-control'
            }
        )
    )

    a_paterno = forms.CharField(
        label = 'Apellido Paterno',
        widget=forms.TextInput(
            attrs={
                'class':'form-control'
            }
        )
    )

    a_materno = forms.CharField(
        label = 'Apellido Materno',
        widget=forms.TextInput(
            attrs={
                'class':'form-control'
            }
        )
    )

    telefono = forms.IntegerField(
        label = 'Teléfono',
        widget=forms.TextInput(
            attrs={
                'class':'form-control'
            }
        )
    )

    email = forms.EmailField(
        label = 'E-mail',
        widget=forms.TextInput(
            attrs={
                'class':'form-control'
            }
        )
    )

    direccion = forms.CharField(
        label = 'Dirección',
        widget=forms.TextInput(
            attrs={
                'class':'form-control'
            }
        )
    )

    administrador = forms.BooleanField(
        label = 'Administrador',
        initial=False,
        required=False,
        widget=forms.CheckboxInput(
            attrs={
                'class':'form-check-input'
            }
        )
    )

    class Meta:
        model  = Empleado
        fields = ['rut_empleado','dv','nombres','a_paterno','a_materno','telefono','email','direccion','administrador']

class EmpleadoUpdateForm(forms.ModelForm):    

    rut_empleado = forms.IntegerField(
        label = 'Rut',
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'readonly':True,
            }
        )
    )

    dv = forms.CharField(
        label = 'Dígito Verificador',
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'readonly':True,
            }
        )
    )

    nombres = forms.CharField(
        label = 'Nombre',
        widget=forms.TextInput(
            attrs={
                'class':'form-control'
            }
        )
    )

    a_paterno = forms.CharField(
        label = 'Apellido Paterno',
        widget=forms.TextInput(
            attrs={
                'class':'form-control'
            }
        )
    )

    a_materno = forms.CharField(
        label = 'Apellido Materno',
        widget=forms.TextInput(
            attrs={
                'class':'form-control'
            }
        )
    )

    telefono = forms.IntegerField(
        label = 'Teléfono',
        widget=forms.TextInput(
            attrs={
                'class':'form-control'
            }
        )
    )

    email = forms.EmailField(
        label = 'E-mail',
        widget=forms.TextInput(
            attrs={
                'class':'form-control'
            }
        )
    )

    direccion = forms.CharField(
        label = 'Dirección',
        widget=forms.TextInput(
            attrs={
                'class':'form-control'
            }
        )
    )

    administrador = forms.BooleanField(
        label = 'Administrador',
        initial=False,
        required=False,
        widget=forms.CheckboxInput(
            attrs={
                'class':'form-check-input'
            }
        )
    )

    class Meta:
        model  = Empleado
        fields = ['rut_empleado','dv','nombres','a_paterno','a_materno','telefono','email','direccion','administrador']