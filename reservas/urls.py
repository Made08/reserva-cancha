from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('register/', views.register, name='register'),
    path('login/', LoginView.as_view(template_name='reservas/login.html'), name='login'),
    path('logout/', LogoutView.as_view(next_page='inicio'), name='logout'), 
    path('dashboard/', views.dashboard, name='dashboard'),  # Ruta para el dashboard
    path('canchas/', views.listar_canchas, name='listar_canchas'),
    path('canchas/agregar/', views.agregar_cancha, name='agregar_cancha'),
    path('reservar/<int:cancha_id>/', views.reservar_cancha, name='reservar_cancha'),
    path('reservas/', views.listar_reservas, name='listar_reservas'),
]
