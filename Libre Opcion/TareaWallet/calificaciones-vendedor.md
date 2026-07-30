# Calificaciones del Vendedor — Reseñas, revisión y respuesta

Módulo de calificaciones/reseñas de vendedores en la API v4. Toda la data vive en la tabla `LO.dbo.pedidosCabeceraVendedor` (una fila por pedido; las columnas `calificacion*` guardan la reseña del comprador y la gestión posterior).

## Endpoints

| Método | URL | Controller | Descripción |
|--------|-----|-----------|-------------|
| `GET` | `/v4/seller/{sellerId}/calificationReviews?offset=0&viewType=seller` | `CalificacionesVendedor` | Listado paginado de reseñas del vendedor |
| `POST` | `/v4/seller/{sellerId}/califications/{calificationId}/review` | `RevisarCalificacionVendedor` | Admin/vendedor marca la reseña en revisión (motivo) |
| `POST` | `/v4/seller/{sellerId}/califications/{calificationId}/reply` | `ResponderCalificacionVendedor` | Vendedor responde públicamente la reseña |

> ⚠️ El grupo de rutas `seller` (`routes/api.php:415`) **no** tiene middleware `token.auth` → el GET es público (sin JWT). Los POST validan solo que `review`/`reply` no vengan vacíos.

## GET calificationReviews — comportamiento

Capa: `CalificacionesVendedor` → `CalificacionService::obtenerCalificaciones` → `CalificacionRepository`.

Respuesta: `{ data: [...], pagination: { total, offset, limit, order } }`.

**Campos base (siempre):** `idCalification`, `calification`, `calificationReview`, `calificationDate`, `calificationType`, `pedidoID`.

**Campos extra solo con `viewType=seller`:**
- `commentLO` ← `calificacionReviewReplica` (observación cargada por el admin del CMS)
- `status` ← `ISNULL(calificacionReviewEstado, 0)` (0 si no hay estado de revisión)
- `resellerReply` ← `calificacionRespuesta` (respuesta del vendedor)

**Filtro de visibilidad:** sin `viewType=seller` solo se devuelven reseñas con `calificacionReviewVisibilidad IS NULL OR = 1` (visibles). Con `viewType=seller` se ven todas, incluidas las ocultas.

## Validación principal (criterios de aceptación)

1. `viewType=seller` devuelve `commentLO`, `status`, `resellerReply` en cada item ✔
2. `status` = 0 cuando no hay estado de revisión (ISNULL) ✔
3. `commentLO` = observación del admin ✔
4. `resellerReply` = respuesta del vendedor ✔
5. Con `viewType=seller` incluye ocultas (total_seller ≥ total_público) ✔
6. Sin `viewType=seller` no expone campos de seller ni reseñas ocultas ✔
7. `data` y `pagination.total` consistentes con el filtro — ✖ **BUG (ver abajo)**

## Script de verificación

`scripts/verify-calification-reviews.sh <sellerId>` — verificador de caja negra. Golpea el endpoint real, compara vista seller vs pública y valida los 7 criterios (PASS/FAIL/WARN, exit ≠ 0 si falla). Solo requiere `curl` + `jq`. `BASE_URL` configurable (default `http://localhost:8097`).

## Bug abierto — paginación inconsistente (criterio 7)

`CalificacionRepository::obtenerCalificaciones()` (SELECT de `data`) filtra por:
`calificacion > 0` **+** `calificacionComentario <> ''` **+** `calificacionType IS NULL OR = 1`.

Pero `countCalificaciones()` (que alimenta `pagination.total`) filtra **solo** por `calificacion > 0` + visibilidad. Resultado: `total` sobrecuenta. Ej. seller 447 → `total=3162` vs filas reales `963`.

**Fix pendiente:** replicar en `countCalificaciones()` los mismos filtros del SELECT de `data`.

## Notas / gotchas

- **`status` llega como `"0"` (string), no `0`.** No es bug: el driver PDO de SQL Server devuelve todos los escalares como string (`idCalification`, `calification`, `pedidoID`… igual). El `ISNULL` sí funciona.
- **`calificacionReviewVisibilidad` está NULL en toda la BD** (4893 filas). El camino de reseñas "ocultas" (criterios 5/6) no está ejercido por datos reales todavía; los invariantes pasan de forma trivial.

## Ver también

- [[changelog]]
- [[contexto]]
- [[TareaWallet]]
