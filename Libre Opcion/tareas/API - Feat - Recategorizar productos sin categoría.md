# API - Feat - Recategorizar productos sin categoría (v4, background job)

**Proyecto:** [[Libre Opcion/Libre Opcion|Libre Opción]]
**Estado:** Pendiente
**Fecha:** 2026-04-15

Crear desde cero en `sitio-api-rest-v4-laravel` (Laravel 10) un **job en segundo plano** que recorra los productos sin categorizar, intente asignarles categoría usando la lógica existente del legacy (`adivinarCategoriaProductoImportado`), y deje un **registro de la corrida** con contadores y resultado por producto. La acción se dispara desde un endpoint REST que devuelve inmediatamente el `run_id` y se consulta después.

Hoy la categorización **solo corre una vez**, cuando el cron `sitio-api-rest-v3/app/crons/importar_productos_nuevos_de_nb.php:225` da de alta el producto. Si el matching falla, el producto queda con `id_categoria_lo = 0` para siempre — aunque después agreguemos un alias nuevo que lo hubiera resuelto. Esta historia da la herramienta para repasar ese backlog cuando queramos, sin esperar al cron y sin tocar el legacy.

> Esta historia **no reemplaza** al cron ni a la lógica de matching del legacy. Solo expone el `adivinar` ya existente como una tarea ejecutable a demanda desde v4, persiste un log de cada corrida, y agrega una columna en `productos` para saber por qué vía se categorizó cada uno.

**Endpoints alcance:**

| # | Método | Ruta v4 | Estado |
|---|--------|---------|--------|
| 1 | `POST` | `/v4/categorias-admin/recategorizar` | A crear (dispatch del job) |
| 2 | `GET`  | `/v4/categorias-admin/recategorizar/runs` | A crear (listado paginado) |
| 3 | `GET`  | `/v4/categorias-admin/recategorizar/runs/{run_id}` | A crear (detalle) |

**Referencia de la lógica de matching (legacy, solo lectura):**
- `sitio-api-rest-v3/app/models/CategoriaModel.php:281` — `actualizarProductoConCategoriaAdivinada($producto_id)`
- `sitio-api-rest-v3/app/models/CategoriaModel.php:635` — `adivinarCategoriaProductoImportado($nombre_categoria, $titulo_producto)` (las 3 ramas: nombre, alias, switch hardcodeado)

**Estado actual en v4:** no existe ningún recurso `categorias-admin`, ni jobs relacionados con categorización. Hay que crear el grupo de rutas, el job, las migraciones, los DTOs y los controllers/services/repositories.

---

## 1) POST — Disparar la recategorización

### Endpoint

`POST /v4/categorias-admin/recategorizar`

### Tabla de definición del recurso

| Campo | Detalle |
|---|---|
| **Método** | `POST` |
| **Autenticación** | Requerida (`token.auth`) |
| **Perfil** | `admin` |
| **Path param** | Ninguno |
| **Query params** | Ninguno |
| **Request body** | `{ "producto_ids": int[], "limite": int, "solo_con_stock": bool }` — todos opcionales |

### Reglas del body

- **`producto_ids` (int[], opcional):** si viene, el job procesa **solo** esos IDs (sin importar si tenían categoría — el admin pidió expresamente recategorizarlos, ej: porque acaba de crear un alias y quiere reasignarlos). Tope 5000.
- **`limite` (int, opcional, default 500, tope 5000):** **se ignora si vino `producto_ids`**. Si no, el job toma los primeros `limite` productos con `id_categoria_lo = 0` ordenados por `id ASC`.
- **`solo_con_stock` (bool, opcional, default `false`):** **se ignora si vino `producto_ids`**. Si `true`, restringe el lote a productos con `stock_cliente > 0`. Es la opción "atacar primero los que están en góndola".

### Ejemplo de llamada

`POST /v4/categorias-admin/recategorizar`

```json
{
  "limite": 1000,
  "solo_con_stock": true
}
```

### Respuesta esperada

`202 Accepted` — el trabajo quedó encolado, devuelve el `run_id` para consultarlo.

