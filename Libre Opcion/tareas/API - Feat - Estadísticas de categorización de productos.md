# API - Feat - Estadísticas de categorización de productos (v4)

**Proyecto:** [[Libre Opcion/Libre Opcion|Libre Opción]]
**Estado:** Pendiente
**Fecha:** 2026-04-15
**Depende de:** [[Libre Opcion/tareas/API - Feat - Recategorizar productos sin categoría|API - Feat - Recategorizar productos sin categoría]]

Crear desde cero en `sitio-api-rest-v4-laravel` (Laravel 10) los endpoints de **estadísticas de categorización de productos**, siguiendo el patrón Controller → Service → Repository del proyecto. **No** se implementa nada en el legacy `sitio-api-rest-v3` (Restler/PHP) — toda funcionalidad nueva relacionada con categorización vive en v4.

> Esta historia es **read-only**: solo expone datos. La acción de recategorizar (UPDATE) la cubre la tarea anterior. La administración de alias (`POST /v4/categorias-admin/{id}/alias`, etc.) ya existe o se migra en su propio ticket — esta historia no la toca.

**Endpoints alcance:**

| # | Método | Ruta v4 | Estado |
|---|--------|---------|--------|
| 1 | `GET` | `/v4/categorias-admin/stats-categorizacion` | A crear |
| 2 | `GET` | `/v4/categorias-admin/stats-categorizacion/ejemplos` | A crear |

**Referencia de la lógica de matching (legacy, solo lectura):** `sitio-api-rest-v3/app/models/CategoriaModel.php:635` — `adivinarCategoriaProductoImportado`. Esta historia **no** ejecuta el matching, solo cuenta cómo está la base hoy.

**Estado actual en v4:** no existe ningún recurso `categorias-admin`. Hay que crear el grupo de rutas y los archivos base (controllers, service, repository).

---

## 1) GET — Snapshot de categorización

### Endpoint

`GET /v4/categorias-admin/stats-categorizacion`

### Tabla de definición del recurso

| Campo | Detalle |
|---|---|
| **Método** | `GET` |
| **Autenticación** | Requerida (`token.auth`) |
| **Perfil** | `admin` |
| **Path param** | Ninguno |
| **Query params** | `vendedor_id` (int, opcional) — filtra todos los conteos a un solo vendedor. `top` (int, opcional, default 20, tope 100) — cuántos nombres atascados devolver en `nombres_sin_match`. |
| **Request body** | Ninguno |

### Ejemplo de llamada

`GET /v4/categorias-admin/stats-categorizacion?vendedor_id=12&top=30`

### Respuesta esperada

`200 OK`

```json
{
  "total_productos": 18432,
  "categorizados": 15910,
  "sin_categorizar": 2522,
  "porcentaje_categorizado": 86.31,

  "nombres_sin_match": [
    { "nombre_crudo": "perifericos gamer", "cantidad": 184 },
    { "nombre_crudo": "almacenamiento ssd", "cantidad": 132 },
    { "nombre_crudo": "rgb",                "cantidad":  97 }
  ],

  "por_vendedor": [
    { "vendedor_id": 12, "vendedor": "NB",       "total": 9420, "sin_categorizar": 410 },
    { "vendedor_id":  7, "vendedor": "Fullhard", "total": 2310, "sin_categorizar": 880 }
  ],

  "por_categoria": [
    { "id_categoria_lo": 14, "nombre": "Auriculares",   "cantidad": 1240 },
    { "id_categoria_lo": 27, "nombre": "Estabilizador", "cantidad":  890 }
  ]
}
```

### Reglas de cada bloque

