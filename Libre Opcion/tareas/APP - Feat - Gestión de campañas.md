# APP - Feat - Gestión de campañas

**Proyecto:** [[Libre Opcion/Libre Opcion|Libre Opcion]]
**Estado:** Pendiente (depende de la tarea de API)
**Fecha:** 2026-04-16
**Depende de:** [[Libre Opcion/tareas/API - Feat - CRUD de campañas|API - Feat - CRUD de campañas]]

Crear la interfaz de gestión de campañas para el catálogo. La UI es agnóstica al sistema que la implemente (Nuxt, PEGA, backoffice externo) — esta historia define las pantallas, flujos y contratos de integración con la API.

Las campañas son filtros nombrados que agrupan productos por `internal_id`, categoría (`category_id_lo`) o marca (`id_brand`). El catálogo ya las consume con `?campaign=nombre` — esta historia permite crearlas y administrarlas visualmente.

---

## Pantallas

### 1. Lista de campañas

**Ruta sugerida:** `/admin/campaigns`

| Elemento | Detalle |
|---|---|
| Tabla principal | Columnas: Nombre, Cantidad de items, Acciones |
| Buscador | Input de texto, filtra por nombre (`?search=`) |
| Paginación | Offset-based, synced con query params |
| Botón "Nueva campaña" | Abre el formulario de creación |
| Acciones por fila | Ver detalle, Editar nombre, Eliminar |

**Consume:** `GET /campaigns?search=&limit=&offset=`

**Eliminar:** confirmación antes de ejecutar `DELETE /campaigns/{id}`. Mostrar advertencia: "Se eliminarán todos los items asociados a esta campaña."

---

### 2. Crear / Editar campaña

**Ruta sugerida:** `/admin/campaigns/new` y `/admin/campaigns/{id}/edit`

| Elemento | Detalle |
|---|---|
| Campo "Nombre" | Input texto, requerido, max 100 chars |
| Botón guardar | `POST /campaigns` (crear) o `PATCH /campaigns/{id}` (editar) |
| Error de duplicado | Mostrar inline si la API devuelve 422 por nombre existente |

Formulario simple, un solo campo. Al crear exitosamente, redirigir al detalle de la campaña recién creada para empezar a agregar items.

---

### 3. Detalle de campaña (gestión de items)

**Ruta sugerida:** `/admin/campaigns/{id}`

Esta es la pantalla principal de trabajo. Muestra la campaña y permite agregar/quitar items.

#### Header

- Nombre de la campaña (editable inline o con botón editar)
- Cantidad total de items

#### Tabla de items asociados

| Columna | Detalle |
|---|---|
| Tipo | Icono o badge indicando si filtra por Producto, Categoría o Marca |
| Valor | `internal_id`, `category_id_lo` o `id_brand` según corresponda |
| Acción | Botón eliminar → `DELETE /campaigns/{id}/items/{itemId}` con confirmación |

**Consume:** `GET /campaigns/{id}` (trae campaña + items)

#### Agregar items — por producto (buscador)

Sección principal para agregar productos individuales a la campaña. Incluye un **buscador con autocompletado** que consulta el catálogo real.

| Elemento | Detalle |
|---|---|
| Input de búsqueda | Texto libre, busca por nombre de producto. Mínimo 3 caracteres para disparar la búsqueda |
| Resultados (dropdown/lista) | Muestra hasta 10 resultados con: **imagen** (thumbnail), **título**, **id** e **internal_id** |
| Selector de campo | Al lado de cada resultado, indicar con qué campo se va a vincular: `id` o `internal_id`. Default: `internal_id` (es el que usa `CatalogueRepository::findCampaing()`) |
| Selección múltiple | Permitir seleccionar varios productos antes de confirmar. Los seleccionados se acumulan en una lista visual debajo del buscador |
| Botón "Agregar seleccionados" | `POST /campaigns/{id}/items` con el array de items |

**Consume:** `GET /campaigns/search-products?search={texto}&limit=10`

**Construcción de imagen:** la API devuelve el campo `image` (checksum). El frontend construye la URL completa: `{STATIC_URL}{checksum}` (ej: `https://static.libreopcion.com/img/{checksum}`).

**Flujo de agregar productos:**

