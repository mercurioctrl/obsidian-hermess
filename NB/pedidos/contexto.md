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

### Gotcha: queries ad-hoc a SQL Server vía el container

Para explorar/consultar la DB desde una sesión de dev se usa el container `api-rest-pedidos-apirest-laravel` (app en `/var/www/app`).

- **No usar `php artisan tinker --execute="..."`** para queries con código no trivial: el doble escaping shell→tinker rompe con `\$`, `::` de namespaces y comillas anidadas (`PHP Parse error: unexpected T_NS_SEPARATOR`). En su lugar, escribir un `.php` y correr `php artisan tinker /ruta/script.php` (tinker ejecuta el archivo, con Laravel ya booteado).
- **El repo back está montado en el container**: el host `api-rest-pedidos-laravel/app/` es volume-mount de `/var/www/app/`. Los archivos del repo (comandos, SQL, `database/data/`) se ven adentro **sin `docker cp`**. Solo hace falta `docker cp` para archivos temporales fuera del repo.
- Aplicar un `.sql` con `GO`: patrón del README de `database/sql/` (`php -r` que splitea por `GO` y hace `unprepared`).

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

## Parámetros del cliente — salespersonId y ccodage

Al actualizar parámetros del cliente via `PATCH /v1/clients/{id}/params`, el campo `salespersonId` escribe **dos columnas** en `NewBytes_DBF.dbo.clientes`:

- `ID_VENDEDOR = salespersonId`
- `ccodage = RIGHT('00'+ISNULL(salespersonId,''),2)` — código del vendedor con padding de 2 dígitos

Ambas deben mantenerse sincronizadas. El campo `ccodage` es el que usa el sistema legado para identificar al vendedor asignado.

Archivo: `Services/Client/ClientParametersService.php` método `buildUpdateColumns`.

## Artículos sin costo promedio (`ncosteprom`)

La restricción `A.ncosteprom > 0` fue removida del endpoint `GET /v1/items`. Artículos recién cargados o con costo en 0 ahora son visibles en el buscador. Si en el futuro se necesita filtrar por costo, agregar el filtro como query param opcional, no hardcodeado.

## Empresas activas (FP_Empresas)

El sistema soporta **11 empresas activas** (`LACTIVA=1` en `NewBytes_DBF.dbo.FP_Empresas`), no solo NB/NBElectric/Libreopción como sugiere el README histórico:

| CODEMP | Nombre | Notas |
|---:|---|---|
| 02 | OXXEN SRL | factura PSO |
| 03 | NBGLOBAL | DOL |
| 04 | NB DISTRIBUIDORA MAYORISTA SRL | NB principal, agente_ret |
| 05 | DIGITO BINARIO SRL | DB, agente_ret |
| 06 | CCRT (Consorcio Red Tecnología) | |
| 07 | SUC 10 | |
| 08 | MUGELLO SRL | |
| 09 | NBElectric | misma CNIF que NB(04), agente_ret |
| 10 | PISOS Y REVESTIMIENTOS | |
| **11** | **LASET** | CNIF 12-dígitos (Uruguay), DOL, `defaultIncoterms=14`, **única importadora** — ver [[feature-laset-import]] |
| 12 | Libre Opción | |

Modelo: `app/Models/Company.php` → `protected $table = 'NewBytes_DBF.dbo.FP_Empresas '`.

## Regla cero: tablas ERP son read-only

**NUNCA emitir** `UPDATE`, `DELETE`, `ALTER TABLE`, `DROP COLUMN`, `INSERT` (excepto en flujos explícitos como MakeSale/Migrate) sobre las tablas existentes del ERP: `pedprot`, `pedprol`, `pedproi`, `pedclit`, `pedclil`, `stocks`, `FP_Empresas`, `FP_FactWebCliEncabezado_Uy`, `FP_FactWebCliDetalle_Uy`, `FP_DocumentosUY`, `FP_ComprobantesUY`, `forwarders`, `rebates`, etc. Tampoco crear vistas/triggers que escriban sobre ellas.

**Por qué:** el ERP legacy maneja datos críticos de producción cargados desde múltiples sistemas. Cambios pueden romper procesos externos (FacturaPlus, scripts de DBA, integraciones no visibles desde el monorepo).

**Cómo aplicar:** features nuevos viven en tablas nuevas con prefijo del feature (`laset_import_*`, `pedclil_oc_asignacion`). El cruce con ERP es solo lectura via `SELECT/JOIN`. Resultados del cruce se persisten en la propia tabla nueva.

## Modelo canónico ERP (compras / ventas / stock)

| Concepto | Tablas | Detalle |
|---|---|---|
| **Compras** (OCs a proveedores) | `pedprot` + `pedprol` + `pedproi` | Cabecera + líneas + cargos extra (`cdescrip='camion'`) |
| **Ventas** (a clientes) | `pedclit` + `pedclil` | Cabecera + líneas |
| **Stock** | `stocks` | Por `cCodAlm`/`ID_ALMACEN` — NO tiene `companyCode` |
| **Linkeo compra↔venta** | `pedclil_oc_asignacion` | [[feature-asignacion-oc]] |
| **CFE Uruguay (output)** | `FP_FactWebCliEncabezado_Uy` + `FP_FactWebCliDetalle_Uy` + `FP_DocumentosUY` + `FP_ComprobantesUY` | tipoCfe 101=eTicket / 102=NC / 103=ND, IVA 22% |

### Gotcha: `pedproi` no es solo impuestos

Pese al nombre "proi" (parece "proveedor impuestos"), guarda **además de percepciones IIBB** los **cargos extra del pedido de compra**: `cdescrip='camion'` $50/$200, etc. Linkea a `pedprot.nNumPed` via `nnumped`, **NO a `pedclit`**. 158 rows totales.

