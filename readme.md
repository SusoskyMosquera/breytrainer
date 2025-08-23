# Proyecto BreyTrainer - Backend con Django

Esta es la base del proyecto para la página web de Breyner Riveros, utilizando Django y Django Rest Framework para el backend, y un frontend estático.

**Novedad:** ¡Ahora casi todo el contenido del sitio es editable desde el panel de Django Admin!

## 🚀 Puesta en Marcha (Instalación Local)

Sigue estos pasos para ejecutar el proyecto en tu computadora.

### Prerrequisitos
- Python 3.8 o superior instalado.
- `pip` (el gestor de paquetes de Python).

### 1. Crear un Entorno Virtual
Es una buena práctica aislar las dependencias del proyecto. Abre tu terminal en la carpeta raíz del proyecto y ejecuta:

```bash
# En Windows
python -m venv venv
venv\\Scripts\\activate

# En macOS / Linux
python3 -m venv venv
source venv/bin/activate
```

### 2. Instalar Dependencias
Instala todas las librerías necesarias que se encuentran en `requirements.txt`:

```bash
pip install -r requirements.txt
```

### 3. Aplicar Migraciones de la Base de Datos
Este comando creará la base de datos (un archivo `db.sqlite3` por defecto) y las tablas necesarias para los posts, rutinas y la nueva configuración del sitio.

```bash
python manage.py migrate
```

### 4. Crear un Superusuario
Necesitas un usuario administrador para acceder al panel de Django (`/admin`).

```bash
python manage.py createsuperuser
```
Sigue las instrucciones para crear tu nombre de usuario, email y contraseña.

### 5. Ejecutar el Servidor de Desarrollo
¡Ya casi está! Inicia el servidor de Django:

```bash
python manage.py runserver
```

### 6. ¡Listo! Accede a la Aplicación
- **Frontend (La página web):** Abre tu navegador y ve a [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
- **Panel de Administrador:** Ve a [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/) e inicia sesión con el superusuario que creaste.

### Cómo Editar el Contenido
1.  Inicia sesión en el panel de administrador.
2.  Verás tres secciones:
    * **Api:** Para añadir/editar **Publicaciones** (del blog) y **Rutinas**.
    * **Site_Config:** Haz clic en **"Site Configurations"**. Verás una única entrada de configuración. Haz clic en ella para editar todo el texto, imágenes y enlaces de la página principal.
3.  Guarda los cambios y recarga la página principal para verlos aplicados al instante.