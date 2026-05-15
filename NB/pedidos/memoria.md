# Memoria

Contexto acumulado de sesiones de trabajo con Claude en este proyecto.

## Usuario

- Desarrollador fullstack senior argentino
- Idioma: español rioplatense
- Prefiere iterar rápido y soluciones simples
- No agregar features no solicitadas

## Feedback

- Siempre verificar cambios con pruebas reales (curl, dev server) antes de reportar como terminado
- MakeSale/RemoveSale usan SQL concatenado — verificar nulls con ISNULL antes de interpolar en queries
- **Cancelaciones LO vs carritos abandonados:** pedidos sin pedclit no son cancelaciones sino carritos abandonados. `motivoCancelacion` tiene prioridad sobre `mp_payment_status`. Total cancelados = created - active (no sumar flags que se solapan)
- **No tocar MakeSale/RemoveSale** desde features nuevos — usar triggers SQL o capa nueva. Decisión explícita en [[feature-asignacion-oc|asignación OC]].
- **Antes de tirar SQL contra dev compartida**, mostrar al usuario host/db/user para que confirme.

## Proyecto

- Frontend necesita `NODE_OPTIONS=--openssl-legacy-provider` con Node v17+
- Firebase no configurado en local, plugin usa stub vacío
- Tablas clave: pedclit (pedidos), albclit/albclil (remitos), clientes, agentes, articulo
- Gotcha: columnas duplicadas en SELECT por JOINs, case sensitivity en nombres de columna PHP
- Backend usa varias DBs: NB_WEB (default), NewBytes_DBF, LO, NEW_BYTES, CS
- Rutas syncUp usan TOKEN_SYNCUP del .env, no JWT
- Branching: Development como base, hotfix/*, deploy frontend via gamma
- **Dashboard LO** en branch `feature/dashboard-lo` — ver [[modulo-dashboard-lo]]
  - Entregados = `MS_VENTAS_REMITOS.ID_STATUS > 1` (no `pedclit.delivered`)
  - Carritos cuenta desde pedidosCabecera sin requerir pedclit
  - navList[1] = Libre Opción, navList[2] = Pedidos (desplazado)
  - opcache PHP: ejecutar `docker exec api-rest-pedidos-apirest-laravel php -r "opcache_reset();"` después de modificar PHP
  - Filtros OrderList agregados: `loOnly`, `loCancelled`, `motivoCancelacion`, `mpPaymentStatus`, `mpPaymentStatusDetail`, `sinMotivo`
- **[[feature-asignacion-oc|Asignación OC ↔ Venta]]** en branch `feature/asignacion-oc-pedclil` (ambos repos)
  - Tabla `pedclil_oc_asignacion` (NewBytes_DBF). FK lógica `pedclil_id` (pedclil.id IDENTITY).
  - Vistas `vw_saldo_oc` y `vw_pedclil_estado_asignacion`. Trigger `tg_pedclit_cestado_asignacion`.
  - 5 endpoints HTTP en `Asignacion/AsignacionController` + command `asignaciones:fifo`.
  - Env vars: `ASSIGNMENT_FEATURE_ENABLED`, `ASSIGNMENT_COMPANIES`, `ASSIGNMENT_ALLOW_PARTIAL` (deben coincidir backend↔frontend).
  - **Driver dblib no soporta índices filtrados** → todos los índices del feature van sin `WHERE`.
  - **pedprol no tiene IDENTITY** → identificación por tupla `(nNumPed, nLinea, cRef)`.
  - Decisiones cerradas con el usuario:
    - FIFO por fecha de OC (sin otras políticas en v1)
    - Asignación parcial permitida; no bloquea MakeSale
    - Sin migración retroactiva (Opción A)
    - Cross-warehouse permitido a nivel asignación
    - Toda OC con saldo es candidata sin filtrar por cEstado (Opción C)
  - Cambios colaterales en backend: `OrderDetailDto.companyCode`, `OrderItemDto.pedclilId`. Eran necesarios para que el frontend del feature funcione (item.id estaba mapeado a articulo.ID_ARTICULO, no a la línea de venta).
  - Documentación canónica: `/Users/hermess/www/pedidos/docs/asignacion-oc-pedclil.md` y `database/sql/README.md`.
  - **Iteraciones 2026-04-24** post primer merge a Development:
    - `cantidad: 0` en `PUT /asignaciones/lineas/{id}` se ignora silenciosamente; items vacíos / todos en 0 = liberar todo (DELETE-like).
    - Modal: columnas nuevas **Proveedor** (`FP_Proveedores.cnompro`) y **Proforma** (`PedProT.CSUPROF_TEMP`) via JOIN en `candidatasFifo` (sin tocar la vista).
    - Modal: número de OC clickeable → `compras.saftel.com/orders` con `companyCode`.
    - **Fix sutil**: el modal NO debe rellenar OCs sin vigente con sugerencia FIFO si la línea ya tiene asignaciones guardadas. Si lo hace, parece que el save anterior falló. Ver [[feedback_modal_asignacion_no_fifo_si_vigentes]] (en memoria local).
    - Workflow de merge: cuando Development recibe PRs paralelos sobre `AsignarOCModal.vue`, hacer `git fetch && git reset --hard origin/Development` antes de pushear, force-push con `--force-with-lease`.
  - **Iteraciones 2026-04-24 (segunda tanda)** — bloques de contexto read-only en el modal:
    - Columna **Costo** (`pedprol.nPreDiv` por `nNumPed + cRef`) agregada a la tabla editable.
    - Dos endpoints GET nuevos: `/asignaciones/stock-almacenes` (stock del SKU por depósito) y `/asignaciones/comprometido` (pedidos pendientes + remitos sin facturar del SKU). Total: **7 endpoints** en `AsignacionController`.
    - Render en modal: chips con `a-tag` para stock (verde si >0) + `a-collapse` con dos `a-table` compactas para órdenes/remitos.
    - Regla general: **separar estado editable (filas con input) de contexto read-only** (chips / collapse). El contexto va fuera del `<a-table>` principal. Ver [[feedback_modal_contexto_vs_edicion]] en memoria local.
    - Schema confirmado (gotchas): `FP_Almacen.CNOMBRE` (no `cDesAlm`); `clientes` tiene dos PKs (`ccodcli` string para pedclit, `ID_CLIENTE` int para albclit); `albclit.lfacturado=0` = reserva formal sin factura; `stocks.nstock` = físico, `stocks.nstock_reserva_pedidos` = ya reservado.
  - **Iteraciones 2026-04-25** — modo read-only, persistencia en DB, JWT extendido:
    - Modal en modo **solo lectura** para pedidos remitidos (`cestado='S'`) — prop `readOnly`, botón 👁️ en `Detail.vue`, acepta asignaciones en estado V o C, filas huérfanas para OCs sin saldo disponible. Permite ver la asignación consumida sin modificarla.
    - **Columna DB nueva** `pedclil_oc_asignacion.costo_seleccionado BIT NOT NULL DEFAULT 0` — reemplaza la persistencia en localStorage (que era por-navegador). Portable entre máquinas. Camino: PUT items → request valida → service propaga → insertAsignacion graba → asignacionesDeLinea devuelve. Persistencia solo al Guardar (no hay endpoint PATCH granular por toggle).
    - Scripts DDL `database/sql/2026_04_25_001_{add,drop}_costo_seleccionado.sql` — con `USE [NewBytes_DBF]; GO` y `sys.columns/sys.tables` para cross-db robusto.
    - **JWT extendido a 60 días** — `.env backend` `JWT_EXPIRATION_TIME="now + 60 days"` (antes 24 hours); `nuxt.config.js` `refreshToken.maxAge = 60 * 60 * 24 * 60`. Rotar `JWT_SIGNATURE_KEY` si hay que invalidar todos los tokens.
    - **Gotcha crítico SSMS**: pegar apply + drop en la misma ventana los ejecuta a ambos, borrando el schema recién creado. Hay que tratarlos como scripts separados. Ver [[feedback_ssms_gotchas|feedback memoria local]].
    - **Gotcha cosmético SSMS**: `SET IMPLICIT_TRANSACTIONS ON` produce warning "ROLLBACK TRANSACTION sin BEGIN TRANSACTION" tras los DDL. Ignorar o desactivar.
  - **Iteraciones 2026-04-24 (tercera tanda)** — flujo "Guardar con costo" y rediseño del dropdown:
    - Título dinámico del modal: `branch - order - id_articulo - producto_nombre (Asignar línea de compra)`. Requiere JOIN a `articulo.cDetalle` en `pedclilInfo`.
    - Checkboxes por fila en columna Costo con persistencia en `localStorage['asignarOC.costoTildados.{pedclilId}']`. El bloque "Costo promedio ponderado" suma las filas tildadas con cantidad > 0.
    - Botón **"Guardar con costo"** hace `PATCH /v1/orders/addItem` con el promedio ponderado como `costForSale`, después persiste la asignación OC. El modal emite `saved: { conCosto }` y `Detail.vue` refresca el detalle solo si `conCosto=true` (sino la columna Costo sigue mostrando el valor viejo).
    - **Gotcha crítico del PATCH `/orders/addItem`**: `selectedPrice` DEBE ser `pedclil.npreunit` (precio unitario real > 0), NO `listaPrecio` (código 0/1/2… — el backend rechaza con *"No se permite un precio menor o igual a 0"* si se manda 0). `pedclilInfo` ahora expone `precio_unitario`, `id_almacen`, `lista_precio`.
    - **Tag "ASIGNADA"** (violeta) en dropdown de Costo de `Detail.vue` cuando `costForSale === costoPonderadoPorLinea` (mismo redondeo en ambos lados). Alternativa al no tener columna `cost_source` en DB; heurística frágil pero suficiente.
    - **Bug de redondeo JS** — `toLocaleString` y `toFixed` redondean distinto en bordes como `139.725` (IEEE-754 lo guarda como `139.7249999…`). Fix: usar `Math.round((x + Number.EPSILON) * 100) / 100` como única regla, tanto en display como en PATCH/store. Ver [[feedback_redondeo_js_consistente]] en memoria local.
    - Dropdown de Costo rediseñado (`Detail.vue`): tags redondeados (ACTUAL/PROMEDIO/ASIGNADA), `tabular-nums` para alinear precios, `dropdown-match-select-width=false` + `minWidth: 320px`. Los estilos van en `<style lang="less">` **no scoped** porque los `a-select-option` se portal-izan al `body`.

## Referencias

- Bugs trackeados en Jira (integrado via apiJira.client.js)
- Docker container backend: `api-rest-pedidos-apirest-laravel` (puerto 8093)
- DB dev: SAFDB2 (host 190.210.23.108:1433), user `eferreyra_devweb01` — autorizada para uso por el usuario
- Documentación de features grandes vive en `docs/` del monorepo + nota dedicada en bóveda

## Ver también

- [[pedidos]] — Índice del proyecto
- [[contexto]] — Gotchas técnicos
- [[arquitectura]] — Estructura
- [[feature-asignacion-oc]] — Feature actual
- [[modulo-dashboard-lo]] — Feature reciente
- [[modulo-makesale]] / [[modulo-removesale]]

- **[[feature-laset-import|Laset Import Framework]]** en branch `lasetImportFramework` (ambos repos)
  - CompanyCode=11. Importadora uruguaya — ver [[contexto#Empresas activas (FP_Empresas)]].
  - **Regla cero**: nunca modificar tablas ERP existentes (`pedprot`/`pedprol`/`pedproi`/`pedclit`/`pedclil`/`stocks`/`FP_*`/`forwarders`/`rebates`). Solo lectura. Toda metadata de matching vive en `laset_import_staging.matched_*`. Ver [[contexto#Regla cero: tablas ERP son read-only]].
  - **Modelo canónico ERP**: compras = `pedprot` + `pedprol` + `pedproi` (incluye cargos extra), ventas = `pedclit` + `pedclil`, stock = `stocks` (por almacén, sin `companyCode`). Ver [[contexto#Modelo canónico ERP (compras / ventas / stock)]].
  - **Gotcha `pedproi`**: NO es solo impuestos — guarda cargos extra del pedido de compra (`cdescrip='camion'` $50/$200). Linkea a `pedprot.nNumPed`, NO a `pedclit`. 158 rows total para companyCode=11.
  - **Gotcha `stocks`**: no tiene `companyCode`. Filtrar por almacenes Laset: DOM, BON, GRI, SAF, URU, ASI.
  - **Gotcha `rebates` huérfana**: 12 rows, schema primitivo, sin `companyCode`, creada con `NewTable` vacía el 2025-11-01. Restos de intento abandonado. NO usar.
  - **Schema staging creado 2026-05-14**: `laset_import_batches` (cabecera por carga) + `laset_import_staging` (67 cols crudas NVARCHAR lossless + 8 cols matching con CHECK enum). Scripts `database/sql/2026_05_14_001_{create,drop}_laset_import_staging.sql`. Aplicados.
  - **Identidad contable**: `SUM(pedprol.nCanPed) − SUM(pedclil.ncanped) = stocks.nstock + nstock_ingresando` por SKU+almacén+companyCode. Sanity check para reconciliación.
  - **CFE Uruguay ya implementado**: tablas `FP_FactWebCliEncabezado_Uy` (179 rows), `FP_FactWebCliDetalle_Uy` (1411), `FP_DocumentosUY` (6), `FP_ComprobantesUY` (9). IVA 22%, DOL, tipoCfe 101=eTicket/102=NC/103=ND. Adendas confirman beneficiario "Laset Sociedad Anonima". Es la mitad downstream del flujo de Laset ya migrada.
  - **Forwarders Laset**: 84 rows con `companyCode=11` en tabla `forwarders` — DHL, Peniel International (Miami), etc.
  - **Insight planilla**: cada fila es 1 venta ↔ 1 compra (Qty=CANTIDAD 100% del tiempo). 339 de 438 Vendor Invoices se repiten en >1 fila → split manual antes de cargar al Excel.
  - **Sistema soporta 11 empresas activas**, no solo NB/NBElectric/LO como decía el CLAUDE.md histórico. Ver [[contexto#Empresas activas (FP_Empresas)]].
  - Próximos pasos: cargador PHP que parsee `docs/laser.xlsx` → poblar staging → reconciliación heurística → migración del delta.
  - Documentación canónica: `docs/laset-import-framework.md` (repo) y [[feature-laset-import]] (Obsidian).
