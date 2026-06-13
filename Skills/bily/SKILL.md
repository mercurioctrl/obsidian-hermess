---
name: sincronizarMenteBily
description: |
  Recorre todas las carpetas dentro de Bily/ de manera recursiva y asegura que
  cada carpeta tenga un archivo Inicio.md que liste y enlace su contenido.
  Si Inicio.md no existe en una carpeta, lo crea. Nunca borra contenido existente.
  Usar cuando Bily diga: /sincronizarMenteBily, "sincronizar mente", "actualizar
  inicio de Bily", "hay carpetas sin índice en Bily".
---

# Skill: sincronizarMenteBily

Recorre `Bily/` recursivamente. Cada carpeta debe tener un `Inicio.md` que liste
y enlace su contenido. Si no existe, lo crea. Si existe, agrega los items que
falten (aditivo). `Bily/Inicio.md` es la raíz que enlaza a todas las subcarpetas.

**Solo mapeo y estructura. No redacta ni modifica el contenido de las notas.**

---

## Raíz del vault

Detectar `VAULT_ROOT` buscando `Home.md` + `.obsidian/` subiendo desde `cwd`:

```bash
dir=$(pwd)
while [[ ! -f "$dir/Home.md" || ! -d "$dir/.obsidian" ]]; do
  dir=$(dirname "$dir")
done
VAULT_ROOT=$dir
BILY_DIR="$VAULT_ROOT/Bily"
```

---

## Proceso

### 1. Mapear toda la estructura de Bily/

Listar recursivamente todas las carpetas y archivos `.md` dentro de `Bily/`:

```bash
find "$BILY_DIR" -type d | sort
find "$BILY_DIR" -name "*.md" | sort
```

Para cada directorio encontrado, registrar:
- Path absoluto
- Path relativo desde `VAULT_ROOT` (ej: `Bily/personas`)
- Lista de archivos `.md` directamente en ese directorio (no en subdirectorios)
- Lista de subdirectorios directos

Excluir de procesamiento:
- Archivos: `Inicio.md`, `MEMORIA.md`, `bitacoras.md`
- Carpetas especiales: `.obsidian/`, `templates/`

### 2. Para cada carpeta en Bily/ (bottom-up, más profunda primero)

Procesar en orden inverso de profundidad para que los hijos estén listos antes
de procesar el padre.

#### 2a. Construir lista de contenido esperado

Para la carpeta en path relativo `Bily/X/`, el contenido esperado es:

**Archivos `.md`** directamente en la carpeta (excluyendo `Inicio.md`, `MEMORIA.md`, `bitacoras.md`):
- Cada uno genera una línea: `- [[Bily/X/nombre-sin-extension|Título legible]]`
- El título se extrae de la primera línea `# Título` del archivo; si no tiene, usar el nombre del archivo con guiones reemplazados por espacios

**Subcarpetas directas** de la carpeta:
- Cada subcarpeta genera: `- [[Bily/X/sub/Inicio|Sub — índice]]`
  - Excepción: si la subcarpeta es `bitacoras/`, usar `[[Bily/bitacoras/bitacoras|Bitácoras — índice de sesiones]]`
- El alias se extrae del `# Título` del `Inicio.md` de esa subcarpeta (si existe)

#### 2b. Leer Inicio.md existente (si existe)

Leer el archivo y extraer todos los wikilinks `[[...]]` ya presentes.

#### 2c. Detectar items faltantes

Comparar la lista esperada con los wikilinks existentes.
Un item está presente si su path base (sin alias) aparece en algún `[[...]]` del archivo.

#### 2d. Si faltan items → actualizar Inicio.md

**Si el archivo NO existe:** crearlo con este template:

```markdown
# {Título de la carpeta}

{Descripción breve si se puede inferir del contenido, sino omitir}

## Contenido

{lista de wikilinks}

## Ver también

- [[Bily/Bily|Inicio de Bily]]
```

El título se forma capitalizando el nombre de la carpeta (ej: `personas` → `Personas`).

**Si el archivo YA existe:** agregar solo los items faltantes al final de la sección
`## Contenido` (o `## Notas`, o la primera sección de lista que exista).
Si no hay ninguna sección de lista, agregar antes de `## Ver también` o al final.

**Nunca borrar ni reordenar** contenido existente.

### 3. Actualizar Bily/Inicio.md (raíz)

`Bily/Inicio.md` es el índice raíz de toda la mente de Bily.

Listar todas las subcarpetas directas de `Bily/` y sus `Inicio.md` (o `bitacoras.md`
en el caso de `bitacoras/`).

Verificar que estén presentes en `Bily/Inicio.md`. Agregar los que falten en la
sección apropiada (o al final si no hay sección definida).

Formato de cada entrada:
```markdown
- [[Bily/personas/personas|Personas]] — equipo y contactos
- [[Bily/bitacoras/bitacoras|Bitácoras]] — registro de sesiones
- [[Bily/Productos/Productos|Productos]] — ideas y productos en desarrollo
```

### 4. Reportar

```
sincronizarMenteBily — resultado
================================

Carpetas procesadas: N
  ✓ Bily/personas/       — Inicio.md creado (11 notas enlazadas)
  ✓ Bily/Productos/      — Inicio.md creado (4 notas enlazadas)
  ✓ Bily/kanban/         — Inicio.md creado (2 notas enlazadas)
  ✓ Bily/tareas/         — Inicio.md creado (1 nota enlazada)
  ✓ Bily/dreams/         — Inicio.md creado (1 nota enlazada)
  ~ Bily/bitacoras/      — ya tiene bitacoras.md (sin cambios)
  ~ Bily/                — Inicio.md actualizado (2 links nuevos)

Inicio.md raíz actualizado: Bily/Inicio.md
```

---

## Casos especiales

### bitacoras/
La carpeta `Bily/bitacoras/` usa `bitacoras.md` en lugar de `Inicio.md` como índice.
- No crear `Inicio.md` en esa carpeta
- En el padre (`Bily/Inicio.md`), enlazar con `[[Bily/bitacoras/bitacoras|Bitácoras]]`

### personas/Catriel/ y otros subdirectorios de personas/
Tratar igual que cualquier otra subcarpeta: crear `Inicio.md` si no existe,
listando los archivos `.md` de esa subcarpeta.

### Carpetas vacías
Si una carpeta no tiene archivos `.md` ni subcarpetas con contenido:
crear `Inicio.md` mínimo con título y `(vacío por ahora)`.

### MEMORIA.md
No incluir en ningún `Inicio.md` — es memoria interna de Claude, no navegación.

---

## Reglas

- **Solo mapeo** — no redactar ni modificar el contenido de las notas.
- **Aditivo** — nunca borrar ni reordenar entradas existentes.
- **Wikilinks siempre** — usar `[[path/nota|Alias]]`, nunca links markdown relativos.
- **Paths desde raíz del vault** — `[[Bily/personas/Catriel|Catriel]]`, no `[[../Catriel]]`.
- **Español rioplatense** — todo el texto generado en español.
- **Títulos desde el archivo** — extraer el `# Título` del `.md`; si no tiene, usar nombre del archivo.
