from django.shortcuts import render
from django.views.generic import TemplateView, UpdateView, CreateView, View
from django.shortcuts import redirect, get_object_or_404
from Apps.Cliente.forms import ProductoForm, ReservaForm, CategoriaForm
from Apps.Cliente.models import Producto, Reserva , Categoria
from django.urls import reverse_lazy

# Create your views here.
class ProductoCRUDView(TemplateView):
    template_name = 'producto_crud.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['productos'] = Producto.objects.all()
        return context

class ProductoView(TemplateView):
    template_name = 'productoVer.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        producto_id = self.kwargs.get('pk')
        try:
            producto = Producto.objects.get(id=producto_id)
            context['producto'] = producto
        except Producto.DoesNotExist:
            context['error_message'] = 'Producto no encontrado.'
        return context

class ProductoEditarView(UpdateView):
    model = Producto
    form_class = ProductoForm
    template_name = 'productoEditar.html'
    success_url = reverse_lazy('Negocio:producto_crud')


class ProductoCrearView(CreateView):
    model = Producto
    form_class = ProductoForm
    template_name = 'productoCrear.html'
    success_url = reverse_lazy('Negocio:producto_crud')

class ProductoEliminarView(View):
    def post(self, request, pk, *args, **kwargs):
        producto = get_object_or_404(Producto, pk=pk)
        producto.delete()
        return redirect('Negocio:producto_crud')   
    

class ReservaCRUDView(TemplateView):
    template_name = 'reserva_crud.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['reservas'] = Reserva.objects.all()
        return context

class ReservaEditarView(UpdateView):
    model = Reserva
    form_class = ReservaForm
    template_name = 'reservaEditar.html'
    success_url = reverse_lazy('Negocio:reserva_crud')


class ReservaCrearView(CreateView):
    model = Reserva
    form_class = ReservaForm
    template_name = 'reservaCrear.html'
    success_url = reverse_lazy('Negocio:reserva_crud')

class ReservaEliminarView(View):
    def post(self, request, pk, *args, **kwargs):
        reserva = get_object_or_404(Reserva, pk=pk)
        reserva.delete()
        return redirect('Negocio:reserva_crud')  


class CategoriaCRUDView(TemplateView):
    template_name = 'categoria_crud.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categorias'] = Categoria.objects.all()
        return context
    

class CategoriaCrearView(CreateView):
    model = Categoria
    form_class = CategoriaForm
    template_name = 'categoriaCrear.html'
    success_url = reverse_lazy('Negocio:categoria_crud')

class CategoriaEditarView(UpdateView):
    model = Categoria
    form_class = CategoriaForm
    template_name = 'categoriaEditar.html'
    success_url = reverse_lazy('Negocio:categoria_crud')

class CategoriaEliminarView(View):
    def post(self, request, pk, *args, **kwargs):
        categoria = get_object_or_404(Categoria, pk=pk)
        categoria.delete()
        return redirect('Negocio:categoria_crud')
