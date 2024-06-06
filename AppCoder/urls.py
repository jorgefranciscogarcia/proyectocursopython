from django.contrib.auth.views import LogoutView
from django.urls import path

from AppCoder.views import *

urlpatterns = [
    path('', inicio, name='Inicio'),
    path('', contacto, name='Contact'),
    path('', projects, name='Projects'),
    path('', resume, name='Resume'),
]
