from django.urls import path
from .views import CrearDireccionView, CrearReservaView, DetalleProductoView, LoginView, PerfilView, RegistroView, MenuView, EditarDireccionView, EliminarDireccionView
from django.contrib.auth.views import LogoutView
from .views import DireccionesCRUDView
app_name = 'Cliente'
urlpatterns = [
	path('login/', LoginView.as_view(), name='loginapp'),
	path('registrar/', RegistroView.as_view(), name='registrarCliente'),
	path('menu/', MenuView.as_view(), name='menu'),
	path('logout/', LogoutView.as_view(next_page='Home:homeapp'), name='logout'),
    path('producto/<int:producto_id>/', DetalleProductoView.as_view(), name='detalle_producto'),
    path('reserva/', CrearReservaView.as_view(), name='reserva'),
    path('perfil/', PerfilView.as_view(), name='perfil'),
    path('direcciones/', DireccionesCRUDView.as_view(), name='direcciones'),
    path('direcciones/crear/', CrearDireccionView.as_view(), name='crear_direccion'),
    path('direcciones/<int:pk>/editar/', EditarDireccionView.as_view(), name='editar_direccion'),
    path('direcciones/<int:pk>/eliminar/', EliminarDireccionView.as_view(), name='eliminar_direccion'),
]
