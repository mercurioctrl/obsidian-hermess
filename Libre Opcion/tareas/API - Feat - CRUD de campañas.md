# API - Feat - CRUD de campañas

**Proyecto:** [[Libre Opcion/Libre Opcion|Libre Opcion]]
**Estado:** Pendiente
**Fecha:** 2026-04-16

Crear en `sitio-api-rest-v4-laravel` (Laravel 10) los endpoints de **gestión de campañas**, siguiendo el patrón Controller → Service → Repository del proyecto. La feature es agnóstica: se consume desde cualquier sistema externo (PEGA, Nuxt, otro backoffice) sin acoplamiento a un frontend específico.

Las campañas son filtros nombrados del catálogo. Cada campaña puede asociar items por `internal_id`, `category_id_lo` o `id_brand`. El catálogo ya consume estas tablas en `CatalogueRepository::findCampaing()` — esta historia crea el ABM para poblarlas.

> **Tablas existentes:** `[LO].[dbo].[campaigns]` y `[LO].[dbo].[campaign_items]`. La columna FK en `campaign_items` se llama `campaing_id` (typo histórico, no corregir).

---

## Endpoints

| # | Método | Ruta | Propósito | Estado |
|---|--------|------|-----------|--------|
| 1 | `GET` | `/campaigns` | Listar campañas | A crear |
| 2 | `GET` | `/campaigns/{id}` | Detalle de una campaña + sus items | A crear |
| 3 | `POST` | `/campaigns` | Crear campaña | A crear |
| 4 | `PATCH` | `/campaigns/{id}` | Editar campaña | A crear |
| 5 | `DELETE` | `/campaigns/{id}` | Eliminar campaña | A crear |
| 6 | `POST` | `/campaigns/{id}/items` | Agregar items a una campaña | A crear |
| 7 | `DELETE` | `/campaigns/{id}/items/{itemId}` | Quitar un item de una campaña | A crear |
| 8 | `GET` | `/campaigns/search-products` | Buscar productos para agregar a campaña | A crear |

---

## 1) GET — Listar campañas

### Endpoint

`GET /campaigns`

| Campo | Detalle |
|---|---|
| **Método** | `GET` |
| **Autenticación** | Por definir (API key o `token.auth` con perfil admin) |
| **Query params** | `search` (string, opcional) — filtra por nombre. `limit` (int, opcional, default 20). `offset` (int, opcional, default 0). |

### Respuesta esperada

`200 OK`

```json
{
  "success": true,
  "data": [
    {
      "id": 1,
      "name": "winter_sale",
      "items_count": 12
    }
  ],
  "total": 5
}
```

### Query SQL

```sql
SELECT
  C.id,
  C.name,
  COUNT(CI.id) AS items_count
FROM [LO].[dbo].[campaigns] C
LEFT JOIN [LO].[dbo].[campaign_items] CI ON CI.campaing_id = C.id
WHERE (? IS NULL OR C.name LIKE '%' + ? + '%')
GROUP BY C.id, C.name
ORDER BY C.id DESC
OFFSET ? ROWS FETCH NEXT ? ROWS ONLY;
```

---

## 2) GET — Detalle de campaña

### Endpoint

`GET /campaigns/{id}`

| Campo | Detalle |
|---|---|
| **Método** | `GET` |
| **Path param** | `id` (int, requerido) |

### Respuesta esperada

`200 OK`

```json
{
  "success": true,
  "data": {
    "id": 1,
    "name": "winter_sale",
    "items": [
      { "id": 10, "internal_id": 118151, "category_id_lo": null, "id_brand": null },
      { "id": 11, "internal_id": null, "category_id_lo": 35, "id_brand": null },
      { "id": 12, "internal_id": null, "category_id_lo": null, "id_brand": 3155 }
    ]
  }
}
```

### Casos especiales

- **Campaña no existe:** `404` con `{ "success": false, "message": "Campaña no encontrada" }`.

### Query SQL

```sql
-- Campaña
SELECT id, name FROM [LO].[dbo].[campaigns] WHERE id = ?;

-- Items
SELECT id, internal_id, category_id_lo, id_brand
FROM [LO].[dbo].[campaign_items]
WHERE campaing_id = ?
ORDER BY id;
```

---