- **`total_productos` / `categorizados` / `sin_categorizar`** — `sin_categorizar` cuenta `WHERE id_categoria_lo = 0`. `categorizados` es el complemento. Si llega `vendedor_id`, todos los contadores se filtran por ese vendedor (incluyendo los demás bloques).
- **`porcentaje_categorizado`** — `categorizados / total_productos * 100`, redondeado a 2 decimales. Si `total_productos = 0` devolver `0`.
- **`nombres_sin_match`** — agrupa `[CS].[dbo].[productos].categoria` (texto crudo del importador) entre los que tienen `id_categoria_lo = 0`, ordenado por `COUNT(*) DESC`, limitado a `top`. **Crítico:** normalizar con `LOWER(LTRIM(RTRIM(REPLACE(categoria, '-', ' '))))` para que `"Perifericos"`, `"perifericos "`, `"perifericos-gamer"` se cuenten coherentes con cómo el matcher legacy compara contra `categoriasAlias.nombre` (mismo `LOWER` + `REPLACE('-',' ')` que usa `CategoriaModel.php:117`). Si esta normalización no es la misma, la lista miente.
- **`por_vendedor`** — un row por vendedor con su total y cuántos sin categorizar. Joinear con `[LO].[dbo].[vendedores].nombre` para devolver el label.
- **`por_categoria`** — distribución del catálogo categorizado por `id_categoria_lo`. Joinear con `[LO].[dbo].[categorias].nombre`. **Excluir** `id_categoria_lo = 0` (eso ya está en `sin_categorizar`).

### Casos especiales

- **Sin productos en la base / vendedor sin productos:** devolver el JSON con `total_productos: 0`, `porcentaje_categorizado: 0` y los arrays vacíos. **Nunca 404.**
- **`vendedor_id` no existe:** mismo caso anterior — todos los conteos en cero. No validar existencia previamente, dejá que el `WHERE` los devuelva en cero.
- **`top` fuera de rango:** clampear a `[1, 100]` en el request DTO. No tirar 422.
- **Sin auth (401):** respuesta estándar de `token.auth`.
- **Perfil distinto de `admin` (403):** respuesta estándar del middleware de perfil.

### Queries SQL

> SQL Server. Se pueden hacer joins cross-database entre `[CS]` y `[LO]` con three-part names (mismo patrón que [[Libre Opcion/tareas/API - Refactor - Migrar recurso de preguntas y respuestas a v4|la migración de preguntas]]).

**Totales:**

```sql
SELECT
  COUNT(*) AS total_productos,
  SUM(CASE WHEN id_categoria_lo = 0 THEN 1 ELSE 0 END) AS sin_categorizar
FROM [CS].[dbo].[productos]
WHERE (? IS NULL OR id_vendedor = ?);
```

**Top de nombres sin match:**

```sql
SELECT TOP (?)
  LOWER(LTRIM(RTRIM(REPLACE(categoria, '-', ' ')))) AS nombre_crudo,
  COUNT(*) AS cantidad
FROM [CS].[dbo].[productos]
WHERE id_categoria_lo = 0
  AND categoria IS NOT NULL
  AND LTRIM(RTRIM(categoria)) <> ''
  AND (? IS NULL OR id_vendedor = ?)
GROUP BY LOWER(LTRIM(RTRIM(REPLACE(categoria, '-', ' '))))
ORDER BY cantidad DESC;
```

**Por vendedor:**

```sql
SELECT
  V.id AS vendedor_id,
  V.nombre AS vendedor,
  COUNT(P.id) AS total,
  SUM(CASE WHEN P.id_categoria_lo = 0 THEN 1 ELSE 0 END) AS sin_categorizar
FROM [CS].[dbo].[productos] P
INNER JOIN [LO].[dbo].[vendedores] V ON V.id = P.id_vendedor
WHERE (? IS NULL OR P.id_vendedor = ?)
GROUP BY V.id, V.nombre
ORDER BY sin_categorizar DESC;
```

**Por categoría:**

```sql
SELECT
  C.id AS id_categoria_lo,
  C.nombre,
  COUNT(P.id) AS cantidad
FROM [CS].[dbo].[productos] P
INNER JOIN [LO].[dbo].[categorias] C ON C.id = P.id_categoria_lo
WHERE P.id_categoria_lo <> 0
  AND (? IS NULL OR P.id_vendedor = ?)
GROUP BY C.id, C.nombre
ORDER BY cantidad DESC;
```

### Origen legacy

