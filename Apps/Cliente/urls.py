
from django.urls import path
from .views import LoginView, CrearClienteView

app_name = 'Cliente'
urlpatterns = [
	path('login/', LoginView.as_view(), name='loginapp'),
	path('registrar/', CrearClienteView.as_view(), name='registrarCliente'),
]
