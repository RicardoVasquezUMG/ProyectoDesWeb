from django import forms
from .models import Cliente, Producto

class ClienteForm(forms.ModelForm):
    
    class Meta:
        model = Cliente
        fields = ['nombre', 'apellido', 'telefono', 'email', 'contrasena']
        widgets = {
            'contrasena': forms.PasswordInput(),
        }

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto        
        exclude = ['creacion'] 