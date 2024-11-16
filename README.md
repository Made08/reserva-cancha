# Sistema de Alquiler de Canchas de Fútbol

Este proyecto es una aplicación web para gestionar el alquiler de canchas de fútbol, incluyendo funcionalidades como registro de usuarios, reservas de canchas y más.

## Requisitos

- Python 3.8 o superior
- PostgreSQL
- Virtualenv o similar

## Instalación

1. Clonar el proyecto y navegar al directorio principal:

    ```bash
    git clone <ruta-del-repo>
    cd Aquilar_canchas
    ```

2. Crear y activar un entorno virtual:

    ```bash
    python -m venv env
    source env/bin/activate  # En Windows usa `env\Scripts\activate`
    ```

3. Instalar las dependencias:

    ```bash
    pip install -r requirements.txt
    ```

4. Configurar la base de datos:

    - Crear una base de datos PostgreSQL con el nombre `reserva`.
    - Configurar usuario y contraseña en el archivo `futbol_app/settings.py`.

5. Aplicar las migraciones:

    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

6. Iniciar el servidor:

    ```bash
    python manage.py runserver
    ```

## Funcionalidades

- Registro y autenticación de usuarios.
- Gestión de canchas: agregar, modificar o eliminar canchas disponibles.
- Realizar reservas de canchas según disponibilidad.
- Posibilidad de cancelación y modificación de reservas.

## Estructura del Proyecto

- `futbol_app/`: Aplicación principal que contiene la lógica y vistas del sistema.
- `reservas/`: Módulo encargado de la gestión de reservas.
- `manage.py`: Script de administración del proyecto.

## Contribuciones

Las contribuciones son bienvenidas. Si deseas colaborar, por favor sigue estos pasos:

1. Haz un fork del repositorio.
2. Crea una rama para tu feature (`git checkout -b feature/nueva-feature`).
3. Haz commit de tus cambios (`git commit -am 'Añadir nueva feature'`).
4. Haz push a la rama (`git push origin feature/nueva-feature`).
5. Abre un Pull Request.

## Licencia

Este proyecto está bajo la Licencia [MIT](https://opensource.org/licenses/MIT).

---
