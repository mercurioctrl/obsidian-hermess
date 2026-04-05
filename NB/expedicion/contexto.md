# Contexto — Expedición

## Qué es

Sistema de **expedición/logística de warehouse** para NB (distribuidor mayorista). Gestiona el flujo completo de mercadería: entrada de proveedores, almacenamiento, serialización, preparación de pedidos, env��os, retiros, devoluciones y comprobantes.

## Estructura del monorepo

Dos sub-proyectos independientes, cada uno con su propio repositorio git:

```
expedicion/
├── api-rest-expedicion/     ← Backend (PHP/Slim 4)
├── expedicion-web-app-v1/   ← Frontend (Nuxt 2/Vue 2)
└── CLAUDE.md
```

## Stack

### Backend
- **PHP 8.3** (originalmente 8.0, actualizado en esta sesión)
- **Slim 4** — micro-framework REST
- **SQL Server** (ODBC Driver 18) — base de datos principal (`NB_WEB`, `NEW_BYTES`, `NewBytes_DBF`)
- **Pimple 3.4** — contenedor de inyección de dependencias
- **Docker** — Ubuntu 22.04 + Apache + PHP + ODBC
- **Phinx** — migraciones de base de datos

### Frontend
- **Nuxt 2** (Vue 2) — framework SSR/SPA
- **Ant Design Vue 1.x** — librería de componentes UI
- **Vuex** — state management (módulos por dominio)
- **Less** — preprocesador CSS (color primario: azul #304794)
- **PM2** — process manager para producción
- **Firebase** — push notifications (client-side)
- **vee-validate** — validación de formularios

### Servicios externos
- **MS Envíos** — microservicio de envíos/tracking
- **MS Comprobantes** — microservicio de facturación
- **Postventa** — API de postventa
- **Jira** — reportes de soporte (via API)

## Dominios de negocio

| Dominio | Descripción |
|---------|-------------|
| **Passes (Pases)** | Transferencias de inventario entre depósitos |
| **Providers (Proveedores)** | Entrada/recepción de mercadería de proveedores |
| **Shipments (Envíos)** | Preparación y despacho de pedidos para envío |
| **PickUp (Retiro)** | Pedidos que el cliente retira en persona |
| **Stock** | Control de inventario y serialización |
| **Refund (Devoluciones)** | Gestión de devoluciones |
| **Vouchers (Comprobantes)** | Emisión de facturas/remitos |
| **Tracking Orders** | Seguimiento de envíos y drops |

## Autenticación

- JWT-based (generado por el backend, almacenado por `@nuxtjs/auth-next`)
- Permisos como flags booleanos en el objeto user: `expPickUp`, `expShipment`, `expEntry`, `expPasses`, `expStock`, `expRefund`, `expVoucher`, `expTracking`
- Route guards en frontend + PermissionMiddleware en backend

## Entornos

- **Desarrollo local:** API en `localhost:8084`, Frontend en `localhost:4149`
- **Gamma:** Deploy automático via GitHub Actions (SSH) al mergear PR a branch Gamma
- **Producción:** `api.warehouse.lio.red`, `api2.warehouse.lio.red`

## Estado actual (2026-04-05)

- App funcionando localmente (front + back conectados)
- Docker actualizado a Ubuntu 22.04 / PHP 8.3 / ODBC 18 para compatibilidad con Apple Silicon (ARM64)
- SQL Server remoto conectado (190.210.23.108:1433, base NB_WEB)
- Sin tests automatizados en ninguno de los dos sub-proyectos

---

## Ver también

- [[NB/expedicion/arquitectura|Arquitectura]] — Diagramas, capas, flujo de request
- [[NB/expedicion/stack|Stack]] — Tecnologías y versiones
- [[NB/expedicion/documentacion|Documentación]] — Setup, comandos, variables de entorno
- [[NB/expedicion/changelog|Changelog]] — Historial de cambios
- [[NB/expedicion/memoria|Memoria]] — Problemas resueltos y decisiones