## 3) POST — Crear campaña

### Endpoint

`POST /campaigns`

| Campo | Detalle |
|---|---|
| **Método** | `POST` |
| **Request body** | `name` (string, requerido, único, max 100) |

### Respuesta esperada

`201 Created`

```json
{
  "success": true,
  "message": "Campaña creada",
  "data": { "id": 5, "name": "cyber_monday_2026" }
}
```

### Validaciones

- `name` requerido, string, max 100 caracteres.
- `name` único en `campaigns`. Si ya existe: `422` con `{ "success": false, "message": "Ya existe una campaña con ese nombre" }`.

### Query SQL

```sql
INSERT INTO [LO].[dbo].[campaigns] (name) VALUES (?);
-- Obtener el ID insertado con SCOPE_IDENTITY() o SELECT @@IDENTITY
```

---

## 4) PATCH — Editar campaña

### Endpoint

`PATCH /campaigns/{id}`

| Campo | Detalle |
|---|---|
| **Método** | `PATCH` |
| **Path param** | `id` (int, requerido) |
| **Request body** | `name` (string, requerido, único, max 100) |

### Respuesta esperada

`200 OK`

```json
{
  "success": true,
  "message": "Campaña actualizada",
  "data": { "id": 5, "name": "cyber_monday_2026_v2" }
}
```

### Casos especiales

- **Campaña no existe:** `404`.
- **Nombre duplicado (otra campaña):** `422`.

### Query SQL

```sql
UPDATE [LO].[dbo].[campaigns] SET name = ? WHERE id = ?;
```

---

## 5) DELETE — Eliminar campaña

### Endpoint

`DELETE /campaigns/{id}`

| Campo | Detalle |
|---|---|
| **Método** | `DELETE` |
| **Path param** | `id` (int, requerido) |

### Respuesta esperada

`200 OK`

```json
{
  "success": true,
  "message": "Campaña eliminada"
}
```

Elimina la campaña **y todos sus items asociados** (DELETE en cascada manual: primero `campaign_items`, luego `campaigns`).

### Casos especiales

- **Campaña no existe:** `404`.

### Query SQL

```sql
DELETE FROM [LO].[dbo].[campaign_items] WHERE campaing_id = ?;
DELETE FROM [LO].[dbo].[campaigns] WHERE id = ?;
```

---

## 6) POST — Agregar items a una campaña

### Endpoint

`POST /campaigns/{id}/items`

| Campo | Detalle |
|---|---|
| **Método** | `POST` |
| **Path param** | `id` (int, requerido) — ID de la campaña |
| **Request body** | `items` (array, requerido) — cada elemento con al menos uno de: `internal_id` (int), `category_id_lo` (int), `id_brand` (int) |

### Ejemplo de request

```json
{
  "items": [
    { "internal_id": 118151 },
    { "category_id_lo": 35 },
    { "id_brand": 3155 }
  ]
}
```

### Respuesta esperada

`201 Created`

```json
{
  "success": true,
  "message": "3 items agregados a la campaña",
  "data": {
    "added": 3
  }
}
```

### Validaciones

- La campaña debe existir (`404` si no).
- `items` requerido, array, mínimo 1 elemento.
- Cada item debe tener **al menos uno** de `internal_id`, `category_id_lo`, `id_brand`. Si los tres son null: `422`.

### Query SQL

```sql
INSERT INTO [LO].[dbo].[campaign_items] (campaing_id, internal_id, category_id_lo, id_brand)
VALUES (?, ?, ?, ?);
-- Repetir por cada item del array
```

---

## 7) DELETE — Quitar un item de una campaña

### Endpoint

`DELETE /campaigns/{id}/items/{itemId}`

| Campo | Detalle |
|---|---|
| **Método** | `DELETE` |
| **Path param** | `id` (int) — ID de la campaña. `itemId` (int) — ID del registro en `campaign_items`. |

### Respuesta esperada

`200 OK`

```json
{
  "success": true,
  "message": "Item eliminado de la campaña"
}
```

### Casos especiales

- **Campaña o item no existe:** `404`.
- **Item no pertenece a esa campaña:** `404`.

### Query SQL

```sql
DELETE FROM [LO].[dbo].[campaign_items] WHERE id = ? AND campaing_id = ?;
```

