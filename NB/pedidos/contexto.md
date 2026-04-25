# Contexto

Reglas de negocio, gotchas técnicos y decisiones del proyecto.

## Multi-marca (companyCode)

El sistema opera para tres marcas de la misma empresa:
- **NB** (New Bytes) — marca principal
- **NBElectric** — electrónica
- **Libreopción** — marca alternativa (tiene stock separado: `nstock_lo`)

La mayoría de tablas y endpoints filtran por `companyCode`. Al loguearse, el usuario queda asociado a una empresa, pero puede cambiar desde la UI (engranaje). Al cambiar de empresa se recargan: vendedores, medios de envío y medios de pago.

CompanyCodes conocidos: **4=NBE**, **9=Meli**, **11=LASET**, **12=Libreopción**.

## Base de datos

### Tablas clave (NewBytes_DBF)

| Tabla | Descripción |
|-------|-------------|
| `pedclit` | Cabecera de pedidos. `cestado`: P=pendiente, S=procesado. `cobserv`: INTERNO/DESCARGADO/PEDIDO LIBRE OPCION/POSTVENTA. `id` IDENTITY. UNIQUE en `(cnumped, cnumsuc)`. |
| `pedclil` | Detalle de pedidos. `id` IDENTITY (FK lógica para [[feature-asignacion-oc|asignaciones]]). |
| `PedProT` | Cabecera de OC (compras a proveedor). `nNumPed` es identificador de negocio (no es IDENTITY; el surrogate `id_pedprod` no se usa). `cEstado`: P/R/s. `companyCode`. |
| `pedprol` | Detalle de OC. **Sin IDENTITY ni PK formal.** Identificación por `(nNumPed, nLinea, cRef)`. |
| `pedclil_oc_asignacion` | **Nueva** — asignación N:M entre líneas de venta y de OC del [[feature-asignacion-oc|feature]]. |
| `albclit` | Cabecera de remitos (se crea en [[modulo-makesale|MakeSale]]) |
| `albclil` | Detalle de remitos |
| `stocks` | Stock por artículo y almacén. Columnas: `nstock`, `nstock_lo`, `nstock_en_cola`, `nstock_postventa`, `nstock_reserva_pedidos` |
| `FP_Almacen` | Almacenes/depósitos. Tiene `companyCode`, `Predeterminado`, `deleted_at` |
| `agentes` | Vendedores/agentes |

### Tablas (NB_WEB)

| Tabla | Descripción |
|-------|-------------|
| `registro_stock` | Log de auditoría de movimientos de stock |

### Vistas (NewBytes_DBF) — del [[feature-asignacion-oc|feature de asignación]]

| Vista | Devuelve |
|---|---|
| `vw_saldo_oc` | Saldo dinámico por línea de OC. Sin filtro `cEstado` (Opción C). |
| `vw_pedclil_estado_asignacion` | Estado por línea pendiente: SIN_ASIGNAR/PARCIAL/COMPLETA. |

### Gotcha: columnas duplicadas en SELECT con LEFT JOIN

En queries con `SELECT PL.*, ... S.ID_ALMACEN FROM pedclil PL LEFT JOIN stocks S ON ...`, el `S.ID_ALMACEN` explícito sobreescribe el `PL.ID_ALMACEN` de `PL.*` en PHP/PDO. Si el LEFT JOIN no matchea, `ID_ALMACEN` queda NULL aunque pedclil lo tenga.

**Solución:** usar `ISNULL(S.ID_ALMACEN, PL.ID_ALMACEN)` como fallback.

### Gotcha: case sensitivity de propiedades PHP

PHP distingue mayúsculas en propiedades de objetos. `$item->ID_Articulo` ≠ `$item->ID_ARTICULO`. En `getDetailOrder`, `PL.*` trae `PL.ID_Articulo` (siempre con valor) y `S.ID_ARTICULO` viene del LEFT JOIN (puede ser NULL). Son dos propiedades distintas en PHP.

**Fix:** usar siempre `ID_Articulo` (la versión de pedclil, que siempre tiene valor).

