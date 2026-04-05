---
name: configurarBoveda
description: |
  Configura la conexión entre un proyecto y su carpeta en la bóveda de Obsidian.
  Detecta el proyecto actual, lista las carpetas de Obsidian, permite elegir o crear
  una carpeta, y escribe las instrucciones en el CLAUDE.md del proyecto para que
  Claude sepa dónde buscar y guardar contexto del proyecto en Obsidian.
  Usar cuando el usuario diga: /configurarBoveda, "conectar proyecto con Obsidian",
  "configurar bóveda", "vincular proyecto a Obsidian".
---

# Skill: configurarBoveda

Vincula el proyecto actual con una carpeta en la bóveda de Obsidian, para que Claude
pueda leer y escribir contexto del proyecto ahí.

## API de Obsidian

```
Endpoint: https://localhost:27124/
Auth: Bearer ed858b7e41f810f0680adf6ffcd18a155b189b01c44100b5146a6927b9f5a6af
Flags: -sk (HTTPS con certificado autofirmado)
```

## Proceso

### 1. Detectar proyecto

- Obtener el directorio de trabajo actual (working directory)
- Inferir nombre del proyecto del directorio o del `package.json`, `composer.json`, o nombre de carpeta

### 2. Listar carpetas de Obsidian

```bash
curl -sk -H "Authorization: Bearer ed858b7e41f810f0680adf6ffcd18a155b189b01c44100b5146a6927b9f5a6af" \
  https://localhost:27124/vault/
```

Mostrar las carpetas disponibles al usuario y preguntar:
- **¿Cuál carpeta usar?** — puede ser una existente o una nueva
- Si el usuario no elige, sugerir crear una con el nombre del proyecto

### 3. Crear carpeta si no existe

Si la carpeta elegida no existe, crear una nota índice para que Obsidian la reconozca:

```bash
curl -sk -X PUT "https://localhost:27124/vault/{CARPETA}/index.md" \
  -H "Authorization: Bearer ..." \
  -H "Content-Type: text/markdown" \
  --data-binary "# {Nombre Proyecto}\n\nBase de conocimiento del proyecto."
```

### 4. Detectar CLAUDE.md del proyecto

Buscar en orden:
1. `{proyecto}/.claude/CLAUDE.md` — CLAUDE.md del proyecto (compartido con equipo via git)
2. `{proyecto}/CLAUDE.md` — CLAUDE.md en raíz del proyecto

Si no existe ninguno, preguntar al usuario cuál crear.
Preferir `.claude/CLAUDE.md` (estándar de Claude Code).

### 5. Escribir configuración en CLAUDE.md

Agregar (o actualizar si ya existe) una sección `## Obsidian` al CLAUDE.md del proyecto con este formato:

```markdown
## Obsidian — Base de conocimiento

Este proyecto tiene su base de conocimiento en la bóveda de Obsidian.

**Carpeta:** `{CARPETA_EN_BOVEDA}`
**API:** `https://localhost:27124/`

### Cómo usar

- **Leer nota:** `curl -sk -H "Authorization: Bearer {TOKEN}" https://localhost:27124/vault/{CARPETA}/{nota}.md`
- **Crear/actualizar nota:** `curl -sk -X PUT https://localhost:27124/vault/{CARPETA}/{nota}.md -H "Authorization: Bearer {TOKEN}" -H "Content-Type: text/markdown" --data-binary @-`
- **Buscar:** `curl -sk -H "Authorization: Bearer {TOKEN}" "https://localhost:27124/search/simple/?query={texto}"`
- **Listar archivos:** `curl -sk -H "Authorization: Bearer {TOKEN}" https://localhost:27124/vault/{CARPETA}/`

### Cuándo consultar Obsidian

- Al inicio de tareas complejas, buscar contexto relevante del proyecto
- Cuando el usuario mencione documentación, notas, o decisiones previas
- Para guardar decisiones de arquitectura o contexto que no pertenece al código
```

### 6. Actualizar Home.md (SIEMPRE)

Regenerar `Home.md` en la raíz de la bóveda para reflejar la nueva carpeta del proyecto.

```bash
# 1. Listar toda la bóveda
curl -sk -H "Authorization: Bearer {TOKEN}" https://localhost:27124/vault/

# 2. Listar cada subdirectorio recursivamente
#    Iterar sobre cada carpeta raíz y sus subcarpetas
```

Reconstruir `Home.md` con:
- Todas las carpetas y notas organizadas por sección
- `[[wikilinks]]` a cada nota y carpeta index
- Sección de Skills linkeando al índice de Skills
- No incluir archivos que no sean `.md`

Esto garantiza que la carpeta recién creada/vinculada aparezca en el índice general.

### 7. Confirmar

Mostrar al usuario:
- Qué carpeta de Obsidian se vinculó
- Qué archivo CLAUDE.md se actualizó
- Que Home.md fue actualizado con la nueva carpeta
- Cómo verificar (abrir Obsidian y ver la carpeta)

## Notas

- El token de Obsidian ya está en la memoria global del usuario, no hardcodearlo en CLAUDE.md de proyectos compartidos con equipo. En su lugar, usar un placeholder `{OBSIDIAN_TOKEN}` y agregar una nota de que cada dev debe configurar su propio token.
- Si el CLAUDE.md es compartido (`.claude/CLAUDE.md` en git), usar placeholder para el token
- Si el CLAUDE.md es privado (en `~/.claude/projects/`), se puede incluir el token directamente
- Siempre preguntar antes de modificar un CLAUDE.md existente

## Skill relacionado

Una vez configurada la bóveda, usar `/sincronizarBoveda` para mantener las notas
actualizadas con la documentación, arquitectura y changelog del proyecto.
Ver `~/.claude/skills/sincronizar-boveda/SKILL.md`.
