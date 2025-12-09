# 📚 Documentación Técnica - Dummy Dog

Descripción técnica detallada de todas las funciones de la aplicación, ordenadas por importancia y complejidad.

---

## 🔄 Cambios Recientes

### Actualización: Imágenes en Vista Admin (Diciembre 2025)
- ✅ **producto_detail.html** ahora utiliza `imagen_url` en lugar de placeholder fijo
- ✅ Sistema de fallback: si la URL no carga, usa placeholder automáticamente
- ✅ Consistencia: todas las vistas (index, producto, carrito, producto_detail) ahora soportan imágenes externas

### Actualización: Productos List y Fallback Mejorado (Diciembre 2025)
- ✅ **productos_list.html** (catálogo admin) ahora utiliza `imagen_url` 
- ✅ **Fallback unificado:** Todos los templates ahora usan la imagen 123rf en lugar de placeholder
- ✅ **Imagen de error:** https://previews.123rf.com/images/keltmd1709/85061079-dead-face-icon.jpg
- ✅ **Aplicado en:** index.html, producto.html, producto_detail.html, productos_list.html, carrito.html

**Nota técnica:** El fallback se aplica tanto en el atributo `src` como en el evento `onerror` para máxima compatibilidad. La URL de error 123rf es consistente en todos los lugares para mantener marca visual uniforme.

---

## 🏆 Funciones Principales (Núcleo del Sistema)

### 1. **index(request)** - Página de Inicio
**Archivo:** `views.py`  
**Ruta:** `/`  
**Complejidad:** ⭐⭐ (Media)  
**Importancia:** 🔴 CRÍTICA

#### Descripción:
Función que carga la página de inicio con los últimos 8 productos agregados a la base de datos. Esta es la primera página que ve el usuario.

#### Código:
```python
def index(request):
    # Obtener productos de la base de datos
    productos = Producto.objects.all().order_by('-id_product')[:8]  # Últimos 8 productos
    return render(request, "index.html", {"productos": productos})
```

#### Técnica:
- **`Producto.objects.all()`** - Obtiene todos los registros de la tabla Producto
- **`.order_by('-id_product')`** - Ordena descendente por ID (más nuevos primero)
- **`[:8]`** - Limita a solo 8 productos (slicing de Python)
- **`render()`** - Renderiza el template HTML con el contexto

#### Flujo:
1. Usuario accede a `/`
2. Se ejecuta `index(request)`
3. Se consultan los últimos 8 productos de BD
4. Se pasan al template `index.html`
5. Se renderiza la página con los productos

#### Variables de Contexto:
- `productos`: Lista de objetos Producto (máximo 8)

#### Relaciones:
- Consume: `Producto` model
- Usa: `index.html` template
- Invocado desde: URL principal

---

### 2. **producto(request, pk=None)** - Página de Detalle (Cliente)
**Archivo:** `views.py`  
**Rutas:** `/producto/` y `/producto/<int:pk>/`  
**Complejidad:** ⭐⭐⭐ (Alta)  
**Importancia:** 🔴 CRÍTICA

#### Descripción:
Función que muestra el detalle de un producto específico con opción de compra. Es la interfaz que usa el cliente/usuario final para ver productos y agregarlos al carrito.

#### Código:
```python
def producto(request, pk=None):
    if pk:
        producto = get_object_or_404(Producto, pk=pk)
        # Obtener productos relacionados (otros productos, excluir el actual)
        productos_relacionados = Producto.objects.exclude(pk=pk)[:4]
        return render(request, 'producto.html', {
            'producto': producto,
            'productos_relacionados': productos_relacionados
        })
    else:
        # Si no hay pk, mostrar el último producto agregado
        producto = Producto.objects.order_by('-id_product').first()
        if producto:
            productos_relacionados = Producto.objects.exclude(pk=producto.pk)[:4]
            return render(request, 'producto.html', {
                'producto': producto,
                'productos_relacionados': productos_relacionados
            })
        else:
            return render(request, 'producto.html', {'producto': None})
```