### Gotcha: SQL concatenado en MakeSale/RemoveSale

Las queries en [[modulo-makesale|MakeSaleService]] y [[modulo-removesale|RemoveSaleService]] se construyen concatenando SQL como strings PHP (no usan query builder). Un campo null genera SQL sintácticamente inválido que rompe TODO el batch.

**Regla:** al modificar estos servicios, siempre verificar que las propiedades interpoladas tengan valor, especialmente las que vienen de LEFT JOINs.

### Gotcha: driver dblib + índices filtrados

El driver `dblib` (alternativo al `sqlsrv`, configurado vía `SqlServerDblibServiceProvider`) no setea los SET options ANSI requeridos para que SQL Server permita escribir en tablas con índices filtrados (`WHERE` en `CREATE INDEX`). Esto rompe `INSERT/UPDATE` con `SQLSTATE[HY000] 20018`.

**Workaround aplicado en [[feature-asignacion-oc|feature de asignación]]:** todos los índices nuevos van **sin** `WHERE`. La pérdida de eficiencia es despreciable hasta tener cientos de miles de filas. Si se migra al driver `sqlsrv` puro, se pueden volver a filtrar.

### Gotcha: pedprol sin IDENTITY ni PK

`pedprol` (líneas de OC) no tiene `id` IDENTITY ni PK formal. La identificación de una línea de OC requiere la tupla `(nNumPed, nLinea, cRef)`. El [[feature-asignacion-oc|feature de asignación]] snapshotea las 3 columnas en cada insert.

## Stock por tipo de pedido

- **Pedido normal:** descuenta de `nstock`
- **Pedido Libre Opción:** descuenta primero de `nstock_lo`, el resto de `nstock`
- **Sucursal 0003 (Postventa):** usa `nstock_postventa`
- **Reserva:** se trackea en `nstock_reserva_pedidos`

## Kits

Los kits (bundles) se descomponen en sus componentes al agregarse a un pedido. Al mover un kit entre pedidos, también se descompone. El precio descompuesto se preserva del origen.

## Asignación OC ↔ Venta

El [[feature-asignacion-oc|feature]] tiene reglas propias importantes:

- **No tocar [[modulo-makesale|MakeSale]] ni [[modulo-removesale|RemoveSale]]** — el feature usa un trigger SQL en `pedclit` que mueve asignaciones V↔C cuando cambia `cestado`. Cero acoplamiento con esos services.
- **OCs candidatas no se filtran por `cEstado`** (decisión del usuario, "Opción C") — el operador ve todo. Pendiente futuro: corte por fecha o backfill histórico.
- **Cross-warehouse permitido** a nivel de asignación. El filtro por almacén opera recién al consumir stock (etapa posterior, no implementada acá).
- **Asignación parcial permitida** (`ASSIGNMENT_ALLOW_PARTIAL=true`) — hoy informativa, no bloquea MakeSale.
- **Filtro multi-marca via env**: `ASSIGNMENT_COMPANIES=4,11` (CSV).
- **Saldo siempre dinámico** — no hay tabla de "disponibles" que mantener sincronizada; se calcula on-the-fly en `vw_saldo_oc`.

## Firebase (local)

El `.env` local no tiene variables `FIREBASE_*`. El plugin detecta esto y retorna un stub vacío. Cualquier código de Firebase debe verificar `$notificationfirebase.messaging` antes de llamar a `getMessaging()`. Sin el guard, Firebase crashea y bloquea toda la app.

## Node.js (local)

Con Node v17+ se requiere `NODE_OPTIONS=--openssl-legacy-provider` para levantar el frontend. Sin esto, webpack crashea con `ERR_OSSL_EVP_UNSUPPORTED`.

## Ver también

- [[arquitectura]] — Estructura del proyecto
- [[modulo-makesale]] — Flujo de ejecución de pedidos
- [[modulo-removesale]] — Flujo de reversión
- [[feature-asignacion-oc]] — Feature de asignación OC↔Venta
- [[stack]] — Tecnologías y versiones
