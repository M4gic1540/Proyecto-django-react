# Hotel Reservations

Este es un sistema de reservas de hotel desarrollado en Django. Permite a los usuarios realizar reservas de habitaciones y gestionar sus perfiles, mientras que los administradores pueden gestionar habitaciones y reservas.

## Requisitos previos

- Python 3.x
- Git (para clonar el repositorio)

## Instalación

Sigue estos pasos para configurar el proyecto en tu máquina local.

### 1. Clonar el repositorio

```bash
git clone https://github.com/tu-usuario/hotel-reservations.git
cd hotel-reservations


2. Crear y activar un entorno virtual

python -m venv venv
## En Windows
venv/Scripts/activate
# En macOS y Linux
source venv/bin/activate
```


## 3. Instalar las dependencias

- pip install -r requirements.txt

## 4. Configurar la base de datos
Ejecuta las migraciones para configurar la base de datos:

python manage.py migrate


 ## 5. Crear un superusuario
Crea un superusuario para acceder al panel de administración de Django:

python manage.py createsuperuser


## 6. Ejecutar el servidor de desarrollo
Inicia el servidor de desarrollo de Django:

python manage.py runserver

## Opcional: Cargar datos de prueba
Si deseas cargar datos de ejemplo, como habitaciones predefinidas, puedes ejecutar el siguiente script

- python populaterooms.py


## Estructura del Proyecto:


- accounts/: Módulo para la gestión de usuarios.

- reservations/: Módulo principal para la gestión de reservas y habitaciones.

- static/: Archivos estáticos (CSS, JS, imágenes).

- templates/: Plantillas HTML para la aplicación.

- hotel_reservations/: Configuración del proyecto Django.