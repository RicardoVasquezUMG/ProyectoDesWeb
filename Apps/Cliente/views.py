from django.shortcuts import render, redirect
from django.views.generic import CreateView, TemplateView
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .forms import ClienteForm
from .models import Cliente, Producto, Categoria

def LoginView(request):
	error_message = None
	if request.method == 'POST':
		email = request.POST.get('email')
		contrasena = request.POST.get('contrasena')
		try:
			cliente = Cliente.objects.get(email=email)
			if cliente.contrasena == contrasena:
				request.session['cliente_id'] = cliente.id
				request.session['cliente_nombre'] = cliente.nombre
				return redirect('Home:homeapp')
			else:
				error_message = 'Contraseña incorrecta.'
		except Cliente.DoesNotExist:
			error_message = 'El correo no está registrado.'
	return render(request, 'login.html', {'error_message': error_message})

def logout_cliente(request):
	if request.method == 'POST':
		request.session.flush()
		return redirect('Cliente:loginapp')
	return redirect('Home:homeapp')

class CrearClienteView(CreateView):
	model = Cliente
	template_name = 'register.html'
	form_class = ClienteForm
	success_url = reverse_lazy('Cliente:loginapp')


class MenuView(TemplateView):
	template_name = 'Menu.html'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
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