#### Técnica:
- **`get_object_or_404(Producto, pk=pk)`** - Obtiene producto por ID o retorna 404
- **`Producto.objects.exclude(pk=pk)`** - Obtiene todos MENOS el producto actual
- **`[:4]`** - Limita a 4 productos relacionados (recomendaciones)
- **`.order_by('-id_product').first()`** - Obtiene el más reciente si no hay pk
- **Condicional `if pk`** - Diferencia entre ruta con y sin parámetro

#### Flujo:
1. Usuario hace clic en un producto desde `index.html`
2. Se redirige a `/producto/123/` (donde 123 es el pk)
3. Se ejecuta `producto(request, pk=123)`
4. Se obtiene el producto y 4 relacionados
5. Se renderiza `producto.html` con toda la información
6. Usuario ve: descripción, precio, botón "Agregar al carrito", productos relacionados

#### Variables de Contexto:
- `producto`: Objeto Producto específico
- `productos_relacionados`: Lista de 4 productos (para recomendaciones)

#### Casos de Uso:
- **Con pk:** Desde `index.html` → `/producto/123/`
- **Sin pk:** Acceso directo a `/producto/` → muestra el más reciente

#### Relaciones:
- Consume: `Producto` model
- Usa: `producto.html` template
- Invocado desde: `index.html`, URLs directas
- Valida: `get_object_or_404` (seguridad)

#### JavaScript Integrado:
El template usa localStorage para guardar productos al carrito:
```javascript
document.querySelector('[data-add-to-cart]').addEventListener('click', () => {
  const product = {
    id_product: {{ producto.pk }},
    nombre: "{{ producto.nombre }}",
    precio: "{{ producto.precio }}",
    imagen_url: "{{ producto.imagen_url }}"
  };
  // Guardar en localStorage
});
```

---

### 3. **crear_producto(request)** - Formulario de Creación (CRUD - CREATE)
**Archivo:** `views.py`  
**Ruta:** `/agregar_producto/`  
**Complejidad:** ⭐⭐⭐ (Alta)  
**Importancia:** 🔴 CRÍTICA

#### Descripción:
Función que maneja la creación de nuevos productos. Procesa tanto GET (mostrar formulario) como POST (guardar datos). Usa `ProductoForm` para validación automática.

#### Código:
```python
# Autor Alberto GJ
def crear_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('productos_list')
    else:
        form = ProductoForm()
    return render(request, 'agregar_productos.html', {'form': form})
```

#### Técnica:
- **`request.method == 'POST'`** - Diferencia GET de POST
- **`ProductoForm(request.POST)`** - Vincula datos POST al formulario
- **`form.is_valid()`** - Valida campos (longitud, tipos, requeridos)
- **`form.save()`** - Guarda directamente en BD (sin lógica manual)
- **`redirect('productos_list')`** - Redirige tras guardado exitoso

#### Validaciones Automáticas (por ProductoForm):
- `nombre`: CharField obligatorio (max 200)
- `marca`: CharField opcional (max 100)
- `precio`: DecimalField (máx 10 dígitos, 2 decimales)
- `inventario`: IntegerField
- `categoria`: CharField opcional
- `id_veter`: IntegerField opcional
- `imagen_url`: URLField (valida formato URL)

#### Flujo HTTP:
```
GET /agregar_producto/
  ↓
view crea ProductoForm()
  ↓
Renderiza agregar_productos.html con form vacío
  ↓
Usuario llena campos y hace submit
  ↓
POST /agregar_producto/
  ↓
form = ProductoForm(request.POST) - vincula datos
  ↓
if form.is_valid() - valida
  ↓
form.save() - INSERT en BD
  ↓
redirect a /productos/ (catálogo admin)
```

#### Variables de Contexto:
- `form`: Instancia de ProductoForm (vacía o con errores)

#### Errores Posibles:
- Precio con más de 10 dígitos → form.is_valid() = False
- URL inválida en imagen_url → form.is_valid() = False
- Campo nombre vacío → form.is_valid() = False