```json
{
  "run_id": 42,
  "status": "pending",
  "params": {
    "producto_ids": null,
    "limite": 1000,
    "solo_con_stock": true
  },
  "url_consulta": "/v4/categorias-admin/recategorizar/runs/42"
}
```

### Casos especiales

- **Ya hay otra corrida en estado `running`:** devolver `409 Conflict` con `{ "error": "Ya hay una recategorización en curso", "run_id": <id de la corrida activa> }`. **Solo una corrida activa a la vez** — ver Notas.
- **`producto_ids` vacío `[]`:** tratarlo como "no vino" y caer al modo lote.
- **`producto_ids` con más de 5000:** 422 con `{ "error": "Máximo 5000 producto_ids por corrida" }`.
- **Sin auth (401)** y **403 si no es admin:** respuestas estándar.

### Lógica del controller

1. Validar request.
2. Verificar que no haya otra `categorizacion_runs.status = 'running'`. Si la hay → 409.
3. Crear row en `categorizacion_runs` con `status = 'pending'` y los params.
4. Despachar `RecategorizarProductosJob::dispatch($runId)` a la cola.
5. Devolver 202 con el `run_id`.

---

## 2) GET — Listar corridas

### Endpoint

`GET /v4/categorias-admin/recategorizar/runs`

### Tabla de definición del recurso

| Campo | Detalle |
|---|---|
| **Método** | `GET` |
| **Autenticación** | Requerida (`token.auth`) |
| **Perfil** | `admin` |
| **Query params** | `p` (int, opcional, default 1), `status` (string, opcional, uno de `pending\|running\|done\|failed`) |
| **Request body** | Ninguno |

### Respuesta esperada

`200 OK` — Page DTO con corridas ordenadas por `started_at DESC`.

```json
{
  "data": [
    {
      "run_id": 42,
      "status": "done",
      "started_at": "2026-04-15T14:00:00",
      "finished_at": "2026-04-15T14:02:11",
      "params": { "producto_ids": null, "limite": 1000, "solo_con_stock": true },
      "resumen": {
        "procesados": 1000,
        "actualizados": 612,
        "sin_match": 388,
        "via": { "nombre": 240, "alias": 320, "switch": 52 }
      }
    }
  ],
  "page": 1,
  "per_page": 20,
  "total": 7
}
```

---

## 3) GET — Detalle de una corrida

### Endpoint

`GET /v4/categorias-admin/recategorizar/runs/{run_id}`

### Tabla de definición del recurso

| Campo | Detalle |
|---|---|
| **Método** | `GET` |
| **Autenticación** | Requerida (`token.auth`) |
| **Perfil** | `admin` |
| **Path param** | `run_id` (int) |
| **Query params** | `incluir_detalle` (bool, opcional, default `false`) — si `true`, devuelve también el array `detalle` con un row por producto procesado |
| **Request body** | Ninguno |

### Respuesta esperada

`200 OK`

```json
{
  "run_id": 42,
  "status": "done",
  "started_at": "2026-04-15T14:00:00",
  "finished_at": "2026-04-15T14:02:11",
  "params": { "producto_ids": null, "limite": 1000, "solo_con_stock": true },

  "resumen": {
    "procesados": 1000,
    "actualizados": 612,
    "sin_match": 388,
    "via": { "nombre": 240, "alias": 320, "switch": 52 }
  },

  "snapshot_post_corrida": {
    "productos_categorizados":          15910,
    "productos_sin_categorizar":         2522,
    "productos_sin_categorizar_con_stock": 318
  },

  "detalle": [
    { "producto_id": 12345, "id_categoria_lo": 14, "via": "alias",     "antes": 0 },
    { "producto_id": 12346, "id_categoria_lo": 27, "via": "switch",    "antes": 0 },
    { "producto_id": 12347, "id_categoria_lo": 0,  "via": "sin_match", "antes": 0 }
  ],

  "error": null
}
```

### Reglas de los bloques

