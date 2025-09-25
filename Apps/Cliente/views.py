from django.shortcuts import render # type: ignore
from django.views.generic import TemplateView

class LoginView(TemplateView):
	template_name = 'login.html'

class CrearClienteView(TemplateView):
	template_name = 'register.html'

class MenuView(TemplateView):
    template_name = 'Menu.html'
