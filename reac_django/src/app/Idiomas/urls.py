from django.contrib import admin
from django.urls import path,include
from .views import RegistrarPersona

urlpatterns = [

    path('registrar/', RegistrarPersona,name='registrar')
]