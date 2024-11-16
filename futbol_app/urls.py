
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),  # Administración
    path('', include('reservas.urls')),  # Redirigir la URL base a 'reservas.urls'
    path('accounts/', include('django.contrib.auth.urls')),  # Autenticación predeterminada de Django
]