#### SQL Generado:
```sql
INSERT INTO Nucleo_producto 
  (nombre, marca, precio, inventario, categoria, id_veter, imagen_url)
VALUES 
  (%s, %s, %s, %s, %s, %s, %s)
```

---

### 4. **editar_producto(request, pk)** - Formulario de Edición (CRUD - UPDATE)
**Archivo:** `views.py`  
**Ruta:** `/productos/<int:pk>/editar/`  
**Complejidad:** ⭐⭐⭐ (Alta)  
**Importancia:** 🔴 CRÍTICA

#### Descripción:
Función que permite modificar un producto existente. Similar a `crear_producto`, pero pre-rellena los datos actuales. Usa `instance=producto` para vincular con registro específico.

#### Código:
```python
# UPDATE - Editar producto
def editar_producto(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    if request.method == 'POST':
        form = ProductoForm(request.POST, instance=producto)
        if form.is_valid():
            form.save()
            return redirect('productos_list')
    else:
        form = ProductoForm(instance=producto)
    return render(request, 'editar_producto.html', {'form': form, 'producto': producto})
```

#### Técnica:
- **`get_object_or_404(Producto, pk=pk)`** - Obtiene el producto o muestra 404
- **`ProductoForm(request.POST, instance=producto)`** - Vincula TANTO datos POST como objeto actual
- **`form.save()`** - Actualiza (porque tiene instance) en lugar de insertar

#### Diferencia con crear_producto:
```
crear_producto:          editar_producto:
ProductoForm()           ProductoForm(instance=producto)
     ↓                              ↓
   Vacío                      Pre-relleno
     ↓                              ↓
form.save()              form.save() → UPDATE
     ↓                              ↓
INSERT                          UPDATE
```

#### Flujo HTTP:
```
GET /productos/123/editar/
  ↓
Obtiene producto pk=123
  ↓
Crea form = ProductoForm(instance=producto)
  ↓
Renderiza con datos previos
  ↓
Usuario modifica y submit
  ↓
POST /productos/123/editar/
  ↓
form = ProductoForm(request.POST, instance=producto)
  ↓
form.is_valid() ✓
  ↓
form.save() → UPDATE en BD
  ↓
redirect a /productos/
```

#### SQL Generado:
```sql
UPDATE Nucleo_producto 
SET nombre=%s, marca=%s, precio=%s, inventario=%s, 
    categoria=%s, id_veter=%s, imagen_url=%s
WHERE id_product=%s
```

#### Casos de Uso:
- Cambiar precio de producto
- Actualizar imagen_url
- Modificar stock disponible
- Cambiar categoría

---

### 5. **eliminar_producto(request, pk)** - Confirmación de Eliminación (CRUD - DELETE)
**Archivo:** `views.py`  
**Ruta:** `/productos/<int:pk>/eliminar/`  
**Complejidad:** ⭐⭐ (Media)  
**Importancia:** 🔴 CRÍTICA

#### Descripción:
Función que maneja la eliminación de productos. Requiere confirmación POST para evitar eliminaciones accidentales por robots o clicks errados. Implementa patrón "GET para confirmar, POST para ejecutar".

#### Código:
```python
# DELETE - Eliminar producto
def eliminar_producto(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    if request.method == 'POST':
        producto.delete()
        return redirect('productos_list')
    return render(request, 'confirmar_eliminar.html', {'producto': producto})
```

#### Técnica:
- **`get_object_or_404()`** - Valida existencia antes de intentar eliminar
- **`producto.delete()`** - Elimina registro y relacionados (cascada)
- **Condicional `if request.method == 'POST'`** - Patrón de confirmación

#### Patrón GET vs POST:
```
GET /productos/123/eliminar/
  ↓
Renderiza confirmar_eliminar.html con aviso
  ↓
Usuario ve: "¿Está seguro?" + botones Sí/No
  ↓
Si hace click "Sí":
  ↓
POST /productos/123/eliminar/
  ↓
Ejecuta delete()
  ↓
redirect a /productos/
```

