# API - Refactor - Migrar recurso de preguntas y respuestas a v4

**Proyecto:** [[Libre Opcion/Libre Opcion|Libre Opción]]
**Estado:** Pendiente
**Fecha:** 2026-04-09

Migrar los endpoints faltantes del recurso **Preguntas y Respuestas** desde el legacy `sitio-api-rest-v3` (PHP) hacia `sitio-api-rest-v4-laravel` (Laravel 10), siguiendo el patrón Controller → Service → Repository del proyecto. El contrato de respuesta debe mantenerse compatible con los clientes que ya consumen el recurso desde el legacy, salvo el endpoint de bloquear usuario, que queda **deprecado**.

**Endpoints alcance:**

| # | Método | Ruta v4 | Estado |
|---|--------|---------|--------|
| 1 | `DELETE` | `/v4/productos/preguntas/{pregunta_id}` | A migrar |
| 2 | `POST` | `/v4/productos/preguntas/producto-bloquear-usuario` | Deprecado (documentar y no implementar) |
| 3 | `POST` | `/v4/productos/preguntas/respuestas/{respuesta_id}/calificar` | A migrar |
| 4 | `GET`  | `/v4/productos/preguntas/usuario` | A migrar |

**Referencia legacy:** `sitio-api-rest-v3/app/resources/ProductosPreguntas.php` + `app/models/ProductoPreguntaModel.php`

**Estado actual en v4:** existe `Questions/SellerQuestionsController` y `BuyerQuestion` (POST de pregunta), pero faltan estos 4 endpoints.

---

## 1) DELETE — Ocultar pregunta

### Endpoint

`DELETE /v4/productos/preguntas/{pregunta_id}`

### Tabla de definición del recurso

| Campo | Detalle |
|---|---|
| **Método** | `DELETE` |
| **Autenticación** | Requerida (`token.auth`) |
| **Perfil** | `vendedor` |
| **Path param** | `pregunta_id` (int) — id de la pregunta a ocultar |
| **Query params** | Ninguno |
| **Request body** | Ninguno |

### Ejemplo de llamada

`DELETE /v4/productos/preguntas/12345`

### Respuesta esperada

`200 OK` — sin body, o `{ "success": true }` para uniformar con el resto de v4.

### Casos especiales

- **Pregunta no existe (404):** `{ "error": "La pregunta no existe" }`
- **Pregunta de otro vendedor (403):** `{ "error": "No tenés permiso para ocultar esta pregunta" }`
- **Sin auth (401):** respuesta estándar de `token.auth`.

### Lógica

1. Obtener la pregunta por id desde `[LO].[dbo].[productosPreguntas]`.
2. Validar que `vendedor_id` de la pregunta == `vendedor_id` del usuario logueado.
3. Soft delete: `UPDATE productosPreguntas SET ocultar = 1 WHERE id = ?`.

### Query SQL

```sql
UPDATE [LO].[dbo].[productosPreguntas]
SET ocultar = 1
WHERE id = ?;
```

### Origen legacy

`ProductosPreguntas::eliminarPregunta()` — `sitio-api-rest-v3/app/resources/ProductosPreguntas.php:130`
Modelo: `ProductoPreguntaModel::eliminar()` línea 670.

---

## 2) POST — Bloquear usuario en preguntas (DEPRECADO)

### Endpoint

`POST /v4/productos/preguntas/producto-bloquear-usuario`

### Estado

**Deprecado.** Documentar en v4 con respuesta 410 Gone o 404, según convención del proyecto. **No implementar lógica nueva.**

### Tabla de definición del recurso (legacy, solo referencia)

| Campo | Detalle |
|---|---|
| **Método legacy** | `POST` |
| **Body** | `{ "producto_id": int, "usuario_id": int }` |
| **Tabla afectada** | `[LO].[dbo].[productosPreguntasUsuariosBloqueados]` |

### Respuesta sugerida en v4

```json
{
  "error": "Endpoint deprecado",
  "message": "El bloqueo de usuario en preguntas ya no está disponible."
}
```
Status: `410 Gone`.

### Origen legacy

