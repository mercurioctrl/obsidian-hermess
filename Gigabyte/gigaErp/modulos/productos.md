# Módulo: Productos / APIs Distri

Catálogo de productos. Dos orígenes:
1. **Sync desde distribuidores mayoristas** vía API partpicker (`/productos`, "APIs Distri").
2. **Carga masiva del catálogo GIGABYTE** desde xlsx/csv (`/productos/importar` + pestaña [[productos#Pestaña Catálogo|Catálogo]] en Inventario).

## Modelo

Tabla `productos` (migraciones `0014` → `0040`).

Columnas relevantes:
- `nombre`, `codigo_distribuidor`, `sku`, `modelo`, `categoria`, `descripcion`, `marca`, `foto_principal`
- `precio`, `precio_oferta`, `iva`, `precio_final` — precios comerciales
- **`precio_lista_1..4`** — 4 listas de precio para órdenes de venta (mig `0026`)
- `precio_usd` — precio neto sin IVA en USD (viene de `precio_sin_iva` de partpicker)
- `distribuidor_id` → FK `clientes` (tipo=distribuidor)
- `stock`, `ultimo_ingreso`, `activo`
- **Campos de catálogo GIGABYTE** (mig `0040`): `bu_code`, `chipset`, `item_no`, `global_part`, `link`, `ean`, `carton_box_qty`, `carton_peso_kg`, `carton_largo_mm`, `carton_ancho_mm`, `carton_alto_mm`
- (vía `stock_deposito`) — stock por depósito físico

## Carga masiva de catálogo GIGABYTE

Pedido del contacto de GIGABYTE: cargar la base de productos (sin stock) con sus campos, y cruzar el stock después.

**Convención de claves:** `sku` = `codigo_distribuidor` = **ITEM NO** · `nombre`/`modelo` = Global Part · `marca`=GIGABYTE · `distribuidor_id`=null. El upsert del catálogo es por `item_no`. Como el SKU queda = ITEM NO, el importador de [[productos#Stock|stock de mercadería]] cruza el stock por ese código sin cambios.

**UPC NO se usa.**

### Importador (`ImportacionCatalogoController`)

- `POST /api/importaciones-catalogo/parsear` — sube xlsx/csv, devuelve `headers`, `rows`, `campos` mapeables
- `POST /api/importaciones-catalogo` — upsert por `item_no`; payload: `staged_id, extension, archivo_nombre, mapping{item_no(req),...}, marca, categoria`. Devuelve `{creados, actualizados, omitidos, errores}`

**Parseo:** CSV nativo con `fgetcsv` (detecta delimitador `, ; \t`); xlsx/xls usa PhpSpreadsheet **solo si está en el vendor** (ver gotcha abajo).

⚠️ **Gotcha validate():** `'mapping' => 'array'` + `'mapping.item_no' => '...'` hace que `$request->validate()` devuelva SOLO `item_no`. Hay que agregar `'mapping.*' => 'nullable|integer|min:0'` para recibir el resto del mapeo.

⚠️ **PhpSpreadsheet no instalado en el container** → xlsx rompe en este y en el importador de mercadería. CSV funciona. Fix: `docker compose build backend`. Ver [[troubleshooting#8. PhpSpreadsheet no instalado en el container|troubleshooting #8]].

### Frontend

- `/productos/importar` — wizard subir → mapear (auto-detecta columnas del mail por regex) → resultado.
- Botón "Cargar catálogo" en `/productos`. Toggle "Mostrar stock" oculta columna+badge. Bloque "Datos de catálogo" en el modal de detalle.

### Pestaña Catálogo

`/mercaderia/catalogo` — cuarta pestaña de Inventario (Stock · **Catálogo** · Depósitos · Subir Masivo). Listar / editar / crear productos con todos los parámetros del catálogo (modal). Al guardar, `sku` se sincroniza con `item_no` (y al crear, también `codigo_distribuidor`).

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

- `GET /api/productos` — paginado 50, filtros: `search` (nombre/cod/sku/item_no/global_part/ean), `marca`, `distribuidor_id`, `stock`
- `GET /api/productos/seleccionables` — liviano para picker OV (ruta estática antes del apiResource)
- `POST /api/productos` — alta manual (acepta campos de catálogo)
- `PUT /api/productos/{id}` — actualiza listas de precio y/o campos de catálogo
- `POST /api/importaciones-catalogo[/parsear]` — carga masiva del catálogo

## Ver también

- [[modulos/resellers]] — resellers vía PreciosGamer (live, sin importar a DB)
- [[ordenes-venta]] — consume las 4 listas de precio
- [[troubleshooting]] — gotcha PhpSpreadsheet + validate nested
- [[arquitectura]] — ProductoController, SincronizarApiController, ImportacionCatalogoController
