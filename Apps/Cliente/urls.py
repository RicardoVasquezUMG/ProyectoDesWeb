from django.urls import path
from .views import DetalleProductoView, LoginView, CrearClienteView, MenuView, logout_cliente

app_name = 'Cliente'
urlpatterns = [
	path('login/', LoginView, name='loginapp'),
	path('registrar/', CrearClienteView.as_view(), name='registrarCliente'),
	path('menu/', MenuView.as_view(), name='menu'),
	path('logout/', logout_cliente, name='logout'),
    path('producto/<int:producto_id>/', DetalleProductoView.as_view(), name='detalle_producto'),
]