- **`resumen`** — contadores **de la corrida** (lo que tocó este run, no el estado global). `procesados` = total de productos que el job miró. `actualizados` = subset que efectivamente cambió `id_categoria_lo`. `sin_match` = procesados que quedaron en cero. `via` = breakdown de los `actualizados` por rama del matcher.
- **`snapshot_post_corrida`** — contadores **globales** del catálogo medidos al terminar la corrida (no en tiempo real). Es la foto del catálogo después de aplicar este run, para que el admin vea de un vistazo cómo quedó la base sin tener que llamar también a `stats-categorizacion`. Los 3 valores que pidió el admin:
  - `productos_categorizados` — `COUNT(*) WHERE id_categoria_lo > 0`
  - `productos_sin_categorizar` — `COUNT(*) WHERE id_categoria_lo = 0`
  - `productos_sin_categorizar_con_stock` — `COUNT(*) WHERE id_categoria_lo = 0 AND stock_cliente > 0` (los urgentes — están en góndola)
- **`detalle`** — solo si `incluir_detalle=true`. Es lo que se persistió en `categorizacion_runs_items`. `antes` es el `id_categoria_lo` que tenía antes de la corrida (siempre `0` cuando no llega `producto_ids`, puede ser distinto cuando vino lista explícita).
- **`error`** — `null` salvo que `status = 'failed'`, en cuyo caso lleva el mensaje del exception.

### Casos especiales

- **`run_id` no existe:** 404 `{ "error": "Corrida no encontrada" }`.
- **`status = pending` o `running`:** devuelve igual, pero `finished_at = null` y `resumen` con los contadores parciales acumulados hasta el momento (el job los va escribiendo cada N productos — ver Notas). `snapshot_post_corrida = null` mientras no haya terminado.

---

## El job — `RecategorizarProductosJob`

Vive en `app/Jobs/CategoriasAdmin/RecategorizarProductosJob.php`, implementa `ShouldQueue`, en cola `categorizacion`. Una sola corrida activa a la vez (ver Notas).

### Pseudocódigo

```
handle():
  run = repo.findRun(runId)
  repo.markRunning(runId)

  productos = service.buildLote(run.params)   // según producto_ids o limite+solo_con_stock
  contadores = { procesados:0, actualizados:0, sin_match:0, via:{nombre:0,alias:0,switch:0} }

  foreach producto in productos:
      resultado = matcher.intentarCategorizar(producto)
      // resultado = { id_categoria_lo:int, via:'nombre'|'alias'|'switch'|'sin_match' }

      if resultado.via != 'sin_match':
          repo.actualizarProducto(producto.id, resultado.id_categoria_lo, resultado.via)
          contadores.actualizados++
          contadores.via[resultado.via]++
      else:
          contadores.sin_match++

      contadores.procesados++

      repo.persistirItem(runId, producto.id, resultado, antes=producto.id_categoria_lo)

      if contadores.procesados % 50 == 0:
          repo.actualizarResumenParcial(runId, contadores)  // para que el GET de detalle muestre progreso

  snapshot = repo.snapshotGlobal()
  repo.markDone(runId, contadores, snapshot)

failed(Throwable $e):
  repo.markFailed(runId, $e->getMessage())
```

### `Matcher` — qué tiene que implementar

`app/Service/CategoriasAdmin/CategoriaMatcher.php`

```php
public function intentarCategorizar(object $producto): array
// retorna ['id_categoria_lo' => int, 'via' => 'nombre'|'alias'|'switch'|'sin_match']
```

Replica las 3 ramas del legacy (`CategoriaModel.php:635`), **en este orden**:

1. **`nombre`** — match exacto contra `[LO].[dbo].[categorias].nombre` con la normalización `LOWER(REPLACE(nombre,'-',' '))` que ya usa el legacy en `CategoriaModel.php:117`.
2. **`alias`** — match contra `[LO].[dbo].[categoriasAlias].nombre` con la misma normalización; si pega, devuelve el `categoria_id` asociado.
3. **`switch`** — el switch hardcodeado de `adivinarCategoriaProductoImportado` líneas 658+. **Portarlo tal cual** a un método PHP en `CategoriaMatcher`. Sí, es feo. **No** mejorar la lógica en esta historia — el objetivo es paridad funcional con el legacy. Si encontrás casos del switch que están mal, anotarlos en una lista para una historia futura.

