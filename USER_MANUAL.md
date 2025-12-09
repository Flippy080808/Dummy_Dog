# 📚 Manual de Usuario - Dummy Dog

Guía visual y textual para usar todas las funciones de la aplicación Dummy Dog.

---

## 🎯 Inicio Rápido

### Acceder al Sitio

1. **Abre tu navegador** (Chrome, Firefox, Edge, Safari)
2. **Escribe en la barra de direcciones:** `http://localhost:8000/`
3. **Presiona Enter**

Deberías ver la **página de inicio** con productos de mascotas.

---

## 🏠 Página de Inicio (Home)

### ¿Qué ves?

```
┌────────────────────────────────────────────┐
│                                            │
│  🐶 DUMMY DOG                             │
│  [Inicio] [Veterinaria] [Servicios]      │
│  [Cuidador] [Adopción]        🛒 0 Items │
│                                            │
├────────────────────────────────────────────┤
│                                            │
│  📦 PRODUCTOS DESTACADOS (últimos 8)     │
│                                            │
│  [Producto 1]  [Producto 2]               │
│  [Producto 3]  [Producto 4]               │
│  [Producto 5]  [Producto 6]               │
│  [Producto 7]  [Producto 8]               │
│                                            │
│  Cada producto muestra:                   │
│  📷 Imagen                                │
│  📝 Nombre: "Croquetas Puppies"           │
│  🏷️  Marca: "Pedigri"                     │
│  💵 Precio: $25.99                        │
│  ⭐ [Ver Detalle]                         │
│                                            │
└────────────────────────────────────────────┘
```

### Acciones en Inicio

**[Ver Detalle]** - Abre la página del producto
- Ves descripción completa
- Puedes agregar al carrito
- Ves productos relacionados

**🛒 Carrito** - Ícono arriba a la derecha
- Muestra número de items
- Haz clic para abrir carrito

**Navegación superior**
- 🐶 **DUMMY DOG** - Vuelve a inicio
- **[Veterinaria]** - Página de veterinarios con mapa
- **[Servicios]** - Servicios disponibles
- **[Cuidador]** - Información del cuidador
- **[Adopción]** - Animales para adoptar

---

## 📦 Página de Producto (Customer View)

### Acceder

Haz clic en **[Ver Detalle]** desde el inicio.

### Contenido

```
┌────────────────────────────────────────────┐
│  [< Volver al inicio]                     │
├────────────────────────────────────────────┤
│                                            │
│  SECCIÓN PRINCIPAL                         │
│  ┌──────────────┐                         │
│  │              │   Nombre: Croquetas     │
│  │   Imagen     │   Puppies               │
│  │   del        │                         │
│  │   Producto   │   Marca: Pedigri       │
│  │              │                         │
│  │              │   Precio: $25.99        │
│  │              │   Stock: 150 unidades   │
│  │              │                         │
│  │              │   Categoría: Alimento   │
│  └──────────────┘                         │
│                   [Agregar al Carrito 🛒]│
│                   [Seguir Comprando 🔍]   │
│                                            │
├────────────────────────────────────────────┤
│                                            │
│  PRODUCTOS RELACIONADOS                    │
│  [Producto 1]  [Producto 2]  [Producto 3]│
│                                            │
└────────────────────────────────────────────┘
```

### Acciones

**[Agregar al Carrito 🛒]**
- Agrega el producto a tu carrito
- Se guarda automáticamente en el navegador
- Ves confirmación visual
- El contador del carrito aumenta

**[Seguir Comprando 🔍]**
- Abre la página de búsqueda
- Puedes buscar otros productos

**Productos Relacionados**
- Muestra 4 productos similares
- Haz clic para ver más detalles

---

## 🛒 Carrito de Compras

### Acceder

Haz clic en el **🛒 Carrito** arriba a la derecha.

### Contenido

