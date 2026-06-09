# NB — New Bytes

Proyectos del sistema NB (New Bytes). Aplicaciones internas de gestión para el grupo empresarial.

---

## [[pedidos/pedidos|Pedidos]]
Sistema de gestión de pedidos multi-empresa. Backend Laravel 9 + Frontend Nuxt.js 2. Docker (puerto 8093) + PM2 (puerto 3702).
- [[pedidos/arquitectura|Arquitectura]] — patrones, controllers, servicios, modelo ERP
- [[pedidos/stack|Stack]] — tecnologías y dependencias
- [[pedidos/changelog|Changelog]] — historial de cambios
- [[pedidos/contexto|Contexto]] — reglas de negocio, gotchas, empresas
- [[pedidos/memoria|Memoria]] — contexto acumulado de sesiones con Claude
- [[pedidos/modulo-makesale|MakeSale]] · [[pedidos/modulo-removesale|RemoveSale]] · [[pedidos/modulo-dashboard-lo|Dashboard LO]]
- [[pedidos/feature-laset-import|Laset Import]] · [[pedidos/feature-asignacion-oc|Asignación OC]] · [[pedidos/feature-asignacion-oc-cookbook|Cookbook OC]] · [[pedidos/feature-integrar-eccn|ECCN]]
- [[pedidos/feature-laset-snapshot-restore|Snapshot/Restore Laset]] · [[pedidos/feature-laset-fix-pedprot-stockonly|Fix bugs Fase C Laset]] · [[pedidos/feature-laset-fix-marcas-comp11|Fix marcas comp=11]] · [[pedidos/feature-laset-wipe-reimport|Borrar todo + reimport limpio]] · [[pedidos/feature-sync-laset-botones|Patrón botones Sync Laset]] · [[pedidos/nota-catalogo-laset|Nota Catálogo Laset]]
- **Esquema ERP:** [[pedidos/relacion-tablas-ped-alb|ventas]] · [[pedidos/relacion-tablas-pedprot-pedprol-pedproi|compras]] · [[pedidos/relacion-tablas-albprot-albprol|remitos compra]] · [[pedidos/relacion-tablas-articulo-stocks|artículo/stocks]] · [[pedidos/relacion-tablas-stocks-almacen|depósitos]] · [[pedidos/relacion-companycode|companyCode]]

---

## [[expedicion/expedicion|Expedición]]
- [[expedicion/arquitectura|Arquitectura]] · [[expedicion/stack|Stack]] · [[expedicion/changelog|Changelog]]
- [[expedicion/contexto|Contexto]] · [[expedicion/documentacion|Documentación]] · [[expedicion/memoria|Memoria]]

---

## [[controldeprecios/controldeprecios|Control de Precios]]
- [[controldeprecios/arquitectura|Arquitectura]] · [[controldeprecios/changelog|Changelog]] · [[controldeprecios/stack|Stack]] · [[controldeprecios/contexto|Contexto]] · [[controldeprecios/memoria|Memoria]]

---

## [[inventario/inventario|Inventario]]
- [[inventario/arquitectura|Arquitectura]] · [[inventario/changelog|Changelog]]
- [[inventario/contexto|Contexto]] · [[inventario/memoria|Memoria]] · [[inventario/stack|Stack]]

---

## [[cobros/cobros|Cobros]]
- [[cobros/cobros|Índice]] · [[cobros/changelog|Changelog]] · [[cobros/arquitectura|Arquitectura]] · [[cobros/stack|Stack]] · [[cobros/contexto|Contexto]]

---

## [[Comprobantes/Comprobantes|Comprobantes]]
- [[Comprobantes/Comprobantes|Índice]] · [[Comprobantes/arquitectura|Arquitectura]] · [[Comprobantes/stack|Stack]] · [[Comprobantes/changelog|Changelog]] · [[Comprobantes/contexto|Contexto]]

---

## [[microservicio-envios/microservicio-envios|Microservicio Envíos]]
- [[microservicio-envios/microservicio-envios|Índice]] · [[microservicio-envios/arquitectura|Arquitectura]] · [[microservicio-envios/stack|Stack]] · [[microservicio-envios/contexto|Contexto]] · [[microservicio-envios/changelog|Changelog]]

---

## [[sincroAfip/sincroAfip|SincroAFIP]]
- [[sincroAfip/sincroAfip|Índice]] · [[sincroAfip/arquitectura|Arquitectura]] · [[sincroAfip/stack|Stack]] · [[sincroAfip/changelog|Changelog]]
- [[sincroAfip/contexto|Contexto]] · [[sincroAfip/despliegue|Despliegue]] · [[sincroAfip/migracion|Migración]] · [[sincroAfip/tabla-referencia|Tabla de referencia]]

---

## [[Compras/Compras|Compras]]
Gestión de compras a proveedores (órdenes, ingresos, comprobantes, posiciones arancelarias) + inteligencia de competencia.
- [[Compras/Compras|Índice]] · [[Compras/arquitectura|Arquitectura]] · [[Compras/stack|Stack]] · [[Compras/changelog|Changelog]]
- [[Compras/competencia|Competencia]] · [[Compras/memoria|Memoria]] · [[Compras/reglas-compras|Reglas de compras]]

---
*Última actualización: 2026-06-04 — compras: nueva sección Competencia (catálogo de competidores, rama `competencia`).*
