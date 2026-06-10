# Contexto y reglas

Reglas de negocio, decisiones y deuda técnica que **no** se infieren leyendo el código de un vistazo. Útil para retomar el proyecto sin re-investigar.

## Reglas de negocio

### Cotización según moneda del proveedor

- Si el proveedor opera en **pesos** (`currencyId = 'PSO'`): la **cotización es siempre 1 y NO se puede editar**; solo se edita la *cotización fiscal*.
- Si opera en **otra moneda** (`currencyId = 'DOL'` u otra): la cotización **sí** es editable.
- Implementado en `Orders/Detail.vue` con el computed `isProviderInPesos` (deshabilita el input de cotización). Ver [[arquitectura#Frontend — Nuxt 2 con Vuex|Frontend]].

### Impuestos globales (NULL = todas las empresas)

- En `NewBytes_DBF.dbo.FP_IMPUESTOS`, las filas con `companyCode = NULL` son **impuestos base globales** que aplican a TODAS las empresas: SIN IMPUESTO, POR PORCENTAJE, IVA, RETENCIONES, GANANCIAS, TASA ESTADISTICA, DERECHOS, BANCARIOS + percepciones de IIBB (Caba y BA).
- Las filas con `companyCode` específico son impuestos propios de esa empresa.
- **Cualquier query de impuestos por empresa debe incluir los globales** con `(companyCode = :cc OR companyCode IS NULL)`. Un `companyCode = :cc` a secas los descarta (en SQL Server `NULL = 4` es UNKNOWN, no matchea).

### Empresas (companyCode → FP_Empresas.CODEMP)

`02` OXXEN · `03` NBGLOBAL · **`04` NB DISTRIBUIDORA MAYORISTA SRL** · `05` DIGITO BINARIO · `06` CONSORCIO RED DE TECNOLOGIA · `07` SUC 10 · `08` MUGELLO · `09` NBElectric · `10` PISOS Y REVESTIMIENTOS · **`11` LASET** · `12` Libre Opción.

- `companyCode == 11` (LASET) es empresa especial: el front oculta IVA, impuestos internos, columnas en pesos, cotización y precio sin IVA (`plugins/permissions.js`).

## Decisiones tomadas (2026-06-10)

- **Búsqueda de items parametrizada**: se eligió parametrizar (named binds) en vez de interpolar el término. Motivo principal de performance: en SQL Server cada texto distinto interpolado genera un plan de ejecución nuevo (recompila + ensucia el plan cache); con parámetros el plan se reutiliza. Bonus: elimina inyección SQL.
- **tariffTax globales vía query, no vía datos**: se descartó hacer `UPDATE FP_IMPUESTOS SET companyCode=4 WHERE companyCode IS NULL`, porque dejaría a LASET (11) y al resto sin IVA/Ganancias/etc. Se resolvió incluyendo los NULL en la query (no se tocó ningún dato).

## Deuda técnica / TODOs

- **Bug latente** en `TariffTaxPrefixRepository::filterByTaxExclusive`: hace `$params = ['taxExclusive' => ...]` (pisa todo el array `$params`) en vez de `$params['taxExclusive'] = ...`. Si se combina `taxExclusive` con `id`, se pierde el binding de `id`. No afecta hoy porque rara vez se combinan. **Pendiente de corregir.**
- **`/v1/items` sin paginación SQL**: recibe `itemsPerPage`/`currentPage` pero no los aplica — devuelve TODAS las filas que matchean (con `ORDER BY`). Oportunidad de optimización con `OFFSET/FETCH`.
- **SKU con `LIKE '%term%'`** (contains) no usa índice. Si se confirma que el SKU se busca por prefijo, cambiar a `'term%'` para habilitar index seek.

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