```
┌──────────────────────────────────────────────┐
│                                              │
│  🛒 CARRITO DE COMPRAS                      │
│                                              │
│  Items en carrito: 3                         │
│                                              │
│  ┌──────────────────────────────────────┐  │
│  │ Producto          Cant. Precio Subtot│  │
│  ├──────────────────────────────────────┤  │
│  │ Croquetas         1    $25.99 $25.99│  │
│  │ [Eliminar]                           │  │
│  │                                      │  │
│  │ Juguete Pelota    2    $10.50 $21.00│  │
│  │ [Eliminar]                           │  │
│  │                                      │  │
│  │ Vitaminas         1    $35.99 $35.99│  │
│  │ [Eliminar]                           │  │
│  │                                      │  │
│  ├──────────────────────────────────────┤  │
│  │ TOTAL:                      $82.98  │  │
│  └──────────────────────────────────────┘  │
│                                              │
│  [Continuar Comprando]  [Checkout]         │
│                                              │
└──────────────────────────────────────────────┘
```

### Funciones

**[Eliminar]**
- Quita el producto del carrito
- Se actualiza automáticamente

**Actualizar Cantidad**
- Usa los botones + y - para cambiar cantidad
- Se actualiza el precio total

**[Continuar Comprando]**
- Vuelve a la búsqueda de productos
- Tu carrito se mantiene guardado

**[Checkout]** ⏳ Futuro
- En próximas versiones
- Para procesar el pago

### Datos del Carrito

- **Automático:** Se guarda en tu navegador (localStorage)
- **Persistente:** Se mantiene aunque cierres la página
- **Seguro:** Nadie más puede ver tu carrito (es solo tuyo)
- **Sin cuenta:** No necesitas registrarte

---

## 🔍 Búsqueda de Productos

### Acceder

1. Desde inicio: Haz clic en **[Seguir Comprando]**
2. O en navbar: Usa **[Buscar]** si está disponible
3. O escribe: `http://localhost:8000/buscar/`

### Interfaz

```
┌────────────────────────────────────┐
│                                    │
│  🔍 BUSCAR PRODUCTOS              │
│                                    │
│  [    Escribe aquí...     ]        │
│                                    │
│  [🔍 Buscar]                       │
│                                    │
│  Resultados: 3 productos encontrados
│                                    │
│  [Croquetas Pedigri]               │
│  [Vitaminas Premium]               │
│  [Juguete Pelota]                  │
│                                    │
└────────────────────────────────────┘
```

### Cómo Usar

1. **Escribe en el cuadro** lo que buscas:
   - Nombre: "Croquetas"
   - Marca: "Pedigri"
   - Parcial: "croqueta" o "pedi"

2. **Presiona Enter o haz clic en [Buscar]**

3. **Ves los resultados**
   - Se busca en nombre Y marca
   - No importa mayúsculas/minúsculas
   - Muestra coincidencias parciales

4. **Haz clic en un producto**
   - Abre la página de detalle
   - Puedes agregarlo al carrito

### Ejemplo

```
Buscas: "pedi"
Encuentra:
- Croquetas Pedigri
- Alimento Pedigri Premium
```

---

## 🔐 Panel de Administrador

### Acceder (Solo Admin)

1. Ve a: `http://localhost:8000/admin/`
2. Ingresa tu usuario y contraseña
3. Verás el panel Django

### Panel Admin

```
┌────────────────────────────────────┐
│  Django Administration             │
│                                    │
│  [Logout]                          │
│                                    │
│  Sitio: Núcleo                     │
│  ├─ Productos                      │
│  │  [+ Add Producto]               │
│  │  [Lista de Productos]           │
│  └─                                │
│                                    │
│  Autenticación y Autorización      │
│  ├─ Usuarios                       │
│  ├─ Grupos                         │
│  └─                                │
│                                    │
└────────────────────────────────────┘
```

---

## ➕ Agregar un Nuevo Producto (Admin)

### Opción 1: Desde Admin Panel

