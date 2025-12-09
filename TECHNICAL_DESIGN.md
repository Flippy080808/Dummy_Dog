# 🏗️ Diseño Técnico - Dummy Dog

Documento que describe la arquitectura técnica, modelos de datos y tecnologías utilizadas en la aplicación.

---

## 🗄️ Diagrama de Base de Datos (Modelos)

### Modelo Principal: Producto

```
┌────────────────────────────────────────────────┐
│              TABLA: Nucleo_producto            │
├────────────────────────────────────────────────┤
│                                                │
│  id_product         INTEGER PRIMARY KEY        │
│  (AutoField - se incrementa automáticamente)  │
│                                                │
│  nombre             VARCHAR(200) NOT NULL      │
│  (Nombre del producto, ej: "Croquetas")       │
│                                                │
│  marca              VARCHAR(100) NULLABLE      │
│  (Marca, ej: "Pedigri", "Purina")             │
│                                                │
│  precio             DECIMAL(10,2) NOT NULL    │
│  (Precio con 2 decimales, ej: 99.99)          │
│                                                │
│  inventario         INTEGER DEFAULT 0         │
│  (Stock disponible, ej: 150)                  │
│                                                │
│  categoria          VARCHAR(100) NULLABLE      │
│  (Categoría, ej: "Alimento", "Juguete")       │
│                                                │
│  id_veter           INTEGER NULLABLE           │
│  (Referencia a veterinaria - futuro FK)       │
│                                                │
│  imagen_url         VARCHAR(500) NULLABLE      │
│  (URL de imagen externa)                      │
│                                                │
└────────────────────────────────────────────────┘
```

### SQL de Creación

```sql
CREATE TABLE Nucleo_producto (
    id_product INTEGER PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(200) NOT NULL,
    marca VARCHAR(100),
    precio DECIMAL(10, 2) NOT NULL,
    inventario INTEGER DEFAULT 0,
    categoria VARCHAR(100),
    id_veter INTEGER,
    imagen_url VARCHAR(500)
);
```

### Relaciones entre Modelos

**Estado actual:** Modelo único (Producto)

```
┌─────────────────────────┐
│     PRODUCTO            │
│  (Tabla única)          │
└─────────────────────────┘
```

**Relaciones futuras (Roadmap):**

```
┌──────────────┐     ┌─────────────┐
│ VETERINARIO  │────▶│  PRODUCTO   │
│              │ 1:N │             │
└──────────────┘     └─────────────┘

┌──────────────┐     ┌──────────────┐
│   USUARIO    │────▶│   PEDIDO     │
│              │ 1:N │              │
└──────────────┘     └──────────────┘
                            │ 1:N
                            ▼
                    ┌──────────────┐
                    │ DETALLE_PED. │
                    │  (M2M con    │
                    │  PRODUCTO)   │
                    └──────────────┘
```

---

## 📦 Estructuras de Datos (en código)

### Producto (Python/Django)

```python
class Producto(models.Model):
    id_product = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=200)
    marca = models.CharField(max_length=100, blank=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    inventario = models.IntegerField(default=0)
    categoria = models.CharField(max_length=100, blank=True)
    id_veter = models.IntegerField(null=True, blank=True)
    imagen_url = models.URLField(max_length=500, blank=True, null=True)
    
    def __str__(self):
        return f"{self.nombre} ({self.marca})"
    
    class Meta:
        ordering = ['-id_product']  # Más nuevo primero
```

### Carrito (JavaScript localStorage)

```javascript
// Formato en localStorage
{
  id_product: 1,
  nombre: "Croquetas Puppies",
  marca: "Pedigri",
  precio: "25.99",
  imagen_url: "https://...",
  quantity: 2
}

// Almacenamiento
localStorage['dummy_dog_cart'] = JSON.stringify(array_de_items)
```

---

## 🏢 Estructura de Apps Django

### App Principal: **Nucleo**

**Propósito:** Contiene toda la lógica de negocio de la tienda online

**Estructura:**

```
Nucleo/
├── models.py           # Modelo Producto
├── views.py            # 13 vistas principales
├── forms.py            # ProductoForm
├── urls.py             # 14 rutas
├── admin.py            # Configuración admin
├── apps.py             # Configuración de app
├── tests.py            # Tests unitarios
├── migrations/         # Historial de cambios BD
│   ├── 0001_initial.py
│   └── 0002_producto_imagen_url.py
├── static/             # CSS y recursos
│   ├── global.css      # Estilos globales
│   ├── styles.css      # Estilos index
│   └── ...             # CSS específicos
└── templates/          # HTML
    ├── index.html
    ├── producto.html
    ├── producto_detail.html
    ├── carrito.html
    ├── productos_list.html
    ├── agregar_productos.html
    ├── editar_producto.html
    ├── confirmar_eliminar.html
    └── ... (8 templates más)
```

**Responsabilidades:**
- ✅ Gestión de productos (CRUD)
- ✅ Búsqueda de productos
- ✅ Vistas de carrito
- ✅ Páginas auxiliares
- ✅ Lógica de negocio

---

## 🛠️ Tecnologías Utilizadas

### Backend

```
Framework:           Django 5.2.8
Lenguaje:            Python 3.13
Servidor:            Django development server
Base de Datos:       SQLite3 (desarrollo)
                     MySQL (producción)
ORM:                 Django ORM
```

### Frontend

```
HTML:                HTML5
CSS:                 CSS3 con variables personalizadas
JavaScript:          Vanilla JS (ES6+)
Framework CSS:       Bootstrap 5.3.3
Iconografía:         Emojis + iconos HTML
Responsividad:       Media queries CSS
```

### Tecnologías Extra

