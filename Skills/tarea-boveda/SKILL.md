---
name: tareaBoveda
description: |
  Crea una nota de tarea en la bóveda de Obsidian dentro de la carpeta del proyecto.
  Detecta el proyecto, pregunta tipo (APP/API) y categoría (Feat/Refactor/Fix/Review/Research),
  y genera la nota en la subcarpeta "tareas/" con el formato estándar.
  Usar cuando el usuario diga: /tareaBoveda, "crear tarea en Obsidian",
  "agregar tarea al proyecto", "nueva tarea", "tarea de Jira en Obsidian".
---

# Skill: tareaBoveda

Crea una nota de tarea dentro de la carpeta del proyecto en Obsidian, organizada
en la subcarpeta `tareas/`. Sigue una convención de nombres para distinguir
frontend (APP) de backend (API) y el tipo de trabajo.

## API de Obsidian

```
Endpoint: https://localhost:27124/
Auth: Bearer ed858b7e41f810f0680adf6ffcd18a155b189b01c44100b5146a6927b9f5a6af
Flags: -sk (HTTPS con certificado autofirmado)
```

## Convención de nombres

El nombre del archivo sigue el patrón: `{CAPA} - {TIPO} - {Título}.md`

| Capa | Cuándo usar |
|------|------------|
| `APP` | Trabajo en frontend (páginas, componentes, stores, UI) |
| `API` | Trabajo en backend (endpoints, modelos, servicios, migraciones) |

| Tipo | Cuándo usar |
|------|------------|
| `Feat` | Feature nueva, funcionalidad que no existía |
| `Refactor` | Mejora o reestructuración de código existente |
| `Fix` | Corrección de bug |
| `Review` | Revisión, ajuste o QA |
| `Research` | Investigación o spike técnico |

**Ejemplos:**
- `APP - Feat - Formulario de alta de clientes.md`
- `API - Refactor - Extraer servicio de facturación.md`
- `APP - Fix - Corregir overflow en tabla de pedidos.md`
- `API - Research - Evaluar migración a PostgreSQL.md`

## Proceso

### 1. Detectar proyecto en Obsidian

Buscar la sección `## Obsidian` en el CLAUDE.md del proyecto actual para obtener la carpeta.

```bash
# Buscar CLAUDE.md del proyecto
cat .claude/CLAUDE.md 2>/dev/null || cat CLAUDE.md 2>/dev/null
```

Extraer el valor de `**Carpeta:**` de la sección Obsidian.

Si no se encuentra la carpeta, preguntar al usuario:
- **¿En qué proyecto de Obsidian va esta tarea?**
- Listar las carpetas disponibles en la bóveda para que elija

Si el proyecto no tiene configuración de Obsidian, sugerir ejecutar `/configurarBoveda` primero.

### 2. Preguntar datos de la tarea

Preguntar al usuario (si no proporcionó la info en el comando):

1. **Capa:** ¿APP o API?
2. **Tipo:** ¿Feat, Refactor, Fix, Review o Research?
3. **Título:** nombre descriptivo y corto
4. **Issue de Jira (opcional):** clave del issue (ej: `LOCAPP-108`, `PROJ-42`)

Si el usuario proporcionó argumentos al invocar el skill, parsearlos.
Ejemplos de invocación con argumentos:
- `/tareaBoveda APP Feat Formulario de alta de clientes`
- `/tareaBoveda API Refactor Extraer servicio de facturación LOCAPP-108`

### 3. Si hay issue de Jira, obtener datos

Si el usuario proporcionó una clave de Jira, usar las herramientas MCP de Atlassian
para obtener los detalles del issue:

```
getJiraIssue(issueIdOrKey: "{ISSUE_KEY}")
```

Extraer:
- Resumen (summary)
- Descripción
- Estado
- Prioridad
- Asignado

Incorporar esta información en la nota.

### 4. Verificar/crear subcarpeta `tareas/`

```bash
# Verificar si existe la subcarpeta tareas
curl -sk -H "Authorization: Bearer {TOKEN}" \
  "https://localhost:27124/vault/{CARPETA}/tareas/"
```

Si no existe (404), se creará automáticamente al subir la primera nota.

### 5. Generar la nota

El nombre del archivo es: `{CAPA} - {TIPO} - {Título}.md`

**Plantilla de la nota:**

```markdown
# {CAPA} - {TIPO} - {Título}

**Proyecto:** [[{CARPETA}/{NombreCarpeta}|{NombreProyecto}]]
**Jira:** {ISSUE_KEY} (si aplica)
**Estado:** Pendiente
**Fecha:** {YYYY-MM-DD}

---

## Descripción

{Descripción del issue de Jira, o pedir al usuario que describa brevemente la tarea}

## Criterios de aceptación

- [ ] {Criterio 1}
- [ ] {Criterio 2}

## Notas técnicas

{Contexto técnico relevante: archivos involucrados, dependencias, consideraciones}

## Ver también

- [[{links a notas relacionadas del proyecto}]]
```

**Reglas de contenido:**
- Si hay datos de Jira, usarlos para llenar descripción y criterios
- Si no hay Jira, pedir al usuario una descripción breve o dejar placeholders claros
- Agregar wikilinks a notas existentes del proyecto que sean relevantes (arquitectura, módulos, etc.)
- Siempre incluir link al índice del proyecto

### 6. Subir la nota a Obsidian

```bash
curl -sk -X PUT \
  "https://localhost:27124/vault/{CARPETA}/tareas/{CAPA} - {TIPO} - {Título}.md" \
  -H "Authorization: Bearer {TOKEN}" \
  -H "Content-Type: text/markdown" \
  --data-binary @-
```

### 7. Actualizar índice del proyecto

Leer el índice del proyecto (`{CARPETA}/{NombreCarpeta}.md`) y agregar una sección
`## Tareas` si no existe, con link a la nueva tarea:

```markdown
## Tareas

- [[{CARPETA}/tareas/{CAPA} - {TIPO} - {Título}|{CAPA} - {TIPO} - {Título}]]
```

Si la sección ya existe, agregar la nueva tarea a la lista.

```bash
# Leer índice actual
curl -sk -H "Authorization: Bearer {TOKEN}" \
  "https://localhost:27124/vault/{CARPETA}/{NombreCarpeta}.md"

# Actualizar índice
curl -sk -X PUT \
  "https://localhost:27124/vault/{CARPETA}/{NombreCarpeta}.md" \
  -H "Authorization: Bearer {TOKEN}" \
  -H "Content-Type: text/markdown" \
  --data-binary @-
```

### 8. Confirmar

Mostrar al usuario:
- Nombre de la nota creada
- Carpeta donde se guardó
- Link al issue de Jira (si aplica)
- Recordar que puede ver la nota en Obsidian

## Notas importantes

- **No inventar contenido** — si no hay Jira ni descripción del usuario, dejar placeholders
- **Español** — todas las notas en español
- **Títulos cortos** — el título del archivo debe ser descriptivo pero conciso
- **Wikilinks** — siempre conectar la tarea al índice del proyecto y a notas relevantes
- **No duplicar** — antes de crear, verificar que no exista una tarea con el mismo nombre en la carpeta
