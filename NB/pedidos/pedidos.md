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
- [[feature-integrar-eccn|Feature: integrarECCN]] — clasificación ECCN (control de exportación) por familia × proveedor para comp=11

## Repos

- Backend: `New-Bytes/api-rest-pedidos-laravel` (branch principal: `Development`)
- Frontend: `New-Bytes/pedidos-web-app-v1` (branch principal: `development`)

## Multi-empresa

El sistema soporta **11 empresas activas** (`LACTIVA=1` en `NewBytes_DBF.dbo.FP_Empresas`). Las históricamente más mencionadas son **NB**, **NBElectric** y **Libreopción**, pero también hay **OXXEN**, **NBGLOBAL**, **DIGITO BINARIO**, **CCRT**, **SUC 10**, **MUGELLO**, **PISOS Y REVESTIMIENTOS** y **LASET** (única importadora — ver [[feature-laset-import]]). Ver [[contexto#Empresas activas (FP_Empresas)]] para la tabla completa.

## Regla cero — tablas ERP read-only

Las tablas legacy del ERP (`pedprot`, `pedprol`, `pedproi`, `pedclit`, `pedclil`, `stocks`, `FP_*`, `forwarders`, `rebates`) **nunca se modifican** desde features nuevos. Se leen via `SELECT/JOIN`. Toda metadata de cualquier feature vive en tablas nuevas con prefijo del feature (`pedclil_oc_asignacion`, `laset_import_*`). Ver [[contexto#Regla cero: tablas ERP son read-only]].

---
*Última sincronización: 2026-05-22 — Feature **[[feature-integrar-eccn|integrarECCN]]** completo y pusheado (rama `integrarECCN`, back `2c87867e` / front `d0083b6`): tabla `ecc_familia_proveedor` + import, permiso RBAC `eccView`, ECCN por ítem en el detalle de orden (JOIN condicional según permiso) y carga manual con lápiz + popover (`POST /v1/ecc`). Documentada la secuencia de **deploy a producción** (DDL → import → activar permiso → re-login) en [[feature-integrar-eccn#Deploy a producción]]. SQL `2026_05_21_00{1,2}` aún solo en dev. Ver [[feature-integrar-eccn]] y [[changelog#2026-05-21 (cont.) — integrarECCN: permiso, detalle de orden y carga manual]].*
