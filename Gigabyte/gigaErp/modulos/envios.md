# Módulo: Envíos

Sección de **solo lectura** que muestra las campañas de mailing (AORUS/GIGABYTE)
consumiendo la API externa `envios.to-aor.us`. No tiene tabla ni CRUD: es un proxy.
Ruta: `/envios` · Sidebar: "Envíos" (grupo **Marketing**) · Permiso: `VER_SECCION_ENVIOS`

**Mismo patrón que [[modulos/resellers|Resellers]]:** proxy a una API externa, sin
importar nada a la DB. La diferencia es que la API es de campañas de email, no de productos.

## Backend: `EnvioController`

Proxy que firma las peticiones con un token guardado en config y devuelve el JSON del origen tal cual.

- `GET /api/envios/campanias` — listado de campañas con su `resumen` y `enlaces`
- `GET /api/envios/campanias/{id}` — detalle de destinatarios de una campaña
  - Acepta `?estado=` (abiertos/no_abiertos/si/no/sin_responder/fallidos) y `?lista=`
  - La ruta usa `->where('id', '.*')` porque el id puede venir como `(sin-campania)`

**Config:** `config/services.php` → `services.envios.{url,token}`, vía env `ENVIOS_API_URL` /
`ENVIOS_API_TOKEN`. Auth con `Http::withToken(...)` (Bearer).

## API externa (`envios.to-aor.us/api.php`)

- **Listado** → `{ generado, total, campanias: [{ id, nombre, actual, listas[], empresas[],
  primer_envio, ultimo_envio, resumen, enlaces }] }`
- **Detalle** → `{ campania, resumen, filtros, enlaces, destinatarios: [{ email, empresa,
  lista, enviado, abrio, aperturas, respuesta(si/no/null), fecha_* }] }`
- `resumen`: destinatarios, enviados, fallidos, abrieron, aceptaron, rechazaron,
  sin_responder + tasas (apertura/respuesta/aceptación).

## Frontend

**`pages/envios/index.vue`** — tarjetas por campaña (nombre, badge "Actual", chips de
empresas/listas, mini-stats Sí/No/Abrió/Sin-resp + tasas) + fila de totales agregados.
Click en tarjeta → detalle.

**`pages/envios/[id].vue`** — 5 StatsCards (Destinatarios, Confirmaron sí, Dijeron no,
Sin responder, Abrieron) + pills de filtro por estado + tabla de destinatarios con badge
de confirmación y aperturas.

## Filtro Real / Test (prefiltrado en Real)

Toggle **Real / Test / Todas** en **ambas** pantallas, que **arranca en Real**.

- **Clasificación:** una lista es *Test* si está vacía o su nombre contiene `prueba`/`test`;
  cualquier otro nombre es *Real*. Una **campaña** es Test si no tiene listas o todas son de
  test; Real si tiene al menos una lista real.
- Se resuelve **client-side** (la API externa no entiende de categorías Real/Test): el detalle
  se trae completo una vez y el toggle recalcula StatsCards + tabla; las pills de estado quedan
  como filtro secundario. En el listado filtra tarjetas y recalcula los totales.
- Con datos de solo-prueba (lista `prueba`), al entrar con el prefiltro Real la pantalla
  aparece vacía a propósito (oculta los envíos de test).

## Gotchas

- Los `destinatarios` no traen `id` y puede haber emails repetidos → se les asigna un id
  sintético por índice para el `:key` del DataTable.
- `useApi.get` devuelve el JSON crudo del proxy (sin desenvolver `.data`).
- Deploy backend en caliente: `docker cp` del controller + `services.php` + `api.php`,
  setear `ENVIOS_API_*` en el `.env` del container, `config:cache` + `route:clear`.

## Ver también

- [[modulos/resellers]] — otro proxy a API externa (partpicker), sin DB
- [[arquitectura]] — patrón proxy, EnvioController
- [[troubleshooting]] — deploy en caliente, config:cache
- [[changelog#2026-07-28 — Sección Envíos (campañas de mailing)|changelog]]

## Reclamo de evidencias (POEs)

En el detalle de una campaña, cada destinatario tiene **🔔 Reclamar**: dispara a mano un mail pidiéndole las POEs (con **carga directa** por link, remitente `mktgigabyte@`, **BCC** a forwarding, contador de reclamos y **"Para" multi-email** con directorio por empresa). La fecha límite sale del correo archivado (`GET /envios/campanias/{id}/fecha-limite`). Detalle completo en [[modulos/reclamo-evidencias]].
