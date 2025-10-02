from django.contrib import admin
from django.urls import path, include
from Apps.Negocio.views import ProductoCRUDView, ProductoCrearView, ProductoEditarView, ProductoView

app_name='Negocio'
urlpatterns = [

    path('CRUDproducto/', ProductoCRUDView.as_view(), name='producto_crud'),
    path('CRUDproducto/<int:pk>/editar/', ProductoEditarView.as_view(), name='producto_editar'),
    path('CRUDproducto/crear/', ProductoCrearView.as_view(), name='producto_crear'),
    path('CRUDproducto/<int:pk>/', ProductoView.as_view(), name='producto_ver'),
]
