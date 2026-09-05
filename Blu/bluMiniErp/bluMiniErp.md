# bluMiniErp

Sistema de gestion interna (ERP) para BluInc Studio. Cubre el ciclo completo: clientes, presupuestos, proyectos, gastos, bancos/cajas, cuenta corriente y personal.

**Ultima sincronizacion:** 2026-09-05

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
| [[Modulo Personal]] | Empleados, asignacion a proyectos, pagos, vínculo con usuario del sistema + **Área de empleado `/mi-area`** (datos, rol, banco, cumpleaños), **vacaciones en días hábiles + feriados + días extra (premio)** (2026-08) y **recordatorio de sueldos pendientes del mes vencido** con deep-link al pago precargado (2026-08-27) |
| [[Modulo People Performance]] | RRHH sobre Personal: rol&expectativas, competencias (1-5), objetivos (OKRs), ausencias (rango), reuniones 1:1, evidencia GitHub/Jira (tab Actividad, auto-vincular Jira). Fase 1 + inicio Fase 2 (2026-07-14) |
| [[Modulo Calendario]] | Vista mensual que unifica tareas con deadline, ausencias/vacaciones, 1:1, objetivos, feriados **y reservas de reuniones** + suscripción externa iCal (Google/Apple/Outlook). `VER_SECCION_CALENDARIO` (2026-07-14) |
| [[Modulo Reservas Reuniones]] | Link público tipo Calendly por usuario (`/agendar/{slug}`): un externo agenda un slot; disponibilidad self-service (`/mi-disponibilidad`) híbrida (reglas semanales + bloqueos/extras) con **editor visual de grilla semanal**; invitados múltiples con invite `.ics`, evento en Calendario, notificación in-app/push y **recordatorios al anfitrión (email+push, el día y 1h antes)** (2026-08-27) |
| [[Modulo Contabilidad]] | Sección `/contabilidad`: liquidación de impuestos del período (IVA/Ganancias/IIBB) + Libro IVA en Excel (Ventas/Compras). Datos fiscales del gasto (mig 0101). Lista de compras incompletas con acceso a completar, simulador de compras (what-if) y "Te queda después de impuestos", Rentabilidad por Cliente en el dashboard (2026-08-23). `VER_SECCION_CONTABILIDAD` (2026-08-21) |
| [[Modulo Remitos]] | Desde un presupuesto genera un remito (copia sus ítems) independiente y editable (no toca el presupuesto). Varios por presupuesto. Tradicional (descripción+cantidad, sin precios), PDF formato BLU. Mig 0102 (2026-08-23) |
| [[Modulo Flota GSM]] | Líneas SIM prepagas: alta de números, cargas, vencimiento (`fecha_carga + meses_vigencia`) y **alertas por email** a contactos por línea (al cargar + 15 días antes vía comando `gsm:alertas-vencimiento`). Seguimiento, no toca finanzas. Mig 0109. `VER_SECCION_FLOTA_GSM` (2026-08-29) |
| [[Modulo Novedades]] | **Blog público multi-tenant por cliente** con enlace secreto rotable (capability URL tipo Calendly, sin login). Se alimenta de activaciones→hitos + adjuntos imagen; aislamiento por `cliente_id` resuelto desde el token. Seguimiento, no toca finanzas. Mig 0110 (rama `feat/novedades-cliente`, 2026-09-03) |
| [[Modulo Requerimientos]] | **Tablero tipo Trello por cliente** en el mismo portal que Novedades (tabs, mismo `novedades_token`). El cliente carga/mueve tarjetas con **comentarios, adjuntos (enlace con fetch de título), checklist y fecha límite**; el equipo gestiona columnas y **convierte un requerimiento en Tarea** interna. Notifica a admins (in-app + push). Seguimiento/intake, no toca finanzas. Mig 0111 (base) + 0112 (tarjetas ricas). `VER_SECCION_REQUERIMIENTOS` (PR #56 mergeado, PR #58 tarjetas ricas) |
| [[Modulo Gastos Personal]] | **Rendición de reembolsos del empleado**: carga desde `/mi-area` sus gastos de bolsillo con **evidencia** (imagen/PDF) → quedan **PENDIENTE** hasta que un admin **aprueba/rechaza** (con motivo, notifica al empleado). Panel admin consolidado `/gastos-personal` + tab en `/staff/{id}`, gate `VER_SECCION_PERSONAL`. Seguimiento/intake, **no toca finanzas** (no genera Gasto real ni descuenta banco/caja). Mig 0113 (`gastos_empleado` + `gasto_empleado_adjuntos`) (rama `feat/gastos-personal`, PR #60, 2026-09-05) |
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
