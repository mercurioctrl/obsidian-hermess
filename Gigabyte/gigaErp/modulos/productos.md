# Módulo: Productos / APIs Distri

Catálogo de productos importados desde distribuidores mayoristas vía API externa.
Ruta: `/productos` · Sidebar: "APIs Distri"

## Modelo

Tabla `productos` (migraciones `0014` + sucesivas hasta `0026`).

Columnas relevantes:
- `nombre`, `codigo_distribuidor`, `sku`, `modelo`, `categoria`, `descripcion`, `marca`, `foto_principal`
- `precio`, `precio_oferta`, `iva`, `precio_final` — precios comerciales
- **`precio_lista_1..4`** — 4 listas de precio para órdenes de venta (mig `0026`)
- `precio_usd` — precio neto sin IVA en USD (viene de `precio_sin_iva` de partpicker)
- `distribuidor_id` → FK `clientes` (tipo=distribuidor)
- `stock`, `ultimo_ingreso`, `activo`
- (vía `stock_deposito`) — stock por depósito físico

## Fuente de datos: partpicker API

`https://partpicker.blustudioinc.com` — pública, sin auth.

**Distribuidores mayoristas:** Air, Ceven, Invid, Stylus (fuentes sin prefijo `preciosgamer_`)

### Sincronización (`SincronizarApiController`)

Endpoints:
- `GET /api/sincronizar/fuentes` — lista mayoristas
- `POST /api/sincronizar/{source}` — upsert masivo por `(distribuidor_id, codigo_distribuidor)`
- `POST /api/sincronizar/vincular-skus` — asigna `sku = strtoupper(nro_parte)` a productos sin SKU

**Mapeo de campos API → Producto:**

| Campo API | Campo Producto | Gotcha |
|-----------|----------------|--------|
| `codigo` | `codigo_distribuidor` | clave de upsert |
| `producto` | `nombre` | |
| `fabricante` | `marca` | |
| `nro_parte` | `modelo` | también se usa como SKU en vincular-skus |
| `precio_sin_iva` | `precio_usd` | puede ser null → default 0 |
| `pct_iva` | `iva` | puede ser null → default 21 |
| `precio_final` | `precio_final` | puede ser null → default 0 |
| `stock` | `stock` | puede ser negativo → `max(0, (int)$val)` |
| `imagen_url` | `foto_principal` | |

**El modal de sync** muestra estado real por distribuidor + paso "Vincular SKUs" al final.

## Filtro de marca — default GIGABYTE

`filtroMarca = "GIGABYTE"` al iniciar la página. Backend: `WHERE marca LIKE "%X%"`.
Se puede limpiar para ver todas las marcas.

## 4 listas de precio

Edición en modal de detalle del producto. Endpoint: `PUT /api/productos/{id}`.
Consumidas en [[ordenes-venta]] como botones en el picker.

## SKU único por distribuidor

Índice `(distribuidor_id, sku)`. El mismo SKU puede existir en varios distribuidores —
eso es lo que permite la vinculación en [[modulos/existencias|Stock Distri]].

**vincular-skus:** usa `modelo` (nro_parte de la API) como SKU para habilitar el cruce en Existencias.

## Endpoints

- `GET /api/productos` — paginado 50, filtros: `search`, `marca`, `distribuidor_id`, `stock`
- `GET /api/productos/seleccionables` — liviano para picker OV (ruta estática antes del apiResource)
- `PUT /api/productos/{id}` — actualiza listas de precio

## Ver también

- [[modulos/resellers]] — resellers vía PreciosGamer (live, sin importar a DB)
- [[ordenes-venta]] — consume las 4 listas de precio
- [[arquitectura]] — ProductoController, SincronizarApiController
