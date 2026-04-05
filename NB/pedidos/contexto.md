# Contexto

Reglas de negocio, gotchas técnicos y decisiones del proyecto.

## Multi-marca (companyCode)

El sistema opera para tres marcas de la misma empresa:
- **NB** (New Bytes) — marca principal
- **NBElectric** — electrónica
- **Libreopción** — marca alternativa (tiene stock separado: `nstock_lo`)

La mayoría de tablas y endpoints filtran por `companyCode`. Al loguearse, el usuario queda asociado a una empresa, pero puede cambiar desde la UI (engranaje). Al cambiar de empresa se recargan: vendedores, medios de envío y medios de pago.

## Base de datos

### Tablas clave (NewBytes_DBF)

| Tabla | Descripción |
|-------|-------------|
| `pedclit` | Cabecera de pedidos. `cestado`: P=pendiente, S=procesado. `cobserv`: INTERNO/DESCARGADO/PEDIDO LIBRE OPCION/POSTVENTA |
| `pedclil` | Detalle de pedidos (items). PK: `cnumped`+`cnumsuc` |
| `albclit` | Cabecera de remitos (se crea en [[modulo-makesale|MakeSale]]) |
| `albclil` | Detalle de remitos |
| `stocks` | Stock por artículo y almacén. Columnas: `nstock`, `nstock_lo`, `nstock_en_cola`, `nstock_postventa`, `nstock_reserva_pedidos` |
| `FP_Almacen` | Almacenes/depósitos. Tiene `companyCode`, `Predeterminado`, `deleted_at` |
| `agentes` | Vendedores/agentes |

### Tablas (NB_WEB)

| Tabla | Descripción |
|-------|-------------|
| `registro_stock` | Log de auditoría de movimientos de stock |

### Gotcha: columnas duplicadas en SELECT con LEFT JOIN

En queries con `SELECT PL.*, ... S.ID_ALMACEN FROM pedclil PL LEFT JOIN stocks S ON ...`, el `S.ID_ALMACEN` explícito sobreescribe el `PL.ID_ALMACEN` de `PL.*` en PHP/PDO. Si el LEFT JOIN no matchea, `ID_ALMACEN` queda NULL aunque pedclil lo tenga.

**Solución:** usar `ISNULL(S.ID_ALMACEN, PL.ID_ALMACEN)` como fallback.

### Gotcha: case sensitivity de propiedades PHP

PHP distingue mayúsculas en propiedades de objetos. `$item->ID_Articulo` ≠ `$item->ID_ARTICULO`. En `getDetailOrder`, `PL.*` trae `PL.ID_Articulo` (siempre con valor) y `S.ID_ARTICULO` viene del LEFT JOIN (puede ser NULL). Son dos propiedades distintas en PHP.

**Fix:** usar siempre `ID_Articulo` (la versión de pedclil, que siempre tiene valor).

### Gotcha: SQL concatenado en MakeSale/RemoveSale

Las queries en [[modulo-makesale|MakeSaleService]] y [[modulo-removesale|RemoveSaleService]] se construyen concatenando SQL como strings PHP (no usan query builder). Un campo null genera SQL sintácticamente inválido que rompe TODO el batch.

**Regla:** al modificar estos servicios, siempre verificar que las propiedades interpoladas tengan valor, especialmente las que vienen de LEFT JOINs.

## Stock por tipo de pedido

- **Pedido normal:** descuenta de `nstock`
- **Pedido Libre Opción:** descuenta primero de `nstock_lo`, el resto de `nstock`
- **Sucursal 0003 (Postventa):** usa `nstock_postventa`
- **Reserva:** se trackea en `nstock_reserva_pedidos`

## Kits

Los kits (bundles) se descomponen en sus componentes al agregarse a un pedido. Al mover un kit entre pedidos, también se descompone. El precio descompuesto se preserva del origen.

## Firebase (local)

El `.env` local no tiene variables `FIREBASE_*`. El plugin detecta esto y retorna un stub vacío. Cualquier código de Firebase debe verificar `$notificationfirebase.messaging` antes de llamar a `getMessaging()`. Sin el guard, Firebase crashea y bloquea toda la app.

## Node.js (local)

Con Node v17+ se requiere `NODE_OPTIONS=--openssl-legacy-provider` para levantar el frontend. Sin esto, webpack crashea con `ERR_OSSL_EVP_UNSUPPORTED`.

## Ver también

- [[arquitectura]] — Estructura del proyecto
- [[modulo-makesale]] — Flujo de ejecución de pedidos
- [[modulo-removesale]] — Flujo de reversión
- [[stack]] — Tecnologías y versiones