---

## 8) GET — Buscar productos para agregar a campaña

### Endpoint

`GET /campaigns/search-products`

| Campo | Detalle |
|---|---|
| **Método** | `GET` |
| **Query params** | `search` (string, requerido, mínimo 3 caracteres) — busca por título de producto. `limit` (int, opcional, default 10, max 30). |

### Respuesta esperada

`200 OK`

```json
{
  "success": true,
  "data": [
    {
      "id": 45231,
      "internal_id": 118151,
      "title": "Mouse Logitech G502 HERO RGB",
      "image": "a1b2c3d4e5f6g7h8i9j0.jpg"
    },
    {
      "id": 45232,
      "internal_id": 118094,
      "title": "Mouse Logitech G203 Lightsync",
      "image": "b2c3d4e5f6g7h8i9j0k1.jpg"
    }
  ]
}
```

El campo `image` es el checksum de la foto. El frontend construye la URL completa con `{STATIC_URL}{checksum}` (ej: `https://static.libreopcion.com/img/a1b2c3d4e5f6g7h8i9j0.jpg`).

### Validaciones

- `search` requerido, mínimo 3 caracteres. Si falta o es menor: `422`.

### Casos especiales

- **Sin resultados:** `200` con `data: []`.
- **Productos sin imagen:** devolver el checksum default `c510dfbb1f578d44c78cb47d47dab575.gif`.

### Query SQL

Usar la tabla desnormalizada `SEARCH_ENGINE_LO.dbo.items` que ya tiene full-text indexing, imagen y los dos IDs:

```sql
SELECT TOP (?)
  I.id_lo AS id,
  I.internal_id,
  I.description AS title,
  I.product_picture AS image
FROM SEARCH_ENGINE_LO.dbo.items I
INNER JOIN FREETEXTTABLE(SEARCH_ENGINE_LO.dbo.items, description, ?) AS FT
  ON I.internal_id = FT.[KEY]
ORDER BY FT.RANK DESC;
```

> Reusar el mismo patrón de full-text search que ya usa `CatalogueRepository`. Si `FREETEXTTABLE` no es viable por la key, usar `WHERE FREETEXT(description, ?)` con `ORDER BY` por relevancia implícita.

---

## Entregables

### Controllers (`app/Http/Controllers/Campaign/`)

| Controller | Acción | Ruta |
|---|---|---|
| `CampaignListController` | `__invoke` | `GET /campaigns` |
| `CampaignShowController` | `__invoke` | `GET /campaigns/{id}` |
| `CampaignCreateController` | `__invoke` | `POST /campaigns` |
| `CampaignUpdateController` | `__invoke` | `PATCH /campaigns/{id}` |
| `CampaignDeleteController` | `__invoke` | `DELETE /campaigns/{id}` |
| `CampaignItemAddController` | `__invoke` | `POST /campaigns/{id}/items` |
| `CampaignItemRemoveController` | `__invoke` | `DELETE /campaigns/{id}/items/{itemId}` |
| `CampaignSearchProductsController` | `__invoke` | `GET /campaigns/search-products` |

### Service (`app/Service/Campaign/`)

- `CampaignService`
  - `list(?string $search, int $limit, int $offset): array`
  - `show(int $id): array`
  - `create(string $name): array`
  - `update(int $id, string $name): array`
  - `delete(int $id): void`
  - `addItems(int $campaignId, array $items): int`
  - `removeItem(int $campaignId, int $itemId): void`
  - `searchProducts(string $search, int $limit): array`

### Repository (`app/Repository/Campaign/CampaignRepository.php`)

Métodos:

- `list(?string $search, int $limit, int $offset): array`
- `count(?string $search): int`
- `findById(int $id): ?object`
- `getItems(int $campaignId): array`
- `create(string $name): int`
- `update(int $id, string $name): void`
- `delete(int $id): void`
- `deleteItemsByCampaignId(int $campaignId): void`
- `addItem(int $campaignId, ?int $internalId, ?int $categoryIdLo, ?int $idBrand): void`
- `removeItem(int $id, int $campaignId): int`
- `nameExists(string $name, ?int $excludeId = null): bool`
- `searchProducts(string $search, int $limit): array`

**Sin Eloquent.** Todo con `DB::select()` / `DB::statement()` y bindings posicionales.

