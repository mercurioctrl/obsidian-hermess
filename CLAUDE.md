# Bóveda de Obsidian — hermess

Bóveda personal de Catriel Mercurio. Contiene documentación de proyectos de software,
reformas del hogar, recursos humanos, infraestructura, skills de Claude Code y la
memoria operativa de Bily.

## Habilidades globales

- `/reconstruirIndices` — Recorre toda la bóveda recursivamente y reconstruye wikilinks en todos los índices. Actualiza `Home.md` con resumen de cada carpeta raíz.
  - Skill: `~/.claude/skills/reconstruir-indices/SKILL.md`

- `/procesarBitacorasBily` — Indexa las bitácoras nuevas de Bily en `Bily/bitacoras/bitacoras.md` y agrega back-links en las bitácoras que no los tengan.
  - Skill: `~/.claude/skills/procesar-bitacoras-bily/SKILL.md`

- ~~`/sincronizarMenteBily`~~ — **DEPRECADO** (2026-06-13). `Bily/` ya usa la convención estándar `{Carpeta}.md`, así que `/reconstruirIndices Bily` lo cubre. Ver el stub en `~/.claude/skills/sincronizar-mente-bily/SKILL.md`.

- `/configurarBoveda` — Vincula un proyecto de código con una carpeta de la bóveda: escribe la sección `## Obsidian` en el `CLAUDE.md` del proyecto. Delega en `/reconstruirIndices` para reflejar la carpeta nueva en `Home.md`.
  - Skill: `~/.claude/skills/configurar-boveda/SKILL.md`

- `/sincronizarBoveda` — Vuelca el estado del proyecto (git, arquitectura, changelog, memoria) a sus notas en la bóveda y reconstruye los wikilinks **entre notas del proyecto**. Delega en `/reconstruirIndices` para índices y `Home.md`.
  - Skill: `~/.claude/skills/sincronizar-boveda/SKILL.md`

## Lógica de un proyecto en la bóveda

Tres skills con responsabilidades separadas. **La regla de oro: solo `/reconstruirIndices` toca índices (`{Carpeta}.md`) y `Home.md`** — siempre de forma aditiva, nunca regenera. Los demás skills, cuando necesitan actualizar un índice, **delegan en él**.

| Capa | Skill responsable |
|------|-------------------|
| Vínculo proyecto ↔ carpeta + `## Obsidian` en su `CLAUDE.md` | `/configurarBoveda` (una vez por proyecto) |
| Contenido de las notas (arquitectura, changelog, memoria…) + wikilinks **internos** del proyecto | `/sincronizarBoveda` (cada sesión de trabajo) |
| Índices de carpeta (`{Carpeta}.md`) y `Home.md` (grafo de carpetas) | `/reconstruirIndices` (única fuente de verdad, aditivo) |

**Flujo típico** (proyecto en `NB/expedicion/`):
1. `/configurarBoveda` → crea/elige carpeta `NB/expedicion`, escribe su `CLAUDE.md`, corre `/reconstruirIndices`.
2. Se trabaja y se hacen commits.
3. `/sincronizarBoveda` → actualiza `changelog.md`, `arquitectura.md`, etc., linkea las notas entre sí, y corre `/reconstruirIndices NB` → actualiza `expedicion.md` → `NB.md` → `Home.md` sin pisar contenido.

## Convenciones de la bóveda

- **Índice por carpeta:** cada carpeta tiene un `{NombreCarpeta}.md` que enlaza a sus notas hijas.
- **Home.md:** índice raíz con todas las carpetas de primer nivel y un resumen de cada una.
- **Wikilinks:** usar siempre `[[ruta/nota|Alias]]` para conectar notas. No usar rutas markdown relativas.
- **Idioma:** español rioplatense en todo el contenido generado.
- **No borrar:** cualquier modificación a índices es aditiva — nunca eliminar contenido existente.

## Estructura principal

- `Blu/` — BLU Digital Agency (proyectos, RRHH, ERP)
- `NB/` — New Bytes (microservicios: pedidos, expedición, inventario, etc.)
- `Libre Opcion/` — libreopcion.com.ar (SEO, features, tareas)
- `Bily/` — Asistente Bily: memoria, bitácoras, personas, productos
- `Hogar/` — Reformas del hogar (lavadero, oficina, servicios)
- `hermess-pc/` — PC personal: red UniFi, sistema, servicios
- `Skills/` — Skills de Claude Code reutilizables
- `Red/` — Infraestructura de red hogareña
- `Home.md` — Índice general de la bóveda
