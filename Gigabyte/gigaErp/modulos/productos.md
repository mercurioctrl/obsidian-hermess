# Módulo: Productos

Catálogo de productos con grid/lista, filtros por distribuidor y stock, y la **ficha
del producto** donde se editan las 4 listas de precio.

## Modelo

Tabla `productos` (migraciones `0014` + sucesivas hasta `0026`).

Columnas relevantes:
- `nombre`, `codigo_distribuidor`, `sku`, `modelo`, `categoria`, `descripcion`, `marca`, `foto_principal`
- `precio`, `precio_oferta`, `iva`, `precio_final` — precios "comerciales" (originales)
- **`precio_lista_1..4`** — las 4 listas de precio para órdenes de venta (mig `0026`)
- `precio_usd` — usado por DemoSeeder cuando `precio` está null
- `distribuidor_id` → FK `clientes` (un producto pertenece a un distribuidor)
- `stock`, `ultimo_ingreso`, `activo`
- (vía `stock_deposito`) — stock por depósito específico

## 4 listas de precio

Cada producto tiene 4 precios paralelos en USD. **No tienen nombres de negocio** —
genéricos Lista 1..4. Se inicializan en `0026`:

```sql
UPDATE productos SET
  precio_lista_1 = COALESCE(precio, precio_usd, 0),
  precio_lista_2 = COALESCE(precio, precio_usd, 0),
  precio_lista_3 = COALESCE(precio, precio_usd, 0),
  precio_lista_4 = COALESCE(precio, precio_usd, 0);
```

**Sin constraint de unicidad entre ellas** — pueden ser todas iguales, todas distintas,
o cualquier combinación. El usuario las edita después.

### Edición

Se editan en el **modal de detalle del producto** (`pages/productos/index.vue`),
sección "Listas de precio (USD)" con 4 inputs numéricos + botón "Guardar listas".
Endpoint: `PUT /api/productos/{id}` con `{ precio_lista_1, ..., precio_lista_4 }`.

### Uso

Las listas se consumen al armar [[ordenes-venta]]: el picker de productos muestra
los 4 precios como botones, el usuario elige uno y se snapshotea en el ítem.

## SKU único POR DISTRIBUIDOR (no global)

Migración `0025` (`fix_sku_unique_per_distribuidor_in_productos`): el índice
`productos_sku_unique` global se reemplazó por `productos_distribuidor_sku_unique`
compuesto `(distribuidor_id, sku)`.

**Por qué:** dos distribuidores legítimamente venden el mismo SKU físico (ej. Invid
y New Bytes ambos venden `GP-P550SS` de Gigabyte). Con el unique global, los
seeders chocaban en duplicate-key.

**Implicancia en validación:** si usás FormRequest, validá contra el par, no global:
```php
'sku' => 'unique:productos,sku,NULL,id,distribuidor_id,' . $request->distribuidor_id
```
Nunca `'sku' => 'unique:productos,sku'` a secas.

## Endpoint adicional: `/api/productos/seleccionables`

Catálogo liviano para selectores (órdenes de venta): todos los productos activos
sin paginar, con campos mínimos + las 4 listas:

```
GET /api/productos/seleccionables
→ { data: [{ id, nombre, sku, codigo_distribuidor, precio, precio_lista_1..4 }, ...] }
```

Ruta estática **antes** del `apiResource('productos')` en `routes/api.php`. Sin esto
`/productos/seleccionables` se interpretaría como `/productos/{id}`.

## Distribuidores con productos cargados

Ver [[contexto]]. Resumen actual:
- **Invid** — 41 productos (seeder `ProductoInvidSeeder`, SKUs Gigabyte reales)
- **New Bytes** — 206 productos (seeder `ProductoNewBytesSeeder`, sku=`codigo_distribuidor`)
- **Elit** y **Air** — sin productos por ahora

## Ver también

- [[ordenes-venta]] — quién consume las 4 listas
- [[invoice-preview]] — cómo aparecen los productos en la invoice generada
- [[arquitectura]] — patrón del ProductoController y Resource
