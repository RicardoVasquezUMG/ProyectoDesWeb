from django import forms
from Apps.Cliente.models import Reserva

class ReservaEstadoForm(forms.ModelForm):
    class Meta:
        model = Reserva
        exclude = ['comentarios', 'cliente']
