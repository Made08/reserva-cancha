
from django.urls import path
from . import views

urlpatterns = [
    path('canchas/', views.listar_canchas, name='listar_canchas'),
    path('canchas/agregar/', views.agregar_cancha, name='agregar_cancha'),
    path('reservar/<int:cancha_id>/', views.reservar_cancha, name='reservar_cancha'),
    path('reservas/', views.listar_reservas, name='listar_reservas'),
]
