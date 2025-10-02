from django import forms
from .models import Cliente

class ClienteForm(forms.ModelForm):
    
    class Meta:
        model = Cliente
        fields = ['nombre', 'apellido', 'telefono', 'email', 'contrasena']
        widgets = {
            'contrasena': forms.PasswordInput(),
        }