1. Usuario escribe en el buscador: "mouse logitech"
2. El dropdown muestra los resultados con imagen, título, id e internal_id
3. Usuario clickea los productos que quiere agregar → se acumulan en la lista de seleccionados
4. Usuario puede quitar productos de la lista antes de confirmar
5. Click en "Agregar seleccionados"
6. La API recibe: `{ "items": [{ "internal_id": 118151 }, { "internal_id": 118094 }] }`
7. La tabla de items se refresca

#### Agregar items — por categoría o marca

Sección secundaria (tabs o toggle) para agregar filtros masivos por categoría o marca.

| Elemento | Detalle |
|---|---|
| Selector de tipo | Toggle/Tab: "Categoría" o "Marca" |
| Input de valor | Numérico. IDs separados por coma para agregar varios |
| Botón "Agregar" | `POST /campaigns/{id}/items` con el array |

**Flujo:**

1. Usuario selecciona "Categoría"
2. Ingresa IDs: `35, 33`
3. Click en "Agregar"
4. La API recibe: `{ "items": [{ "category_id_lo": 35 }, { "category_id_lo": 33 }] }`
5. La tabla se refresca

---

## Integración con API

| Acción | Endpoint | Método |
|--------|----------|--------|
| Listar campañas | `/campaigns` | `GET` |
| Ver detalle + items | `/campaigns/{id}` | `GET` |
| Crear campaña | `/campaigns` | `POST` |
| Editar campaña | `/campaigns/{id}` | `PATCH` |
| Eliminar campaña | `/campaigns/{id}` | `DELETE` |
| Agregar items | `/campaigns/{id}/items` | `POST` |
| Quitar item | `/campaigns/{id}/items/{itemId}` | `DELETE` |
| Buscar productos | `/campaigns/search-products?search=&limit=` | `GET` |

---

## Criterios de aceptación

- [ ] La lista de campañas muestra nombre y cantidad de items por campaña
- [ ] Se puede buscar campañas por nombre
- [ ] Se puede crear una campaña con nombre único
- [ ] Al crear, se redirige al detalle para agregar items
- [ ] Se puede editar el nombre de una campaña existente
- [ ] Error de nombre duplicado se muestra inline en el formulario
- [ ] Se puede eliminar una campaña con confirmación previa
- [ ] El detalle muestra todos los items con su tipo (producto/categoría/marca)
- [ ] El buscador de productos muestra resultados con imagen (thumbnail) y título
- [ ] Cada resultado muestra id e internal_id del producto
- [ ] Se pueden seleccionar múltiples productos del buscador antes de confirmar
- [ ] Se puede elegir vincular por `id` o `internal_id` (default: `internal_id`)
- [ ] La búsqueda se dispara con mínimo 3 caracteres
- [ ] Se pueden agregar categorías y marcas por ID en la sección secundaria
- [ ] Se puede eliminar un item individual con confirmación
- [ ] La tabla de items se refresca después de agregar/eliminar
- [ ] Feedback visual de éxito/error en todas las operaciones

---

## Notas técnicas

- **Agnóstico de framework:** esta historia define pantallas y flujos, no componentes específicos de Nuxt/Vue/React. El equipo que implemente elige el stack.
- **Autenticación:** la misma que use el backoffice donde se implemente. Coordinar con la historia de API qué mecanismo se define (JWT admin, API key, etc.).
- **No se valida existencia de `internal_id` / `category_id_lo` / `id_brand`:** la API acepta cualquier valor numérico. Si el ID no existe en el catálogo, la campaña simplemente no filtra nada para ese item. Esto es intencional — permite precargar campañas antes de que los productos estén publicados.
- **URL del catálogo filtrado:** para previsualizar la campaña en el sitio, construir el link: `/search?campaign={nombre_campaña}`.

## Fuera de alcance

- **No** implementar drag & drop para reordenar items.
- **No** implementar previsualización en vivo del catálogo filtrado dentro del admin.
- **No** agregar campos adicionales a la campaña (fecha inicio/fin, estado activa/inactiva, banner, etc.). Si se necesitan, van en otra historia con su migración de base de datos.
- **No** implementar importación masiva desde CSV/Excel.

## Ver también

- [[Libre Opcion/Libre Opcion|Indice del proyecto]]
- [[Libre Opcion/tareas/API - Feat - CRUD de campañas|API - Feat - CRUD de campañas]] — endpoints que consume esta UI
