# 🐶 Dummy Dog - Tienda Online para Mascotas

Una aplicación web completa que permite vender productos para mascotas y facilitar el acceso a servicios veterinarios.

## 🆕 Cambios Recientes

### Actualización: Sistema de Imágenes por URL (Diciembre 2025)
- ✨ Nuevo campo `imagen_url` en el modelo Producto para URLs de imágenes externas
- ✨ Formularios actualizados: ahora puedes agregar/editar imágenes al crear productos
- ✨ Los templates `producto.html`, `index.html` y `carrito.html` ahora usan las imágenes del producto
- ✨ Sistema de fallback: si la URL no funciona, automáticamente se muestra un placeholder
- 🗑️ Eliminado: Enlace "Productos" del navbar (solo accesible desde botón "➕ Agregar")

**Ventaja:** Las imágenes no se guardan localmente, evitando consumo de almacenamiento en tu host

---

## 📋 Características Principales

✅ **Catálogo de Productos** - Gestión completa de productos (CRUD)  
✅ **Imágenes de Productos** - Sistema de URLs para imágenes sin consumir almacenamiento local  
✅ **Carrito de Compras** - Sistema de carrito con almacenamiento local  
✅ **Búsqueda de Veterinarias** - Integración con Google Maps  
✅ **Panel de Administración** - Agregar, editar y eliminar productos  
✅ **Interfaz Responsiva** - Compatible con móviles y desktop  
✅ **Diseño Moderno** - UI/UX profesional con color scheme personalizado

---

## 🏗️ Estructura del Proyecto

```
Dummy_Dog/
├── DummyDog/              # Configuración principal de Django
│   ├── settings.py        # Configuración del proyecto
│   ├── urls.py            # URLs principales
│   ├── wsgi.py            # Configuración WSGI
│   └── asgi.py            # Configuración ASGI
│
├── Nucleo/                # App principal
│   ├── models.py          # Modelos de BD (Producto)
│   ├── views.py           # Vistas y lógica
│   ├── urls.py            # Rutas de la app
│   ├── forms.py           # Formularios Django
│   ├── admin.py           # Panel admin
│   ├── static/            # CSS y recursos
│   │   ├── global.css     # Estilos globales
│   │   ├── styles.css     # Estilos index
│   │   └── ...            # Otros CSS
│   └── templates/         # Templates HTML
│       ├── index.html           # Página inicio (productos)
│       ├── producto.html        # Detalle producto (compra)
│       ├── producto_detail.html # Detalle producto (admin)
│       ├── carrito.html         # Carrito de compras
│       ├── productos_list.html  # Catálogo completo
│       ├── agregar_productos.html
│       ├── editar_producto.html
│       ├── confirmar_eliminar.html
│       ├── veter.html           # Veterinarias
│       ├── serv.html            # Servicios
│       ├── cuidador.html        # Perfil cuidador
│       └── adopcion.html        # Adopciones
│
├── db.sqlite3             # Base de datos
├── manage.py              # Comando Django
└── requirements.txt       # Dependencias
```

---

## 📁 Descripción de Archivos Clave

### **Backend - views.py**
```python
# Gestión de vistas principales
- index()              # Página de inicio con productos dinámicos de BD
- producto()           # Página de producto (interfaz de compra)
- detalle_producto()   # Detalle de producto (admin)
- lista_productos()    # Catálogo completo de productos
- crear_producto()     # Formulario para agregar producto
- editar_producto()    # Formulario para editar producto
- eliminar_producto()  # Confirmación de eliminación
- carrito()            # Página del carrito de compras
- veter()              # Página de veterinarias con Google Maps
- serv()               # Página de servicios
- cuidador()           # Perfil de cuidador
- adopcion()           # Página de adopciones
- buscar_productos()   # Búsqueda de productos
```

### **Modelos - models.py**
```python
class Producto(models.Model):
    id_product    = AutoField(primary_key=True)  # ID único
    nombre        = CharField(max_length=200)    # Nombre del producto
    marca         = CharField(max_length=100, blank=True)  # Marca
    precio        = DecimalField(max_digits=10, decimal_places=2)  # Precio
    inventario    = IntegerField()               # Cantidad disponible
    categoria     = CharField(max_length=100, blank=True)  # Categoría
    id_veter      = IntegerField(null=True, blank=True)  # ID veterinaria
    imagen_url    = URLField(max_length=500, blank=True, null=True)  # URL de imagen
```

### **Formularios - forms.py**
```python
class ProductoForm(ModelForm):
    # Formulario para crear/editar productos
    # Genera campos automáticos del modelo
    # Incluye validación integrada
```

### **URLs - urls.py**
```
/                           → index (inicio)
/producto/<id>/             → producto.html (página de compra)
/productos/                 → productos_list.html (catálogo)
/productos/<id>/            → producto_detail.html (detalle admin)
/productos/<id>/editar/     → editar_producto (formulario edición)
/productos/<id>/eliminar/   → confirmar_eliminar (confirmación)
/agregar_producto/          → crear_producto (nuevo producto)
/carrito                    → carrito.html (carrito de compras)
/Veterinaria                → veter.html (veterinarias)
/servicios                  → serv.html (servicios)
/cuidador                   → cuidador.html (cuidador)
/adopcion                   → adopcion.html (adopciones)
/buscar/                    → buscar_productos (búsqueda)
```

