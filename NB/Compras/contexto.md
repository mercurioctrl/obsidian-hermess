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

## Deuda técnica / TODOs

- **Bug latente** en `TariffTaxPrefixRepository::filterByTaxExclusive`: hace `$params = ['taxExclusive' => ...]` (pisa todo el array `$params`) en vez de `$params['taxExclusive'] = ...`. Si se combina `taxExclusive` con `id`, se pierde el binding de `id`. No afecta hoy porque rara vez se combinan. **Pendiente de corregir.**
- **`/v1/items` sin paginación SQL**: recibe `itemsPerPage`/`currentPage` pero no los aplica — devuelve TODAS las filas que matchean (con `ORDER BY`). Oportunidad de optimización con `OFFSET/FETCH`.
- **SKU con `LIKE '%term%'`** (contains) no usa índice. Si se confirma que el SKU se busca por prefijo, cambiar a `'term%'` para habilitar index seek.
- **`fullSerialized` hardcodeado a 0** en el detalle de ingreso (`ProviderOrderInboundRepository::getDetail`). No es confiable a nivel orden; usar `serializedAmount > 0` por ítem.

## Infraestructura / Base de datos (gotcha importante)

- DB canónica del proyecto: **`190.210.23.97:4444`** (DB `NB_WEB`, user `web`). Es la del `.env` habitual.
- Servidor alternativo `190.210.23.108`: SQL escucha en **1433** (user `eferreyra_devweb01`).
- ⚠️ **`190.210.23.108:4444` es un servidor SSH (OpenSSH), NO SQL.** El TCP abre pero el handshake TDS falla con `SQLSTATE[01002] Adaptive Server connection failed (severity 9)` / "login packet rejected". Si aparece ese error, casi seguro `DB_PORT` apunta a un puerto que no es SQL.
- El login y muchas queries hacen **joins cross-database**: las 4 bases (`NewBytes_DBF`, `NB_WEB`, `NEW_BYTES`, `PRODUCTOS`) deben existir en el server elegido.
- Tras tocar `.env`: `docker exec api-rest-compras-apirest-laravel bash -c "cd /var/www/app && php artisan config:clear"`.

## Ver también

- [[arquitectura|Arquitectura]]
- [[changelog|Changelog]]
- [[memoria|Memoria del proyecto]]
- [[NB/compras/reglas-compras|Reglas de negocio — Compras]]
