# Contexto y reglas

Reglas de negocio, decisiones y deuda técnica que **no** se infieren leyendo el código de un vistazo. Útil para retomar el proyecto sin re-investigar.

## Reglas de negocio

### Cotización según moneda del proveedor

- Si el proveedor opera en **pesos** (`currencyId = 'PSO'`): la **cotización es siempre 1 y NO se puede editar**; solo se edita la *cotización fiscal*.
- Si opera en **otra moneda** (`currencyId = 'DOL'` u otra): la cotización **sí** es editable.
- Implementado en `Orders/Detail.vue` con el computed `isProviderInPesos` (deshabilita el input de cotización). Ver [[arquitectura#Frontend — Nuxt 2 con Vuex|Frontend]].

### Cotización en pesos (currencyQuote === 1) — display

Cuando una orden/ingreso tiene `currencyQuote === 1` **está en pesos** (no en dólares). Reglas de visualización en el detalle (`Orders/Detail.vue`, `ProviderOrderInbound/Detail.vue`, `Table/EditableCell2.vue`):

- El **Costo** debe mostrar el signo `$`, no `u$d`. El símbolo se inyecta vía prop `currency` de `EditableCell2.vue` (default `'u$d'`); pasar `'$'` si `currencyQuote === 1`.
- Las clases de color `.dolar` / `.peso` se eligen con `currencyQuote === 1 ? 'peso' : 'dolar'` (estaban invertidas).
- La fila resumen **Cotización fiscal** (`type:'resumenfiscal'`) **no** debe multiplicar los subtotales por `currencyFiscalQuote` cuando está en pesos — el cálculo fiscal no aplica; solo se muestra el valor de la cotización fiscal (en la columna "Cant.").
- En órdenes no editables (remitidas) la cotización / cotización fiscal se muestran en la columna "Cant.".

> Nota: es distinto de la regla de *editabilidad* de arriba (`currencyId='PSO'`). Acá hablamos del **valor numérico** de la cotización (1 = pesos) para decidir cómo se muestra.

### IVA por defecto del artículo al agregar ítem (2026-06-20)

- Al **agregar** un ítem a una orden, el selector de IVA arranca con el `ivaCompra` del artículo (`NewBytes_DBF.dbo.articulo.ivaCompra`), no en 0. Sigue siendo editable.
- Para eso el buscador `/v1/items` devuelve el campo `iva` (= `ivaCompra`) en cada ítem (`ItemRepository` + `Dto/Item/ItemDto`), y `Orders/AddItem.vue` lo manda como `price.iva` al PATCH (antes hardcodeaba 0, que se guardaba en `PedProL.nivaserv` pisando el fallback del detalle).
- El detalle de orden ya resolvía `ISNULL(PL.nivaserv, AR.ivaCompra)`, así que ítems sin `nivaserv` ya mostraban el IVA del artículo. El selector ofrece solo 0 / 10.5 / 21.

### Filtro de Empresa (companyCode) por defecto en pestañas (2026-06-20)

- Al **entrar a cualquier pestaña** que tenga el filtro de empresa, este arranca en `Number($auth.user.companyCode) || 4` (el companyCode del usuario, o **4** por defecto si no tiene ninguno asignado). **Nunca queda en null al entrar.**
- Solo queda libre/null si el usuario lo **limpia a mano** (y se mantiene así mientras no cambie de pestaña ni recargue).
- Implementado en el `created()` de las **9** `components/Filters/*.vue` (Orders, ProviderOrderInbound, Categories, Providers, Forwarders, Warehouses, ProviderVoucher, TariffTax, TariffPosition). Antes la condición era `this.company && this.company !== -1`, que dejaba en null a los usuarios sin empresa.

### Filtro por serial — Órdenes e Ingresos (2026-06-20)

- Busca en qué orden / ingreso está un serial. Los seriales viven en `NEW_BYTES.dbo.ST_DETALLE_STOCK` (`SERIAL`, `ID_COMPRA` = `PedProT.nNumPed`, `cref`). **No hay vínculo directo al ingreso puntual** (`nnumalb`), solo a la orden.
- **Órdenes:** `EXISTS` sobre `ST_DETALLE_STOCK` por `ID_COMPRA = pedprot.nNumPed` + `SERIAL`.
- **Ingresos:** `EXISTS` correlacionado con la línea del ingreso (`albprol.ID_ARTICULO` = artículo cuyo `cRef` = `sds.cref`), para acotar al artículo del serial dentro del ingreso.
- **Rendimiento:** el `EXISTS` **solo se concatena al WHERE cuando el filtro está presente**; si no se filtra por serial, el listado corre igual que antes (sin subqueries extra). Misma idea para SKU / ID interno.

### Cuenta corriente de proveedores (ledger MS_MOV_CTACTE_PROVEEDORES)

Modal accesible desde el ojito 👁️ en el listado de Proveedores. Endpoint `GET v1/providers/{providerCode}/currentAccount`. Detalle de flujo en [[arquitectura#Cuenta corriente de proveedores|arquitectura]].

> **Refactor 2026-06-24:** la fuente es el **ledger oficial `NEW_BYTES.dbo.MS_MOV_CTACTE_PROVEEDORES`** (~29k movimientos). La primera versión (armar desde `FACPROT`/`FACPROL`) **fue descartada**.

- **Fuente de datos:** tabla `NEW_BYTES.dbo.MS_MOV_CTACTE_PROVEEDORES`. Vínculo `ID_PROVEEDOR` (char, = `CCODPRO` con ceros). Se excluyen anulados (`ANULADO <> 'SI'`). Incluye pagos (es un ledger completo, no solo comprobantes).
- **Importe:** `IMPORTE_USD` (**siempre positivo**; la dirección la da el tipo de transacción). Pesos = `IMPORTE_USD × COTIZACION`. (`MONEDA` es un código interno; el importe ya viene normalizado a USD.)
- **Tipo de movimiento:** `TR_CODIGO` → `NEW_BYTES.dbo.GL_TRANSACCIONES.TR_NOMBRE` (Pedidos Proveedores, Pago a Proveedores, Pago con Cheque, Créditos/Débitos Varios, Cobro a Proveedores).
- **Débito / crédito (mapeo confirmado por el usuario; saldo = deuda con el proveedor):** **suman deuda** `38` (Pedidos Proveedores), `32` (Débitos Varios); **restan** `30` (Créditos Varios), `40` (Pago a Proveedores), `128` (Pago con Cheque), `44` (Cobro a Proveedores). El indicador `GL_TRANSACCIONES.TR_INDICADOR_SIGNO_F10` es ambiguo ('X' en la mayoría), por eso el mapeo se definió a mano.
- **Fecha:** `FECHA_MOV` es **float YYYYMMDD** (ej. `20180717`). Los filtros `from`/`to` (YYYY-MM-DD) se convierten a ese número.
- **Saldos:** `balanceUsd` = Σ(signo × `IMPORTE_USD`); `balancePeso` = Σ(signo × `IMPORTE_USD` × `COTIZACION`). Ambas monedas se calculan (todo normalizado a USD con cotización real).
- **Comprobante:** `INVOICE` o, si vacío, `DATOS_FACTURA` (en pagos suele venir vacío).
- **Id de proveedor:** el endpoint recibe `providerCode` = `CCODPRO` = `ID_PROVEEDOR` del ledger.
- El DTO mantiene la misma forma de respuesta que la v1 (FACPROT) → el front no cambió; `currency` queda fijo en `'USD'`.

### Impuestos globales (NULL = todas las empresas)

- En `NewBytes_DBF.dbo.FP_IMPUESTOS`, las filas con `companyCode = NULL` son **impuestos base globales** que aplican a TODAS las empresas: SIN IMPUESTO, POR PORCENTAJE, IVA, RETENCIONES, GANANCIAS, TASA ESTADISTICA, DERECHOS, BANCARIOS + percepciones de IIBB (Caba y BA).
- Las filas con `companyCode` específico son impuestos propios de esa empresa.
- **Cualquier query de impuestos por empresa debe incluir los globales** con `(companyCode = :cc OR companyCode IS NULL)`. Un `companyCode = :cc` a secas los descarta (en SQL Server `NULL = 4` es UNKNOWN, no matchea).

### Empresas (companyCode → FP_Empresas.CODEMP)

`02` OXXEN · `03` NBGLOBAL · **`04` NB DISTRIBUIDORA MAYORISTA SRL** · `05` DIGITO BINARIO · `06` CONSORCIO RED DE TECNOLOGIA · `07` SUC 10 · `08` MUGELLO · `09` NBElectric · `10` PISOS Y REVESTIMIENTOS · **`11` LASET** · `12` Libre Opción.

- `companyCode == 11` (LASET) es empresa especial: el front oculta IVA, impuestos internos, columnas en pesos, cotización y precio sin IVA (`plugins/permissions.js`).

### companyCode 4 (NB) y depósito SAFcom

- **`companyCode = 4` = NB (New Bytes / NB Distribuidora Mayorista)**. Vive en `PedProT` y `albprot`.
- Depósito **SAFcom** = `FP_Almacen.ID_ALMACEN` **2** = `CCODALM` **'SAF'**. `PedProT` guarda ambos (`warehousesId` numérico=2 + `cCodAlm` char='SAF'); `albprot` solo guarda `ccodalm` (char='SAF'), no tiene `warehousesId`.
- Resto de depósitos relevantes: 1=DE1/Depósito 1, 9=Miami (DOMESTIC MIAMI), 11/13/16=BONDED, etc.

## Decisiones tomadas (2026-06-10)

- **Búsqueda de items parametrizada**: se eligió parametrizar (named binds) en vez de interpolar el término. Motivo principal de performance: en SQL Server cada texto distinto interpolado genera un plan de ejecución nuevo (recompila + ensucia el plan cache); con parámetros el plan se reutiliza. Bonus: elimina inyección SQL.
- **tariffTax globales vía query, no vía datos**: se descartó hacer `UPDATE FP_IMPUESTOS SET companyCode=4 WHERE companyCode IS NULL`, porque dejaría a LASET (11) y al resto sin IVA/Ganancias/etc. Se resolvió incluyendo los NULL en la query (no se tocó ningún dato).
- **Limpieza de companyCode/depósito (sí se tocaron datos, prod)**: `companyCode IS NULL` → 4 en `PedProT` (78) y `albprot` (11.914). Depósito SAFcom seteado **solo donde faltaba/estaba vacío** para `companyCode=4` (`PedProT.warehousesId=2` en 10.319 filas que ya tenían `cCodAlm='SAF'`; `albprot.ccodalm='SAF'` en 3 vacías). **No** se pisaron 7 filas con depósito puesto a propósito (3×DE1 + 2×Miami; 1×DOM + 1×006). Criterio del usuario: normalizar sin sobrescribir lo intencional.
- **Regla operativa para UPDATEs masivos en prod**: contar primero (`SELECT COUNT`) y confirmar alcance con el usuario antes de ejecutar. La base es externa, productiva y sin migraciones → no hay rollback fácil.

## Decisiones tomadas (2026-06-22)

- **companyCode de comprobantes vía query, no vía datos**: igual que con tariffTax, se decidió derivar `companyCode` de `FACPROT` desde el proveedor en la query (`ISNULL(...)`) en vez de hacer un `UPDATE` masivo (37k filas, 161 quedarían NULL igual por proveedores sin empresa). No se tocó dato.
- **Cuenta corriente sin pagos (primera versión)**: se decidió arrancar la cuenta corriente solo con comprobantes (deuda) y dejar los **pagos para una segunda iteración** (no se sabe aún de qué tabla salen / no se linkean todavía).
- **Saldos separados por moneda**: en vez de un saldo único cross-convertido (imposible porque los PSO guardan cotización 1), se muestran `balanceUsd` (comprobantes DOL) y `balancePeso` (comprobantes PSO) por separado.

## Exportación de tablas (XLSX/CSV) — 2026-06-26

- Los botones de export en **Órdenes** e **Ingresos** bajan **todo lo filtrado**, no solo la página visible: se decidió re-consultar el endpoint con los mismos filtros (`route.query`) pero `itemsPerPage` alto (100000). Interpretación de "bajar lo que veo según los filtros".
- Export 100% **en el browser** con SheetJS (`xlsx`) — no se agregó endpoint ni dependencia en el backend.
- El export reusa **las columnas visibles** de cada tabla (incluye las que dependen de permisos en Órdenes) para que coincida con lo que se ve; valores legibles (`status`→Pendiente/Remitido, `serializado`→Si/No).
- En el detalle de orden, los botones se ubicaron **arriba de la tabla** (primero estaban junto a "Columnas opcionales" y tapaban los checkboxes).

## Deuda técnica / TODOs

- **Cuenta corriente de proveedores**: ✅ ya lee el ledger `MS_MOV_CTACTE_PROVEEDORES` (incluye pagos). Lo de FACPROT/NTIPOCOMP/FOB quedó obsoleto (era la v1). Si aparece un `TR_CODIGO` nuevo, revisar el mapeo de signo en `ProviderCurrentAccountRepository`.
- **Bug latente** en `TariffTaxPrefixRepository::filterByTaxExclusive`: hace `$params = ['taxExclusive' => ...]` (pisa todo el array `$params`) en vez de `$params['taxExclusive'] = ...`. Si se combina `taxExclusive` con `id`, se pierde el binding de `id`. No afecta hoy porque rara vez se combinan. **Pendiente de corregir.**
- **`/v1/items` sin paginación SQL**: recibe `itemsPerPage`/`currentPage` pero no los aplica — devuelve TODAS las filas que matchean (con `ORDER BY`). Oportunidad de optimización con `OFFSET/FETCH`.
- **SKU con `LIKE '%term%'`** (contains) no usa índice. Si se confirma que el SKU se busca por prefijo, cambiar a `'term%'` para habilitar index seek.
- **`fullSerialized` hardcodeado a 0** en el **detalle** de ingreso (`ProviderOrderInboundRepository::getDetail`). No es confiable a nivel orden; usar `serializedAmount > 0` por ítem. (Distinto del `fullSerialized` del **listado**, que sí se calcula — ver abajo.)
- **`fullSerialized` del listado** (Órdenes e Ingresos) marca "Sí" cuando una orden **no tiene líneas** (`COUNT=0 = COUNT=0`). Edge heredado; si molesta, agregar `COUNT(líneas) > 0` a la condición.

### Moneda y cotizaciones del Ingreso vienen de PedProt (2026-06-30)

En el recurso `providerOrderInbound` los datos de moneda del ingreso deben salir de **`PedProt`** (cabecera del pedido), **no de `albprot`** (remito):

- `albprot.ccoddiv` guarda el **id numérico** de moneda (ej. `1`); `PedProt.ccoddiv` guarda el **código** `PSO`/`DOL`. El listado/detalle de orden ya usaban `PedProt`/`PT`; el ingreso quedó alineado.
- `currencyId` ← `PedProt.ccoddiv` · `currencyQuote` ← `PedProt.nValDiv` · `currencyFiscalQuote` ← `PedProt.nvaldiv_FISCAL`.
- `PedProt` ya estaba joineada en el query del ingreso (no se agregaron joins). Regla general: en compras, los datos de cabecera de un ingreso (moneda, cotización) vienen del **pedido**, no del remito.

### Duplicados en listado de Ingresos (GROUP BY nullable) (2026-06-30)

`providerOrderInbound` (listado) mostraba cada remito **dos veces** (uno con total real, otro con total 0/NULL). Causa: el `GROUP BY` incluía **`albprol.nnumalb`** además de `albprot.nnumalb`. Como `albprol` entra por **LEFT JOIN**, las líneas del pedido (`PedProL`) que **no** están en ese remito dejan `albprol.nnumalb = NULL` → se forma un segundo grupo "fantasma". Fix: quitar `albprol.nnumalb` del `GROUP BY` (queda solo `albprot.nnumalb`, no nullable). Lección: **cuidado con columnas nullable de un LEFT JOIN dentro del GROUP BY.**

Relacionado: el `count()` de paginación usaba `COUNT(albprot.nnumalb)` **sin GROUP BY** → contaba todas las filas del join (inflado, generaba páginas de más). Pasó a `COUNT(DISTINCT albprot.nnumalb)`.

## Infraestructura / Base de datos (gotcha importante)

- **DB en uso (2026-06-30):** el `.env` de la API apunta a **`10.10.10.47:1433`** con user **`cmercurio`** (DB `NB_WEB`), entorno **saftel** (`compras.saftel.com`, companyCode 4). La DB canónica histórica `190.210.23.97:4444` (user `web`) quedó **comentada** en el `.env`. El 2026-06-29 se usó el mismo host con user `fcallipo`; el 2026-06-24 `db-nb-dev.blu.net.ar:41433` (cayó). Las 3 bases del join de login (`NB_WEB.dbo.usuarios_nb`, `NewBytes_DBF.dbo.agentes`, `NEW_BYTES.dbo.PGM_USUARIOS`) existen en `10.10.10.47` y conectan OK. Tras tocar `.env`, correr `php artisan config:clear && php artisan cache:clear` en el contenedor.
- DB canónica histórica: **`190.210.23.97:4444`** (DB `NB_WEB`, user `web`). Server alternativo `190.210.23.108`: SQL en **1433** (user `eferreyra_devweb01`).
- ⚠️ **`190.210.23.108:4444` es un servidor SSH (OpenSSH), NO SQL.** El TCP abre pero el handshake TDS falla con `SQLSTATE[01002] Adaptive Server connection failed (severity 9)`. Si aparece ese error, casi seguro `DB_PORT` apunta a un puerto que no es SQL.
- El login y muchas queries hacen **joins cross-database**: las 4 bases (`NewBytes_DBF`, `NB_WEB`, `NEW_BYTES`, `PRODUCTOS`) deben existir en el server elegido.
- Tras tocar `.env`: `docker exec api-rest-compras-apirest-laravel bash -c "cd /var/www/app && php artisan config:clear"`.

## Ver también

- [[arquitectura|Arquitectura]]
- [[changelog|Changelog]]
- [[memoria|Memoria del proyecto]]
- [[NB/compras/reglas-compras|Reglas de negocio — Compras]]
