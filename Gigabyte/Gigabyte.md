# Gigabyte

Proyectos y sistemas para la marca **Gigabyte** (hardware IT).

## Proyectos

### gigaErp

Sistema interno de gestión de distribuidores, marketing, mercadería, catálogo, órdenes de venta, facturación, cuenta corriente, línea de crédito, notas de crédito y tareas.

- [[gigaErp/gigaErp|gigaErp — Sistema de gestión]] — `http://localhost:8824`

**Cheatsheet y troubleshooting:**
- [[gigaErp/troubleshooting|Troubleshooting]] — gotchas (Sanctum, optimize:clear, nginx, Nuxt routing) con causa y fix
- [[gigaErp/stack|Stack]] — tecnologías, versiones, comandos de deploy

**Arquitectura:**
- [[gigaErp/arquitectura|Arquitectura]] — estructura, patrones backend/frontend, rutas, módulos, notas de crédito, línea de crédito
- [[gigaErp/design-system|Design System]] — paleta hex, tipografía, layout, botones
- [[gigaErp/componentes-ui|Componentes UI]] — Modal, DataTable, FormField, StatusBadge

**Módulos de negocio:**
- [[gigaErp/modulos/productos|Productos]] — catálogo, 4 listas de precio, SKU per-distribuidor
- [[gigaErp/modulos/ordenes-venta|Órdenes de Venta]] — BORRADOR→APROBADA→FACTURADA, notas de crédito desde orden
- [[gigaErp/modulos/invoice-preview|Invoice Preview]] — HTML preview estilo Blu + PDF cliente-side

**Contexto y registros:**
- [[gigaErp/contexto|Contexto]] — reglas de negocio, distribuidores, saldos cc, línea de crédito, TODOs actualizados
- [[gigaErp/memoria|Memoria]] — gotchas, nota de crédito, patrones de filtros, authStore
- [[gigaErp/changelog|Changelog]] — historial de construcción sesión a sesión
