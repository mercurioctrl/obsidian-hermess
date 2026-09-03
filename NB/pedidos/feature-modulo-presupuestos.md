# Feature: Módulo de Presupuestos

Módulo nuevo para **armar, guardar, editar y descargar** presupuestos, con ítems del **inventario por empresa** e ítems **libres** (concepto/IVA/cantidad/precio). Implementado 2026-08-31/09-01. Rama `feature/modulo-presupuestos` en ambos repos, **stacked sobre** [[feature-pdf-fiscal-por-empresa]] (reusa el encabezado fiscal por empresa). Precios en **u$d** con cotización, para reusar el layout del PDF del pedido.

## Datos (SQL Server, `NB_WEB.dbo`)

Script `app/database/sql/2026_08_31_001_create_presupuestos.sql` (+ `_drop_`). Se aplica en dev por tinker; **el DBA lo corre en prod**.

- **`presupuestos`** (cabecera): `id`, `number` (correlativo por empresa = `MAX(number)+1 WHERE companyCode`), `companyCode`, `agentId`, `sellerName`, `clientId`, `clientName`, `clientTaxId`, `clientTaxCondition`, `currencyQuote`, `observations`, `status` (`draft`), `validUntil`, `total`, `created/updated/deleted_at` (soft delete).
- **`presupuestos_items`**: `id`, `presupuestoId`, `type` (`inventory`|`free`), `itemId` (ID_ARTICULO), `sku`, `description`, `quantity`, `unitPrice` (sin IVA, u$d), `iva` %, `internalTax` %, `sortOrder`.
- Permiso `presupuestos` en `permisos_agente` — ver el checklist en [[decision-permiso-nuevo-agente]].

## Backend (`api-rest-pedidos-laravel`)

CRUD `GET/POST/PUT/DELETE /v1/presupuestos`, grupo con `PresupuestoMiddleware` dentro del grupo `['middleware'=>'permission']` (junto al grupo `items` en `routes/api.php`). Clases en `App\...\Presupuesto\` (Controller/Service/Repository + `Dto\Presupuesto\PresupuestoDto`+`PresupuestoItemDto`), SQL raw estilo `OrderRepository`.

- **Repository**: insert con `OUTPUT INSERTED.id`; `updateHeader` bindea **solo** las columnas del UPDATE (PDO exige match exacto binds↔tokens, si no `HY093`).
- **Service**: totales u$d (subtotal + iva% + internalTax%), `number` por empresa, cliente/sellerName. **Ojo listado:** `list()` NO fuerza la empresa del usuario desbloqueado (si no, oculta las de otras empresas) — solo la fuerza cuando `unlockedCompanyFilter` es falsy.
- Búsqueda de inventario **reusa** `GET /v1/items?search=&companyCode=` (devuelve `{response:[ProductDto]}`, con `price.value/iva/internalTax` y también `price.priceList` (mapa `{A..E, PM/SP/MK}`) + `price.letra`).

## Frontend (`pedidos-web-app-v1`)

**No es ítem del menú superior**: es una **pestaña** en la sección Pedidos, a la derecha de "Ordenes", en `components/Table/TabMenu.vue` (`v-if="$auth.user.presupuestos"`, `name:'presupuestos'`). La página renderiza `<TableTabMenu />`.

- `pages/presupuestos.vue` — listado (N°, Fecha, Empresa, Cliente, **Generado por**, Total, Estado, acciones editar/PDF/borrar) + botón "Nuevo".
- `components/Presupuestos/Builder.vue` — armador (modal): empresa (respeta `unlockedCompanyFilter`), cliente opcional (buscador `/clients` + texto libre; trae CUIT de `getDetailClient`), buscador de inventario, ítems libres, tabla editable, totales u$d+$, observaciones.
- `mixins/presupuestoPdf.js` — `getPresupuestoEmisor(companyCode)` + `buildPresupuestoPdf()` (jsPDF+autoTable, encabezado fiscal por empresa). `getPresupuestoEmisor` está **duplicado** con `pages/orders.vue` (follow-up: unificar).
- `store/presupuestos.js` + grupo `presupuestos` en `plugins/api.js`.

### Selector de lista de precios por ítem (2026-09-03, commit `c0d9fd3`)

Réplica del comportamiento de las órdenes editables, dentro del `Builder.vue`. **Solo frontend, sin cambios de backend ni schema.**

- Cada ítem **de inventario** muestra una flechita (`caret-down`) azul junto al `P.Unit u$d`. Al clickearla se abre un `a-dropdown`/`a-menu` con las listas de precios del artículo (`A — u$d …`, `B`, …, y `PM/SP/MK` si aplican). La lista actualmente aplicada aparece resaltada (`.pl-active`).
- Al elegir una, `applyPriceList(it, letra)` setea `it.unitPrice = priceList[letra]` y guarda `it.letra`; se recalculan los totales.
- Ítems **libres** no tienen flechita (no tienen lista de precios).
- **Modo edición:** los ítems guardados vuelven de la DB sin `priceList` (la tabla `presupuestos_items` solo persiste `unitPrice`). Se resuelve con fetch **diferido** `ensurePriceList(it)`: la 1ª vez que se abre la flechita, busca por SKU/código vía `/v1/items`, matchea por `itemId` y rellena `priceList`/`letra`. Muestra "Cargando…" y, si falla, "Sin listas".
- Se agregaron `priceList`/`letra`/`loadingPriceList` a los ítems en `mapItem`/`addInventoryItem`/`addFreeItem` (pre-declarados para reactividad de Vue 2).
- **No se persiste la letra elegida** (evita columna nueva + backend): solo se aplica el precio a la línea, que es lo pedido.

## Gotcha resuelto — la pestaña no aparecía

`$auth.user` se puebla desde `/auth/user`, que pasa por `Dto/Auth/UserDto.php` (lista blanca). Faltaba declarar `presupuestos` ahí → el flag no llegaba al front. Ver [[decision-permiso-nuevo-agente]].

## Estado y follow-ups

Completo y funcionando en local (build + `pm2 restart WebExpedition`). PRs abiertos en ambos repos. Follow-ups: convertir a pedido, ítems ARS nativo, estados (enviado/vencido), unificar `getPresupuestoEmisor`, persistir la letra elegida por ítem (opcional).

## Ver también

- [[feature-pdf-fiscal-por-empresa]] — encabezado por empresa que reusa
- [[feature-ficha-producto]] — comparte el patrón de reuso de `/v1/items` y datos de empresa
- [[decision-listas-precios-nombradas]] — listas de precios (fuente del `priceList`/`letra`)
- [[changelog]]