1. Panel Django → Nucleo → Productos → [+ Add]
2. Llena los campos:

```
Nombre *             [Croquetas Premium     ]
Marca                [Pedigri               ]
Precio *             [25.99                 ]
Inventario           [100                   ]
Categoría            [Alimento              ]
ID Veterinario       [1                     ]
Imagen URL           [https://example.com...] (opcional)
```

3. **[Save]** - Guardaa

### Opción 2: Desde Aplicación

1. URL: `http://localhost:8000/agregar_producto/`
2. O botón en navbar (si existe)
3. Mismos campos que arriba
4. **[Guardar]** botón

### Campos Explicados

```
Nombre *              Requerido. Ej: "Croquetas Puppies"
Marca                Opcional. Ej: "Pedigri"
Precio *             Requerido. Con decimales: 25.99
Inventario           Cantidad en stock. Ej: 150
Categoría            Tipo de producto: "Alimento", "Juguete", etc.
ID Veterinario       Para productos veterinarios (futuro)
Imagen URL           URL externa de imagen
                     Ej: https://example.com/foto.jpg
                     Si no pones, usa imagen por defecto
```

---

## ✏️ Editar un Producto (Admin)

### Acceder

1. **Desde Admin:**
   - Productos → Haz clic en el producto → [Edit]
   - O URL directo: `/productos/1/editar/`

2. **O desde la aplicación:**
   - Vista de productos admin
   - Botón [Editar]

### Página de Edición

```
┌──────────────────────────────────┐
│  EDITAR PRODUCTO                 │
│                                  │
│  [< Volver]                      │
│                                  │
│  Nombre *        [Croquetas...  ]│
│  Marca           [Pedigri       ]│
│  Precio *        [25.99         ]│
│  Inventario      [100           ]│
│  Categoría       [Alimento      ]│
│  ID Veter.       [1             ]│
│  Imagen URL      [https://...   ]│
│                                  │
│  [Guardar Cambios] [Cancelar]    │
│                                  │
└──────────────────────────────────┘
```

### Cambiar Imagen

Para **cambiar la imagen:**

1. Abre la URL de tu nueva imagen en navegador
2. Cópiala: `https://ejemplo.com/nueva-imagen.jpg`
3. Pégala en el campo **Imagen URL**
4. **[Guardar Cambios]**