> Hay un helper legacy `HelperProducto::es($keyword)` que el switch usa para inspeccionar el título. Reimplementarlo en v4 como método privado de `CategoriaMatcher` (`titulo->contiene($palabra)`). No es lógica complicada — un `stripos` con normalización.

> El matcher **no** pisa `id_categoria_lo` ni hace `UPDATE`. Solo decide. El job es el que escribe.

---

## Tablas involucradas

### Lectura

- `[CS].[dbo].[productos]` — `id`, `titulo`, `id_familia_original` (= "categoria" cruda del importador NB), `categoria` (texto crudo de otros importadores), `id_categoria_lo`, `id_vendedor`, `stock_cliente`. Es la fuente del lote.
- `[LO].[dbo].[categorias]` — `id`, `nombre`. Match directo (rama 1).
- `[LO].[dbo].[categoriasAlias]` — `categoria_id`, `nombre`. Match por alias (rama 2).

### Escritura

- `[CS].[dbo].[productos]` — `id_categoria_lo` y `id_categoria_lo_via` (columna nueva, ver migraciones). **Solo estos dos campos.** No tocar `categoria` (texto crudo importado) ni nada más.
- `categorizacion_runs` (tabla nueva, ver migraciones) — un row por corrida.
- `categorizacion_runs_items` (tabla nueva, ver migraciones) — un row por producto procesado en cada corrida.

### Tablas NUEVAS — migraciones

#### Migración A — agregar `id_categoria_lo_via` a `productos`

Va al directorio `sql/` del legacy (las migraciones siguen viviendo ahí), formato `YYYYMMDDhhmm-agrega-via-categorizacion-a-productos.sql`. SQL Server.

```sql
ALTER TABLE [CS].[dbo].[productos]
ADD id_categoria_lo_via varchar(20) NULL
    CONSTRAINT DF_productos_id_categoria_lo_via DEFAULT NULL;
```

Valores posibles: `'nombre'`, `'alias'`, `'switch'`, `'manual'` (este último para cuando un admin asigna categoría desde el ABM, fuera de esta historia — solo lo dejamos previsto).

> Productos categorizados antes de esta migración quedan con `id_categoria_lo_via = NULL`. Es esperado: no sabemos por qué vía les llegó. La columna empieza a poblarse desde la primera corrida del job en adelante.

#### Migración B — `categorizacion_runs`

Tabla nativa de Laravel v4, va por el sistema de migraciones de Laravel (no por `sql/`). Conexión `sqlsrv`.

```php
Schema::connection('sqlsrv')->create('categorizacion_runs', function (Blueprint $t) {
    $t->bigIncrements('id');
    $t->string('status', 20);              // pending | running | done | failed
    $t->json('params');                    // body original del POST
    $t->unsignedInteger('procesados')->default(0);
    $t->unsignedInteger('actualizados')->default(0);
    $t->unsignedInteger('sin_match')->default(0);
    $t->unsignedInteger('via_nombre')->default(0);
    $t->unsignedInteger('via_alias')->default(0);
    $t->unsignedInteger('via_switch')->default(0);
    $t->unsignedInteger('snapshot_categorizados')->nullable();
    $t->unsignedInteger('snapshot_sin_categorizar')->nullable();
    $t->unsignedInteger('snapshot_sin_categorizar_con_stock')->nullable();
    $t->text('error')->nullable();
    $t->timestamp('started_at')->nullable();
    $t->timestamp('finished_at')->nullable();
    $t->timestamps();
    $t->index(['status', 'started_at']);
});
```

#### Migración C — `categorizacion_runs_items`

```php
Schema::connection('sqlsrv')->create('categorizacion_runs_items', function (Blueprint $t) {
    $t->bigIncrements('id');
    $t->unsignedBigInteger('run_id');
    $t->unsignedInteger('producto_id');
    $t->unsignedInteger('antes')->default(0);             // id_categoria_lo previo
    $t->unsignedInteger('id_categoria_lo')->default(0);   // resultado
    $t->string('via', 20);                                 // nombre|alias|switch|sin_match
    $t->timestamp('created_at')->useCurrent();

    $t->foreign('run_id')->references('id')->on('categorizacion_runs')->cascadeOnDelete();
    $t->index('run_id');
});
```

