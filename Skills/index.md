# Skills de Claude Code

Skills reutilizables para Claude Code, almacenados en la bóveda para compartir entre equipos.

## Skills disponibles

### Generación de proyectos
- [[SKILL|fullstack-docker-app]] — Genera infraestructura Docker completa (Nuxt 3 + Laravel 11 + MySQL + Redis + Nginx)

### Integración con Obsidian
- [[Skills/configurar-boveda/SKILL|configurarBoveda]] — Vincula un proyecto con una carpeta en la bóveda
- [[Skills/sincronizar-boveda/SKILL|sincronizarBoveda]] — Sincroniza documentación, arquitectura y changelog del proyecto con Obsidian

## Cómo usar

1. Copiar la carpeta del skill a `~/.claude/skills/` en la máquina del desarrollador
2. Registrar en `~/.claude/CLAUDE.md` bajo `## Habilidades globales`
3. Invocar con `/nombreDelSkill` en Claude Code

## Flujo recomendado para proyectos

1. `/configurarBoveda` — Vincular proyecto con Obsidian (una vez)
2. Trabajar normalmente con Claude Code
3. `/sincronizarBoveda` — Actualizar notas al terminar la sesión