#### Por qué no eliminar en GET:
- GET debe ser **idempotente** (no cambiar datos)
- Los buscadores indexan URLs GET
- Evita eliminaciones accidentales
- Cumple con HTTP standards

#### SQL Generado:
```sql
DELETE FROM Nucleo_producto WHERE id_product = %s
```

#### Restricciones de Base de Datos:
- Si hay relaciones con `id_veter`, Django maneja cascada según ForeignKey
- En este caso, `id_veter` es solo IntegerField, no ForeignKey, así que no hay restricciones

---

## 📋 Funciones de Lectura (READ)

### 6. **lista_productos(request)** - Catálogo Administrativo
**Archivo:** `views.py`  
**Ruta:** `/productos/`  
**Complejidad:** ⭐ (Baja)  
**Importancia:** 🟡 IMPORTANTE

#### Descripción:
Muestra todos los productos ordenados alfabéticamente. Interfaz administrativa con botones Editar/Eliminar para cada producto.

#### Código:
```python
# READ - Lista de productos
def lista_productos(request):
    productos = Producto.objects.all().order_by('nombre')
    return render(request, 'productos_list.html', {'productos': productos})
```

#### Técnica:
- **`Producto.objects.all()`** - SELECT * FROM Nucleo_producto
- **`.order_by('nombre')`** - Ordena alfabético ascendente (A→Z)

#### SQL Generado:
```sql
SELECT * FROM Nucleo_producto ORDER BY nombre ASC
```

#### Diferencia con index():
| Función | orden_by | Cantidad | Template | Usar |
|---------|----------|----------|----------|------|
| index | -id_product (nuevo primero) | 8 | index.html | Cliente: primeros productos |
| lista_productos | nombre (A-Z) | Todos | productos_list.html | Admin: gestión CRUD |

#### Variables de Contexto:
- `productos`: QuerySet con todos los productos

---

### 7. **detalle_producto(request, pk)** - Página de Detalle (Admin)
**Archivo:** `views.py`  
**Ruta:** `/productos/<int:pk>/`  
**Complejidad:** ⭐⭐ (Media)  
**Importancia:** 🟡 IMPORTANTE

#### Descripción:
Muestra el detalle de un producto con botones administrativos (Editar/Eliminar). Diferente de `producto()` que es para clientes. Esta es la versión admin.

#### Código:
```python
# READ - Detalle de producto
def detalle_producto(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    return render(request, 'producto_detail.html', {'producto': producto})
```

#### Técnica:
- **`get_object_or_404(Producto, pk=pk)`** - SELECT con validación

#### SQL Generado:
```sql
SELECT * FROM Nucleo_producto WHERE id_product = %s LIMIT 1
```

#### Flujo:
```
Click en producto desde /productos/
  ↓
GET /productos/123/
  ↓
Obtiene producto (SELECT)
  ↓
Renderiza producto_detail.html
  ↓
Muestra: info + botones [Editar] [Eliminar]
```

#### Diferencia producto() vs detalle_producto():
```
producto(pk):              detalle_producto(pk):
Para: CLIENTE              Para: ADMIN
URL: /producto/123/        URL: /productos/123/
Template: producto.html    Template: producto_detail.html
Botones: [Carrito]         Botones: [Editar] [Eliminar]
Relacionados: Sí (4)       Relacionados: No
Carrito JS: Sí             Carrito JS: No
Imágenes: imagen_url       Imágenes: imagen_url (igual)
```

#### Manejo de Imágenes:
Ambos templates (`producto.html` y `producto_detail.html`) implementan el mismo sistema:
- **Si existe `imagen_url`:** Carga la imagen desde la URL externa
- **Si la URL falla:** Fallback automático a imagen 123rf con `onerror`
- **Si no existe `imagen_url`:** Usa imagen 123rf directo