No hay recurso legacy equivalente. La normalización del nombre se replica de `CategoriaModel::obtener()` — `sitio-api-rest-v3/app/models/CategoriaModel.php:117`.

---

## 2) GET — Drilldown de un nombre crudo atascado

### Endpoint

`GET /v4/categorias-admin/stats-categorizacion/ejemplos`

### Tabla de definición del recurso

| Campo | Detalle |
|---|---|
| **Método** | `GET` |
| **Autenticación** | Requerida (`token.auth`) |
| **Perfil** | `admin` |
| **Path param** | Ninguno |
| **Query params** | `nombre_crudo` (string, **requerido**) — el nombre normalizado tal cual viene del bloque `nombres_sin_match` del endpoint anterior. `limite` (int, opcional, default 20, tope 100). `vendedor_id` (int, opcional). |
| **Request body** | Ninguno |

### Ejemplo de llamada

`GET /v4/categorias-admin/stats-categorizacion/ejemplos?nombre_crudo=perifericos+gamer&limite=20`

### Respuesta esperada

`200 OK`

```json
{
  "nombre_crudo": "perifericos gamer",
  "data": [
    { "id": 12345, "titulo": "Mouse Logitech G502 HERO RGB", "vendedor": { "id": 12, "nombre": "NB" } },
    { "id": 12346, "titulo": "Teclado Redragon Kumara K552 RGB", "vendedor": { "id": 7,  "nombre": "Fullhard" } }
  ],
  "total_estimado": 184
}
```

`total_estimado` es el mismo número que ya devolvió el endpoint anterior para ese `nombre_crudo`, recalculado para no obligar al admin a tener los dos endpoints sincronizados.

### Casos especiales

- **`nombre_crudo` ausente o vacío (422):** `{ "error": "nombre_crudo es requerido" }`.
- **No hay productos con ese nombre crudo:** `data: []`, `total_estimado: 0`. **No 404.** Es válido pedir un nombre que ya quedó vacío después de crear el alias.
- **Sin auth (401)** y **403 si no es admin:** respuestas estándar.

### Query SQL

```sql
SELECT TOP (?)
  P.id,
  P.titulo,
  V.id AS vendedor_id,
  V.nombre AS vendedor_nombre
FROM [CS].[dbo].[productos] P
INNER JOIN [LO].[dbo].[vendedores] V ON V.id = P.id_vendedor
WHERE P.id_categoria_lo = 0
  AND LOWER(LTRIM(RTRIM(REPLACE(P.categoria, '-', ' ')))) = ?
  AND (? IS NULL OR P.id_vendedor = ?)
ORDER BY P.id DESC;
```

Para `total_estimado` reusar la query del top del endpoint anterior pero filtrando por el mismo `nombre_crudo` en el `HAVING` (o hacer un `COUNT(*)` simple con el mismo `WHERE`).

---

## Esquema de campos compartido

### `StatsCategorizacionDto`

| Campo | Tipo | Descripción |
|---|---|---|
| total_productos | int | Total de productos del catálogo (filtrados por vendedor si aplica) |
| categorizados | int | Productos con `id_categoria_lo > 0` |
| sin_categorizar | int | Productos con `id_categoria_lo = 0` |
| porcentaje_categorizado | float | `categorizados / total * 100`, 2 decimales |
| nombres_sin_match | `NombreSinMatchDto[]` | Top de nombres crudos sin matchear |
| por_vendedor | `StatsVendedorDto[]` | Distribución por vendedor |
| por_categoria | `StatsCategoriaDto[]` | Distribución por categoría asignada |

### `NombreSinMatchDto`

| Campo | Tipo |
|---|---|
| nombre_crudo | string (normalizado) |
| cantidad | int |

### `StatsVendedorDto`

| Campo | Tipo |
|---|---|
| vendedor_id | int |
| vendedor | string |
| total | int |
| sin_categorizar | int |

### `StatsCategoriaDto`

| Campo | Tipo |
|---|---|
| id_categoria_lo | int |
| nombre | string |
| cantidad | int |

### `EjemploProductoSinMatchDto`

