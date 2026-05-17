---
name: reconstruirIndices
description: |
  Recorre toda la bóveda de Obsidian de manera recursiva y reconstruye los wikilinks
  en todos los archivos índice ({Carpeta}/{Carpeta}.md), asegurando que cada índice
  enlace a sus notas y subcarpetas hijas. Actualiza Home.md con todas las carpetas
  raíz y un resumen de cada una. NUNCA borra contenido existente — solo agrega links
  faltantes. Usar cuando el usuario diga: /reconstruirIndices, "reconstruir índices",
  "actualizar todos los homes", "rebuild vault graph", "enlazar toda la bóveda",
  "hay notas huérfanas", "el grafo está desconectado".
---

# Skill: reconstruirIndices

Recorre toda la bóveda recursivamente y reconstruye los `[[wikilinks]]` en cada
archivo índice, sin tocar el contenido existente. Al final actualiza `Home.md`
con todas las secciones raíz y un resumen de cada una.

## Reglas fundamentales

- **NUNCA borrar contenido** de un índice — solo agregar lo que falta.
- **No crear índices nuevos** — solo actualizar los que ya existen.
- **No tocar** archivos que no sean índices (`{dir}/{dirname}.md` o `Home.md`).
- **Español rioplatense** en todo texto generado.
- **Edición directa** con Read/Edit/Write — no usar HTTP de Obsidian.
- Un directorio es "indexado" si tiene un archivo `{dirname}.md` dentro de él.

---

## Proceso

### 1. Detectar la raíz del vault

Subir desde el directorio de trabajo hasta encontrar `Home.md` y `.obsidian/` en
el mismo directorio. Ese es `VAULT_ROOT`.

```bash
dir=$(pwd)
while [[ ! -f "$dir/Home.md" || ! -d "$dir/.obsidian" ]]; do
  parent=$(dirname "$dir")
  [[ "$parent" == "$dir" ]] && echo "ERROR: raíz no encontrada" && exit 1
  dir=$parent
done
echo "Vault root: $dir"
```

### 2. Mapear toda la bóveda

Obtener el árbol completo de archivos `.md` y directorios:

```bash
# Todos los .md (excluyendo .obsidian)
find "$VAULT_ROOT" -name "*.md" -not -path "*/.obsidian/*" | sort

# Todos los directorios (excluyendo .obsidian)
find "$VAULT_ROOT" -type d -not -path "*/.obsidian*" | sort
```

Para cada directorio, determinar si tiene un índice:
- `VAULT_ROOT` → índice: `Home.md`
- `VAULT_ROOT/{Carpeta}/` → índice: `{Carpeta}/{Carpeta}.md`
- `VAULT_ROOT/{Carpeta}/{Sub}/` → índice: `{Carpeta}/{Sub}/{Sub}.md`

Construir la lista de directorios indexados (los que tienen su `{dirname}.md`).

### 3. Procesar cada directorio indexado (bottom-up)

Ordenar los directorios de mayor profundidad a menor, para procesar hijos antes
que padres. Excluir `Home.md` de este paso — se trata en el paso 4.

Para cada directorio indexado `{dir}` con índice `{dir}/{dirname}.md`:

#### 3a. Listar hijos directos

- **Notas hijas:** todos los `.md` dentro de `{dir}` excepto el índice mismo.
  Incluir notas en subdirectorios solo si ese subdirectorio NO tiene su propio índice
  (si lo tiene, aparece como "subcarpeta indexada").
- **Subcarpetas indexadas:** subdirectorios dentro de `{dir}` que tienen su propio
  `{subdir}/{subdir}.md`.

#### 3b. Leer el índice actual

Leer el contenido actual del `{dirname}.md`.

#### 3c. Detectar qué falta

Extraer todos los `[[wikilinks]]` existentes del índice (ignorar alias: en
`[[nota|alias]]` el target es `nota`). Comparar contra:

- Notas hijas cuyo stem no aparezca como target en ningún wikilink existente.
- Subcarpetas indexadas cuyo stem no aparezca como target.

Si no falta nada: saltar este directorio (no modificar).

#### 3d. Agregar los links faltantes

Estrategia para insertar los links nuevos **sin destruir el contenido existente:**

1. Buscar si existe una sección `## Ver también` o `## Notas` al final del archivo.
   - Si existe `## Ver también` → insertar los links faltantes dentro de esa sección.
   - Si existe `## Notas` → insertar dentro de esa sección.
   - Si ninguna existe → agregar al final del archivo:
     ```markdown

     ## Ver también

     - [[link-faltante-1|Alias legible]]
     - [[link-faltante-2|Alias legible]]
     ```

2. Para subcarpetas indexadas, usar el formato:
   ```markdown
   - [[{Sub}/{Sub}|{Sub}]] — {primer párrafo del índice de Sub, truncado a ~60 chars}
   ```

3. Para notas sueltas:
   ```markdown
   - [[{nota}|{Título de la nota}]]
   ```
   El título se obtiene leyendo la primera línea `# Título` del archivo.