---

## 🎨 Frontend - Templates HTML

### **index.html** - Página de Inicio
- Hero section con presentación
- Carrusel promocional (3 slides)
- Grid de productos dinámicos desde BD
- Enlaces a `/producto/<id>/` para ver detalles
- Navbar con enlace a carrito

### **producto.html** - Página de Compra (desde Index)
- Imagen del producto
- Nombre, marca, categoría (badges)
- Precio destacado con gradiente
- Stock disponible
- **Botones de compra:**
  - 🛒 Agregar al carrito (localStorage)
  - ✅ Ir al carrito (redirige a /carrito)
- Productos recomendados (relacionados)
- **NO tiene** botones Editar/Eliminar

### **producto_detail.html** - Página Admin (desde CRUD)
- Misma información que producto.html
- **Botones administrativos:**
  - ✏️ Editar producto
  - 🗑️ Eliminar producto
- Para gestión interna solamente

### **carrito.html** - Carrito de Compras
- Almacenamiento en localStorage (sin servidor)
- Lista de productos agregados
- Controles de cantidad (+/-)
- Botón eliminar por producto
- Resumen de precios:
  - Subtotal
  - IVA (19%)
  - Total
- Botón "Proceder al pago"
- Botón "Continuar comprando"

### **productos_list.html** - Catálogo Administrativo
- Grid de todos los productos
- Información: nombre, marca, precio, stock
- Enlaces a producto_detail.html
- Botones Editar/Eliminar (solo admin)

### **agregar_productos.html** - Formulario de Creación
- Header con gradiente verde
- Campos: nombre*, marca, precio*, inventario*, categoría, id_veter
- Validación visual de errores
- Botones: Guardar, Ver catálogo, Inicio
- Indicadores de campos obligatorios (*)

### **editar_producto.html** - Formulario de Edición
- Mismo diseño que agregar_productos
- Header con gradiente azul (diferenciador)
- Pre-rellena datos del producto
- Botones: Guardar cambios, Ver producto, Catálogo

### **confirmar_eliminar.html** - Confirmación de Eliminación
- Modal de advertencia con fondo rojo
- Muestra información del producto
- Aviso de irreversibilidad
- Botones: Sí eliminar, Cancelar

### **veter.html** - Veterinarias
- Navbar personalizado
- Google Maps embed integrado
- Información de ubicación
- Contacto directo

---

## 🖼️ Sistema de Imágenes

### ¿Por qué URLs en lugar de archivos locales?

Para garantizar que tu hosting (como PythonAnywhere) no consume espacio de almacenamiento, Dummy Dog utiliza un sistema de **URLs de imágenes externas**. Esto significa:

✅ **Sin consumo de almacenamiento** - Las imágenes se guardan en servidores externos  
✅ **Sin límites de tamaño** - Puedes usar imágenes de alta calidad sin preocupaciones  
✅ **Carga rápida** - Servidores especializados optimizan la entrega de imágenes  
✅ **Fácil actualización** - Cambiar imagen = cambiar URL (sin modificar BD)  
✅ **Escalabilidad** - Perfecto para crecer sin problemas de espacio

### ¿Cómo obtener URLs de imágenes?

#### **Opción 1: Imgur.com (Más fácil - Sin registro)**
1. Ve a https://imgur.com
2. Drag & drop tu imagen o haz click para subir
3. Copia el enlace directo (botón "Copy Link")
4. Pega en el campo "URL de la Imagen" al crear/editar producto
5. ✅ ¡Listo! La imagen aparecerá instantáneamente

**Ventajas:**
- No requiere registro
- Interfaz muy simple
- Enlace permanente
- Perfecto para principiantes

#### **Opción 2: ImgBB.com (Gratuito - Cuenta gratis)**
1. Ve a https://imgbb.com
2. Haz click en "Upload image" o arrastra la imagen
3. Espera a que se cargue
4. Copia la URL mostrada (en la sección "Direct Link")
5. Pega en el campo "URL de la Imagen"
6. ✅ ¡Listo!

**Ventajas:**
- Almacenamiento ilimitado
- Gestiona tus imágenes en un panel
- URLs permanentes (no expiran)
- Opción de cuenta con contraseña

#### **Opción 3: Cloudinary (Profesional - Plan gratuito)**
1. Crea cuenta en https://cloudinary.com (gratuito)
2. Ve a "Upload" en el panel
3. Sube tu imagen
4. En "Asset Details", copia la "URL de la imagen"
5. Pega en el campo "URL de la Imagen"
6. ✅ ¡Listo!

**Ventajas:**
- Transformación automática de imágenes
- Optimización automática de calidad
- Estadísticas de uso
- Plan gratuito muy generoso

#### **Opción 4: Usar tu propio servidor web**
Si tienes un servidor web (hosting):
1. Sube la imagen via FTP o panel de control
2. Obtén la URL completa (ej: `https://tudominio.com/imagenes/producto.jpg`)
3. Pega en el campo "URL de la Imagen"
4. ✅ ¡Listo!

