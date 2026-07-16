# Addons de marketing

Sección **Marketing → Addons**. Catálogo de lanzadores a apps/paneles externos. Introducido 2026-07-16 (commit `455663e`). Ver [[changelog#2026-07-16 — Addons de marketing (lanzadores externos url + token)|changelog]].

## Qué hace
- Botón **Agregar** abre un modal que pide: **nombre, URL, token, descripción**.
- Los addons quedan listados abajo como cards.
- Clic en una card → abre en pestaña nueva la **URL con el token concatenado literalmente** (`url + token`, sin separador) con `noopener,noreferrer`.
- Editar / eliminar al pasar el mouse por la card.

## Backend
- Tabla `addons_marketing`: `nombre`, `url` (text), `token` (text, nullable), `descripcion` (text, nullable), `usuario_id` (FK `usuarios`, nullOnDelete). Migración `0044`.
- Modelo `AddonMarketing` (relación `creador`).
- `AddonMarketingController`: `index` (orden por `created_at`), `store` (setea `usuario_id`), `update`, `destroy`.
- Rutas: `apiResource('addons')->only([index,store,update,destroy])` bajo `auth:sanctum`.

## Permiso
- `VER_SECCION_ADDONS` (opt-in). Admin ve todo. Bloqueo **solo frontend** — ver [[arquitectura#Permisos de visualización por sección|arquitectura]].

## Seguridad
- Token en **texto plano** en DB; viaja literal en la URL al abrir. Tenerlo en cuenta si los tokens son sensibles.

## Ver también
- [[arquitectura]] · [[changelog]] · [[gigaErp]]
