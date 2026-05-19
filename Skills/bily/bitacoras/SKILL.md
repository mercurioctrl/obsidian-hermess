---
name: procesarBitacorasBily
description: |
  Actualiza el índice de bitácoras de Bily (Bily/bitacoras/bitacoras.md) con todas
  las entradas nuevas que existan como archivos pero no estén aún en el índice.
  Agrega back-links en las bitácoras que no los tengan. NO genera contenido ni
  redacta bitácoras — solo reconstruye el mapeo/grafo entre los archivos existentes.
  Usar cuando Bily diga: /procesarBitacorasBily, "actualizar índice de bitácoras",
  "hay bitácoras sin indexar", "procesar bitácoras", al final de una sesión de trabajo
  donde se crearon nuevas bitácoras.
---

# Skill: procesarBitacorasBily

Recorre `Bily/bitacoras/` y subcarpetas, detecta archivos `YYYY-MM-DD*.md` que no
estén en el índice `bitacoras.md`, y los agrega en el lugar cronológico correcto.
También verifica que cada bitácora tenga su back-link al índice.

**Solo reconstruye el mapeo. No redacta ni modifica el contenido de las bitácoras.**

---

## Raíz del vault

Detectar `VAULT_ROOT` buscando `Home.md` + `.obsidian/` subiendo desde `cwd`:

```bash
dir=$(pwd)
while [[ ! -f "$dir/Home.md" || ! -d "$dir/.obsidian" ]]; do
  dir=$(dirname "$dir")
done
VAULT_ROOT=$dir
BITACORAS_DIR="$VAULT_ROOT/Bily/bitacoras"
INDEX="$BITACORAS_DIR/bitacoras.md"
```

---

## Proceso

### 1. Listar todas las bitácoras existentes

Buscar todos los `.md` en `$BITACORAS_DIR` y subcarpetas (`dailys/`, etc.) cuyo
nombre empiece con `YYYY-MM-DD` (4 dígitos, guion, 2, guion, 2):

```bash
find "$BITACORAS_DIR" -name "*.md" | grep -E '/[0-9]{4}-[0-9]{2}-[0-9]{2}' | sort
```

Excluir `bitacoras.md` y cualquier archivo que no sea una entrada de bitácora.

Para cada archivo encontrado, extraer:
- **fecha**: los primeros 10 caracteres del nombre (`YYYY-MM-DD`)
- **año**: primeros 4 dígitos
- **mes**: dígitos 6-7 (nombre completo en español: enero, febrero, ..., diciembre)
- **resumen**: leer el archivo y extraer un resumen de ~60 chars:
  - Primero intentar la primera línea de la primera sección (`## ...`) que tenga
    contenido de lista (`- **algo**`) — tomar el primer bullet sin markdown
  - Si no, tomar la primera línea no-vacía después del título `#`
  - Si no hay nada, usar `(sin resumen)`

### 2. Leer el índice actual

Leer `bitacoras.md` completo. Extraer todos los wikilinks del tipo
`[[Bily/bitacoras/YYYY-MM-DD` o `[[Bily/bitacoras/dailys/YYYY-MM-DD` para saber
cuáles ya están indexadas.

### 3. Detectar faltantes

Comparar la lista de archivos contra los links en el índice. Las bitácoras sin
link en el índice son las que hay que agregar.

Si no falta ninguna: informar y terminar.

### 4. Insertar en el índice (orden cronológico)

Para cada bitácora faltante, insertar en la sección correcta de `bitacoras.md`:

**Estructura del índice:**
```markdown
## YYYY

### Mes (en español)

- [[Bily/bitacoras/YYYY-MM-DD|YYYY-MM-DD]] — {resumen}
```

**Algoritmo de inserción:**

1. ¿Existe la sección `## YYYY`? Si no → crearla antes de `## Ver también`.
2. ¿Existe la subsección `### Mes`? Si no → crearla dentro de `## YYYY`.
3. Insertar la línea al final de esa subsección, ordenada por fecha.
4. Para bitácoras en subdirectorios (ej. `dailys/`), usar el path completo:
   `[[Bily/bitacoras/dailys/YYYY-MM-DD-daily|YYYY-MM-DD]]`

**Nunca borrar ni reordenar** las entradas existentes — solo insertar las nuevas.

La sección `## Ver también` siempre queda al final del archivo.

### 5. Verificar back-links

Para cada bitácora que se indexó (nueva O existente), abrir el archivo y verificar
si contiene `[[Bily/bitacoras/bitacoras` o `[[bitacoras` como wikilink.

Si no lo tiene: agregar al final del archivo (antes de `## Pendientes` si existe,
o al final si no):

```markdown

## Ver también

- [[Bily/bitacoras/bitacoras|Bitácoras]] — Índice de sesiones
```

Si ya tiene `## Ver también` pero sin el link: agregar el link dentro de esa sección.

### 6. Reportar

```
Bitácoras indexadas: N nuevas
  ✓ 2026-05-17 — "Decisiones producto Bot WhatsApp, arquitectura"
  ✓ 2026-05-18 — "Arquitectura NB, reglas de negocio, daily Blu"
  — 2026-05-16 — ya estaba

Back-links agregados: N
  ✓ 2026-05-17.md
  ✓ 2026-05-18.md

Índice actualizado: Bily/bitacoras/bitacoras.md
```

---

## Nombres de meses en español

| Número | Nombre     |
|--------|------------|
| 01     | Enero      |
| 02     | Febrero    |
| 03     | Marzo      |
| 04     | Abril      |
| 05     | Mayo       |
| 06     | Junio      |
| 07     | Julio      |
| 08     | Agosto     |
| 09     | Septiembre |
| 10     | Octubre    |
| 11     | Noviembre  |
| 12     | Diciembre  |

---

## Reglas

- **Solo mapeo** — no redactar, no resumir con IA, no modificar el contenido
  de las bitácoras salvo agregar el back-link.
- **Aditivo** — nunca borrar entradas del índice ni contenido de las bitácoras.
- **Resumen desde el archivo** — el texto después del `—` en el índice se extrae
  del contenido real, no se inventa.
- Si el archivo de bitácora está vacío o solo tiene título: usar `(en progreso)`.
