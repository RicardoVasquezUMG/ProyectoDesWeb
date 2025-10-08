from django.urls import path
from .views import CrearReservaView, DetalleProductoView, LoginView, RegistroView, MenuView
from django.contrib.auth.views import LogoutView

app_name = 'Cliente'
urlpatterns = [
	path('login/', LoginView.as_view(), name='loginapp'),
	path('registrar/', RegistroView.as_view(), name='registrarCliente'),
	path('menu/', MenuView.as_view(), name='menu'),
	path('logout/', LogoutView.as_view(next_page='Home:homeapp'), name='logout'),
    path('producto/<int:producto_id>/', DetalleProductoView.as_view(), name='detalle_producto'),
    path('reserva/', CrearReservaView.as_view(), name='reserva'),
]
