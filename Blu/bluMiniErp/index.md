# bluMiniErp

Sistema de gestion interna (ERP) para BluInc Studio. Cubre el ciclo completo: clientes, presupuestos, proyectos, gastos, bancos/cajas, cuenta corriente y personal.

**Ultima sincronizacion:** 2026-04-04

## Arquitectura

| Documento | Contenido |
|-----------|-----------|
| [[Stack e Infraestructura]] | Docker, puertos, variables de entorno, comandos de deploy |
| [[Base de Datos]] | 22 tablas, columnas, relaciones y migraciones |
| [[Backend - Modelos]] | Modelos Eloquent: fillable, casts, relaciones, metodos |
| [[Backend - API]] | Todas las rutas API y controllers |
| [[Frontend]] | Paginas, stores, composables, layout, convenciones |

## Modulos

| Documento | Contenido |
|-----------|-----------|
| [[Modulo Personal]] | Empleados, asignacion a proyectos, pagos |
| [[Reglas de Negocio]] | Reglas de dominio criticas y comportamientos no obvios |
| [[Modulo Permisos]] | Sistema de permisos granular por usuario |
| [[Medios de Pago]] | MercadoPago, Stripe y Mercury |
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
| [[Changelog]] | Registro de commits y features por fecha |
| [[Memoria]] | Feedback, decisiones y contexto del proyecto |

## Stack

| Capa | Tecnologia |
|------|-----------|
| Frontend | Nuxt 3 + Vue 3 + Tailwind CSS + Pinia |
| Backend | Laravel 11 + PHP 8.3 |
| Base de datos | MySQL 8 |
| Cache | Redis 7 |
| Auth | Laravel Sanctum (Bearer token) |
| PDF | barryvdh/laravel-dompdf + TCPDF + FPDI |
| IA | DeepSeek API |
| Proxy | Nginx |
| Infraestructura | Docker Compose |

## Acceso

- App: `http://localhost:8823`
- Admin: `admin@empresa.com` / `admin123`