#### URL de Fallback:
```
https://previews.123rf.com/images/keltmd/keltmd1709/keltmd170900112/85061079-dead-face-icon-in-outline-style-vector-illustration-for-design-and-web-isolated-on-white-background.jpg
```
Esta imagen se usa consistentemente en TODOS los templates cuando:
- URL no existe o está vacía
- URL falla al cargar (timeout, 404, error de servidor)
- Proporciona feedback visual consistente al usuario

---

## 🖼️ Sistema de Imágenes (Detalle Técnico)

### Arquitectura de Imágenes

Dummy Dog implementa un sistema de imágenes basado en **URLs externas** sin almacenar archivos locales.

#### Estructura de Fallback:

```
┌─ Usuario solicita producto
│
├─ ¿Existe imagen_url? 
│  ├─ SÍ → Intenta cargar desde URL
│  │      ├─ ✅ Carga OK → Muestra imagen
│  │      └─ ❌ Error → Ejecuta onerror
│  │
│  └─ NO → Carga fallback directo
│
└─ Fallback: Imagen 123rf (feedback visual)
```

### URLs de Fallback por Template:

| Template | Ruta | Fallback | Comportamiento |
|----------|------|----------|----------------|
| index.html | `/` | 123rf | Carga directo si no existe URL |
| producto.html | `/producto/<pk>/` | 123rf | onerror + fallback directo |
| producto_detail.html | `/productos/<pk>/` | 123rf | onerror + fallback directo |
| productos_list.html | `/productos/` | 123rf | Carga directo si no existe URL |
| carrito.html | `/carrito` | 123rf | JavaScript valida con \|\| |

### Implementación en Templates:

#### Patrón 1: Con condicional (HTML/Django)
```html
{% if producto.imagen_url %}
  <img src="{{ producto.imagen_url }}" 
       onerror="this.src='[URL_FALLBACK]'">
{% else %}
  <img src="[URL_FALLBACK]">
{% endif %}
```

#### Patrón 2: Con JS (Carrito - localStorage)
```javascript
src="${item.imagen_url || '[URL_FALLBACK]'}"
```

### Por qué URL 123rf:

1. **Consistencia visual:** Misma imagen de error en toda la app
2. **Indicador claro:** Usuario entiende que la imagen no cargó
3. **Permanente:** No desaparece (a diferencia de placeholder.com)
4. **Branding:** Mantiene identidad visual de la app
5. **Licencia:** Uso permitido para propósitos educativos

### Manejo de Errores:

```javascript
// Evento onerror en img tags
onerror="this.src='https://previews.123rf.com/...'"

// Alternativa: JavaScript manual
img.onerror = function() {
  this.src = 'https://previews.123rf.com/...';
}
```

### Optimizaciones de Carga:

```html
<!-- En index.html -->
<img ... loading="lazy">  <!-- Carga perezosa para performance -->

<!-- En carrito (JS) -->
const imageUrl = item.imagen_url || fallbackUrl;  <!-- Valida antes -->
```

---

### 8. **buscar_productos(request)** - Sistema de Búsqueda
**Archivo:** `views.py`  
**Ruta:** `/buscar/?consulta_de_productos=...`  
**Complejidad:** ⭐⭐ (Media)  
**Importancia:** 🟡 IMPORTANTE

#### Descripción:
Busca productos por nombre o marca usando queries case-insensitive. Implementa búsqueda OR (encuentra si coincide NOMBRE O MARCA).

#### Código:
```python
# Autor Jose FDA
def buscar_productos(request):
    q = request.GET.get('consulta_de_productos', '')
    resultados = []
    if q:
        resultados = Producto.objects.filter(
            nombre__icontains=q
        ) | Producto.objects.filter(
            marca__icontains=q
        )
    return render(request, 'buscar.html', {'resultados': resultados})
```

#### Técnica:
- **`request.GET.get('consulta_de_productos', '')`** - Obtiene parámetro query string
- **`nombre__icontains=q`** - "icontains" = case-insensitive contains (i=insensitive)
- **`|` operador** - OR en Django ORM (union de QuerySets)

#### SQL Generado:
```sql
SELECT * FROM Nucleo_producto 
WHERE nombre LIKE %q% 
OR marca LIKE %q%
```

