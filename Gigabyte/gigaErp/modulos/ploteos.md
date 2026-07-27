# Módulo Ploteos

Gestión del **branding físico** (ploteos / vinilos de sucursales) de los resellers, con **mapa geolocalizado**. Sección `/ploteos` en el sidebar (grupo Marketing). Commits `46e6dab`, `009b911`, `8e58069`, `815c284`.

## Modelo `Ploteo` (tabla `ploteos`)

Migraciones `0051`–`0055`.

| Campo | Notas |
|-------|-------|
| `cliente_id` | FK a `clientes` (reseller). `belongsTo(Cliente)` |
| `sucursal` | nombre de la sucursal. Dropeada en `0054` y re-agregada en `0055` |
| `ploteo` | descripción del ploteo |
| `url` | link opcional (foto/arte). Agregada en `0052` |
| `medidas_cm` | medidas del vinilo (WxHxZ) |
| `ubicacion` | **dirección a geocodificar** (agregada en `0053`) |
| `lat` / `lng` | coordenadas (cast `float`). Se llenan geocodificando `ubicacion` |
| `fecha` | cast `date` |
| `estado` | `Ploteo::ESTADOS = ['programado', 'en_proceso']` |
| `notas` | libre |

> ⚠️ **Historial de migraciones sinuoso**: `0054` dropeó `sucursal` y `0055` la volvió a agregar. El campo que manda para el mapa es **`ubicacion`**, no `sucursal`.

## Endpoints (`PloteoController`)

Rutas **estáticas ANTES del apiResource** (patrón del proyecto):

- `GET /ploteos/paises` — países disponibles para el filtro
- `GET /ploteos/mapa` — ploteos con `whereNotNull('lat')->whereNotNull('lng')` (solo geolocalizados)
- `apiResource('ploteos')` — CRUD estándar

### Geocodificación (Nominatim)

`PloteoController::geocodificar()` le pega a `https://nominatim.openstreetmap.org/search` con header `User-Agent: config('services.nominatim.user_agent')` (bloque nuevo en `config/services.php`, default `gigaErp/1.0 (ezequielm789@gmail.com)`).

- Se dispara al **crear** (si viene `ubicacion`) y al **editar** (si cambió el texto, o si quedó sin pin de un intento previo fallido — `$sinPinPrevio`).
- **Falla silenciosa**: si Nominatim no responde, el ploteo se guarda igual sin coordenadas.
- ⚠️ **Nominatim devuelve `lon`, no `lng`** → el mapeo hace `['lng' => (float) $r['lon']]`.

## Importación masiva (`ImportacionPloteosController`)

- `POST /importaciones-ploteos/parsear` — preview del Excel
- `POST /importaciones-ploteos` — persiste

Excel con columnas: **País, Reseller, Sucursal, Ploteo, Medidas cm (WxHxZ), Fecha**. Mapea **`sucursal` → `ubicacion`** y geocodifica **fuera de la transacción** (respeta el rate-limit de Nominatim, ~1 req/seg; tope de 80 por corrida). Frontend en `pages/ploteos/importar.vue`.

## Frontend (`pages/ploteos/index.vue`)

Mapa **Leaflet** + `leaflet.markercluster` (import dinámico), tiles de OpenStreetMap. `cargarMapa()` pide `/ploteos/mapa` y dibuja un marker por ploteo con `lat`/`lng`; popup con nombre del cliente + link. Filtros por país/estado/búsqueda recargan lista y mapa. Requiere las deps de Leaflet en `frontend/package.json`.

## Gotcha operativo (2026-07-27)

Los ploteos **previos** a la migración `0053` no tienen `ubicacion` ni `lat`/`lng` → **no aparecen en el mapa** (`/ploteos/mapa` devuelve `[]`). No es un bug de deploy: hay que cargarles la dirección (edición → geocodifica) o re-importar desde la planilla. Ver [[troubleshooting]].

## Ver también

- [[modulos/clientes]] — los ploteos cuelgan de clientes `reseller`
- [[changelog#2026-07-27 — Ploteos con mapa + estados de proyecto configurables|changelog]]
- [[arquitectura]] — patrón rutas estáticas antes de apiResource, geocodificación
- [[troubleshooting]]
