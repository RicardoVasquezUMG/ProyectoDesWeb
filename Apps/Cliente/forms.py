from django import forms
from .models import Categoria, Cliente, Direccion, Producto, Reserva
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class ClienteForm(UserCreationForm):
    nombre = forms.CharField(max_length=30, required=True, label='Nombre')
    apellido = forms.CharField(max_length=140, required=True, label='Apellido')
    telefono = forms.CharField(max_length=20, required=True, label='Teléfono')
    email = forms.EmailField(required=True, label='Correo Electrónico')

    class Meta:
        model = User
        fields = ['nombre', 'apellido', 'telefono', 'email', 'password1', 'password2']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.first_name = self.cleaned_data['nombre']
        user.last_name = self.cleaned_data['apellido']
        user.email = self.cleaned_data['email']
        user.username = self.cleaned_data['email']
        if commit:
            user.save()
            Cliente.objects.update_or_create(perfil=user, defaults={'telefono': self.cleaned_data['telefono']})
        return user


class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto        
        exclude = ['creacion'] 

class ReservaForm(forms.ModelForm):
    class Meta:
        model = Reserva
        fields = ['fecha', 'hora', 'numero_personas', 'comentarios']
        widgets = {
            'fecha': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'hora': forms.TimeInput(attrs={'type': 'time', 'class': 'form-control'}),
            'numero_personas': forms.NumberInput(attrs={'class': 'form-control', 'min': 1, 'max': 7}),
            'comentarios': forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
        }

    def clean_numero_personas(self):
        numero = self.cleaned_data['numero_personas']
        if numero < 1 or numero > 7:
            raise forms.ValidationError('El número de personas debe ser entre 1 y 7.')
        return numero
        # ...existing code...

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['nombre']

class DireccionForm(forms.ModelForm):
    class Meta:
        model = Direccion
        exclude = ['cliente']
        widgets = {
            'direccion_linea1': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Dirección principal'}),
            'direccion_linea2': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Dirección secundaria (opcional)'}),
            'Colonia': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Colonia'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Teléfono'}),
            'etiqueta': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Etiqueta (ej. Casa, Oficina)'}),
            'entrega': forms.Select(attrs={'class': 'form-control'}),
        }