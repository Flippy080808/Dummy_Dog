# 📖 Guía de Instalación - Dummy Dog

Pasos detallados para instalar y ejecutar la aplicación Dummy Dog en tu computadora.

---

## 📋 Requisitos Previos

Antes de comenzar, asegúrate de tener:

### Hardware Mínimo
```
Procesador:   Intel/AMD (2 GHz o superior)
RAM:          2 GB mínimo (4 GB recomendado)
Disco:        500 MB disponibles
```

### Software Requerido
```
✅ Python 3.13 (o 3.11+)
✅ pip (gestor de paquetes Python)
✅ Git (opcional, para clonar repositorio)
✅ Navegador web moderno (Chrome, Firefox, Edge)
```

---

## 🖥️ Instalación en Windows

### Paso 1: Instalar Python

1. Descarga Python desde [python.org](https://www.python.org/downloads/)
2. **IMPORTANTE:** Marca la opción "Add Python to PATH"
3. Haz clic en "Install Now"
4. Verifica la instalación:

```powershell
python --version
pip --version
```

Deberías ver:
```
Python 3.13.x
pip 24.x.x
```

### Paso 2: Clonar o Descargar el Proyecto

**Opción A - Con Git (recomendado):**

```powershell
cd Desktop
git clone <URL_del_repositorio> Dummy_Dog
cd Dummy_Dog
```

**Opción B - Descargar ZIP:**

1. Descarga el ZIP del proyecto
2. Extrae en `C:\Users\Tu_Usuario\Desktop\Dummy_Dog`
3. Abre PowerShell en esa carpeta

### Paso 3: Crear Entorno Virtual

```powershell
python -m venv venv
```

Esto crea una carpeta `venv` con el entorno aislado.

### Paso 4: Activar Entorno Virtual

```powershell
.\venv\Scripts\Activate.ps1
```

Deberías ver `(venv)` al inicio de la línea en PowerShell:
```
(venv) PS C:\...\Dummy_Dog>
```

Si obtienes error de permisos, ejecuta PowerShell como administrador o usa:
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

### Paso 5: Instalar Dependencias

```powershell
pip install -r requirements.txt
```

Esto instala:
- Django 5.2.8
- mysqlclient (para MySQL en producción)
- Otros paquetes necesarios

El proceso toma 2-5 minutos. Espera a ver `Successfully installed...`

### Paso 6: Aplicar Migraciones

```powershell
python manage.py migrate
```

Verás mensajes como:
```
Running migrations:
  Applying Nucleo.0001_initial... OK
  Applying Nucleo.0002_producto_imagen_url... OK
```

Esto crea la base de datos SQLite.

### Paso 7: Crear Superusuario (Admin)

```powershell
python manage.py createsuperuser
```

Te pedirá:
```
Username: admin
Email: admin@dummy.dog
Password: (ingresa contraseña)
Password (again): (confirma)
```

### Paso 8: Recopilar Archivos Estáticos

```powershell
python manage.py collectstatic --noinput
```

Esto organiza los CSS e imágenes.

### Paso 9: Ejecutar Servidor

```powershell
python manage.py runserver
```

Verás:
```
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.
```

### Paso 10: Acceder a la Aplicación

Abre tu navegador:
- 🏠 **Sitio:** http://localhost:8000/
- 🔧 **Admin:** http://localhost:8000/admin/

Ingresa con las credenciales que creaste en Paso 7.

---

## 🍎 Instalación en macOS

### Paso 1: Instalar Python (si no tienes)

```bash
# Opción A: Con Homebrew
brew install python@3.13

# Opción B: Descarga de python.org
# (descarga e instala el .pkg)
```

Verifica:
```bash
python3 --version
pip3 --version
```

### Paso 2-5: Mismo que Windows

```bash
cd ~/Desktop
git clone <URL> Dummy_Dog
cd Dummy_Dog

python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Paso 6-10: Mismo que Windows

```bash
python manage.py migrate
python manage.py createsuperuser
python manage.py collectstatic --noinput
python manage.py runserver
```

Accede a http://localhost:8000/

---

## 🐧 Instalación en Linux (Ubuntu/Debian)

### Paso 1: Instalar Python y pip

```bash
sudo apt update
sudo apt install python3 python3-pip python3-venv
```

Verifica:
```bash
python3 --version
pip3 --version
```

### Paso 2-5: Igual que macOS

```bash
cd ~/Desktop
git clone <URL> Dummy_Dog
cd Dummy_Dog

python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Paso 6-10: Igual que macOS

```bash
python manage.py migrate
python manage.py createsuperuser
python manage.py collectstatic --noinput
python manage.py runserver
```

Accede a http://localhost:8000/

---

## 📁 Estructura de Carpetas Después de Instalar

```
Dummy_Dog/                      # Carpeta principal
├── venv/                       # Entorno virtual (NO modificar)
├── Nucleo/                     # App Django
│   ├── models.py
│   ├── views.py
│   ├── forms.py
│   ├── urls.py
│   ├── static/                 # CSS e imágenes
│   └── templates/              # HTML templates
├── DummyDog/                   # Configuración Django
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── db.sqlite3                  # Base de datos (creada tras migrate)
├── manage.py                   # Comando principal Django
├── requirements.txt            # Lista de dependencias
├── README.md                   # Este archivo
├── TECHNICAL_DOCUMENTATION.md
├── CHANGELOG.md
└── ...
```

---

## 🐛 Solución de Problemas Comunes

### Error: "python: command not found"

**Solución:**
```powershell
# Windows
python3 --version

# Si aún no funciona, reinstala Python desde python.org
# ¡Marca "Add Python to PATH"!
```

### Error: "No module named 'django'"

**Solución:**
```powershell
# Verifica que el entorno virtual está activado
# Deberías ver (venv) al inicio de tu línea

# Reinstala dependencias
pip install -r requirements.txt
```

### Error: "Port 8000 already in use"

**Solución:**
```powershell
# Usa otro puerto
python manage.py runserver 8001

# O mata el proceso anterior
# Windows PowerShell:
Get-Process -Name python | Stop-Process

# macOS/Linux:
lsof -i :8000
kill -9 <PID>
```

### Error: "Table doesn't exist"

**Solución:**
```powershell
# Ejecuta migraciones
python manage.py migrate

# O si hay conflictos, borra BD y reinicia:
# (¡Esto elimina datos!)
rm db.sqlite3
python manage.py migrate
python manage.py createsuperuser
```

### Las imágenes no cargan

**Solución:**
```powershell
# Recopila archivos estáticos
python manage.py collectstatic --noinput

# Verifica que las URLs en base de datos sean válidas
# (deben comenzar con http:// o https://)
```

---

## 🔄 Comandos Útiles Día a Día

### Activar el entorno (cada vez que abres la terminal)

```powershell
# Windows
.\venv\Scripts\Activate.ps1

# macOS/Linux
source venv/bin/activate
```

### Ejecutar el servidor

```powershell
python manage.py runserver
```

### Acceder a Django shell (para pruebas)

```powershell
python manage.py shell

# Dentro de Python:
from Nucleo.models import Producto
Producto.objects.all()  # Ver todos los productos
```

### Crear backup de base de datos

```powershell
# Windows
copy db.sqlite3 db.sqlite3.backup

# macOS/Linux
cp db.sqlite3 db.sqlite3.backup
```

### Ver todas las migraciones

```powershell
python manage.py showmigrations
```

---

## 🌍 Desplegar en PythonAnywhere (Producción)

Si quieres llevar la app a internet:

### Paso 1: Crear cuenta en PythonAnywhere

1. Visita https://www.pythonanywhere.com/
2. Crea una cuenta gratuita
3. Confirma tu email

### Paso 2: Subir código

Opción A - Git:
```bash
# En PythonAnywhere console
git clone <tu_repo> DummyDog
cd DummyDog
```

Opción B - Archivos:
```bash
# Descarga ZIP y sube por el panel web
```

### Paso 3: Crear virtualenv

```bash
mkvirtualenv --python=/usr/bin/python3.9 myenv
pip install -r requirements.txt
```

### Paso 4: Configurar Web App

1. En PythonAnywhere: Web → Add new web app
2. Selecciona Python 3.9 + Django
3. Apunta WSGI a: `/path/to/DummyDog/DummyDog/wsgi.py`
4. Configura Static files:
   - URL: `/static/`
   - Path: `/path/to/DummyDog/staticfiles/`

### Paso 5: Ejecutar migraciones

```bash
cd DummyDog
python manage.py migrate
python manage.py createsuperuser
```

### Paso 6: Reload

En PythyAnywhere Web, haz clic en "Reload"

Tu sitio estará en: `tu_usuario.pythonanywhere.com`

---

## ✅ Checklist de Instalación

```
□ Python 3.13 instalado
□ Proyecto clonado/descargado
□ Entorno virtual creado
□ Entorno virtual activado
□ Dependencias instaladas (pip install -r requirements.txt)
□ Migraciones aplicadas (python manage.py migrate)
□ Superusuario creado (python manage.py createsuperuser)
□ Archivos estáticos recopilados (python manage.py collectstatic)
□ Servidor ejecutándose (python manage.py runserver)
□ Acceso a http://localhost:8000/ verificado
□ Acceso a admin en /admin/ verificado
□ Productos visibles en el sitio
□ Carrito funciona (localStorage)
□ Búsqueda de productos funciona
```

---

## 📞 Soporte

Si tienes problemas:

1. ✅ Verifica Python version: `python --version`
2. ✅ Verifica que el entorno virtual está activado (debe mostrar `(venv)`)
3. ✅ Revisa los mensajes de error en la terminal
4. ✅ Consulta la sección "Solución de Problemas" arriba
5. ✅ Revisa TECHNICAL_DOCUMENTATION.md para detalles técnicos

---

**Última actualización:** 8 de Diciembre de 2025
