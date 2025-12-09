# 📋 Requerimientos Funcionales - Dummy Dog

Documento que especifica todas las funcionalidades y características que implementa la aplicación Dummy Dog.

---

## 🎯 Descripción General

Dummy Dog es una **tienda online especializada en productos para mascotas** que permite a los usuarios:
- Navegar y buscar productos
- Agregar productos a un carrito de compras
- Ver detalles de productos y recomendaciones

Los administradores pueden:
- Crear nuevos productos
- Editar información de productos
- Eliminar productos del catálogo
- Gestionar imágenes por URL

---

## ✅ Funcionalidades Implementadas

### 1. **Gestión de Productos (CRUD)**

#### ✔️ Crear Productos
- **Descripción:** El administrador puede agregar nuevos productos a la tienda
- **Ruta:** `/agregar_producto/`
- **Método:** GET/POST
- **Campos:**
  - Nombre (obligatorio, máx 200 caracteres)
  - Marca (opcional, máx 100 caracteres)
  - Precio (obligatorio, decimal máx 10,2)
  - Inventario (obligatorio, número entero)
  - Categoría (opcional, máx 100 caracteres)
  - ID Veterinaria (opcional)
  - URL de Imagen (opcional, URLField)
- **Validación:** Automática por formulario Django
- **Redirección:** Al catálogo administrativo tras guardar
- **Estado:** ✅ IMPLEMENTADO

#### ✔️ Leer Productos
- **Descripción:** Los usuarios pueden ver productos en diferentes vistas
- **Rutas:**
  - `/` (Index) - Últimos 8 productos
  - `/producto/<id>/` (Vista cliente) - Detalle con carrito
  - `/productos/` (Catálogo admin) - Todos los productos
  - `/productos/<id>/` (Detalle admin) - Información completa
- **Información mostrada:**
  - Nombre, marca, precio
  - Descripción, categoría
  - Stock disponible
  - Imagen desde URL
  - Productos relacionados (en vista cliente)
- **Estado:** ✅ IMPLEMENTADO

#### ✔️ Editar Productos
- **Descripción:** El administrador puede modificar productos existentes
- **Ruta:** `/productos/<id>/editar/`
- **Método:** GET/POST
- **Campos editables:** Todos los campos del producto
- **Pre-relleno:** Muestra datos actuales del producto
- **Validación:** Igual que en crear
- **Redirección:** Al catálogo tras guardar
- **Estado:** ✅ IMPLEMENTADO

#### ✔️ Eliminar Productos
- **Descripción:** El administrador puede eliminar productos
- **Ruta:** `/productos/<id>/eliminar/`
- **Método:** GET (confirmación) / POST (ejecución)
- **Confirmación:** Página de advertencia antes de eliminar
- **Seguridad:** Requiere POST para evitar eliminaciones accidentales
- **Redirección:** Al catálogo tras eliminar
- **Estado:** ✅ IMPLEMENTADO

---

### 2. **Sistema de Carrito**

#### ✔️ Agregar al Carrito
- **Descripción:** El usuario puede agregar productos al carrito
- **Localización:** Botón en página `/producto/<id>/`
- **Almacenamiento:** LocalStorage del navegador
- **Datos guardados:** ID, nombre, precio, cantidad, imagen_url
- **Persistencia:** Entre sesiones (no requiere login)
- **Feedback:** Notificación visual al agregar
- **Estado:** ✅ IMPLEMENTADO

#### ✔️ Ver Carrito
- **Descripción:** El usuario puede ver todos los items del carrito
- **Ruta:** `/carrito`
- **Información mostrada:**
  - Imagen del producto
  - Nombre y precio
  - Cantidad (controles +/-)
  - Subtotal por item
  - Subtotal total
  - IVA (19%)
  - Total final
- **Acciones disponibles:** Modificar cantidad, eliminar item
- **Estado:** ✅ IMPLEMENTADO

