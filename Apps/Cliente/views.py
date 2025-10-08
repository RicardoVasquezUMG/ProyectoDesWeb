from django.shortcuts import render, redirect
from django.views.generic import CreateView, TemplateView
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .forms import ClienteForm, ReservaForm
from .models import Cliente, Producto, Categoria, Reserva
from django.contrib.auth.views import LoginView


class RegistroView(CreateView):
    template_name = 'register.html'
    model = Cliente
    form_class = ClienteForm
    success_url = reverse_lazy('Cliente:loginapp')

class LoginView(LoginView):
	template_name = 'login.html'
	success_url = reverse_lazy('Home:homeapp')
	2


class MenuView(TemplateView):
	template_name = 'Menu.html'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		categoria_id = self.request.GET.get('categoria')
		if categoria_id:
			context['productos'] = Producto.objects.filter(categoria_id=categoria_id)
		else:
			context['productos'] = Producto.objects.all()
		context['categorias'] = Categoria.objects.all()
		return context

class DetalleProductoView(TemplateView):
	template_name = 'detalle_producto.html'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		producto_id = self.kwargs.get('producto_id')
		try:
			producto = Producto.objects.get(id=producto_id)
			context['producto'] = producto
		except Producto.DoesNotExist:
			context['error_message'] = 'Producto no encontrado.'
		return context

class CrearReservaView(CreateView):
	model = Reserva	
	template_name = 'reserva.html'
	form_class = ReservaForm
	success_url = reverse_lazy('Cliente:menuapp')
