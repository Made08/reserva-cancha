from django.contrib import admin
from django.urls import path, include
from reservas import views  # Asegúrate de importar 'views'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('reservas/', include('reservas.urls')),  # Incluye las URLs de la aplicación 'reservas'
    path('', views.inicio, name='inicio'),  # Configura la URL raíz
    path('accounts/', include('django.contrib.auth.urls')),  # Incluye las URLs de autenticación predeterminadas de Django
]
