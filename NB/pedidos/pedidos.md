# Pedidos

Sistema de gestión de pedidos de **NB** (New Bytes). Aplicación web interna para vendedores y administradores.

## Stack

- **Frontend:** Nuxt.js 2.15 (Vue 2) + Ant Design Vue 1.7
- **Backend:** Laravel 9 (PHP 8.1) + SQL Server
- **Deploy:** Docker (backend) + PM2 (frontend)

Ver detalles completos en [[stack|Stack e infraestructura]].

## Notas del proyecto

- [[arquitectura|Arquitectura]] — Estructura, patrones, controllers, modelos y servicios
- [[stack|Stack]] — Tecnologías, versiones y dependencias
- [[changelog|Changelog]] — Registro de cambios por fecha
- [[contexto|Contexto]] — Reglas de negocio, gotchas y decisiones
- [[memoria|Memoria]] — Contexto acumulado de sesiones con Claude
- [[modulo-makesale|MakeSale]] — Flujo de ejecución de pedidos (pedido → remito)
- [[modulo-removesale|RemoveSale]] — Flujo de reversión de remitos
- [[modulo-dashboard-lo|Dashboard Libre Opción]] — Estadísticas exclusivas del marketplace LO
- [[feature-asignacion-oc|Feature: Asignación OC ↔ Venta]] — Trazabilidad pedclil ↔ pedprol antes de serializar

## Repos

- Backend: `New-Bytes/api-rest-pedidos-laravel` (branch principal: `Development`)
- Frontend: `New-Bytes/pedidos-web-app-v1` (branch principal: `Development`)

## Multi-marca

El sistema soporta tres marcas: **NB**, **NBElectric** y **Libreopción**. Se filtran por `companyCode` en la mayoría de endpoints y tablas.

---
*Última sincronización: 2026-04-24*