#### Ejemplos:
```
Búsqueda: "alimento"
Encuentra:
  - "Alimento Premium" (coincide nombre)
  - "ALIMENTO Gato" (case-insensitive)
  - Cualquier marca "XYZ Alimento"

Búsqueda: "pedigri"
Encuentra:
  - Cualquier producto con marca "Pedigri"
  - "Croquetas Pedigri"
```

#### Flujo:
```
Usuario tipea en buscador y presiona buscar
  ↓
GET /buscar/?consulta_de_productos=alimento
  ↓
q = "alimento"
  ↓
Ejecuta búsqueda:
  - filter(nombre__icontains="alimento")
  - filter(marca__icontains="alimento")
  ↓
Retorna union de ambas
  ↓
Renderiza buscar.html con resultados
```

#### Variables de Contexto:
- `resultados`: QuerySet de productos que coinciden (puede estar vacío)

---

### 9. **carrito(request)** - Página del Carrito
**Archivo:** `views.py`  
**Ruta:** `/carrito`  
**Complejidad:** ⭐ (Baja)  
**Importancia:** 🟡 IMPORTANTE

#### Descripción:
Renderiza la página del carrito. El carrito es **100% JavaScript/localStorage** en el cliente, esta función solo sirve para mostrar el template.

#### Código:
```python
def carrito(request):
    return render(request, 'carrito.html')
```

#### Técnica:
- Simple pass-through (no lógica en servidor)
- Todo el manejo se hace en JavaScript del cliente

#### Funcionamiento del Carrito (Client-Side):
```javascript
// localStorage key
'dummy_dog_cart' = [
  {
    id_product: 1,
    nombre: "Croquetas",
    precio: "25.99",
    quantity: 2,
    imagen_url: "https://..."
  }
]

// Operaciones:
- ADD: JSON.stringify(product)
- REMOVE: filter()
- UPDATE QTY: map()
- GET TOTAL: reduce()
```

#### Por qué Client-Side:
✅ No consume espacio BD  
✅ No requiere login  
✅ Persiste entre sesiones  
✅ Presión nula en servidor  

#### Flujo:
```
Usuario clicks [Agregar al carrito]
  ↓
JavaScript captura evento
  ↓
Guarda en localStorage
  ↓
Actualiza navbar badge
  ↓
Usuario va a /carrito
  ↓
Renderiza carrito.html
  ↓
JavaScript recupera localStorage
  ↓
Muestra items + total
```

---

### 10. **veter(request)** - Página de Veterinarias
**Archivo:** `views.py`  
**Ruta:** `/Veterinaria`  
**Complejidad:** ⭐ (Muy Baja)  
**Importancia:** 🟢 AUXILIAR

#### Descripción:
Renderiza página de veterinarias con Google Maps embed. No consulta BD, solo muestra HTML estático.

#### Código:
```python
def veter(request):
    return render(request, 'veter.html')
```

#### Features:
- Google Maps embed
- Información de contacto
- Enlaces a reservas
- Descripción de servicios

---

### 11. **serv(request)** - Página de Servicios
**Archivo:** `views.py`  
**Ruta:** `/servicios`  
**Complejidad:** ⭐ (Muy Baja)  
**Importancia:** 🟢 AUXILIAR

#### Código:
```python
def serv(request):
    return render(request, 'serv.html')
```

#### Contenido:
- Descripción de servicios
- Precios
- Horarios
- Contacto

---

### 12. **cuidador(request)** - Página de Perfil Cuidador
**Archivo:** `views.py`  
**Ruta:** `/cuidador`  
**Complejidad:** ⭐ (Muy Baja)  
**Importancia:** 🟢 AUXILIAR

#### Código:
```python
def cuidador(request):
    return render(request, 'cuidador.html')
```

---

### 13. **adopcion(request)** - Página de Adopciones
**Archivo:** `views.py`  
**Ruta:** `/adopcion`  
**Complejidad:** ⭐ (Muy Baja)  
**Importancia:** 🟢 AUXILIAR

