---
name: notaReforma
description: |
  Crea una nota liviana en un proyecto genérico de la bóveda de Obsidian (reformas,
  investigación, planillas, proyectos no-software). Plantilla simple con estado,
  decisión, gastos y fotos. Al crear la nota, recorre recursivamente los índices
  padre hasta Home.md para mantener los wikilinks coherentes y el graph conectado.
  Usar cuando el usuario diga: /notaReforma, "nueva nota de reforma", "agregar
  nota al proyecto", "crear nota en la bóveda" en contexto no-software.
---

# Skill: notaReforma

Crea una nota liviana en un proyecto genérico de la bóveda de Obsidian y mantiene
los índices padres sincronizados. Pensado para proyectos que **ya viven dentro del
vault** (reformas del hogar, planillas, investigación, etc.) — no usa HTTP, edita
archivos directo.

Contracara del par `configurarBoveda` / `tareaBoveda`, que asumen proyecto de
software externo al vault con capas APP/API.

## Cuándo usar

- Proyecto dentro del vault (`{vault}/Proyecto/Subproyecto/...`), sin código.
- No tiene capas APP/API. No tiene endpoints, SQL, DTOs.
- Querés una nota con **estado / decisión / gastos / fotos**, no con criterios de aceptación.

Si el proyecto es de software → usar `tareaBoveda` en su lugar.

## Proceso

### 1. Parsear argumentos

Invocación: `/notaReforma [título]`. Si no hay título, preguntarlo.

Opcionales que se pueden inferir del contexto o preguntar:
- **Tipo** (para el cuerpo, no el nombre): Presupuesto / Decisión / Compra / Investigación / Estado
- **Carpeta destino** — default: `cwd`. Si el cwd es la raíz del vault, preguntar.

### 2. Detectar la raíz del vault

Subir desde `cwd` hasta encontrar un directorio con `Home.md` **y** `.obsidian/`.
Ese es el vault root. Guardar esa ruta — se usa en el paso 6 como tope de la
recursión.

```bash
# Pseudocódigo
dir=$cwd
while [[ ! -f "$dir/Home.md" || ! -d "$dir/.obsidian" ]]; do
  dir=$(dirname "$dir")
  [[ "$dir" == "/" ]] && error "No se encontró la raíz del vault"
done
VAULT_ROOT=$dir
```

### 3. Elegir el nombre del archivo

Buscar en la carpeta destino el mayor prefijo numérico `NN-*.md` existente y usar
`NN+1`. Si no hay ninguno, arrancar en `01`.

```
slug = título en minúsculas, sin acentos, espacios → guiones
filename = {NN}-{slug}.md
```

Ejemplo: si en `Hogar/Lavadero/` ya hay `01-mesada-presupuestos.md`,
`02-bachas.md`, `03-durlock-presupuesto.md`, y el usuario pide "Pintura
impermeable", el archivo se llama `04-pintura-impermeable.md`.

### 4. Generar la nota con plantilla

```markdown
# {Título}

**Proyecto:** [[{Carpeta}/{NombreCarpeta}|{NombreCarpeta}]]
**Tipo:** {Presupuesto | Decisión | Compra | Investigación | Estado}
**Fecha:** {YYYY-MM-DD}
**Estado:** En curso

## Contexto

{Párrafo breve: qué se está evaluando/decidiendo/comprando y por qué ahora}

## Opciones / Detalle

{Tabla o lista con opciones, precios, pros y contras. Si es una sola compra, describirla}

| Opción | Detalle | Monto | Observación |
| ------ | ------- | ----- | ----------- |
| —      | —       | —     | —           |

## Decisión

_Pendiente._

{O: "Opción X — razón técnica / económica"}

## Gastos

| Fecha       | Concepto | Monto    |
| ----------- | -------- | -------- |
| —           | —        | —        |
| **Total**   |          | **—**    |

## Fotos

_(enlaces a imágenes en `attachments/` o referencias externas)_

## Ver también

- [[{NombreCarpeta}]]
```

**Reglas:**
- No inventar datos. Si no hay info, dejar placeholders con `—`.
- Si el usuario dio datos concretos (precios, opciones), volcarlos.
- Siempre linkear de vuelta al índice de la carpeta padre.

### 5. Actualizar el índice de la carpeta destino

El índice es `{CarpetaDestino}/{NombreCarpetaDestino}.md` (ej:
`Lavadero/Lavadero.md`). Buscar la sección `## Notas` — si no existe, crearla al
final. Agregar línea:

```markdown
- [[{NN}-{slug}|{Título}]]
```

Si el índice no existe, crearlo con un header mínimo:

```markdown
# {NombreCarpeta}

## Notas

- [[{NN}-{slug}|{Título}]]
```

### 6. Recursión hacia arriba: reconstruir índices padres

Desde la carpeta destino, subir carpeta por carpeta hasta `VAULT_ROOT`. En cada
nivel:

**a)** Determinar el índice del padre:
- Si existe `{Padre}/{NombrePadre}.md` → ese es el índice.
- Si el padre es `VAULT_ROOT` → el índice es `VAULT_ROOT/Home.md`.
- Si no hay índice intermedio → saltar ese nivel.

**b)** En ese índice, asegurar que exista un link a la subcarpeta inmediata por
la que venimos subiendo. Buscar la sección que represente esa subcarpeta (ej.
`### Lavadero` dentro de `## Hogar` en `Home.md`) o, si no existe, agregarla.

**c)** Dentro de esa sección, listar **todos** los `.md` de la subcarpeta
inmediata (no recursivo — cada subcarpeta se encarga de su propio nivel),
regenerando la lista de wikilinks. Esto garantiza que al agregar una nota nueva,
el índice padre la refleje sin que haya links huérfanos.

**d)** Si se cruzó con `Home.md` y la sección del proyecto top-level no existe,
crearla antes del separador final siguiendo el estilo de las secciones vecinas.

Parar cuando ya se procesó `Home.md`.

### 7. Verificación de integridad (opcional pero recomendado)

Antes de terminar, hacer una pasada de sanity check sobre el subárbol del
proyecto top-level (desde `VAULT_ROOT/{ProyectoTop}/` hacia abajo):

- Para cada carpeta con `.md`, si existe un índice `{NombreCarpeta}.md`,
  verificar que liste todos los `.md` de esa carpeta (salvo el propio índice).
- Reportar al usuario cualquier nota huérfana (archivo sin link desde su índice)
  pero **no** tocarla sin confirmación — puede ser intencional.

### 8. Confirmar al usuario

Mostrar:
- Ruta del archivo creado
- Índices actualizados (lista de paths)
- Notas huérfanas encontradas (si hay)
- Recordatorio de que puede abrir Obsidian y ver la nota y el graph

## Reglas

- **Español rioplatense** en todo el contenido.
- **No usar HTTP de Obsidian.** Edición directa con Read/Edit/Write.
- **No inventar datos de negocio** — montos, opciones y fotos los pone el usuario.
- **Wikilinks siempre con `|alias`** si el nombre del archivo es feo (ej:
  `[[03-durlock-presupuesto|Durlock — Presupuesto revestimiento paredes]]`).
- **No duplicar** — si ya existe un archivo con el mismo slug, preguntar si
  sobrescribir o elegir otro nombre.
- **Respetar el estilo vecino** — si las notas hermanas usan cierta estructura
  (ej. tabla de gastos con columna "Fecha"), mantenerla.
