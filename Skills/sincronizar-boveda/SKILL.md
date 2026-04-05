---
name: sincronizarBoveda
description: |
  Sincroniza el estado actual del proyecto con su carpeta en la bóveda de Obsidian.
  Lee cambios recientes (git), documentación, arquitectura y memoria del proyecto,
  y actualiza/crea notas en Obsidian. Al final, reconstruye los [[wikilinks]] entre
  todas las notas del proyecto para mantener el grafo conectado.
  Usar cuando el usuario diga: /sincronizarBoveda, "actualizar Obsidian",
  "sincronizar bóveda", "guardar en Obsidian lo que hicimos", "actualizar notas",
  "sync boveda", o al terminar una sesión de trabajo.
---

# Skill: sincronizarBoveda

Sincroniza el proyecto actual con su carpeta en Obsidian: documenta lo trabajado,
actualiza arquitectura/memoria, y reconstruye los grafos de conexiones.

## API de Obsidian

```
Endpoint: https://localhost:27124/
Auth: Bearer ed858b7e41f810f0680adf6ffcd18a155b189b01c44100b5146a6927b9f5a6af
Flags: -sk (HTTPS con certificado autofirmado)
```

## Prerequisito

El proyecto debe tener configurada su carpeta en Obsidian (via `/configurarBoveda`).
Buscar la sección `## Obsidian` en el CLAUDE.md del proyecto para obtener la carpeta.
Si no existe, preguntar al usuario y sugerir ejecutar `/configurarBoveda` primero.

## Proceso

### 1. Detectar carpeta de Obsidian

Leer el CLAUDE.md del proyecto y extraer la carpeta de Obsidian configurada.
Verificar que la carpeta existe en la bóveda:

```bash
curl -sk -H "Authorization: Bearer {TOKEN}" https://localhost:27124/vault/{CARPETA}/
```

### 2. Recopilar información del proyecto

Ejecutar en paralelo:

```bash
# Cambios recientes (últimos commits desde la última sincronización o últimos 10)
git log --oneline -10

# Cambios en la sesión actual (archivos modificados)
git diff --name-only HEAD~3..HEAD 2>/dev/null || git diff --name-only

# Estructura del proyecto
find . -type f -name "*.md" -o -name "*.json" -o -name "*.yml" | head -30

# CLAUDE.md del proyecto (memoria/contexto)
cat .claude/CLAUDE.md 2>/dev/null || cat CLAUDE.md 2>/dev/null

# Package/composer para detectar stack
cat package.json 2>/dev/null | head -20
cat composer.json 2>/dev/null | head -20

# README si existe
cat README.md 2>/dev/null | head -50
```

### 3. Leer notas existentes en Obsidian

```bash
curl -sk -H "Authorization: Bearer {TOKEN}" https://localhost:27124/vault/{CARPETA}/
```

Leer las notas existentes para saber qué actualizar vs crear.

### 4. Generar/actualizar notas

Crear o actualizar las siguientes notas según corresponda. NO crear notas vacías ni
con información genérica — solo crear si hay contenido real y útil.

#### 4.1 — `index.md` (siempre)

Nota índice del proyecto con:
- Nombre y descripción breve del proyecto
- Stack tecnológico
- Links a todas las demás notas del proyecto (`[[nota]]`)
- Fecha de última sincronización

#### 4.2 — `arquitectura.md` (si aplica)

Decisiones de arquitectura del proyecto:
- Estructura de carpetas relevante
- Patrones usados (API REST, SSR, SPA, etc.)
- Servicios y cómo se conectan
- Base de datos y modelos principales
- Decisiones de diseño y **por qué** se tomaron

Solo crear si se puede inferir arquitectura real del código. Actualizar con
decisiones nuevas sin borrar las anteriores.

#### 4.3 — `changelog.md` (si hay commits)

Registro de lo trabajado, agrupado por fecha:

```markdown
## 2026-04-04

- feat: Agregado módulo de facturación (controllers, modelos, vistas)
- fix: Corregido cálculo de IVA en totales
- refactor: Extraído servicio de PDF a clase dedicada

Archivos principales: `app/Services/PdfService.php`, `resources/views/facturas/`
```

Append al final (no reemplazar contenido anterior). Cada entrada debe ser
concisa y útil, no un copy-paste del git log.

#### 4.4 — `stack.md` (si aplica)

Tecnologías, versiones, dependencias clave:
- Framework y versión
- Base de datos
- Dependencias importantes y para qué se usan
- Servicios externos (APIs, storage, etc.)

#### 4.5 — `contexto.md` (si hay información relevante)

Información de contexto que no es código ni arquitectura:
- Reglas de negocio importantes
- Decisiones del usuario durante la sesión
- Cosas que se intentaron y no funcionaron (y por qué)
- TODOs o próximos pasos mencionados

#### 4.6 — `memoria.md` (si existe memoria del proyecto)

Sincronizar la memoria de Claude del proyecto (`~/.claude/projects/{path}/memory/`)
con una nota en Obsidian. Consolidar los archivos de memoria en una sola nota
organizada por tipo (usuario, feedback, proyecto, referencia).

#### 4.7 — Notas de módulos/features (si el proyecto es grande)

Para proyectos con múltiples módulos, crear una nota por módulo principal:
- `modulo-{nombre}.md` — Descripción, modelos, endpoints, vistas

Solo si el proyecto es lo suficientemente grande para justificarlo.

