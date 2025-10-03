from django import forms
from .models import Cliente, Producto, Reserva

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
        widgets = {
            'fecha': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'hora': forms.TimeInput(attrs={'type': 'time', 'class': 'form-control'}),
        }
