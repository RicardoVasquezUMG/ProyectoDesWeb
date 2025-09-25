from django.shortcuts import render
from django.views.generic import TemplateView

class HomeView(TemplateView):
    template_name = 'home.html'

class AcercaView(TemplateView): 
    template_name = 'acerca.html'

 
