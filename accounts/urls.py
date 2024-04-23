from django.urls import path
from . import views

urlpatterns = [
    path('ingreso/', views.ingreso, name='ingreso'),
    path('registro/', views.registro, name='registro'),
    # Otras URLs de tu aplicación...
]

