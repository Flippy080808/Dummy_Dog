# 📋 Bitácora de Cambios - Dummy Dog

Registro completo de todos los cambios, mejoras y correcciones realizadas en la aplicación Dummy Dog.

---

## [v1.2.0] - 8 de Diciembre de 2025

### ✅ Añadido
- **Sistema de Imágenes por URL:** Nuevo campo `imagen_url` en el modelo Producto
- **Fallback de Imágenes:** Sistema automático de respaldo cuando la URL no carga
- **Formularios Mejorados:** Campo para URL de imagen en agregar_productos.html y editar_producto.html
- **Bitácora de Cambios:** Este archivo (CHANGELOG.md) para registro histórico

### 🔧 Arreglado
- ✅ Imágenes no cargaban en `/productos` (productos_list.html)
- ✅ Fallback inconsistente entre templates
- ✅ Placeholder genérico ahora reemplazado por imagen 123rf unificada

### 📝 Modificado
- **Navbar:** Removido enlace "Productos" de todas las vistas (solo accesible desde "➕ Agregar")
- **Templates actualizados:**
  - `index.html` - Ahora usa `imagen_url` con fallback
  - `producto.html` - Imagen mejorada con fallback 123rf
  - `producto_detail.html` - Imagen admin con fallback
  - `productos_list.html` - Imagen catálogo admin con fallback
  - `carrito.html` - Imágenes de items con fallback
  - `agregar_productos.html` - Campo URL de imagen agregado
  - `editar_producto.html` - Campo URL de imagen agregado

### 📋 Documentación
- Actualizado `TECHNICAL_DOCUMENTATION.md` con cambios recientes
- Crear `CHANGELOG.md` (este archivo) para registro histórico
- Actualizado `README.md` con sección de imágenes por URL

---

## [v1.1.0] - 8 de Diciembre de 2025

### ✅ Añadido
- **Sistema de Imágenes por URL:** Campo `imagen_url` en Producto model
- **Carrito Mejorado:** Ahora soporta imágenes desde URLs externas
- **Documentación Técnica:** Archivo TECHNICAL_DOCUMENTATION.md creado

### 🔧 Arreglado
- CSS no cargaba correctamente en templates (implementó {% static %})
- Productos no mostraban desde índice (cambió de API a consultas BD)

### 📝 Modificado
- **forms.py:** Agregó widgets personalizados a ProductoForm
- **models.py:** Nuevo campo URLField para imágenes
- **views.py:** Mejoras en queries para performance
- **Migración:** 0002_producto_imagen_url.py creada

---

## [v1.0.0] - Inicios de Diciembre de 2025

### ✅ Añadido
- **Sistema CRUD completo:** Create, Read, Update, Delete para productos
- **Carrito de Compras:** Implementado con localStorage (client-side)
- **Catálogo de Productos:** Dos vistas (cliente y admin)
- **Búsqueda:** Sistema de búsqueda por nombre o marca
- **Autenticación:** Páginas auxiliares (veterinaria, servicios, adopción, cuidador)
- **Responsive Design:** Compatible móvil, tablet, desktop
- **Google Maps:** Integración en página de veterinarias

### 🔧 Arreglado
- Problemas de rutas (configuró urls.py con patrones correctos)
- Ordenamiento de productos (order_by('-id_product'))
- Conflictos entre vistas (separó cliente vs admin)

### 📝 Modificado
- **Estructura:** Creó app Nucleo dentro del proyecto DummyDog
- **Templates:** 14 templates HTML creados
- **Static:** CSS global y específicos para cada página
- **Database:** Modelo Producto con 7 campos iniciales

### 🎨 Diseño
- Color scheme implementado (verde, amarillo, azul)
- Bootstrap 5.3.3 integrado
- CSS variables para fácil personalización
- Navbar consistente en todas las páginas

---

## Patrones de Versiones

```
[v MAYOR.MENOR.PATCH] - DD de Mes de Año

MAYOR: Cambios grandes de funcionalidad
MENOR: Nuevas características o mejoras
PATCH: Fixes/correcciones
```

---

## Categorías de Cambios

- **✅ Añadido:** Nuevas características
- **🔧 Arreglado:** Bugs corregidos
- **📝 Modificado:** Cambios en funcionalidad existente
- **❌ Removido:** Características deprecadas
- **⚠️ Seguridad:** Fixes de seguridad
- **📋 Documentación:** Cambios en docs

---

## Cambios Próximos (Roadmap)

- 🔜 Integración de pasarela de pago (Stripe/PayPal)
- 🔜 Sistema de autenticación de usuarios
- 🔜 Historial de compras
- 🔜 Wishlist/Favoritos
- 🔜 Sistema de reviews y calificaciones
- 🔜 Notificaciones por email
- 🔜 Panel de analytics para admin
- 🔜 Descuentos y cupones
- 🔜 Multi-idioma
- 🔜 Soporte a múltiples formatos de pago

---

## Notas de Desarrollo

### Decisiones de Diseño Importantes:

1. **URLs por Query String:**
   - Carrito: Almacenado en `localStorage` (no BD)
   - Motivo: Escalabilidad, sin requerir login
   - Alternativa considerada: Sesiones Django (descartada por complejidad)

2. **Imágenes Externas:**
   - URLs en lugar de archivos locales
   - Motivo: Ahorro de almacenamiento en host (PythonAnywhere)
   - Fallback: Imagen 123rf unificada

3. **Dos Vistas de Producto:**
   - Cliente (`/producto/<pk>/`): Con carrito
   - Admin (`/productos/<pk>/`): Con editar/eliminar
   - Motivo: Separación clara cliente vs admin

4. **Bootstrap 5.3.3:**
   - Usado para componentes base (navbar, form, grid)
   - Personalizado con CSS variables para brand consistency

### Testing Manual Realizado:

✅ Creación de productos (POST)
✅ Lectura de productos (GET)
✅ Edición de productos (PUT)
✅ Eliminación de productos (DELETE)
✅ Búsqueda case-insensitive
✅ Carrito persistencia (localStorage)
✅ Imágenes URL válidas
✅ Fallback de imágenes
✅ Responsive en móvil/tablet/desktop
✅ Navbar consistente

---

## Autores y Créditos

- **Jose FDA** - Formularios y gestión CRUD
- **Alberto GJ** - Vistas y lógica principal  
- **Emily VQ** - Templates y diseño UI/UX
- **Equipo Dummy Dog** - Mantenimiento general

---

## Licencia

Este proyecto es de código abierto y puede ser utilizado libremente.

---

**Última Actualización:** 8 de Diciembre de 2025 - v1.2.0
