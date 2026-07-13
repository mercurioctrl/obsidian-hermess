# bluMiniErp

Sistema de gestion interna (ERP) para BluInc Studio. Cubre el ciclo completo: clientes, presupuestos, proyectos, gastos, bancos/cajas, cuenta corriente y personal.

**Ultima sincronizacion:** 2026-07-13

## Arquitectura

| Documento                   | Contenido                                                 |
| --------------------------- | --------------------------------------------------------- |
| [[Stack e Infraestructura]] | Docker, puertos, variables de entorno, comandos de deploy |
| [[Base de Datos]]           | 23 tablas, columnas, relaciones y migraciones             |
| [[Backend - Modelos]]       | Modelos Eloquent: fillable, casts, relaciones, metodos    |
| [[Backend - API]]           | Todas las rutas API y controllers                         |
| [[Frontend]]                | Paginas, stores, composables, layout, convenciones        |

## Modulos

| Documento | Contenido |
|-----------|-----------|
| [[Modulo Tareas]] | Tablero kanban estilo Jira: seguimiento (watchers) y notificaciones in-app / correo / push (VAPID) / WhatsApp |
| [[Modulo GitHub]] | Integración GitHub solo lectura (PAT): dashboard de rendimiento por dev + vista detallada con commits día a día. Persistencia + sync incremental (2026-07-11) |
| [[Modulo Documentos]] | Descarga de documentos corporativos: original + versión con formato BLU (registry en config, sin DB) (2026-07-11) |
| [[Modulo Personal]] | Empleados, asignacion a proyectos, pagos, vínculo con usuario del sistema |
| [[Reglas de Negocio]] | Reglas de dominio criticas y comportamientos no obvios |
| [[Modulo Permisos]] | Sistema de permisos granular por usuario |
| [[Medios de Pago]] | MercadoPago, Stripe y Mercury (cuenta + invoicing) |
| [[Modulo Mercury Invoicing]] | Facturación electrónica USD via Mercury AR API (2026-04-14) |
| [[Modulo WhatsApp Inbox]] | Integración con Inbox API externa + compartir adjuntos por WhatsApp (2026-04-15). OG preview con logo Blu (2026-04-16) |
| [[Errores Comunes]] | Bugs ya cometidos y como evitarlos |

## Sistema de Diseno

| Documento | Contenido |
|-----------|-----------|
| [[Dashboard UI Skill]] | Skill para generar interfaces admin |
| [[Design Tokens]] | Paleta de colores, tipografia, espaciado |
| [[Componentes UI]] | Especificaciones de componentes reutilizables |
| [[Layout System]] | Sidebar + contenido principal, grid |
| [[Page Templates]] | Plantillas de paginas completas |

## Historial y Contexto

| Documento | Contenido |
|-----------|-----------|
| [[changelog|Changelog]] | Registro de commits y features por fecha |
| [[memoria|Memoria]] | Feedback, decisiones y contexto del proyecto |

## Stack

| Capa | Tecnologia |
|------|-----------|
| Frontend | Nuxt 3 + Vue 3 + Tailwind CSS + Pinia |
| Backend | Laravel 11 + PHP 8.3 |
| Base de datos | MySQL 8 |
| Cache | Redis 7 |
| Auth | Laravel Sanctum (Bearer token) |
| PDF presupuestos | Spatie Browsershot + Chromium headless (desde Node 20 + Puppeteer) |
| PDF activaciones | TCPDF + FPDI sobre membretada |
| IA | DeepSeek API |
| Mail | SMTP (box.lio.red, cuenta `payments@blustudioinc.com`) |
| Proxy | Nginx |
| Infraestructura | Docker Compose |

## Acceso

- App: `http://localhost:8823`
- Admin: `admin@empresa.com` / `admin123` (⚠️ el default puede no aplicar en cada entorno si se restauró un backup de prod — la password puede estar cambiada. Para probar endpoints sin login: generar token Sanctum vía SQL directo, ver [[Errores Comunes]])