### NO tocar

- `[LO].[dbo].[categoriasAlias]` — la administra el admin desde los endpoints existentes de alias. El job **lee** alias pero nunca los crea ni borra.
- El switch hardcodeado en su nueva versión PHP — **no** agregar casos nuevos en esta historia. Si encontrás nombres que faltan, se resuelven creando alias desde el ABM, no parchando código.

---

## Esquema de campos compartido

### `RecategorizarRunDto`

| Campo | Tipo | Descripción |
|---|---|---|
| run_id | int | PK de `categorizacion_runs` |
| status | string | `pending` \| `running` \| `done` \| `failed` |
| started_at | datetime ISO 8601 \| null | Cuándo arrancó el job (null si todavía está `pending`) |
| finished_at | datetime ISO 8601 \| null | Cuándo terminó (null si todavía no terminó) |
| params | object | Body original del POST |
| resumen | `ResumenCorridaDto` | Contadores de la corrida |
| snapshot_post_corrida | `SnapshotDto` \| null | Contadores globales medidos al cierre |
| detalle | `ItemCorridaDto[]` \| null | Solo si `incluir_detalle=true` |
| error | string \| null | Mensaje si `status = failed` |

### `ResumenCorridaDto`

| Campo | Tipo |
|---|---|
| procesados | int |
| actualizados | int |
| sin_match | int |
| via | `{ nombre: int, alias: int, switch: int }` |

### `SnapshotDto`

| Campo | Tipo | Descripción |
|---|---|---|
| productos_categorizados | int | `id_categoria_lo > 0` |
| productos_sin_categorizar | int | `id_categoria_lo = 0` |
| productos_sin_categorizar_con_stock | int | `id_categoria_lo = 0 AND stock_cliente > 0` |

### `ItemCorridaDto`

| Campo | Tipo |
|---|---|
| producto_id | int |
| antes | int |
| id_categoria_lo | int |
| via | string (`nombre`\|`alias`\|`switch`\|`sin_match`) |

---

## Entregables

### Controllers (`app/Http/Controllers/CategoriasAdmin/`)

| Controller | Acción | Ruta |
|---|---|---|
| `RecategorizarDispatchController` | `__invoke` | `POST /categorias-admin/recategorizar` |
| `RecategorizarRunsListController` | `__invoke` | `GET /categorias-admin/recategorizar/runs` |
| `RecategorizarRunDetalleController` | `__invoke` | `GET /categorias-admin/recategorizar/runs/{run_id}` |

### Service (`app/Service/CategoriasAdmin/`)

- `RecategorizarService`
  - `dispatch(RecategorizarRequest $req): RecategorizarRunDto` — valida que no haya otra running, crea el run, dispatch del job, devuelve el DTO inicial.
  - `obtenerRun(int $runId, bool $incluirDetalle): RecategorizarRunDto`
  - `listarRuns(?string $status, int $page): array`
  - `buildLote(array $params): iterable<object>` — usado por el job para armar el lote según `producto_ids` / `limite` / `solo_con_stock`.
  - `snapshotGlobal(): SnapshotDto` — las 3 queries del bloque snapshot.
- `CategoriaMatcher` — las 3 ramas del legacy en PHP puro (descripto arriba).

### Repository (`app/Repository/CategoriasAdmin/`)

- `CategorizacionRunRepository`
  - `crear(array $params): int` (devuelve `run_id`)
  - `marcarRunning(int $runId): void`
  - `marcarDone(int $runId, ResumenCorridaDto $resumen, SnapshotDto $snapshot): void`
  - `marcarFailed(int $runId, string $error): void`
  - `actualizarResumenParcial(int $runId, ResumenCorridaDto $resumen): void`
  - `findRun(int $runId): ?object`
  - `listar(?string $status, int $page, int $perPage): array`
  - `count(?string $status): int`
  - `existeRunActivo(): ?int`
  - `persistirItem(int $runId, int $productoId, int $antes, int $idCategoriaLo, string $via): void`
  - `obtenerItems(int $runId): array`