### 5. Reconstruir wikilinks (SIEMPRE)

Este paso es **obligatorio** en cada sincronización. Para cada nota del proyecto:

1. Leer todas las notas existentes en la carpeta del proyecto
2. Identificar conceptos, archivos y notas que se mencionan entre sí
3. Agregar `[[wikilinks]]` donde corresponda:
   - En texto que mencione otra nota → `[[nombre-nota]]`
   - En el index → links a todas las notas
   - Entre notas relacionadas → sección `## Ver también` al final
4. Usar links con alias cuando mejore legibilidad: `[[stack|tecnologías]]`

**Reglas de wikilinks:**
- El nombre del link debe coincidir con el nombre del archivo sin extensión
- Usar `[[nota#Sección]]` para links a secciones específicas
- No crear links circulares innecesarios (A→B→A está ok si ambos son relevantes)
- El index.md debe ser el hub central conectado a todas las notas

### 6. Subir notas a Obsidian

Para cada nota, usar PUT:

```bash
curl -sk -X PUT "https://localhost:27124/vault/{CARPETA}/{nota}.md" \
  -H "Authorization: Bearer {TOKEN}" \
  -H "Content-Type: text/markdown" \
  --data-binary @-
```

Subir en paralelo cuando sea posible (múltiples curl en paralelo).

### 7. Actualizar índices recursivamente (SIEMPRE)

La actualización de índices es **recursiva hacia arriba**: desde la carpeta del proyecto
hasta `Home.md`, pasando por cada carpeta padre que tenga un `index.md`.

**Ejemplo:** si el proyecto está en `NB/expedicion/`, se actualizan:
1. `NB/expedicion/index.md` — ya actualizado en paso 4.1
2. `NB/index.md` — debe listar `expedicion/` con sus notas
3. `Home.md` — debe listar `NB/` con sus subcarpetas

#### Algoritmo

```
carpeta_proyecto = "NB/expedicion"
segmentos = carpeta_proyecto.split("/")  # ["NB", "expedicion"]

# Subir desde el padre del proyecto hasta la raíz
for i in range(len(segmentos) - 1, 0, -1):
    carpeta_padre = "/".join(segmentos[:i])  # "NB"
    # 1. Listar contenido de carpeta_padre
    # 2. Para cada subcarpeta, listar sus notas
    # 3. Leer index.md actual de carpeta_padre (si existe)
    # 4. Regenerar index.md con wikilinks a todas las subcarpetas y notas

# Finalmente, actualizar Home.md (raíz de la bóveda)
```

#### Para cada `index.md` padre:

1. Listar subcarpetas y notas del directorio:
   ```bash
   curl -sk -H "Authorization: Bearer {TOKEN}" https://localhost:27124/vault/{CARPETA_PADRE}/
   ```
2. Para cada subcarpeta, listar su contenido (notas):
   ```bash
   curl -sk -H "Authorization: Bearer {TOKEN}" https://localhost:27124/vault/{CARPETA_PADRE}/{SUB}/
   ```
3. Regenerar el `index.md` con:
   - Título y descripción breve de la carpeta
   - Wikilinks a cada subcarpeta (via su `index.md`) y sus notas principales
   - No incluir archivos que no sean `.md`

#### Para `Home.md` (último paso):

```bash
# 1. Listar toda la bóveda
curl -sk -H "Authorization: Bearer {TOKEN}" https://localhost:27124/vault/

# 2. Listar cada subdirectorio recursivamente
```

Reconstruir `Home.md` con:
- Todas las carpetas y notas organizadas por sección
- `[[wikilinks]]` a cada nota y carpeta index
- Sección de Skills linkeando al índice de Skills
- No incluir archivos que no sean `.md`

**Formato de Home.md:**

```markdown
# Home

Índice general de la bóveda.

---

## {Carpeta raíz}

- [[{Carpeta}/index|{Título}]]

### {Subcarpeta}
{Descripción breve inferida del contenido}
- [[{path/nota}|{título legible}]]
  - [[{sub-nota}]]

---

## Skills de Claude Code
Ver [[Skills/index|índice de Skills]].
- [[Skills/{skill}/SKILL|{nombre}]] — {descripción corta}

---

## Otros
- [[nota-suelta]]
```

Esto garantiza que cualquier carpeta o nota nueva aparezca en toda la cadena de índices.

### 8. Confirmar

Mostrar al usuario:
- Cuántas notas se crearon/actualizaron
- Lista de notas con descripción breve de qué cambió
- Si Home.md fue actualizado (y qué carpetas nuevas se detectaron)
- Recordar que puede ver el grafo en Obsidian

## Modos de uso

### Sincronización completa (por defecto)
`/sincronizarBoveda` — Analiza todo el proyecto y actualiza todas las notas.

### Sincronización parcial (con argumento)
`/sincronizarBoveda changelog` — Solo actualiza el changelog con lo reciente.
`/sincronizarBoveda arquitectura` — Solo actualiza la nota de arquitectura.
`/sincronizarBoveda links` — Solo reconstruye wikilinks sin tocar contenido.

## Notas importantes

- **No borrar contenido previo** del changelog — siempre append
- **No inventar** — solo documentar lo que realmente existe en el código
- **Ser conciso** — las notas deben ser útiles, no exhaustivas
- **Fechas absolutas** — siempre usar formato YYYY-MM-DD
- **Español** — todas las notas en español
- Las notas deben ser útiles para retomar el proyecto después de días/semanas sin tocarlo
