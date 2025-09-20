from django.contrib import admin
from django.urls import path,include
from Apps.Home.views import HomeView, AcercaView

app_name = 'Home'
urlpatterns = [
    path('', HomeView.as_view(), name='homeapp'),
    path('acerca/', AcercaView.as_view(), name='acerca_app'),
]

