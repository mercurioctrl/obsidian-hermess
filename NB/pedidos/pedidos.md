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
- [[nota-catalogo-laset|Nota a Catálogo — alta 39 SKUs Laset]] — pedido de alta de artículos comp=11 que destraban Fase D (para enviar a catálogo)
- [[feature-laset-snapshot-restore|Snapshot/Restore Laset]] — punto de restauración comp=11; correr antes de cada proceso/sesión
- [[feature-laset-fix-pedprot-stockonly|Fix bugs históricos Fase C Laset]] — pedprot/pedprol duplicados (2026-05-29) + stock-only descartado (2026-05-30): 369 OCs consolidadas, 33k unidades restauradas al pedprol
- [[feature-integrar-eccn|Feature: integrarECCN]] — clasificación ECCN (control de exportación) por familia × proveedor para comp=11

## Esquema ERP — Tablas y relaciones

- [[relacion-tablas-ped-alb|Relación pedclit / pedclil / albclit / albclil]] — ventas: pedido → remito, encabezado → líneas
- [[relacion-tablas-pedprot-pedprol-pedproi|Relación pedprot / pedprol / pedproi]] — compras: OC encabezado, líneas y cargos extra
- [[relacion-tablas-albprot-albprol|Relación albprot / albprol]] — remito de compra y su vínculo con pedprot
- [[relacion-tablas-articulo-stocks|Relación articulo / stocks]] — maestro de productos y stock por almacén
- [[relacion-tablas-stocks-almacen|Stocks y depósitos (FP_Almacen)]] — estructura de stocks, columnas de depósito en líneas, flujo de movimientos
- [[relacion-companycode|companyCode — mapa por tabla]] — qué tablas tienen companyCode propio y cuáles lo heredan

## Repos

- Backend: `New-Bytes/api-rest-pedidos-laravel` (branch principal: `Development`)
- Frontend: `New-Bytes/pedidos-web-app-v1` (branch principal: `development`)

## Multi-empresa

El sistema soporta **11 empresas activas** (`LACTIVA=1` en `NewBytes_DBF.dbo.FP_Empresas`). Las históricamente más mencionadas son **NB**, **NBElectric** y **Libreopción**, pero también hay **OXXEN**, **NBGLOBAL**, **DIGITO BINARIO**, **CCRT**, **SUC 10**, **MUGELLO**, **PISOS Y REVESTIMIENTOS** y **LASET** (única importadora — ver [[feature-laset-import]]). Ver [[contexto#Empresas activas (FP_Empresas)]] para la tabla completa.

## Regla cero — tablas ERP read-only

Las tablas legacy del ERP (`pedprot`, `pedprol`, `pedproi`, `pedclit`, `pedclil`, `stocks`, `FP_*`, `forwarders`, `rebates`) **nunca se modifican** desde features nuevos. Se leen via `SELECT/JOIN`. Toda metadata de cualquier feature vive en tablas nuevas con prefijo del feature (`pedclil_oc_asignacion`, `laset_import_*`). Ver [[contexto#Regla cero: tablas ERP son read-only]].

---
*Última sincronización: 2026-05-30 — Análisis completo del esquema ERP: relaciones entre tablas de pedidos/remitos/compras/ventas, mapa de companyCode, depósitos compartidos. Fix: columna companyCode agregada a albclit (ALTER + UPDATE 395k filas + fix en MakeSaleRepository). Ver [[changelog#2026-05-30 — Análisis de esquema ERP y companyCode en albclit]].*