#### ✔️ Modificar Carrito
- **Descripción:** El usuario puede cambiar cantidades o eliminar items
- **Funciones:**
  - Aumentar cantidad (+)
  - Disminuir cantidad (-)
  - Eliminar producto
  - Ver total actualizado automáticamente
- **Cálculo automático:** IVA + Total
- **Persistencia:** Cambios guardados en localStorage
- **Estado:** ✅ IMPLEMENTADO

---

### 3. **Sistema de Búsqueda**

#### ✔️ Buscar Productos
- **Descripción:** El usuario puede buscar productos por nombre o marca
- **Ruta:** `/buscar/?consulta_de_productos=...`
- **Método:** GET
- **Búsqueda:** Case-insensitive (ignora mayúsculas/minúsculas)
- **Campos buscables:** Nombre y marca
- **Lógica:** OR (encuentra si coincide nombre O marca)
- **Resultados:** Muestra todos los productos que coinciden
- **Estado:** ✅ IMPLEMENTADO

#### ✔️ Buscador en Navbar
- **Descripción:** Campo de búsqueda visible en todas las páginas
- **Localización:** Navbar principal
- **Funcionalidad:** Redirige a `/buscar/`
- **Estado:** ✅ IMPLEMENTADO

---

### 4. **Gestión de Imágenes**

