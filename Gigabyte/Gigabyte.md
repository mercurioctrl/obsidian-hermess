# Gigabyte

Proyectos y sistemas para la marca **Gigabyte** (hardware IT).

## Proyectos

### gigaErp

Sistema interno de gestión de distribuidores, marketing, mercadería, catálogo, órdenes de venta, facturación, cuenta corriente y tareas.

- [[gigaErp/gigaErp|gigaErp — Sistema de gestión]] — `http://localhost:8824`

**Cheatsheet y troubleshooting:**
- [[gigaErp/troubleshooting|Troubleshooting]] — gotchas (Sanctum, optimize:clear, nginx, Nuxt routing) con causa y fix
- [[gigaErp/stack|Stack]] — tecnologías, versiones, comandos de deploy

**Arquitectura:**
- [[gigaErp/arquitectura|Arquitectura]] — estructura, patrones backend/frontend, rutas, módulos, convenciones, importaciones XLSX
- [[gigaErp/design-system|Design System]] — paleta hex, tipografía, layout, botones
- [[gigaErp/componentes-ui|Componentes UI]] — Modal, DataTable, FormField, StatusBadge

**Módulos de negocio:**
- [[gigaErp/modulos/productos|Productos]] — catálogo, 4 listas de precio, SKU per-distribuidor, importaciones XLSX
- [[gigaErp/modulos/ordenes-venta|Órdenes de Venta]] — pipeline BORRADOR → FACTURADA, validación stock en depósito
- [[gigaErp/modulos/invoice-preview|Invoice Preview]] — HTML preview estilo Blu + PDF cliente-side

**Contexto y registros:**
- [[gigaErp/contexto|Contexto]] — reglas de negocio, distribuidores, saldos cc, nomenclatura UI, TODOs
- [[gigaErp/memoria|Memoria]] — convenciones críticas, endpoints, debugging checklist
- [[gigaErp/changelog|Changelog]] — historial de construcción sesión a sesión
