# Memoria Claude Code — inventario

Resumen de la memoria de Claude Code para este proyecto.
Última actualización: 2026-05-05.

## Entorno configurado

- **Backend**: uvicorn en puerto 8000, DB SQL Server en `190.210.23.97,4444`, base `NB_WEB`
- **Frontend**: Nuxt dev en puerto 3000, apuntando a `http://localhost:8000`
- **ODBC**: Solo Driver 18 instalado

## Variables de entorno críticas

El `.env` original del backend tenía nombres incorrectos. El código espera:
- `DB_DRIVER` (no `DB_TYPE`)
- `DB_SERVER` (no `DB_HOST`)
- `DB_PASS` (no `DB_PASSWORD`)
- `ALLOWED_ORIGINS` es crítico: el servidor crashea si no está definido

## Obsidian configurada

- **Carpeta**: `NB/inventario/`
- **Configurada**: 2026-05-05

## Ver también

- [[contexto]] — Detalles completos del entorno
- [[inventario]] — Índice del proyecto