### Gotcha: `stocks` sin `companyCode`

Filtrar solo por `cCodAlm`/`ID_ALMACEN`. Cada empresa tiene su set de almacenes. Para Laset: DOM, BON, GRI, SAF, URU, ASI.

### Gotcha: `rebates` + `NewTable` huérfanas

Creadas el 2025-11-01 con schema primitivo, sin `companyCode`. Restos de intento abandonado de modelar rebates. **NO usar**. Modelar nuevo si se necesita.

### Identidad contable de chequeo

`SUM(pedprol.nCanPed) − SUM(pedclil.ncanped) = stocks.nstock + nstock_ingresando` por SKU + almacén + `companyCode`. Si no cierra, hay bug previo.

## macOS y branches case-insensitive

El backend usa branch `Development` (mayúscula), el frontend `development` (minúscula). En macOS con HFS+/APFS default (case-insensitive), `git branch -D development` puede borrar también `Development`. El resultado: rama queda "sin commits", `origin/Development [gone]`, archivos todos como `A` en status — pero `origin/Development` sigue intacto.

Recuperación:
```
git reset --hard origin/Development
git branch --set-upstream-to=origin/Development Development
```

## Laset: planilla = fuente de verdad

Para el [[feature-laset-import|feature Laset Import Framework]] (`companyCode=11`), cuando los datos de la planilla `docs/laser.xlsx` y los datos del ERP difieren, **la planilla wins**. Razón: la data actual en `pedprot`/`pedprol`/`pedproi`/`pedclit`/`pedclil` para comp=11 es de una **carga fallida previa**: tiene duplicaciones de hasta 10× (ej. `Ajuste precio A520MAPRO` plC=280 / erpC=2260), faltantes, y cantidades incorrectas.

## Laset: regla de aislamiento companyCode != 11

Excepción acotada al [[contexto#Regla cero: tablas ERP son read-only|read-only ERP]]: durante las fases de migración del feature laset-import SÍ se hacen `DELETE`+`INSERT` sobre `pedprot`/`pedprol`/`pedproi`/`pedclit`/`pedclil`, **pero exclusivamente con `WHERE companyCode = 11`**. Toda otra empresa (NB=4, NBE=9, LO=12, OXXEN=2, MUGELLO=8, etc.) queda intocable — operan en producción desde otros sistemas.

## Laset: plan de migración (3 fases)

```
Fase A — Alta huérfanos en articulo (equipo catálogo, externo)
    100 SKUs únicos de docs/laset_orphan_skus.csv
    INSERT INTO articulo (ID_PRODUCTO, …)
    Después: la vista vw_laset_sku_bridge los toma automáticamente.

Fase B — DELETE ERP comp=11 sin contraparte en planilla
    DELETE FROM pedprot/pedprol/pedproi/pedclit/pedclil
    WHERE companyCode = 11 AND NOT EXISTS (matching en planilla MATCHED)
    Filtro estricto siempre. NUNCA tocar el resto.

Fase C — INSERT planilla → ERP (2461 filas MATCHED)
    INSERT a pedprot/pedprol/pedproi (compra)
    INSERT a pedclit/pedclil (venta)
    INSERT a pedclil_oc_asignacion (linkeo)
    Update staging.matched_* + match_status='IMPORTED'
```

Stock queda correcto como consecuencia (no se INSERT manualmente).

## Laset: Fase D y defecto de Fase C (2026-05-15)

Fase C creó solo las **órdenes** comp=11 (pedprot/pedprol + pedclit/pedclil),
sin remitos ni `pedproi` ni stock. **Fase D** (`laset:import-fase-d`) los
genera sobre las órdenes existentes: `albprot`+`albprol` (compra),
`albclit`+`albclil` (venta, `ccodalm` del pedclit — NO el `'SAF'` de MakeSale),
`pedproi cdescrip='camion'`, y replica stock compra(+)/venta(−).

**Por qué importa (gotcha)**: el pre-check de aislamiento de Fase D destapó
que `LasetImportFaseCCommand::resolveMasters` resolvía SKU→`ID_ARTICULO` **sin
filtrar `companyCode`**, ligando 56 pedprol + 56 pedclil comp=11 a 44
artículos NB (comp=4). Regla derivada: **toda resolución de maestro
(SKU/cliente/proveedor) lleva siempre `WHERE companyCode=N`**, y antes de
cualquier UPDATE sobre tabla compartida sin companyCode (`stocks`) va un
pre-check THROW que aborte si el set incluye otra company. Ver
[[memoria#Resolución de maestros filtra companyCode]] y
[[feature-laset-import#12. Sesión 2026-05-15 (cont.) — Fase D + fix defecto Fase C]].

**Fechas de documento**: los remitos respetan la fecha del documento
(`pedprot.dFecPed`/`pedclit.dfecped` cargadas de la planilla), nunca
`GETDATE()`.

**Estado**: Fase D **pasada 1 ejecutada en dev** (~870 órdenes limpias migradas).
Pasada 2 (15+15 órdenes con los 39 SKUs de `docs/laset_fasec_skus_sin_comp11.csv`)
espera Fase A catálogo + re-bind.

## Reversibilidad: snapshot/restore (regla operativa)

**Antes de CUALQUIER proceso o sesión que toque comp=11** (Fase C/D, fixes,
y especialmente producción): `php artisan laset:snapshot <tag>`. Si algo sale
mal: `php artisan laset:restore <tag> --force` deja la tajada comp=11 (14
tablas, incl. `NB_WEB.registro_stock`) exactamente como estaba. Probado
end-to-end. Es restauración a un PUNTO (no undo incremental). Detalle en
[[feature-laset-snapshot-restore]]. Pedido explícito del usuario: "si pasa
algo malo en producción, dejar todo como estaba antes".