#### Código:
```python
def adopcion(request):
    return render(request, 'adopcion.html')
```

---

## 🗄️ Modelos de Datos

### Modelo: Producto
**Archivo:** `models.py`

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
```

#### Campos:

| Campo | Tipo | Max | Obligatorio | Descripción |
|-------|------|-----|-------------|-------------|
| id_product | AutoField | - | Sí | PK auto-incrementado |
| nombre | CharField | 200 | Sí | Nombre producto |
| marca | CharField | 100 | No | Marca (Pedigri, etc) |
| precio | DecimalField | 10,2 | Sí | Precio con 2 decimales |
| inventario | IntegerField | - | Sí | Stock disponible |
| categoria | CharField | 100 | No | Categoría (Alimento, etc) |
| id_veter | IntegerField | - | No | ID veterinaria (referencia) |
| imagen_url | URLField | 500 | No | URL de imagen externa |

#### Tabla SQL:
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
)
```

#### Métodos:
- **`__str__()`** - Representación en admin: "Croquetas (Pedigri)"

---

## 📋 Formularios

### ProductoForm
**Archivo:** `forms.py`

```python
class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'marca', 'precio', 'inventario', 
                  'categoria', 'id_veter', 'imagen_url']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'marca': forms.TextInput(attrs={'class': 'form-control'}),
            'precio': forms.NumberInput(attrs={'step': '0.01'}),
            'inventario': forms.NumberInput(),
            'categoria': forms.TextInput(),
            'id_veter': forms.NumberInput(),
            'imagen_url': forms.URLInput(),
        }
```

#### Funcionalidades:
- **ModelForm** - Genera campos automáticos del modelo
- **Validación automática** - Tipo, longitud, formato
- **Widgets personalizados** - Clases CSS Bootstrap
- **Placeholders** - Mensajes de ayuda al usuario

#### Validaciones:
```
nombre: CharField, max 200, required
precio: DecimalField, max 10 dígitos totales, 2 decimales, required
imagen_url: URLField, debe ser URL válida (https://...)
```

---

## 🔌 Sistema de Rutas (URLs)

**Archivo:** `urls.py`

```python
urlpatterns = [
    path('', views.index, name='index'),                              # GET /
    path('Veterinaria', views.veter, name='veter'),                   # GET /Veterinaria
    path('servicios', views.serv, name='serv'),                       # GET /servicios
    path('producto', views.producto, name='producto'),                # GET /producto (sin pk)
    path('producto/<int:pk>/', views.producto, name='producto_by_pk'),# GET /producto/123/
    path('cuidador', views.cuidador, name='cuidador'),                # GET /cuidador
    path('adopcion', views.adopcion, name='adopcion'),                # GET /adopcion
    path('carrito', views.carrito, name='carrito'),                   # GET /carrito
    path('agregar_producto/', views.crear_producto, name='agregar_producto'), # GET/POST /agregar_producto/
    path('buscar/', views.buscar_productos, name='buscar_productos'), # GET /buscar/?consulta_de_productos=...
    path('productos/', views.lista_productos, name='productos_list'), # GET /productos/
    path('productos/<int:pk>/', views.detalle_producto, name='producto_detail'), # GET /productos/123/
    path('productos/<int:pk>/editar/', views.editar_producto, name='editar_producto'), # GET/POST /productos/123/editar/
    path('productos/<int:pk>/eliminar/', views.eliminar_producto, name='eliminar_producto'), # GET/POST /productos/123/eliminar/
]
```

#### Patrón de Rutas Dual (Cliente vs Admin):

```
CLIENTE (Comprador):
GET /               → index()           → Productos destacados
GET /producto/123/  → producto()        → Detalle + Carrito

ADMIN (Gestor):
GET /productos/                         → lista_productos()     → Todos
GET /productos/123/                     → detalle_producto()    → Detalle
GET /productos/123/editar/              → editar_producto()     → Formulario
GET /productos/123/eliminar/            → eliminar_producto()   → Confirmación
```

