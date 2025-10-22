from django.views.generic import UpdateView, DeleteView

from django.shortcuts import render, redirect
from django.views.generic import CreateView, TemplateView
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .forms import ClienteForm, ReservaForm, DireccionForm
from .models import Cliente, Producto, Categoria, Reserva, Direccion
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
	success_url = reverse_lazy('Cliente:menu')

	def form_valid(self, form):
		reserva = form.save(commit=False)
		try:
			cliente = Cliente.objects.get(perfil=self.request.user)
			reserva.cliente = cliente
		except Cliente.DoesNotExist:
			messages.error(self.request, "No se encontró el cliente asociado al usuario.")
			return redirect('Cliente:loginapp')
		# Asignar estado 'pendiente' por defecto
		reserva.estado = 'pendiente'
		reserva.save()
		messages.info(self.request, "Formulario de reserva enviado.")
		return redirect(self.success_url)


class PerfilView(TemplateView):
	template_name = 'perfil.html'

	@method_decorator(login_required)
	def dispatch(self, *args, **kwargs):
		return super().dispatch(*args, **kwargs)

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		try:
			cliente = Cliente.objects.get(perfil=self.request.user)
			context['cliente'] = cliente
			context['reservas'] = Reserva.objects.filter(cliente=cliente).order_by('-creacion')
		except Cliente.DoesNotExist:
			context['error_message'] = "No se encontró el cliente asociado al usuario."
		return context
	
class DireccionesCRUDView(TemplateView):
	template_name = 'direccionesCRUD.html'

	@method_decorator(login_required)
	def dispatch(self, *args, **kwargs):
		return super().dispatch(*args, **kwargs)

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		try:
			cliente = Cliente.objects.get(perfil=self.request.user)
			context['cliente'] = cliente
			context['direcciones'] = Direccion.objects.filter(cliente=cliente)
		except Cliente.DoesNotExist:
			context['error_message'] = "No se encontró el cliente asociado al usuario."
		return context
	

class CrearDireccionView(CreateView):
	# Implementación para crear una nueva dirección
	model = Direccion
	form_class = DireccionForm
	template_name = 'direccionesCrear.html'
	success_url = reverse_lazy('Cliente:direcciones')

	def form_valid(self, form):
		direccion = form.save(commit=False)
		try:
			cliente = Cliente.objects.get(perfil=self.request.user)
			direccion.cliente = cliente
		except Cliente.DoesNotExist:
			messages.error(self.request, "No se encontró el cliente asociado al usuario.")
			return redirect('Cliente:loginapp')
		direccion.save()
		messages.success(self.request, "Dirección creada exitosamente.")
		return redirect(self.success_url)
	
# Vista para editar dirección
class EditarDireccionView(UpdateView):
	model = Direccion
	form_class = DireccionForm
	template_name = 'editar_direccion.html'
	success_url = reverse_lazy('Cliente:direcciones')

	def form_valid(self, form):
		direccion = form.save(commit=False)
		try:
			cliente = Cliente.objects.get(perfil=self.request.user)
			direccion.cliente = cliente
		except Cliente.DoesNotExist:
			messages.error(self.request, "No se encontró el cliente asociado al usuario.")
			return redirect('Cliente:loginapp')
		direccion.save()
		messages.success(self.request, "Dirección editada exitosamente.")
		return redirect(self.success_url)

# Vista para eliminar dirección
class EliminarDireccionView(DeleteView):
	model = Direccion
	template_name = 'eliminar_direccion.html'
	success_url = reverse_lazy('Cliente:direcciones')

	def delete(self, request, *args, **kwargs):
		messages.success(self.request, "Dirección eliminada exitosamente.")
		return super().delete(request, *args, **kwargs)