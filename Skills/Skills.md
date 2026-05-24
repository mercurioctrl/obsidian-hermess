# Skills de Claude Code

Skills reutilizables para Claude Code, almacenados en la bóveda para compartir entre equipos.

## Skills disponibles

### Generación de proyectos
- [[Skills/fullstack-docker-app/SKILL|fullstack-docker-app]] — Genera infraestructura Docker completa (Nuxt 3 + Laravel 11 + MySQL + Redis + Nginx)
- [[Skills/blu-report/SKILL|blu-report]] — Genera informes de seguimiento SEO para Libre Opción
- [[Skills/replicar-microsite/SKILL|replicarMicrosite]] — Replica microsites de producto (ASUS y otras marcas) para aplus-server

### Bily
- [[Skills/bily/bitacoras/SKILL|procesarBitacorasBily]] — Indexa las bitácoras nuevas de Bily en `bitacoras.md` y agrega back-links
- [[Skills/bily/SKILL|sincronizarMenteBily]] — Recorre `Bily/` recursivamente y asegura que cada carpeta tenga su `Inicio.md`

### Integración con Obsidian
- [[Skills/configurar-boveda/SKILL|configurarBoveda]] — Vincula un proyecto con una carpeta en la bóveda
- [[Skills/sincronizar-boveda/SKILL|sincronizarBoveda]] — Sincroniza documentación, arquitectura y changelog del proyecto con Obsidian
- [[Skills/tarea-boveda/SKILL|tareaBoveda]] — Crea notas de tareas (APP/API + Feat/Refactor/Fix) en la subcarpeta `tareas/` del proyecto
- [[Skills/nota-reforma/SKILL|notaReforma]] — Crea una nota liviana (estado/decisión/gastos/fotos) en proyectos no-software del vault y actualiza índices padres recursivamente
- [[Skills/reconstruir-indices/SKILL|reconstruirIndices]] — Recorre toda la bóveda recursivamente y reconstruye wikilinks en todos los índices; actualiza Home.md con resumen de cada carpeta

### Documentos y archivos
- [[Skills/docx/SKILL|docx]] — Crea, edita y analiza archivos DOCX
- [[Skills/pdf/SKILL|pdf]] — Procesamiento de PDFs (lectura, extracción, generación)
- [[Skills/pptx/SKILL|pptx]] — Crea y edita presentaciones PPTX
- [[Skills/xlsx/SKILL|xlsx]] — Crea y edita planillas Excel (XLSX)

### Agentes y automatización
- [[Skills/schedule/SKILL|schedule]] — Crea tareas programadas que se ejecutan bajo demanda o en intervalos automáticos
- [[Skills/skill-creator/SKILL|skillCreator]] — Crea nuevos skills reutilizables para Claude Code

## Cómo usar

1. Copiar la carpeta del skill a `~/.claude/skills/` en la máquina del desarrollador
2. Registrar en `~/.claude/CLAUDE.md` bajo `## Habilidades globales`
3. Invocar con `/nombreDelSkill` en Claude Code

## Flujo recomendado para proyectos

1. `/configurarBoveda` — Vincular proyecto con Obsidian (una vez)
2. `/tareaBoveda` — Crear nota de tarea antes de empezar a trabajar
3. Trabajar normalmente con Claude Code
4. `/sincronizarBoveda` — Actualizar notas al terminar la sesión
