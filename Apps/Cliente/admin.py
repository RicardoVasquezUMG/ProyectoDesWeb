from django.contrib import admin
from .models import Categoria, Cliente , Producto 


# Register your models here.
admin.site.register(Cliente)
admin.site.register(Producto)
admin.site.register(Categoria)