| Campo | Tipo |
|---|---|
| id | int |
| titulo | string |
| vendedor | `{ id: int, nombre: string }` |

> Si ya existe un `VendedorMiniDto` en v4, **reusarlo** en lugar de definir el inline `vendedor`. Mismo criterio para cualquier otro DTO existente.

---

## Entregables

### Controllers (`app/Http/Controllers/CategoriasAdmin/`)

| Controller | Acción | Ruta |
|---|---|---|
| `StatsCategorizacionController` | `__invoke` | `GET /categorias-admin/stats-categorizacion` |
| `StatsCategorizacionEjemplosController` | `__invoke` | `GET /categorias-admin/stats-categorizacion/ejemplos` |

### Service (`app/Service/CategoriasAdmin/`)

- `StatsCategorizacionService`
  - `obtener(?int $vendedorId, int $top): StatsCategorizacionDto`
  - `obtenerEjemplos(string $nombreCrudo, int $limite, ?int $vendedorId): EjemplosNombreCrudoDto`

Toda la lógica de orquestación vive acá. Los controllers **solo** validan request, llaman al service y serializan.

### Repository (`app/Repository/CategoriasAdmin/CategorizacionStatsRepository.php`)

Métodos:

- `contarTotales(?int $vendedorId): array{total: int, sin_categorizar: int}`
- `topNombresSinMatch(int $top, ?int $vendedorId): array`
- `statsPorVendedor(?int $vendedorId): array`
- `statsPorCategoria(?int $vendedorId): array`
- `ejemplosPorNombreCrudo(string $nombreCrudoNormalizado, int $limite, ?int $vendedorId): array`
- `contarPorNombreCrudo(string $nombreCrudoNormalizado, ?int $vendedorId): int`

**Sin Eloquent.** Todo con `DB::connection('sqlsrv')->select(..., [...])` y bindings posicionales. La normalización del `nombre_crudo` la hace **el repositorio en SQL**, no PHP — así garantizamos que el endpoint del top y el de ejemplos siempre comparen el mismo string.

### Request validation

- `StatsCategorizacionRequest` — valida `vendedor_id` (int|nullable), `top` (int|nullable, clampea a [1,100]).
- `StatsCategorizacionEjemplosRequest` — valida `nombre_crudo` (string, required, max 255), `limite` (int|nullable, clampea a [1,100]), `vendedor_id` (int|nullable).

### Rutas — `app/routes/api.php`

Crear el grupo `categorias-admin` dentro de `token.auth` con middleware de perfil `admin`:

```php
Route::middleware(['token.auth', 'profile:admin'])
    ->prefix('categorias-admin')
    ->group(function () {
        Route::get('stats-categorizacion', StatsCategorizacionController::class);
        Route::get('stats-categorizacion/ejemplos', StatsCategorizacionEjemplosController::class);
    });
```

> Si en v4 todavía no existe el middleware `profile:admin`, usar el helper que esté en uso (mirar cómo otros endpoints admin protegen el perfil — no inventes uno nuevo solo para esta historia).

---

## Criterios de aceptación

- [ ] `GET /v4/categorias-admin/stats-categorizacion` devuelve el JSON con la estructura exacta del ejemplo (mismos nombres de campos, mismo orden de bloques)
- [ ] `categorizados + sin_categorizar = total_productos` siempre
- [ ] `porcentaje_categorizado` es `categorizados / total * 100` con 2 decimales, y devuelve `0` cuando `total = 0`
- [ ] `nombres_sin_match` agrupa correctamente `"Perifericos"`, `"perifericos"`, `"perifericos-gamer"`, `"  perifericos  "` con la misma normalización que usa el matcher legacy en `CategoriaModel.php:117`
- [ ] `nombres_sin_match` respeta el `top` (default 20, max 100)
- [ ] `por_categoria` excluye `id_categoria_lo = 0`
- [ ] Filtrar por `vendedor_id` reduce **todos** los contadores y bloques, no solo `por_vendedor`
- [ ] `vendedor_id` inexistente devuelve 200 con conteos en cero, no 404
- [ ] `GET /v4/categorias-admin/stats-categorizacion/ejemplos` devuelve productos cuyo `categoria` normalizado coincida exactamente con el `nombre_crudo` recibido
- [ ] `ejemplos` con `nombre_crudo` ausente devuelve 422
- [ ] `ejemplos` con `nombre_crudo` que no matchea ningún producto devuelve 200 con `data: []`
- [ ] Ambos endpoints protegidos con `token.auth` + perfil `admin`
- [ ] Ningún endpoint hace `INSERT` / `UPDATE` / `DELETE` (verificable mirando el repositorio: solo `DB::select`)
- [ ] Una llamada al snapshot, en una base de tamaño productivo, responde en menos de 2 segundos. Si no, agregar índice en migración nueva (ver Notas).

