from django.contrib import admin
from .models import Categoria, Cliente , Producto, Reserva , Direccion


# Register your models here.
admin.site.register(Cliente)
admin.site.register(Producto)
admin.site.register(Categoria)
admin.site.register(Reserva)
admin.site.register(Direccion)
