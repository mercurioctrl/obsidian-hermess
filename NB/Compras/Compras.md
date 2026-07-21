# Compras

Sistema de gestión de compras a proveedores para New Bytes (NB). Permite crear órdenes de compra, gestionar proveedores, ingresos parciales/totales, comprobantes, cuenta corriente de proveedores, posiciones arancelarias y depósitos.

## Stack

- **API:** Laravel 9 + PHP 8.1, dockerizada con Apache — [[stack#API|ver detalle]]
- **Frontend:** Nuxt 2 + Vue 2 + Ant Design Vue — [[stack#Frontend|ver detalle]]
- **Base de datos:** SQL Server (externa, sin migraciones Laravel)

## Notas del proyecto

- [[arquitectura|Arquitectura]] — Estructura, patrones, módulos
- [[stack|Stack tecnológico]] — Frameworks, dependencias, servicios externos
- [[changelog|Changelog]] — Historial de cambios
- [[contexto|Contexto y reglas]] — Reglas de negocio, decisiones y deuda técnica
- [[memoria|Memoria del proyecto]] — Consolidado de la memoria persistente de Claude
- [[competencia|Competencia]] — Catálogo de competidores (mayoristas y revendedores)

## Ver también

- [[NB/compras/reglas-compras|Reglas de negocio — Compras]] — reglas del proceso de compras

## Repositorios

- `api-rest-compras-laravel/` — API REST (repo Git independiente)
- `compras-web-app-v1-/` — Web app Nuxt (repo Git independiente)

## Proyecto Jira

Las tareas se trackean con prefijo `COM-` en Jira.

---
*Última sincronización: 2026-07-21 — fix (API, hotfix): `ncosteprom` en ingresos de órdenes en pesos (PSO) ahora se convierte a dólares con `nvaldiv_FISCAL` en vez de `nValDiv` (que en PSO es 1) — antes guardaba el costo promedio en pesos sin convertir (orden 13973: 100 en vez de 0,0667). Rama `hotfix-ncosteprom-cotizacion-fiscal-pso` (base `Development`, `7e12bdc`, pusheada). Corrige el hotfix previo PR #425. Ver [[changelog#2026-07-21|changelog]].*
*2026-07-20 — feat: eliminar línea puntual de orden pendiente desde el tacho del detalle. Nuevo `DELETE /providerOrder/{orderId}/item/{itemId}` (API) + reapuntado del tacho (front); el tacho antes pegaba al endpoint de impuestos distribuidos. Ramas `feature/eliminar-linea-orden-pendiente` en ambos repos (pusheadas, sin PR aún).*
*2026-07-02 — front COM-320: moneda y cotización única en el header del detalle (pesos→fiscal, dólares→quote), consumiendo los campos de divisa de la API. En `gamma`, pendiente de `development`.*
*2026-06-30 — columna "Pedido"/inboundIds en Órdenes (COM-444); moneda y cotizaciones del Ingreso desde PedProt; `items` sin filtro `ocultarDeNb`; fix de Ingresos duplicados (GROUP BY nullable + count distinct); `.env` apuntado a saftel `10.10.10.47` (cmercurio).*