- `ProductoCategorizacionRepository`
  - `obtenerLotePorIds(array $ids): iterable<object>`
  - `obtenerLotePorFiltro(int $limite, bool $soloConStock): iterable<object>`
  - `actualizarCategoria(int $productoId, int $idCategoriaLo, string $via): void`
  - `obtenerCategoriasMap(): array<string,int>` — usado por el matcher (rama 1)
  - `obtenerAliasMap(): array<string,int>` — usado por el matcher (rama 2)
  - `snapshotTotales(): SnapshotDto`

> Los maps de categorías y alias se cargan **una vez por corrida** al arrancar el job, no por producto. Son ~cientos de filas, entran tranquilos en memoria, y evita N+1 contra la base.

### Job (`app/Jobs/CategoriasAdmin/`)

- `RecategorizarProductosJob` — `ShouldQueue`, queue `categorizacion`, `tries = 1` (no reintentar automáticamente: si falla queremos investigar a mano).

### Request validation

- `RecategorizarRequest` — valida `producto_ids` (array|nullable, max 5000, cada item int), `limite` (int|nullable, default 500, clampea a [1,5000]), `solo_con_stock` (bool|nullable, default false).
- `RunDetalleRequest` — valida `incluir_detalle` (bool|nullable, default false).
- `RunsListRequest` — valida `p` (int|nullable, default 1), `status` (string|nullable, in:pending,running,done,failed).

### Rutas — `app/routes/api.php`

```php
Route::middleware(['token.auth', 'profile:admin'])
    ->prefix('categorias-admin')
    ->group(function () {
        Route::post('recategorizar', RecategorizarDispatchController::class);
        Route::get('recategorizar/runs', RecategorizarRunsListController::class);
        Route::get('recategorizar/runs/{runId}', RecategorizarRunDetalleController::class);
    });
```

> Si en v4 todavía no existe el middleware `profile:admin`, usar el helper que esté en uso (mirar cómo otros endpoints admin protegen el perfil — no inventes uno nuevo solo para esta historia).

---

## Criterios de aceptación

- [ ] `POST /v4/categorias-admin/recategorizar` devuelve 202 con `run_id` y deja la corrida en `pending` en `categorizacion_runs`
- [ ] El job `RecategorizarProductosJob` se ejecuta en cola `categorizacion` y mueve la corrida `pending → running → done` (o `failed` si tira excepción)
- [ ] Si ya hay otra corrida `running`, el POST devuelve 409 con el `run_id` de la activa y **no** crea una nueva
- [ ] Cuando llega `producto_ids`, el job procesa exactamente esos productos (incluso si ya tenían `id_categoria_lo > 0`)
- [ ] Cuando **no** llega `producto_ids`, el job toma los primeros `limite` productos con `id_categoria_lo = 0`, y respeta `solo_con_stock` filtrando por `stock_cliente > 0`
- [ ] Cada producto que matchea actualiza `[CS].[dbo].[productos].id_categoria_lo` **y** `id_categoria_lo_via` con el valor de la rama (`nombre` / `alias` / `switch`)
- [ ] La corrida persiste un row en `categorizacion_runs_items` por **cada producto procesado** (matcheado o no), con `antes`, `id_categoria_lo` resultante y `via`
- [ ] `GET /v4/categorias-admin/recategorizar/runs/{run_id}` devuelve `resumen` con `procesados`, `actualizados`, `sin_match` y `via.{nombre,alias,switch}` correctos
- [ ] `GET .../runs/{run_id}` devuelve `snapshot_post_corrida` con los 3 contadores globales: `productos_categorizados`, `productos_sin_categorizar`, `productos_sin_categorizar_con_stock`
- [ ] `GET .../runs/{run_id}?incluir_detalle=true` devuelve también el array `detalle` desde `categorizacion_runs_items`
- [ ] Mientras la corrida está `running`, los contadores parciales se ven en el detalle (se actualizan cada ~50 productos)
- [ ] `GET /v4/categorias-admin/recategorizar/runs` lista paginado, ordenado por `started_at DESC`, filtrable por `status`
- [ ] El cron legacy `importar_productos_nuevos_de_nb.php` sigue funcionando exactamente igual (no hay regresión en la importación de nuevos productos)
- [ ] Las 3 migraciones (productos.id_categoria_lo_via, categorizacion_runs, categorizacion_runs_items) corren limpias en una base nueva
- [ ] Todos los endpoints protegidos con `token.auth` + perfil `admin`
- [ ] `vendor/bin/pint` pasa sin diff

