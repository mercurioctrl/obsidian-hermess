# Pedidos

Sistema de gestión de pedidos de **NB** (New Bytes). Aplicación web interna para vendedores y administradores. Multi-empresa: soporta las **11 empresas activas** del grupo (NB, NBElectric, Libreopción, **Laset**, Mugello, Oxxen, etc.) filtrando por `companyCode`.

## Stack

- **Frontend:** Nuxt.js 2.15 (Vue 2) + Ant Design Vue 1.7
- **Backend:** Laravel 9 (PHP 8.1) + SQL Server
- **Deploy:** Docker (backend, puerto 8093) + PM2 (frontend, puerto 3702)

Ver detalles completos en [[stack|Stack e infraestructura]].

## Notas del proyecto

- [[arquitectura|Arquitectura]] — Estructura, patrones, controllers, modelos, servicios, modelo canónico ERP
- [[stack|Stack]] — Tecnologías, versiones y dependencias
- [[changelog|Changelog]] — Registro de cambios por fecha
- [[contexto|Contexto]] — Reglas de negocio, gotchas, empresas, regla cero ERP
- [[memoria|Memoria]] — Contexto acumulado de sesiones con Claude
- [[modulo-makesale|MakeSale]] — Flujo de ejecución de pedidos (pedido → remito)
- [[modulo-removesale|RemoveSale]] — Flujo de reversión de remitos
- [[modulo-dashboard-lo|Dashboard Libre Opción]] — Estadísticas exclusivas del marketplace LO
- [[feature-asignacion-oc|Feature: Asignación OC ↔ Venta]] — Trazabilidad pedclil ↔ pedprol antes de serializar
- [[feature-asignacion-oc-cookbook|Cookbook Asignación OC]] — Recetas, SQL de debug, curl examples y mapa de archivos
- [[feature-laset-import|Feature: Laset Import Framework]] — Importación de operación FOB de Laset (CODEMP=11) desde planilla histórica al ERP existente
- [[feature-laset-cuenta-corriente|Feature: Import Cuenta Corriente Laset]] — cuenta corriente histórica USD (comp=11) a MC_CCORRIENTES_MOVIMIENTOS; parser Python + reemplazo por cuenta + NB Inc
- [[nota-catalogo-laset|Nota a Catálogo — alta 39 SKUs Laset]] — pedido de alta de artículos comp=11 que destraban Fase D
- [[feature-laset-snapshot-restore|Snapshot/Restore Laset]] — punto de restauración comp=11
- [[feature-laset-fix-pedprot-stockonly|Fix bugs históricos Fase C Laset]] — pedprot/pedprol duplicados + stock-only descartado
- [[feature-laset-fix-marcas-comp11|Fix marcas comp=11]] — refactor Fase C marcas + backfill articulo.Id_Marca + cleanup FP_Marcas dups
- [[feature-laset-wipe-reimport|Borrar todo comp=11 + reimport limpio]] — wipe transaccional con barrido de huérfanos + validación de stocks; flujo Borrar todo → Importar todo
- [[feature-sync-laset-botones|Patrón Sync Laset — botones de mantenimiento]] — service+command+controller+UI para fixes Laset
- [[feature-integrar-eccn|Feature: integrarECCN]] — clasificación ECCN por familia × proveedor para comp=11
- [[feature-pedidos-olvidados|Feature: Pedidos Olvidados]] — filtro oculto de órdenes pendientes/remitidas >2 meses hasta 3 años; fix de timeout acotando la ventana de fecha
- [[feature-descarga-listado-xlsx|Feature: Descarga xlsx de listados]] — botón solo-icono que exporta el listado filtrado de pedidos/clientes a xlsx; endpoint `orders/download` reutilizando `OrderListRepository` sin paginar
- [[feature-ranking-vendedores|Feature: Ranking de vendedores]] — pestaña que rankea vendedores por la suma de puntos (travel miles) de sus clientes en el juego NB Travel Mundial de resellers; modal de desglose por cumplimiento
- [[feature-incentivo-netac|Feature: Incentivo Netac]] — incentivo por unidades vendidas de Netac (Memorias + SSD): cada 12 u = USD 4; reemplaza al Incentivo Gigabyte; detalle por pedido/producto/fecha

## Esquema ERP — Tablas y relaciones

- [[relacion-tablas-ped-alb|Ventas: pedclit / pedclil / albclit / albclil]] — pedido → remito, encabezado → líneas
- [[relacion-tablas-pedprot-pedprol-pedproi|Compras: pedprot / pedprol / pedproi]] — OC encabezado, líneas y cargos extra
- [[relacion-tablas-albprot-albprol|Remitos de compra: albprot / albprol]] — vínculo con pedprot
- [[relacion-tablas-articulo-stocks|Artículo y stocks]] — maestro de productos, balance por almacén, reglas de FK
- [[relacion-tablas-stocks-almacen|Stocks y depósitos (FP_Almacen)]] — columnas de depósito por tabla, depósitos compartidos
- [[relacion-companycode|companyCode — mapa por tabla]] — qué tablas tienen companyCode propio y cuáles lo heredan

## Runbooks y referencias

- [[runbook-alta-usuario-interno|Runbook — Alta de usuario interno]] — pasos para dar de alta un agente interno en el sistema

## Repos

- Backend: `New-Bytes/api-rest-pedidos-laravel` (branch principal: `Development`)
- Frontend: `New-Bytes/pedidos-web-app-v1` (branch principal: `development`)

## Multi-empresa

El sistema soporta **11 empresas activas** (`LACTIVA=1` en `NewBytes_DBF.dbo.FP_Empresas`). Ver [[contexto#Empresas activas (FP_Empresas)]] para la tabla completa.

## Regla cero — tablas ERP read-only

Las tablas legacy del ERP nunca se modifican desde features nuevos. Toda metadata vive en tablas nuevas con prefijo del feature. Ver [[contexto#Regla cero: tablas ERP son read-only]].

## Tareas

- [[API - Fix - Corregir doble-descuento de stock por race en MakeSale|API - Fix - Doble-descuento de stock (race MakeSale/RemoveSale)]]
- [[API - Fix - Script de regularización stock doble-descuento|API - Fix - Script de regularización stock doble-descuento]]
- [[API - Research - Causas del stockDelta distinto de cero|API - Research - Causas del stockDelta != 0 (auditoría global)]]
- [[API - Research - Stock en estanteria no reflejado en el sistema|API - Research - Stock en estantería no reflejado en el sistema]]
- [[API - Fix - Correccion albclil faltante en ventas cobradas (caso DIAMOND)|API - Fix - Corrección: albclil faltante en ventas cobradas (DIAMOND)]]

---
*Última sincronización: 2026-06-23 — Tanda Laset 19–23/06: nueva [[feature-laset-cuenta-corriente|Import de cuenta corriente histórica comp=11]] (parser Python, reemplazo por cuenta, matching NB Inc, exclusión USDT, fix autoFilter openpyxl) y regla [[contexto#FLETE nunca en la compra|FLETE nunca en la compra]] (Fase C). DB dev pasó a remota (db-nb-dev.blu.net.ar:41433). Ver [[changelog#2026-06-22 — Cuenta corriente histórica Laset (botón) + FLETE nunca en la compra]].*