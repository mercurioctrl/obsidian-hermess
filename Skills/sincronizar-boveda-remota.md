---
name: sincronizarBoveda
description: |
  Sincroniza el estado actual del proyecto con su carpeta en la bóveda de Obsidian REMOTA
  (via Cloudflare Tunnel + Access). Lee cambios recientes (git), documentación, arquitectura
  y memoria del proyecto, y actualiza/crea notas en Obsidian por el REST API.
  Usar cuando el usuario diga: /sincronizarBoveda, "actualizar Obsidian",
  "sincronizar bóveda", "guardar en Obsidian lo que hicimos", "actualizar notas",
  "sync boveda", o al terminar una sesión de trabajo.
---

# Skill: sincronizarBoveda (variante REMOTA)

Sincroniza el proyecto actual con su carpeta en Obsidian: documenta lo trabajado,
actualiza arquitectura/memoria y escribe las notas por el REST API remoto.

> Esta es la variante para correr en un server que **NO** tiene la bóveda en disco.
> La reconstrucción de índices (`/reconstruirIndices`) NO se hace acá: se corre en el
> **server principal** (10.10.10.7), que sí tiene los archivos. Ver paso 7.

## API de Obsidian (remota)

Se accede por el helper `boveda` (`~/bin/boveda`), que lee las credenciales de
`~/.config/boveda-remota/creds.env` y agrega los headers de Cloudflare Access + el Bearer.

```
Endpoint: https://cmer-boveda.blustudioinc.com  (via helper `boveda`)
Auth:     CF-Access-Client-Id + CF-Access-Client-Secret (Access) y Bearer (plugin)
Helper:   boveda <METODO> <ruta> [args curl...]
```

**Prueba de conectividad** (hacer al inicio, debe listar la raíz de la bóveda):

```bash
boveda GET /vault/
```

Si falla: verificar que `~/.config/boveda-remota/creds.env` existe y que Obsidian
está abierto en el server principal (el plugin no responde si Obsidian está cerrado).

## Prerequisito

El proyecto debe tener configurada su carpeta en Obsidian (via `/configurarBoveda`).
Buscar la sección `## Obsidian` en el CLAUDE.md del proyecto para obtener la carpeta.
Si no existe, preguntar al usuario y sugerir ejecutar `/configurarBoveda` primero.

## Proceso

### 1. Detectar carpeta de Obsidian

Leer el CLAUDE.md del proyecto y extraer la carpeta de Obsidian configurada.
Verificar que la carpeta existe en la bóveda:

```bash
boveda GET /vault/{CARPETA}/
```

### 2. Recopilar información del proyecto

Ejecutar en paralelo:

```bash
git log --oneline -10
git diff --name-only HEAD~3..HEAD 2>/dev/null || git diff --name-only
find . -type f -name "*.md" -o -name "*.json" -o -name "*.yml" | head -30
cat .claude/CLAUDE.md 2>/dev/null || cat CLAUDE.md 2>/dev/null
cat package.json 2>/dev/null | head -20
cat composer.json 2>/dev/null | head -20
cat README.md 2>/dev/null | head -50
```

### 3. Leer notas existentes en Obsidian

```bash
boveda GET /vault/{CARPETA}/
```

Leer las notas existentes (`boveda GET /vault/{CARPETA}/{nota}.md`) para saber qué
actualizar vs crear.

### 4. Generar/actualizar notas

Crear o actualizar las notas según corresponda. NO crear notas vacías ni con
información genérica — solo si hay contenido real y útil. (Idéntico a la versión local.)

- **4.1 `{NombreCarpeta}.md` (siempre)** — nota índice del proyecto. El nombre del
  archivo coincide con el de la carpeta (NO `index.md`). Contenido: nombre y
  descripción, stack, links `[[nota]]` a las demás notas, fecha de última sync.
- **4.2 `arquitectura.md`** — decisiones de arquitectura (estructura, patrones,
  servicios, DB/modelos, y el *por qué*). Solo si se infiere del código; actualizar sin borrar.
- **4.3 `changelog.md`** — registro por fecha (YYYY-MM-DD), conciso, **append** (no reemplazar).
- **4.4 `stack.md`** — framework/versión, DB, dependencias clave, servicios externos.
- **4.5 `contexto.md`** — reglas de negocio, decisiones del usuario, cosas que no
  funcionaron (y por qué), TODOs.
- **4.6 `memoria.md`** — consolidar la memoria de Claude del proyecto
  (`~/.claude/projects/{path}/memory/`) en una nota por tipo.
- **4.7 Notas de módulos** — `modulo-{nombre}.md` si el proyecto es grande.

### 5. Reconstruir wikilinks DENTRO de las notas del proyecto (SIEMPRE)

Igual que la versión local, pero leyendo/escribiendo por API:

1. Leer todas las notas de la carpeta del proyecto (`boveda GET /vault/{CARPETA}/...`).
2. Identificar menciones cruzadas y agregar `[[wikilinks]]` donde corresponda
   (en texto, en el índice, sección `## Ver también`, alias `[[nota|texto]]`).
3. El índice `{NombreCarpeta}.md` es el hub central conectado a todas las notas.

> Esto sólo toca las notas **del proyecto**. Los índices padres y `Home.md` los
> reconstruye el server principal (paso 7).

### 6. Subir notas a Obsidian (por API)

Para cada nota, PUT con el helper (contenido por stdin):

```bash
printf '%s' "$CONTENIDO" | boveda PUT "/vault/{CARPETA}/{nota}.md" \
  -H "Content-Type: text/markdown" --data-binary @-
```

Subir en paralelo cuando sea posible.

### 7. Reconstruir índices y Home.md → EN EL SERVER PRINCIPAL

**No se hace acá.** Las notas ya quedaron escritas en los archivos reales de la bóveda
(el REST API escribe en disco en el server principal), así que basta con correr, en el
**server principal 10.10.10.7**:

```
/reconstruirIndices {Carpeta}
```

Al terminar la sync, **recordarle al usuario** que corra `/reconstruirIndices {Carpeta}`
en el server principal (o `/reconstruirIndices` sin argumento para toda la bóveda) para
enlazar los índices padres y `Home.md`. Si no se hace, las notas están igual guardadas y
enlazadas entre sí; solo faltarían los links desde los índices superiores.

### 8. Confirmar

Mostrar al usuario:
- Cuántas notas se crearon/actualizaron y qué cambió en cada una.
- Recordatorio de correr `/reconstruirIndices {Carpeta}` en el server principal.
- Que puede ver el grafo en Obsidian.

## Modos de uso

- `/sincronizarBoveda` — completa (todas las notas).
- `/sincronizarBoveda changelog` — solo changelog.
- `/sincronizarBoveda arquitectura` — solo arquitectura.
- `/sincronizarBoveda links` — solo wikilinks internos del proyecto.

## Notas importantes

- **No borrar contenido previo** del changelog — siempre append.
- **No inventar** — solo documentar lo que existe en el código.
- **Ser conciso**, **fechas absolutas** (YYYY-MM-DD), **español**.
- **Obsidian debe estar abierto** en el server principal para que el API responda.
- Las credenciales viven en `~/.config/boveda-remota/creds.env` (nunca hardcodear ni subir a git).