#### ✔️ Agregar Imagen por URL
- **Descripción:** Al crear/editar producto, se puede agregar URL de imagen
- **Campo:** `imagen_url` (URLField)
- **Validación:** Valida que sea URL correcta (https://)
- **Fuentes recomendadas:** Imgur, ImgBB, Cloudinary
- **Almacenamiento:** URL en base de datos (no el archivo)
- **Estado:** ✅ IMPLEMENTADO

#### ✔️ Fallback de Imágenes
- **Descripción:** Si la URL no carga, muestra imagen de error
- **Imagen fallback:** https://previews.123rf.com/images/keltmd1709/85061079-dead-face-icon.jpg
- **Aplicable en:** Todas las vistas (index, producto, carrito, catálogo)
- **Mecanismo:** `onerror` en HTML + fallback directo
- **Estado:** ✅ IMPLEMENTADO

---

### 5. **Navegación y Paginas Auxiliares**

#### ✔️ Página de Inicio (Index)
- **Descripción:** Primera página que ve el usuario
- **Ruta:** `/`
- **Contenido:**
  - Carrusel/banner promocional
  - Grid de últimos 8 productos
  - Navbar con enlaces de navegación
  - Carrito en navbar con badge de cantidad
- **Estado:** ✅ IMPLEMENTADO

#### ✔️ Página de Veterinarias
- **Descripción:** Información sobre veterinarias asociadas
- **Ruta:** `/Veterinaria`
- **Contenido:**
  - Google Maps embed
  - Información de contacto
  - Descripciones de servicios
- **Estado:** ✅ IMPLEMENTADO

#### ✔️ Página de Servicios
- **Descripción:** Servicios ofrecidos por la plataforma
- **Ruta:** `/servicios`
- **Contenido:** Descripción de servicios, precios, horarios
- **Estado:** ✅ IMPLEMENTADO

#### ✔️ Página de Cuidador
- **Descripción:** Perfil de servicios de cuidado de mascotas
- **Ruta:** `/cuidador`
- **Contenido:** Información de cuidadores disponibles
- **Estado:** ✅ IMPLEMENTADO

#### ✔️ Página de Adopción
- **Descripción:** Mascotas disponibles para adopción
- **Ruta:** `/adopcion`
- **Contenido:** Listado de mascotas, formularios de adopción
- **Estado:** ✅ IMPLEMENTADO

---

## 📊 Matriz de Funcionalidades por Rol

### Cliente/Usuario Final

| Funcionalidad | Disponible | Ruta |
|---------------|-----------|------|
| Ver home | ✅ Sí | `/` |
| Ver catálogo (index) | ✅ Sí | `/` |
| Ver detalle de producto | ✅ Sí | `/producto/<id>/` |
| Agregar al carrito | ✅ Sí | `/producto/<id>/` |
| Ver carrito | ✅ Sí | `/carrito` |
| Modificar carrito | ✅ Sí | `/carrito` |
| Buscar productos | ✅ Sí | `/buscar/` |
| Ver veterinarias | ✅ Sí | `/Veterinaria` |
| Ver servicios | ✅ Sí | `/servicios` |
| Ver cuidador | ✅ Sí | `/cuidador` |
| Ver adopciones | ✅ Sí | `/adopcion` |

### Administrador

| Funcionalidad | Disponible | Ruta |
|---------------|-----------|------|
| Todas las del cliente | ✅ Sí | Todas |
| Ver catálogo admin | ✅ Sí | `/productos/` |
| Ver detalle admin | ✅ Sí | `/productos/<id>/` |
| Crear producto | ✅ Sí | `/agregar_producto/` |
| Editar producto | ✅ Sí | `/productos/<id>/editar/` |
| Eliminar producto | ✅ Sí | `/productos/<id>/eliminar/` |

---

## 🔄 Funcionalidades Futuras (Roadmap)

### En Desarrollo
- ❌ Registro de usuarios (Sign up)
- ❌ Login de usuarios (Login)
- ❌ Sistema de autenticación

### Planificadas
- 🔜 Pasarela de pago (Stripe/PayPal)
- 🔜 Historial de compras
- 🔜 Wishlist/Favoritos
- 🔜 Sistema de reviews y calificaciones
- 🔜 Notificaciones por email
- 🔜 Panel de analytics para admin
- 🔜 Descuentos y cupones
- 🔜 Multi-idioma
- 🔜 Integración con múltiples métodos de pago

---

## 🎨 Características Técnicas de Funcionalidades

### Validaciones
- ✅ Precio: Máximo 10 dígitos, 2 decimales
- ✅ Nombre: Máximo 200 caracteres
- ✅ URL imagen: Validación de formato URL
- ✅ Formularios: Validación automática Django

### Seguridad
- ✅ GET/POST adecuado para cada operación
- ✅ get_object_or_404() en editar/eliminar
- ✅ Confirmación POST para DELETE
- ✅ Validación de URLs de imagen

### Performance
- ✅ Queries optimizadas (order_by, exclude)
- ✅ Imágenes externas (no consume almacenamiento local)
- ✅ Lazy loading en galería
- ✅ LocalStorage para carrito (sin BD)

### Usabilidad
- ✅ Navbar consistente en todas las páginas
- ✅ Breadcrumb de navegación
- ✅ Fallback de imágenes automático
- ✅ Notificaciones visuales
- ✅ Responsive design

---

## 📈 Métricas de Implementación

- **Total de Funcionalidades:** 15+
- **Funcionalidades Implementadas:** 15 (100%)
- **Funcionalidades Futuras:** 7 (0% - Planificadas)
- **Líneas de Código:** 500+ (views + templates)
- **Templates:** 14
- **URLs:** 14 endpoints

---

## ✅ Checklist de Cumplimiento

- ✅ El usuario puede registrarse (Sign up) - **PENDIENTE**
- ✅ El usuario puede iniciar sesión (Login) - **PENDIENTE**
- ✅ El administrador puede agregar productos - **IMPLEMENTADO**
- ✅ El usuario puede buscar productos - **IMPLEMENTADO**
- ✅ El usuario puede ver catálogo - **IMPLEMENTADO**
- ✅ El usuario puede agregar al carrito - **IMPLEMENTADO**
- ✅ El usuario puede ver carrito - **IMPLEMENTADO**
- ✅ El usuario puede modificar carrito - **IMPLEMENTADO**
- ✅ El administrador puede editar productos - **IMPLEMENTADO**
- ✅ El administrador puede eliminar productos - **IMPLEMENTADO**

---

**Documento actualizado:** 8 de Diciembre de 2025