**Importante:** La imagen debe tener una URL válida (comenzar con http:// o https://)

---

## 🗑️ Eliminar un Producto (Admin)

### Acceder

1. **Desde Admin:**
   - Productos → Producto → [Delete]

2. **Desde App:**
   - Página de producto admin
   - Botón [Eliminar]
   - O URL: `/productos/1/eliminar/`

### Confirmación

```
┌────────────────────────────────┐
│                                │
│  ⚠️  ¿CONFIRMAR ELIMINACIÓN?   │
│                                │
│  Vas a eliminar:               │
│  "Croquetas Puppies - Pedigri" │
│                                │
│  Esta acción NO se puede deshacer
│                                │
│  [Cancelar]  [Eliminar Producto]
│                                │
└────────────────────────────────┘
```

### Pasos

1. Ves el producto que vas a eliminar
2. Haz clic en **[Eliminar Producto]** para confirmar
3. El producto desaparece del carrito y catálogo
4. **NO se puede recuperar**

---

## 📋 Ver Todos los Productos (Admin)

### Acceder

1. URL: `http://localhost:8000/productos/`
2. O navbar: **[Productos]** (si existe)

### Vista de Administrador

```
┌──────────────────────────────────────┐
│  CATÁLOGO DE PRODUCTOS               │
│                                      │
│  [+ Agregar Producto]                │
│                                      │
│  Ordenados por: Nombre ↑             │
│                                      │
│  [Producto 1] [Editar] [Eliminar]    │
│  [Producto 2] [Editar] [Eliminar]    │
│  [Producto 3] [Editar] [Eliminar]    │
│  [Producto 4] [Editar] [Eliminar]    │
│  [Producto 5] [Editar] [Eliminar]    │
│                                      │
└──────────────────────────────────────┘
```

### Acciones

- **Haz clic en producto** → Ver detalle admin
- **[Editar]** → Cambiar información
- **[Eliminar]** → Confirmar eliminación
- **[+ Agregar]** → Nuevo producto

---

## 🗺️ Otras Páginas

### Veterinaria

```
http://localhost:8000/Veterinaria

✓ Información de veterinarios
✓ Ubicación en mapa Google Maps
✓ Datos de contacto
✓ Horarios de atención
```

### Servicios

```
http://localhost:8000/servicios

✓ Lista de servicios disponibles
✓ Descripción de cada servicio
✓ Precios de servicios
✓ Cómo solicitar
```

### Cuidador

```
http://localhost:8000/cuidador

✓ Perfiles de cuidadores
✓ Experiencia y especialidades
✓ Calificaciones
✓ Cómo contratarlos
```

### Adopción

```
http://localhost:8000/adopcion

✓ Animales disponibles para adoptar
✓ Información de cada animal
✓ Fotos
✓ Cómo adoptar
```

---

## 💡 Consejos y Trucos

### Guardar el Carrito

```
✓ El carrito se guarda automáticamente
✓ Abre el navegador developer (F12)
✓ Sección "Application" → "localStorage"
✓ Busca "dummy_dog_cart"
✓ Puedes verlo en formato JSON
```

### Borrar el Carrito

```
Si quieres empezar de nuevo:
1. F12 → Application
2. localStorage
3. Busca "dummy_dog_cart"
4. Haz clic derecho → Delete
5. Recarga la página
```

### Cambiar Tema (CSS)

El sitio usa **variables CSS**. En `static/global.css`:

```css
--primary-green: #4CE64C;    /* Verde principal */
--yellow: #FCFA86;            /* Amarillo */
--blue: #3483fa;              /* Azul */
--text-dark: #333333;         /* Texto oscuro */
--bg-light: #f5f5f5;          /* Fondo claro */
```

Cambialos para modificar los colores de toda la app.

### Imágenes Que No Cargan

Si una imagen no se carga:

1. **Verifica la URL:**
   - Debe comenzar con `http://` o `https://`
   - Debe ser accesible en el navegador

2. **Si la URL es inválida:**
   - Se muestra imagen fallback (paw emoji)
   - Puedes cambiarla en editar producto

---

## 🎨 Personalización (Para Desarrolladores)

### Cambiar Logo

En `templates/base.html`:

```html
<!-- Busca: -->
<h1 class="navbar-brand">🐶 DUMMY DOG</h1>

<!-- Cambia a: -->
<h1 class="navbar-brand">🦮 MI TIENDA PET</h1>
```

### Agregar Nueva Página

1. Crea función en `views.py`
2. Agrega ruta en `urls.py`
3. Crea template en `templates/`
4. Enlaza en navbar

---

## ❓ Preguntas Frecuentes

### ¿Cómo agrego muchos productos rápido?

Admin → Productos → Importar/Bulk create (futuro)
Por ahora: agregar uno por uno

### ¿Puedo cambiar la moneda?

Sí, en el template. Busca `$` y cambia a `€`, `£`, `₡`, etc.

### ¿Cómo hago reportes de ventas?

Todavía no. En roadmap para próximas versiones.

### ¿Puedo ver si el cliente compró?

El carrito es solo frontend. Para ver órdenes necesitas integración backend (futuro).

### ¿Las imágenes se cargan siempre?

Depende de:
- Que la URL sea válida
- Que el sitio de la imagen esté activo
- Tu conexión a internet

Si una falla, se muestra imagen fallback (🐾 paw)

---

**Última actualización:** 8 de Diciembre de 2025

¿Necesitas ayuda? Consulta la sección **Soporte** en INSTALLATION_GUIDE.md
