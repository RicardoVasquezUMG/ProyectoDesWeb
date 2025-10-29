from django import forms
from Apps.Cliente.models import Reserva
from .models import Pedido

class PedidoForm(forms.ModelForm):
    class Meta:
        model = Pedido
        exclude = []

class ReservaEstadoForm(forms.ModelForm):
    class Meta:
        model = Reserva
        exclude = ['comentarios', 'cliente']