`ProductosPreguntas::bloquearProductoPreguntasUsuario()` — `sitio-api-rest-v3/app/resources/ProductosPreguntas.php:215`
Modelo: `ProductoPreguntaModel::bloquearUsuarioPreguntasProducto()` línea 697.

> **Nota:** El handler legacy tenía un bug — referenciaba `preguntaId` que no estaba en los params validados. Otro motivo más para no migrarlo tal cual.

---

## 3) POST — Calificar respuesta útil

### Endpoint

`POST /v4/productos/preguntas/respuestas/{respuesta_id}/calificar`

### Tabla de definición del recurso

| Campo | Detalle |
|---|---|
| **Método** | `POST` |
| **Autenticación** | Requerida (`token.auth`) |
| **Perfil** | `comprador` (autor de la pregunta) — **NO** vendedor (corregir bug del legacy) |
| **Path param** | `respuesta_id` (int) — id de la respuesta a calificar |
| **Query params** | Ninguno |
| **Request body** | `{ "util": bool }` — true si fue útil, false si no |

### Ejemplo de llamada

`POST /v4/productos/preguntas/respuestas/456/calificar`

```json
{
  "util": true
}
```

### Lógica

1. Obtener la pregunta por `respuesta_id` (la respuesta pertenece a una pregunta).
2. Validar que `pregunta.usuario_id` == usuario logueado (solo el autor de la pregunta puede calificar).
3. `UPDATE productosRespuestas SET respuesta_util = ? WHERE id = ?`.
4. **Side effect — disparar notificación al vendedor** (web + push) avisándole que su respuesta fue calificada como útil/no útil.

### Query SQL

```sql
UPDATE [LO].[dbo].[productosRespuestas]
SET respuesta_util = ?
WHERE id = ?;
```

### Respuesta esperada

`200 OK` — devuelve el DTO completo de la pregunta con la respuesta actualizada.

```json
{
  "id": 123,
  "texto": "¿Tiene garantía?",
  "fecha": "2026-04-08T10:30:00",
  "usuario": { "id": 789, "nombre": "Juan Pérez", "avatar": "...", "bloqueado": false },
  "producto": { "id": 999, "nombre": "Notebook ASUS X415", "img": "..." },
  "vendedor": { "id": 42, "usuarioId": 100, "nombre": "TecnoStore" },
  "respuesta": {
    "id": 456,
    "texto": "Sí, 12 meses oficial.",
    "fecha": "2026-04-08T11:15:00",
    "usuario_id": 100,
    "respuesta_util": true
  }
}
```

### Casos especiales

- **Pregunta/respuesta no existe (404):** `{ "error": "La respuesta no existe" }`
- **No es el autor de la pregunta (403):** `{ "error": "Solo el autor de la pregunta puede calificar" }`

### Notificación (lógica del legacy a replicar)

Después del UPDATE, el legacy crea una notificación en 2 canales:
- **website:** con URL al producto y texto personalizado.
- **push:** mismo contenido, prioridad 1.

En v4 esto se debe disparar via `NotificationService` (ver controladores existentes en `app/Service/Notification/`).

### Origen legacy

`ProductosPreguntas::calificarRespuestaUtil()` — `sitio-api-rest-v3/app/resources/ProductosPreguntas.php:243`
Modelo: `ProductoPreguntaModel::calificarRespuestaUtilPorId()` línea 580 (UPDATE) + líneas 621-650 (notificaciones).

---

## 4) GET — Obtener preguntas y respuestas del usuario logueado

### Endpoint

`GET /v4/productos/preguntas/usuario`

### Tabla de definición del recurso

| Campo | Detalle |
|---|---|
| **Método** | `GET` |
| **Autenticación** | Requerida (`token.auth`) |
| **Perfil** | `comprador`, `vendedor`, `admin` |
| **Path param** | Ninguno |
| **Query params** | `estado` (opcional) — `pendientes` \| `respondidas`. `p` (opcional, default 1) — número de página |
| **Request body** | Ninguno |

### Ejemplo de llamada

`GET /v4/productos/preguntas/usuario?estado=pendientes&p=2`

### Respuesta esperada

`200 OK` — Page DTO con array de preguntas del usuario logueado.

