from django.urls import path
from .views import LoginView, CrearClienteView, MenuView

app_name = 'Cliente'
urlpatterns = [
	path('login/', LoginView.as_view(), name='loginapp'),
	path('registrar/', CrearClienteView.as_view(), name='registrarCliente'),
    path('menu/', MenuView.as_view(), name='menu')
]
