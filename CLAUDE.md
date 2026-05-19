# Bóveda de Obsidian — hermess

Bóveda personal de Catriel Mercurio. Contiene documentación de proyectos de software,
reformas del hogar, recursos humanos, infraestructura, skills de Claude Code y la
memoria operativa de Bily.

## Habilidades globales

- `/reconstruirIndices` — Recorre toda la bóveda recursivamente y reconstruye wikilinks en todos los índices. Actualiza `Home.md` con resumen de cada carpeta raíz.
  - Skill: `~/.claude/skills/reconstruir-indices/SKILL.md`

- `/procesarBitacorasBily` — Indexa las bitácoras nuevas de Bily en `Bily/bitacoras/bitacoras.md` y agrega back-links en las bitácoras que no los tengan.
  - Skill: `~/.claude/skills/procesar-bitacoras-bily/SKILL.md`

- `/sincronizarMenteBily` — Recorre `Bily/` recursivamente y asegura que cada carpeta tenga un `Inicio.md` que liste su contenido. Crea los que falten. Nunca borra.
  - Skill: `~/.claude/skills/sincronizar-mente-bily/SKILL.md`

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