### ¿Qué sucede si la URL está rota?

Si una imagen no carga correctamente (URL inválida o servicio caído):
- Automáticamente se muestra un **placeholder genérico** 
- El producto sigue siendo funcional
- Puedes editar el producto y actualizar la URL en cualquier momento

### Formato de URL válido:
```
✅ Válidas:
- https://i.imgur.com/abc123.jpg
- https://imgbb.com/imagen.jpg
- https://res.cloudinary.com/abc/imagen.jpg
- https://tudominio.com/imagenes/producto.png

❌ Inválidas (no funcionarán):
- http://imagen.jpg (sin https)
- /imagenes/local.jpg (rutas relativas)
- imagen.jpg (sin dominio)
- C:\Usuarios\Imagenes\foto.jpg (rutas de PC)
```

### Recomendación para empezar:
**🎯 Usa Imgur para pruebas rápidas y ImgBB para almacenamiento permanente**

---

## 🛒 Sistema de Carrito

### Funcionamiento:
1. Usuario hace clic en "Agregar al carrito" en `producto.html`
2. Producto se guarda en `localStorage` (almacenamiento local del navegador)
3. Badge en navbar muestra cantidad de artículos
4. En `/carrito` se visualizan todos los items
5. Usuario puede modificar cantidades o eliminar productos
6. Cálculo automático de subtotal, IVA y total

### LocalStorage:
```javascript
Key: 'dummy_dog_cart'
Value: [
  {
    id_product: 1,
    nombre: "Croquetas Puppies",
    precio: "25.99",
    quantity: 2
  },
  ...
]
```

---

## 🎨 Sistema de Colores (CSS Variables)

```css
--primary-green: #4CE64C    /* Verde principal */
--dark-green: #2db02d      /* Verde oscuro */
--light-green: #e8f5e9     /* Verde claro */
--yellow: #FCFA86           /* Amarillo (categorías) */
--blue: #3483fa             /* Azul (acciones) */
--dark-blue: #2968c8        /* Azul oscuro */
--gray-light: #f5f5f5       /* Gris claro */
--gray-dark: #333           /* Gris oscuro (texto) */
--text-muted: #777          /* Texto secundario */
```

---

## 🔧 Guía de Desarrollo

### Crear un Nuevo Producto:
1. Ir a `/agregar_producto/`
2. Llenar formulario
3. Guardar → redirige a `/productos/`
4. El producto aparecerá automáticamente en `/`

### Editar un Producto:
1. Ir a `/productos/` (catálogo admin)
2. Click en producto
3. Click "Editar"
4. Modificar campos
5. Guardar cambios

### Eliminar un Producto:
1. Ir a `/productos/` (catálogo admin)
2. Click en producto
3. Click "Eliminar"
4. Confirmar eliminación

### Acceder a un Producto:
- **Desde Index:** `/producto/<id>/` → interfaz de compra
- **Desde Catálogo:** `/productos/<id>/` → interfaz de detalle admin

---

## 📱 Responsividad

La aplicación es completamente responsiva:
- **Desktop:** Grid de 4 columnas
- **Tablet:** Grid de 3 columnas
- **Mobile:** Grid de 2 columnas
- Navbar colapsable en mobile
- Carrito adaptado a pantallas pequeñas

---

## 🚀 Instalación y Uso

### Requisitos:
```
Django 5.2.8
Python 3.13
Bootstrap 5.3.3
SQLite3
```

### Instalación:
```bash
git clone https://github.com/Flippy080808/Dummy_Dog.git
cd Dummy_Dog
python -m venv venv
source venv/Scripts/activate  # Windows
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

### Acceso:
- Sitio: `http://localhost:8000`
- Admin: `http://localhost:8000/admin`

---

## 📝 Tecnologías Utilizadas

- **Framework:** Django 5.2.8
- **Frontend:** Bootstrap 5.3.3, HTML5, CSS3
- **Base de Datos:** SQLite3
- **JavaScript:** Vanilla JS (carrito, validaciones)
- **Almacenamiento:** LocalStorage (carrito)
- **Mapas:** Google Maps API (veter.html)

---

## 👥 Autores

- **Jose FDA** - Formularios y gestión CRUD
- **Alberto GJ** - Vistas y lógica principal
- **Emily VQ** - Templates y diseño
- **Equipo Dummy Dog** - Mantenimiento general

---

## 📄 Licencia

Este proyecto es de código abierto y puede ser utilizado libremente.

---

## 🐛 Notas Importantes

- El carrito se almacena en el navegador (localStorage), no en servidor
- Los precios se calculan automáticamente con IVA (19%)
- Las imágenes de productos usan URLs externas (no se guardan localmente)
- Si una URL de imagen no funciona, se muestra automáticamente un placeholder
- El enlace "Productos" ha sido removido del navbar (solo accesible desde "➕ Agregar")
- La app es completamente funcional pero lista para integrar pasarela de pago
- Todos los estilos utilizan CSS custom properties para fácil personalización

---

**¡Gracias por usar Dummy Dog! 🐾**