### Rutas — `app/routes/api.php`

```php
Route::prefix('campaigns')->group(function () {
    Route::get('', CampaignListController::class);
    Route::post('', CampaignCreateController::class);
    Route::get('/search-products', CampaignSearchProductsController::class); // antes de /{id}
    Route::get('/{id}', CampaignShowController::class);
    Route::patch('/{id}', CampaignUpdateController::class);
    Route::delete('/{id}', CampaignDeleteController::class);
    Route::post('/{id}/items', CampaignItemAddController::class);
    Route::delete('/{id}/items/{itemId}', CampaignItemRemoveController::class);
});
```

> **Importante:** `/search-products` debe registrarse **antes** de `/{id}` para que Laravel no lo interprete como un ID.

> **Autenticación:** definir si se protege con `token.auth` + perfil admin, o con un mecanismo de API key para sistemas externos. Si es solo para PEGA/backoffice interno, `token.auth` con perfil admin es suficiente.

---

## Criterios de aceptacion

- [ ] `GET /campaigns` devuelve lista paginada con `items_count` por campaña
- [ ] `GET /campaigns/{id}` devuelve la campaña con todos sus items detallados
- [ ] `POST /campaigns` crea una campaña con nombre único
- [ ] `POST /campaigns` con nombre duplicado devuelve 422
- [ ] `PATCH /campaigns/{id}` actualiza el nombre validando unicidad
- [ ] `DELETE /campaigns/{id}` elimina la campaña y todos sus items asociados
- [ ] `POST /campaigns/{id}/items` agrega uno o más items a la campaña
- [ ] Cada item requiere al menos uno de `internal_id`, `category_id_lo`, `id_brand`
- [ ] `DELETE /campaigns/{id}/items/{itemId}` elimina un item específico de la campaña
- [ ] Campaña inexistente devuelve 404 en todos los endpoints que reciben `{id}`
- [ ] `GET /campaigns/search-products?search=mouse` devuelve productos con `id`, `internal_id`, `title` e `image` (checksum)
- [ ] La búsqueda usa full-text search sobre `SEARCH_ENGINE_LO.dbo.items`
- [ ] Búsqueda con menos de 3 caracteres devuelve 422
- [ ] Productos sin foto devuelven el checksum default (`c510dfbb1f578d44c78cb47d47dab575.gif`)
- [ ] El filtro `?campaign=nombre` del catálogo (`CatalogueRepository`) sigue funcionando igual con los datos creados por estos endpoints
- [ ] Todas las respuestas siguen el formato `{ success, message, data }` del proyecto
- [ ] Sin Eloquent — todo con `DB::select()` / `DB::statement()`

---

## Notas tecnicas

- **Typo histórico:** la FK en `campaign_items` se llama `campaing_id` (sin la "n" de "campaign"). No corregir — el catálogo ya usa ese nombre en `CatalogueRepository::findCampaing()`.
- **Sin Eloquent**, siguiendo el patrón del proyecto.
- **Transacciones:** el DELETE de campaña (que borra items + campaña) debe ir dentro de `DB::transaction()`.
- **Lint:** correr `vendor/bin/pint` antes de commitear.
- **Columnas de la tabla `campaign_items`:** antes de implementar, verificar la estructura exacta con `sp_columns campaign_items` desde tinker, ya que solo conocemos `id`, `campaing_id`, `internal_id`, `category_id_lo`, `id_brand` por el código existente. Puede haber columnas adicionales (timestamps, estado, etc.).

## Fuera de alcance

- **No** crear frontend/UI. Esta historia es solo API.
- **No** renombrar el typo `campaing_id` → `campaign_id`.
- **No** modificar la lógica de consumo en `CatalogueRepository` — esa ya funciona.
- **No** agregar cache Redis. Si se necesita, va en otra historia.

## Ver tambien

- [[Libre Opcion/Libre Opcion|Indice del proyecto]]
- [[Libre Opcion/tareas/APP - Feat - Gestión de campañas|APP - Feat - Gestión de campañas]] — historia de frontend que consume estos endpoints
- `sitio-api-rest-v4-laravel/app/app/Repository/Catalogue/CatalogueRepository.php:304` — `findCampaing()`, consumo actual de las tablas
