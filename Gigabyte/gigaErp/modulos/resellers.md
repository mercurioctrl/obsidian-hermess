# Módulo: Resellers

Listado live de productos de resellers (37 tiendas vía PreciosGamer) desde `partpicker.blustudioinc.com`.
Ruta: `/resellers` · Sidebar: "Resellers" (debajo de APIs Distri)

**Diferencia clave con [[modulos/productos|APIs Distri]]:** no importa nada a la DB. Todo se consulta en tiempo real como proxy.

## Backend: `ResellersController`

- `GET /api/resellers/fuentes` — lista resellers (fuentes con prefijo `preciosgamer_`), formatea nombre
- `GET /api/resellers/items` — proxy a `/items?distribuidor=0` con filtros pasados

**Filtros disponibles:** `source`, `fabricante` (exact match case-insensitive), `isinstock` (0/1), `q` (texto libre), `limit` (max 200), `offset`

## Frontend: `pages/resellers/index.vue`

Filtros:
- **Reseller** (select): todos o uno específico
- **Marca** (text, default `GIGABYTE`): pasa como `fabricante` a la API
- **Stock** (select): todos / con stock / sin stock
- **Búsqueda** (text): pasa como `q`

Tabla: imagen · nombre + link a ficha · nro_parte · marca · categoría · precio ARS · badge stock

Paginación: 50 items por página con offset.

## Gotcha: precio

- `precio_ars` siempre viene `null` en items de resellers
- El precio real está en **`precio_convertido`**
- `moneda` siempre es `"ARS"` para resellers

## Fuentes de resellers (37)

Todas tienen prefijo `preciosgamer_`. Ejemplos: `preciosgamer_libre-opcion` (1471 items), `preciosgamer_compra-gamer` (1382), `preciosgamer_armytech` (406).

## Ver también

- [[modulos/productos]] — distribuidores mayoristas (con importación a DB)
- [[arquitectura]] — ResellersController, patrón proxy API externa
