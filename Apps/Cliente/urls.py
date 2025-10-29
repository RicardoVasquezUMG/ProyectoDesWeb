from django.urls import path
from .views import CrearDireccionView, CrearReservaView, DetalleProductoView, LoginView, PerfilView, RegistroView, MenuView, EditarDireccionView, EliminarDireccionView, ReservaView
from django.contrib.auth.views import LogoutView
from .views import DireccionesCRUDView , CarritoView, agregar_al_carrito, quitar_del_carrito, formulario_pedido
from .views import OrdenesView, OrdenesVerView


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
    path('reservasCliente/', ReservaView.as_view(), name='reservas'),
    path('carrito/', CarritoView.as_view(), name='carrito'),
    path('carrito/agregar/<int:producto_id>/', agregar_al_carrito, name='carrito_agregar'),
    path('carrito/quitar/<int:producto_id>/', quitar_del_carrito, name='carrito_quitar'),
    path('pedido/formulario/', formulario_pedido, name='formulario_pedido'),
    path('ordenes/', OrdenesView.as_view(), name='ordenes'),
    path('ordenes/<int:pedido_id>/', OrdenesVerView.as_view(), name='ordenes_ver'),
]