```
Google Maps API:     Mapas embed en página veterinaria
localStorage:        Persistencia de carrito (sin backend)
URLField:            Validación de URLs en modelo
StaticFiles:         Gestión de archivos estáticos Django
CSRF Protection:     Django default CSRF tokens
Media Queries:       Responsive design (mobile-first)
```

### Base de Datos

```
Desarrollo:          SQLite3 (db.sqlite3)
Producción:          MySQL (con mysqlclient)
Migraciones:         Django migrations
Queries:             ORM Django con Q objects
```

### Utilidades Externas

```
Placeholder imagen:  via.placeholder.com
Fallback imagen:     previews.123rf.com
Maps:                Google Maps embed API
Hosting:             PythonAnywhere
```

---

## 🔌 Arquitectura de Software

### Patrón MTV (Model-Template-View)

```
Usuario
  ↓
URL (urls.py)
  ↓ Enruta a
View (views.py)
  ↓ Consulta
Model (models.py)
  ↓ Queryset
Database
  ↓ Retorna
Model instance
  ↓ Pasa a
Template (*.html)
  ↓ Renderiza
HTML Response
  ↓
Usuario (HTML en navegador)
```

### Flujo de una Solicitud

```
1. Usuario accede a http://localhost:8000/productos/
                  ↓
2. Django matchea URL en urls.py
   path('productos/', views.lista_productos, name='productos_list')
                  ↓
3. Ejecuta vista: lista_productos(request)
   productos = Producto.objects.all().order_by('nombre')
                  ↓
4. Pasa datos al template: producto_list.html
   render(request, 'productos_list.html', {'productos': productos})
                  ↓
5. Template renderiza HTML con datos
   {% for p in productos %}
     <div>{{ p.nombre }}</div>
   {% endfor %}
                  ↓
6. Retorna HTML al navegador
   HTTP 200 OK + HTML response
                  ↓
7. Navegador muestra página
```

---

## 📊 Stack Tecnológico Completo

```
┌─────────────────────────────────────────┐
│          DUMMY DOG TECH STACK            │
├─────────────────────────────────────────┤
│                                         │
│  LAYER        TECNOLOGÍA               │
│  ───────────────────────────────────── │
│  
│  Frontend     HTML5 + CSS3 + JS        │
│               Bootstrap 5.3.3          │
│               localStorage             │
│               Google Maps API          │
│                                         │
│  Backend      Django 5.2.8             │
│               Python 3.13              │
│               Django ORM               │
│                                         │
│  Database     SQLite3 (dev)            │
│               MySQL (prod)             │
│                                         │
│  Server       Django dev server        │
│               (development)            │
│               WSGI (production)        │
│                                         │
│  Deploy       PythonAnywhere           │
│                                         │
└─────────────────────────────────────────┘
```

---

## 🔐 Patrones de Seguridad

```
✅ CSRF Protection
   - Django default CSRF tokens
   - Validado en formularios POST

✅ SQL Injection Prevention
   - Django ORM (no raw SQL)
   - Parameterized queries

✅ XSS Prevention
   - Template escaping automático
   - form.is_valid() validación

✅ Object-Level Security
   - get_object_or_404() - 404 en acceso no autorizado
   - Method validation (GET vs POST)

✅ Input Validation
   - Modelo: CharField, IntegerField, URLField
   - Formulario: validación automática
   - Template: filtros Django

✅ Secure Deletion
   - Confirmación POST requerida
   - Patrón GET → Mostrar | POST → Ejecutar
```

---

## 📈 Escalabilidad Considerada

```
Decisiones escalables:

1. URLs Externas de Imágenes
   ✓ No consume almacenamiento servidor
   ✓ CDN capable
   ✓ Facil de actualizar

2. localStorage para Carrito
   ✓ No requiere BD
   ✓ Presión cero en servidor
   ✓ Persiste entre sesiones

3. Queries Optimizadas
   ✓ order_by()
   ✓ exclude()
   ✓ filter()
   ✓ [:8] slicing

4. Static Files Management
   ✓ {% static %} tags
   ✓ CSS variables personalizadas
   ✓ Fácil cambio de theme
```

---

## 🔄 Migraciones de Base de Datos

### Migración 1: Initial (Producto básico)

```python
# 0001_initial.py
class Migration(migrations.Migration):
    initial = True
    dependencies = []
    
    operations = [
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id_product', models.AutoField(...)),
                ('nombre', models.CharField(max_length=200)),
                ('marca', models.CharField(...)),
                ('precio', models.DecimalField(...)),
                ('inventario', models.IntegerField(...)),
                ('categoria', models.CharField(...)),
                ('id_veter', models.IntegerField(...)),
            ],
        ),
    ]
```

### Migración 2: Agregar imagen_url

```python
# 0002_producto_imagen_url.py
class Migration(migrations.Migration):
    dependencies = [('Nucleo', '0001_initial')]
    
    operations = [
        migrations.AddField(
            model_name='producto',
            name='imagen_url',
            field=models.URLField(max_length=500, blank=True, null=True),
        ),
    ]
```

---

## 📋 Configuraciones Django

### settings.py Relevantes

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'Nucleo',  # App principal
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
    }
]
```

---

## 📊 Estadísticas de Código

```
Python:              ~500 líneas (models, views, forms)
HTML:                ~3000 líneas (14 templates)
CSS:                 ~1500 líneas (global + específicos)
JavaScript:          ~300 líneas (carrito, notificaciones)
───────────────────────────────────
Total:               ~5300 líneas de código

Funciones:           13+ vistas
Modelos:             1 modelo principal
Templates:           14 templates
Rutas:               14 endpoints
```

---

**Documento actualizado:** 8 de Diciembre de 2025