---

## Notas técnicas

- **Una sola corrida activa a la vez.** Es a propósito: evita que dos jobs pisen el mismo producto y dejen contadores inconsistentes. La verificación del `running` se hace en el controller (rápido para devolver 409) **y** al inicio del job con `SELECT ... FOR UPDATE` o un lock equivalente, por las dudas de carrera entre dos POSTs casi simultáneos. Si esto resulta restrictivo más adelante, lo flexibilizamos en otra historia.
- **El job no reintenta automáticamente** (`tries = 1`). Si falla queremos abrir el `categorizacion_runs` y mirar qué pasó — no que el sistema mate la base con reintentos en loop.
- **Contadores parciales:** el job hace `actualizarResumenParcial` cada 50 productos para que el detalle muestre progreso si el admin lo consulta mientras corre. No es batch atómico — si el job revienta a mitad de corrida, el `categorizacion_runs_items` ya tiene los productos procesados hasta ahí y el `resumen` refleja esos contadores parciales. El producto en sí queda con la categoría que el job alcanzó a escribir (lo cual está bien — no hay nada que rollback-ear).
- **Snapshot al final:** las 3 queries del `snapshot_post_corrida` se corren **una vez**, al terminar exitosamente, y se guardan congeladas en las columnas `snapshot_*` del run. **No** se calculan al vuelo cada vez que el admin pide el detalle: queremos que el snapshot sea la foto del momento de cierre, no de "ahora".
- **Sin Eloquent**, igual que el resto de v4: `DB::connection('sqlsrv')->select(..., [...])` con bindings posicionales.
- **Maps de categorías y alias en memoria por corrida:** evitar N+1. Cargás ~cientos de filas una sola vez al arrancar el job y matcheás contra el array.
- **Normalización idéntica al legacy:** la rama 1 y 2 del matcher tienen que normalizar igual que `CategoriaModel.php:117` (`LOWER(REPLACE(nombre,'-',' '))` + trim). Si esto se desvía, productos que el legacy categorizaba dejan de categorizarse — regresión silenciosa.
- **Switch hardcodeado:** porting **literal** del legacy. Es código viejo y no muy lindo, pero la única forma de garantizar paridad es replicarlo tal cual. Si querés mejorarlo, va en una historia aparte de "refactorizar matcher de categorías" después de validar que esta corre bien.
- **Performance del lote:** procesar 5000 productos con maps en memoria debería tardar pocos segundos. Si en producción tarda más de un par de minutos para 5000, el cuello probablemente esté en los `UPDATE` uno por uno — agrupar en transacciones de 100 antes de optimizar más a fondo.
- **`stock_cliente`:** confirmar el nombre exacto de la columna de stock en `[CS].[dbo].[productos]` antes de implementar (`sql/201808301039-agrega-control-de-stock.sql` define `stock_cliente`). Si en algún momento se renombró, ajustar el WHERE del modo `solo_con_stock` y de la query de `productos_sin_categorizar_con_stock`.
- **DATEFORMAT:** SQL Server prod usa `mdy`. Las fechas que devuelve el endpoint van en ISO 8601 con `T`.
- **Patrón Controller → Service → Repository:** una acción por controller (`__invoke`).
- **Lint:** `vendor/bin/pint` antes de commitear.
- **Sin tests automatizados todavía** — el job tiene mucho I/O contra una base con esquema real; armar fixtures equivalentes no escala. Smoke test manual con Postman + queue worker corriendo en local alcanza para mergear. Si después se decide invertir en tests, va en su propia historia.

## Cómo probarlo

