# bluMiniErp

Sistema de gestion interna (ERP) para BluInc Studio. Cubre el ciclo completo: clientes, presupuestos, proyectos, gastos, bancos/cajas, cuenta corriente y personal.

**Ultima sincronizacion:** 2026-08-23

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
| [[Modulo Personal]] | Empleados, asignacion a proyectos, pagos, vínculo con usuario del sistema + **Área de empleado `/mi-area`** (datos, rol, banco, cumpleaños) y **vacaciones en días hábiles + feriados + días extra (premio)** (2026-08) |
| [[Modulo People Performance]] | RRHH sobre Personal: rol&expectativas, competencias (1-5), objetivos (OKRs), ausencias (rango), reuniones 1:1, evidencia GitHub/Jira (tab Actividad, auto-vincular Jira). Fase 1 + inicio Fase 2 (2026-07-14) |
| [[Modulo Calendario]] | Vista mensual que unifica tareas con deadline, ausencias/vacaciones, 1:1, objetivos, feriados **y reservas de reuniones** + suscripción externa iCal (Google/Apple/Outlook). `VER_SECCION_CALENDARIO` (2026-07-14) |
| [[Modulo Reservas Reuniones]] | Link público tipo Calendly por usuario (`/reservar/{token}`): un externo agenda un slot; disponibilidad self-service (`/mi-disponibilidad`) híbrida (reglas semanales + bloqueos/extras); invitados múltiples con invite `.ics`, evento en Calendario y notificación in-app/push (2026-08-10) |
| [[Modulo Contabilidad]] | Sección `/contabilidad`: liquidación de impuestos del período (IVA/Ganancias/IIBB) + Libro IVA en Excel (Ventas/Compras). Datos fiscales del gasto (mig 0101). `VER_SECCION_CONTABILIDAD` (2026-08-21) |
| [[Modulo Remitos]] | Desde un presupuesto genera un remito (copia sus ítems) independiente y editable (no toca el presupuesto). Varios por presupuesto. Tradicional (descripción+cantidad, sin precios), PDF formato BLU. Mig 0102 (2026-08-23) |
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