```json
{
  "data": [
    {
      "id": 123,
      "texto": "¿Tiene garantía?",
      "fecha": "2026-04-08T10:30:00",
      "usuario": { "id": 789, "nombre": "Juan Pérez", "avatar": "...", "bloqueado": false },
      "producto": { "id": 999, "nombre": "Notebook ASUS X415", "img": "..." },
      "vendedor": { "id": 42, "usuarioId": 100, "nombre": "TecnoStore" },
      "respuesta": {
        "id": 456,
        "texto": "Sí, 12 meses oficial.",
        "fecha": "2026-04-08T11:15:00",
        "usuario_id": 100,
        "respuesta_util": null
      }
    },
    {
      "id": 124,
      "texto": "¿Hacen envío al interior?",
      "fecha": "2026-04-09T08:00:00",
      "usuario": { "id": 789, "nombre": "Juan Pérez", "avatar": "...", "bloqueado": false },
      "producto": { "id": 1000, "nombre": "Auriculares Sony WH-1000XM5", "img": "..." },
      "vendedor": { "id": 50, "usuarioId": 110, "nombre": "AudioPro" },
      "respuesta": null
    }
  ],
  "page": 1,
  "per_page": 10,
  "total": 42
}
```

### Casos especiales

- **Sin preguntas:** `data: []`, `total: 0`.
- **Sin auth (401):** respuesta estándar de `token.auth`.
- **`estado` inválido:** ignorar y devolver todas (compatible con legacy).

### Lógica

1. Obtener `usuario_id` del JWT.
2. Listar IDs de preguntas del usuario filtrando por `ocultar = 0` y por estado (LEFT JOIN a respuestas).
3. Paginar (10 por página, hardcoded en legacy — confirmar si se mantiene).
4. Hidratar cada pregunta con: usuario, producto, vendedor, respuesta (LEFT JOINs).

### Query SQL — listar IDs paginados

```sql
SELECT [PP].id
FROM [LO].[dbo].[productosPreguntas] PP
LEFT JOIN [LO].[dbo].[productosRespuestas] PR
  ON [PP].id = [PR].pregunta_id
WHERE [PP].ocultar = 0
  AND [PP].usuario_id = ?
  -- Filtro de estado (dinámico):
  -- estado = 'pendientes'  → AND [PR].pregunta_id IS NULL
  -- estado = 'respondidas' → AND [PR].pregunta_id IS NOT NULL
ORDER BY [PP].id DESC;
```

### Tablas involucradas

- `[LO].[dbo].[productosPreguntas]`
- `[LO].[dbo].[productosRespuestas]`
- `[LO].[dbo].[vendedores]`
- `[LO].[dbo].[usuarios]`
- `[CS].[dbo].[productos]`
- `[LO].[dbo].[productosPreguntasUsuariosBloqueados]` (LEFT JOIN para flag `bloqueado` del usuario)

### Origen legacy

`ProductosPreguntas::obtenerParaUsuario()` — `sitio-api-rest-v3/app/resources/ProductosPreguntas.php:30`
Modelo: `ProductoPreguntaModel::obtenerPaginados()` líneas 240-275.

---

## Esquema de campos compartido

### `ProductoPreguntaDTO`

| Campo | Tipo | Descripción |
|---|---|---|
| id | int | ID de la pregunta |
| texto | string | Texto de la pregunta |
| fecha | datetime ISO 8601 | Fecha de creación |
| usuario | `UsuarioMiniDTO` | Quien hizo la pregunta |
| producto | `ProductoMiniDTO` | Producto preguntado |
| vendedor | `VendedorMiniDTO` | Vendedor del producto |
| respuesta | `RespuestaDTO`\|null | Respuesta del vendedor (puede ser null) |

### `RespuestaDTO`

| Campo | Tipo | Descripción |
|---|---|---|
| id | int | ID de la respuesta |
| texto | string | Texto de la respuesta |
| fecha | datetime ISO 8601 | Fecha de respuesta |
| usuario_id | int | ID del vendedor que respondió |
| respuesta_util | bool\|null | true/false según calificación del comprador, null si no calificó |

> Reutilizar los DTOs ya existentes en v4: `QuestionDto`, `QuestionUserDto`, `QuestionVendorDto`, `QuestionProductDto`. Completar lo que falte.