---

## 🔐 Seguridad Implementada

### 1. **get_object_or_404()**
Previene acceso a objetos que no existen:
```python
producto = get_object_or_404(Producto, pk=pk)
# Si pk=999 y no existe → HTTP 404 (no 500 error)
```

### 2. **Validación de Formularios**
```python
if form.is_valid():  # Valida tipos, rangos, formatos
    form.save()
```

### 3. **Confirmación POST para DELETE**
```python
if request.method == 'POST':  # No elimina en GET
    producto.delete()
```

### 4. **Case-Insensitive Search**
```python
nombre__icontains=q  # Busca "ALIMENTO", "alimento", "Alimento"
```

---

## 📊 Flujos de Datos

### Flujo 1: Crear Producto
```
User → GET /agregar_producto/ 
  ↓
View renderiza formulario vacío
  ↓
User completa y POST
  ↓
ProductoForm valida
  ↓
form.save() → INSERT BD
  ↓
redirect a /productos/
```

### Flujo 2: Ver Carrito
```
User clicks [Agregar al carrito] en /producto/123/
  ↓
JavaScript captura
  ↓
Recupera {id, nombre, precio, imagen_url}
  ↓
Guarda en localStorage['dummy_dog_cart']
  ↓
Actualiza navbar badge
  ↓
User navega a /carrito
  ↓
Template carrito.html carga
  ↓
JavaScript lee localStorage
  ↓
Renderiza items + total
  ↓
User modifica cantidades o elimina
  ↓
localStorage actualizado (no BD)
```

### Flujo 3: Buscar Producto
```
User tipea "alimento" en buscador
  ↓
GET /buscar/?consulta_de_productos=alimento
  ↓
View ejecuta búsqueda OR:
  - nombre LIKE %alimento%
  - marca LIKE %alimento%
  ↓
Renderiza resultados
```

---

## 🎯 Resumen de Complejidad

| Función | Complejidad | Líneas | QueryDB | Validación |
|---------|-------------|--------|---------|-----------|
| index() | ⭐ | 3 | 1 | No |
| producto() | ⭐⭐⭐ | 15 | 2 | get_object_or_404 |
| crear_producto() | ⭐⭐⭐ | 10 | 1 (form.save) | Automática |
| editar_producto() | ⭐⭐⭐ | 12 | 1 (form.save) | Automática |
| eliminar_producto() | ⭐⭐ | 8 | 1 | get_object_or_404 |
| lista_productos() | ⭐ | 3 | 1 | No |
| detalle_producto() | ⭐⭐ | 4 | 1 | get_object_or_404 |
| buscar_productos() | ⭐⭐ | 8 | 1 | No |
| carrito() | ⭐ | 1 | 0 | No (JS) |
| veter() | ⭐ | 1 | 0 | No |
| serv() | ⭐ | 1 | 0 | No |
| cuidador() | ⭐ | 1 | 0 | No |
| adopcion() | ⭐ | 1 | 0 | No |

---

## 📝 Notas de Implementación

### QuerySets vs Queries
```python
# Lazy evaluation - no ejecuta hasta acceder
productos = Producto.objects.all()

# Fuerza ejecución (evalúa)
list(productos)
for p in productos:
    print(p)

# QuerySets soportan operadores
q1 = Producto.objects.filter(nombre__icontains="a")
q2 = Producto.objects.filter(marca="Pedigri")
resultado = q1 | q2  # OR
resultado = q1 & q2  # AND
```

### Migraciones (changes al modelo)
Cada cambio al modelo requiere migración:
```bash
# 1. Crear migración
python manage.py makemigrations

# 2. Aplicar a BD
python manage.py migrate
```

### Testing de Funciones
```python
# Pruebas simuladas (sin servidor)
from django.test import TestCase, Client

client = Client()
response = client.get('/productos/')
assert response.status_code == 200
assert 'productos' in response.context
```

---

**Documento Técnico Versión 1.0 - Diciembre 2025**