1. Correr las 3 migraciones en una base de QA con datos productivos copiados.
2. Levantar el queue worker: `php artisan queue:work --queue=categorizacion`.
3. Buscar un puñado de productos con `id_categoria_lo = 0` cuyo `categoria` cruda matchee contra un alias existente:
   ```sql
   SELECT TOP 20 p.id, p.titulo, p.categoria, p.id_familia_original, p.stock_cliente
   FROM [CS].[dbo].[productos] p
   WHERE p.id_categoria_lo = 0
   ORDER BY p.id DESC;
   ```
4. **Modo lista:** `POST /v4/categorias-admin/recategorizar` con `{ "producto_ids": [<los del paso 3>] }`. Verificar 202 + `run_id`.
5. Consultar `GET /v4/categorias-admin/recategorizar/runs/{run_id}?incluir_detalle=true` y confirmar que:
   - Productos con alias matcheable quedaron con `via: "alias"` y `id_categoria_lo` correcto.
   - `[CS].[dbo].[productos]` tiene `id_categoria_lo_via = 'alias'` para esos mismos productos.
6. **Modo lote con stock:** `POST` con `{ "limite": 200, "solo_con_stock": true }`. Verificar que el `snapshot_post_corrida.productos_sin_categorizar_con_stock` haya bajado en una cantidad consistente con `resumen.actualizados`.
7. **Modo lote sin stock:** `POST` con `{ "limite": 50 }` solo (default `solo_con_stock=false`). Verificar que procesa los más viejos del backlog.
8. **Conflicto:** disparar dos POSTs seguidos rápido. El segundo tiene que devolver 409 con el `run_id` del primero.
9. **Listado:** `GET /v4/categorias-admin/recategorizar/runs?status=done` y verificar que aparece la corrida con su `resumen` resumido.
10. (Opcional) Forzar un fallo en el job (ej: tirar exception a mano en el matcher) y verificar que la corrida queda `failed` con `error` poblado y `snapshot_post_corrida = null`.

## Fuera de alcance (no hacer en esta historia)

- **No** crear pantalla de admin frontend. Los endpoints se consumen desde Postman / Restler Client por ahora; la UI va en otra historia si validamos que el flujo se usa seguido.
- **No** automatizar la corrida via cron. Esta historia entrega solo el dispatch a demanda. Cuando confirmemos que el job es estable y los resultados son razonables, en otra historia se agenda.
- **No** mejorar la lógica de matching del legacy. Paridad funcional, nada más.
- **No** tocar el cron `importar_productos_nuevos_de_nb.php` para que use el nuevo matcher. Eso va en otra historia (probablemente "deprecate del módulo de categorización del legacy").
- **No** implementar nada en el legacy v3.
- **No** cachear nada.
- **No** mandar notificación / mail / Slack al terminar la corrida. Si después lo querés, va aparte.

## Ver también

- [[Libre Opcion/Libre Opcion|Índice del proyecto]]
- [[Libre Opcion/tareas/API - Feat - Estadísticas de categorización de productos|API - Feat - Estadísticas de categorización de productos]] — historia hermana, expone los stats que esta historia mueve la aguja
- [[Libre Opcion/tareas/API - Refactor - Migrar recurso de preguntas y respuestas a v4|API - Refactor - Migrar recurso de preguntas y respuestas a v4]] — referencia del patrón Controller → Service → Repository en v4
- `sitio-api-rest-v3/app/models/CategoriaModel.php:117` — normalización del nombre crudo a replicar exacto en el matcher
- `sitio-api-rest-v3/app/models/CategoriaModel.php:281` — `actualizarProductoConCategoriaAdivinada` (la versión legacy de un solo producto)
- `sitio-api-rest-v3/app/models/CategoriaModel.php:635` — `adivinarCategoriaProductoImportado` (las 3 ramas: nombre, alias, switch)
- `sitio-api-rest-v3/app/crons/importar_productos_nuevos_de_nb.php:225` — único lugar donde hoy se dispara la categorización; **no se toca** en esta historia
- `sql/201808301039-agrega-control-de-stock.sql` — define `stock_cliente` (confirmar antes de implementar)
- `sql/201808061125-agrega-algunos-indices.sql` — revisar antes de proponer un índice nuevo si el lote queda lento