---

## Entregables

### Controllers (`app/Http/Controllers/Questions/`)

| Controller | Acción | Ruta |
|---|---|---|
| `HideQuestionController` | `__invoke` | `DELETE /productos/preguntas/{pregunta_id}` |
| `BlockUserDeprecatedController` | `__invoke` | `POST /productos/preguntas/producto-bloquear-usuario` (devuelve 410) |
| `RateAnswerController` | `__invoke` | `POST /productos/preguntas/respuestas/{respuesta_id}/calificar` |
| `BuyerQuestionsController` | `__invoke` | `GET /productos/preguntas/usuario` |

### Services (`app/Service/Questions/`)

- `HideQuestionService` — valida ownership y soft-delete.
- `RateAnswerService` — valida autoría, actualiza, dispara notificación.
- `BuyerQuestionsService` — paginación + hidratación.

### Repository (`app/Repository/Questions/QuestionRepository.php`)

Agregar métodos:
- `hideById(int $preguntaId): void`
- `findById(int $preguntaId): ?object`
- `findByAnswerId(int $respuestaId): ?object`
- `rateAnswer(int $respuestaId, bool $util): void`
- `listByUser(int $usuarioId, ?string $estado, int $page, int $perPage): array`
- `countByUser(int $usuarioId, ?string $estado): int`

### Rutas — `app/routes/api.php`

Dentro del grupo `token.auth` con prefix `productos/preguntas`:

```php
Route::delete('{preguntaId}', HideQuestionController::class);
Route::post('producto-bloquear-usuario', BlockUserDeprecatedController::class);
Route::post('respuestas/{respuestaId}/calificar', RateAnswerController::class);
Route::get('usuario', BuyerQuestionsController::class);
```

---

## Criterios de aceptación

- [ ] DELETE oculta la pregunta solo si el vendedor logueado es dueño; soft-delete `ocultar=1`
- [ ] DELETE devuelve 403 si la pregunta es de otro vendedor; 404 si no existe
- [ ] POST `producto-bloquear-usuario` devuelve 410 con mensaje de deprecado, sin tocar la BD
- [ ] POST `calificar` solo permite al **autor de la pregunta** (no al vendedor) marcar útil/no útil
- [ ] POST `calificar` actualiza `respuesta_util` y dispara notificación web + push al vendedor
- [ ] POST `calificar` devuelve el DTO completo de la pregunta con la respuesta actualizada
- [ ] GET `usuario` devuelve preguntas del usuario logueado paginadas (10 por página)
- [ ] GET `usuario` filtra por `estado=pendientes` (sin respuesta) y `estado=respondidas` (con respuesta)
- [ ] GET `usuario` ignora preguntas con `ocultar=1`
- [ ] Todas las respuestas usan formato de fecha ISO 8601 con `T`
- [ ] Todos los endpoints protegidos con middleware `token.auth`
- [ ] Contratos de respuesta compatibles con el legacy (mismos nombres de campos en los DTO)

---

## Notas técnicas

- **Bug a corregir del legacy:** en `calificarRespuestaUtil` el legacy validaba perfil `vendedor` pero después chequeaba `pregunta->usuario->id === usuario->id`, lo cual nunca matchea para un vendedor. En v4 el perfil correcto es `comprador` (autor de la pregunta).
- **Notificaciones:** reusar `NotificationService` de v4 (`app/Service/Notification/`). El legacy mete dos registros (website + push) — replicar el mismo comportamiento.
- **Paginación:** el legacy hardcodea 10 items/página. Mantener el mismo valor para no romper UI del comprador.
- **DATEFORMAT:** SQL Server prod usa `mdy`. Cualquier fecha que se mande como param debe ir en ISO 8601 con `T`.
- **Patrón Controller → Service → Repository:** seguir el mismo patrón que el resto de v4. Una acción por controller (`__invoke`).
- **Sin Eloquent:** usar `DB::select()` / `DB::statement()` con bindings.
- **Lint:** correr `vendor/bin/pint` antes de commitear.

## Ver también

- [[Libre Opcion/Libre Opcion|Índice del proyecto]]
