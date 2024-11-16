# Sistema de Alquiler de Canchas de Fútbol

Este proyecto es una aplicación web para gestionar el alquiler de canchas de fútbol, incluyendo funcionalidades como registro de usuarios, reservas de canchas y más.

## Requisitos

- Python 3.8 o superior
- PostgreSQL
- Virtualenv o similar
- Docker

## Descarga de Repositorio

1. Clonar el proyecto y navegar al directorio principal:

    ```bash
    git clone git@github.com:Made08/reserva-cancha.git
    cd reserva-cancha
    ```

## Instalación Infra DB
1. Instanciar los contenedores de base de datos y visor dataminer

    ```bash
    docker compose up -d
    ```

### Nota: Bajar infra

    ```bash
    docker compose down
    ```

## Habilitar Entorno Python

1. Crear y activar un entorno virtual:

    ```bash
    python3 -m venv venv
    source venv/bin/activate  # En Windows usa `env\Scripts\activate`
    ```

2. Instalar las dependencias:

    ```bash
    pip install -r requirements.txt
    ```

3. Configurar la base de datos:

    - Crear una base de datos PostgreSQL con el nombre `reserva` <-- Ya creada si se ejecuto docker compose
    - Configurar usuario y contraseña en el archivo `futbol_app/settings.py`.

4. Aplicar las migraciones:

    ```bash
    python3 manage.py makemigrations
    python3 manage.py migrate
    ```

5. Iniciar el servidor:

    ```bash
    python3 manage.py runserver
    ```

6. Entrar a la Aplicacion

    Aplicacion:   http://localhost:8000/
    Dataminer:    http://localhost:8080

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
