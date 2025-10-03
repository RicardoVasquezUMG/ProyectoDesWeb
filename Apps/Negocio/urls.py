from django.contrib import admin
from django.urls import path, include
from Apps.Negocio.views import ProductoCRUDView, ProductoCrearView, ProductoEditarView, ProductoView, ProductoEliminarView, ReservaCRUDView, ReservaCrearView, ReservaEliminarView, ReservaEditarView

app_name='Negocio'
urlpatterns = [

    path('CRUDproducto/', ProductoCRUDView.as_view(), name='producto_crud'),
    path('CRUDproducto/<int:pk>/editar/', ProductoEditarView.as_view(), name='producto_editar'),
    path('CRUDproducto/crear/', ProductoCrearView.as_view(), name='producto_crear'),
    path('CRUDproducto/<int:pk>/', ProductoView.as_view(), name='producto_ver'),
    path('CRUDproducto/<int:pk>/eliminar/', ProductoEliminarView.as_view(), name='producto_eliminar'),
    path('CRUDreserva/', ReservaCRUDView.as_view(), name='reserva_crud'),
    path('CRUDreserva/<int:pk>/editar/', ReservaEditarView.as_view(), name='reserva_editar'),
    path('CRUDreserva/crear/', ReservaCrearView.as_view(), name='reserva_crear'),
    path('CRUDreserva/<int:pk>/eliminar/', ReservaEliminarView.as_view(), name='reserva_eliminar'), 
]