---

## Notas técnicas

- **Sin Eloquent**, igual que el resto de v4: `DB::connection('sqlsrv')->select(sql, bindings)`.
- **Normalización del nombre crudo en SQL, no en PHP.** Si dos endpoints normalizan distinto, el drilldown va a devolver `data: []` para nombres que sí aparecen en el top y la pantalla queda inservible. Es la trampa más fácil de caer en esta historia.
- **Performance:** las queries de agrupación corren sobre todo el catálogo (decenas de miles de productos). Si en producción tarda más de 1-2s, agregar índice sobre `(id_categoria_lo, id_vendedor)` en `[CS].[dbo].[productos]` con migración nueva en el directorio `sql/` del legacy (las migraciones siguen viviendo ahí), formato `YYYYMMDDhhmm-descripcion.sql`. **Antes de crear el índice**, revisar `sql/201808061125-agrega-algunos-indices.sql` por si ya existe uno equivalente.
- **`top` clampeado:** clampear en el Request, no en el Service — así el contrato de la API queda explícito.
- **Cache:** **no cachear** en esta historia. Si lo necesitamos después, va en otra. El admin va a usar este endpoint en ráfagas cortas (mira → crea alias → recategoriza → mira de nuevo) y el cache solo agrega ruido.
- **Sin tests automatizados todavía.** v4 tiene PHPUnit configurado, pero esta historia es read-only y agregar fixtures de catálogo entero no escala. Smoke test manual con Restler Client / Postman alcanza para mergear.
- **DATEFORMAT:** este endpoint no maneja fechas, no aplica.
- **Patrón Controller → Service → Repository:** una acción por controller (`__invoke`).
- **Lint:** correr `vendor/bin/pint` antes de commitear.

## Fuera de alcance (no hacer en esta historia)

- **No** crear pantalla de admin frontend. Primero validamos consumiendo los endpoints desde Postman / Restler Client. Si el flujo se mira seguido, la UI va en otra historia.
- **No** automatizar la creación de alias. La decisión sigue siendo del admin desde los endpoints existentes de alias.
- **No** agregar histórico/series temporales (cómo evoluciona el % en el tiempo). Si hace falta, va en una historia con su propia tabla de snapshots.
- **No** mandar el reporte por mail / Slack / cron.
- **No** implementar nada en el legacy v3.

## Ver también

- [[Libre Opcion/Libre Opcion|Índice del proyecto]]
- [[Libre Opcion/tareas/API - Feat - Recategorizar productos sin categoría|API - Feat - Recategorizar productos sin categoría]] — historia previa, define el ciclo completo "ver atasco → crear alias → recategorizar → ver mejora"
- [[Libre Opcion/tareas/API - Refactor - Migrar recurso de preguntas y respuestas a v4|API - Refactor - Migrar recurso de preguntas y respuestas a v4]] — referencia del patrón Controller → Service → Repository en v4
- `sitio-api-rest-v3/app/models/CategoriaModel.php:117` — normalización del nombre crudo a replicar exacto en SQL
- `sitio-api-rest-v3/app/models/CategoriaModel.php:635` — lógica de matching legacy (solo lectura, no se reimplementa en esta historia)
- `sql/201808061125-agrega-algunos-indices.sql` — revisar antes de proponer un índice nuevo