4. Agrupar los links nuevos: primero subcarpetas, luego notas sueltas.

### 4. Reconstruir Home.md

`Home.md` es el índice raíz y tiene una estructura de secciones por carpeta.
El objetivo es que **cada carpeta raíz tenga su sección** con:
- Un link al índice de la carpeta (`[[{Carpeta}/{Carpeta}|{Carpeta}]]`)
- Un resumen de una línea (inferido del primer párrafo del índice)
- Links a las notas y subcarpetas más importantes

#### 4a. Listar carpetas raíz

Todos los subdirectorios directos de `VAULT_ROOT` que tengan su índice
`{Carpeta}/{Carpeta}.md`. Excluir `.obsidian` y carpetas sin índice.

#### 4b. Para cada carpeta raíz:

1. **Verificar si ya tiene sección en Home.md.** Una sección existe si hay un
   `[[{Carpeta}/{Carpeta}` o `[[{Carpeta}` o un encabezado `## {Carpeta}` en el
   archivo. Si ya existe: ir a 4c.

2. **Si no existe:** extraer resumen del índice:
   - Leer `{Carpeta}/{Carpeta}.md`
   - Tomar el primer párrafo de texto (no encabezado, no lista, no frontmatter)
   - Truncar a ~80 caracteres si es largo

3. **Agregar sección nueva** al final de `Home.md`, antes de `---` final si existe,
   siguiendo el estilo de las secciones existentes:

   ```markdown
   ## {Carpeta}

   - [[{Carpeta}/{Carpeta}|{Título del índice}]] — {resumen}
     - {links a notas principales separados por ·}
   ```

#### 4c. Para carpetas ya presentes en Home.md:

Verificar que el link al índice esté presente. Si la sección existe pero no linkea
al índice `{Carpeta}/{Carpeta}.md`, agregar el link dentro de la sección.
No regenerar la sección completa — solo agregar lo que falta.

### 5. Generar reporte

Al terminar, mostrar al usuario un resumen claro:

```
Índices actualizados: N
  ✓ NB/NB.md           — +2 links (Compras, nota-catalogo-laset)
  ✓ Home.md            — +1 sección (Bily)
  — hermess-pc.md      — sin cambios

Notas sin índice padre (huérfanas potenciales):
  • Bily/bitacoras/2026-05-16.md  → no hay índice en Bily/bitacoras/

Total links agregados: N
```

Las "huérfanas potenciales" son notas en directorios que **no tienen índice propio**
y no están linkeadas desde ningún índice padre. Reportarlas pero NO tocarlas.

---

## Casos especiales

### Directorios con archivos que no son notas de Obsidian

Los skills (`Skills/pdf/FORMS.md`, `Skills/pptx/editing.md`, etc.) usan markdown
links relativos en lugar de wikilinks, por diseño. Para estos, el criterio es:

- Si el `SKILL.md` ya tiene una referencia al archivo (aunque sea via markdown link
  `[nombre](archivo.md)`), considerar ese archivo como "ya enlazado" y no agregar
  wikilink duplicado.

Para detectarlo: buscar en el índice el stem del archivo como substring, no solo
como `[[wikilink]]`. Si aparece de cualquier forma → ya está enlazado.

### Índices con frontmatter YAML

Si el archivo índice empieza con `---` frontmatter, preservarlo intacto.
Los links nuevos siempre van **después** del contenido existente.

### Carpetas de tareas (`tareas/`)

Las subcarpetas `tareas/` normalmente no tienen índice propio (el índice padre ya
las referencia). Si tienen un `tareas/tareas.md`, tratarlo como cualquier otro
índice. Si no tienen índice, reportar las notas como huérfanas potenciales pero no
crear el índice.

### Archivos con nombres especiales

- `CLAUDE.md` — ignorar, no es una nota de contenido.
- `MEMORY.md` — ignorar, es metadata de Claude.
- `SKILL.md` — no linkear desde índices padres (son archivos de Claude Code, no
  de Obsidian).
- Archivos en carpetas `agents/`, `references/`, `templates/` dentro de Skills —
  ignorar.

---

## Invocación con argumentos (opcional)

`/reconstruirIndices` — barrido completo de toda la bóveda.

`/reconstruirIndices {Carpeta}` — solo reconstruir índices dentro de esa carpeta
(y subir hasta Home.md para actualizar esa sección).

`/reconstruirIndices --dry-run` — mostrar qué cambiaría sin escribir nada.
Útil para revisar antes de aplicar.

---

## Notas importantes

- Este skill es **aditivo y conservador**: agrega, nunca elimina.
- Si un índice padre tiene una organización cuidadosa (secciones por categoría,
  notas con descripciones personalizadas), respetar esa estructura — solo agregar
  lo que falta al final de la sección correspondiente, no reorganizar.
- Los wikilinks nuevos usan el alias cuando el nombre del archivo es poco legible
  (ej: `[[01-mesada-presupuestos|Mesada — Presupuestos]]`). El alias es el `# Título`
  de la nota.
- No agregar links a archivos que no sean `.md`.
