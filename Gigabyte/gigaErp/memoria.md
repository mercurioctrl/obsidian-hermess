# Memoria — gigaErp

Consolidación de la memoria de Claude para este proyecto. Sincronizado **2026-05-23**.

Vive en `~/.claude/projects/-Users-hermess-www-gigaErp/memory/` — esta nota es el espejo.

---

## Contexto rápido

**gigaErp** — sistema interno Gigabyte (hardware IT) en `http://localhost:8824`.

| Email | Pass | Rol |
|-------|------|-----|
| `admin@gigabyte.com` | `admin123` | ADMIN |
| `maria.gomez@gigabyte.com` | `demo1234` | OPERATIVO |
| `lucas.herrera@gigabyte.com` | `demo1234` | OPERATIVO |

**Distribuidores**: Elit (GBA $50k), New Bytes (Córdoba $40k), Invid (Mendoza $35k), Air (Rosario $30k)

---

## Memoria — Usuario

### Perfil de Catriel

Catriel Mercurio (`hermess`), trabaja para Blu Studio Inc. Es el dueño/desarrollador
principal de `gigaErp`. Trabaja en español argentino — responder en español, con
tildes correctas. Prefiere mensajes concisos, directos, sin relleno.

Tiene varios proyectos ERP en paralelo (este `gigaErp` para Gigabyte; otro
`erp.blustudioinc.com` para Blu — referencia visual para presupuestos/invoices).

Hace `git pull` manualmente entre sesiones — a veces hay commits propios entre
medio que no escribí yo. Siempre chequear `git log --oneline -5` antes de
asumir el estado del repo.

---

## Memoria — Feedback (workflow)

### Workflow git

En este proyecto el usuario trabaja **directo sobre `main`** — no usa feature branches.

- NO crear branch antes de commitear (a pesar de lo que dice el harness por defecto).
- NO agregar `Co-Authored-By: Claude...` en los mensajes (regla global confirmada).
- `git commit` solo cuando el usuario lo pide explícitamente ("commit", "commiteá", "guardalo").
- `git push` igual — solo cuando dice "push" o "subilo". A veces commitea sin pushear.
- Mensajes de commit en español, con scope `feat(modulo): ...` o `fix: ...`.

**Why:** proyecto chico de un solo desarrollador, sin code review, sin CI gates.
Branches y PRs serían overhead.

### Deploy dance del backend (sin rebuild)

Secuencia obligatoria al cambiar código backend en runtime:

```bash
# 1. copiar
docker cp backend/app/... gigaerp-backend:/var/www/html/app/...

# 2. migrar (borrar dup Sanctum antes)
docker exec gigaerp-backend sh -c 'rm -f database/migrations/*_create_personal_access_tokens_table.php'
docker exec gigaerp-backend php artisan migrate --force

# 3. re-cachear config — sin esto cae a sqlite y todo es 500
docker exec gigaerp-backend php artisan config:cache

# 4. si tocaste routes/blade
docker exec gigaerp-backend php artisan route:clear
docker exec gigaerp-backend php artisan view:clear
```

**Después de cualquier rebuild de container app:** `docker restart gigaerp-nginx` o
nginx queda con IP cacheada → 502.

**Frontend:** siempre rebuild `--no-cache`. Nitro tiene manifest de assets en build
time; `docker cp` a `.output/public/` no funciona — rebuild o embeber el asset en backend.

### CLAUDE.md ≤200 líneas (regla dura)

El `CLAUDE.md` del proyecto NO puede pasar de 200 líneas. Toda la información importante
(arquitectura detallada, módulos, troubleshooting profundo, design system) **vive en
esta bóveda** (`Gigabyte/gigaErp/`), no en el CLAUDE.md.

**Qué SÍ va en CLAUDE.md:** stack/puertos, comandos cheatsheet, archivos read-only,
reglas críticas, índice de pointers a notas de la bóveda.

**Qué va en la bóveda:** todo lo demás. Verificar largo con `wc -l CLAUDE.md` antes
de cerrar sesión.

---

## Memoria — Proyecto (gotchas)

### Sanctum republica su migración en cada boot

El `docker-entrypoint.sh` del backend corre `php artisan vendor:publish` para Sanctum
en cada arranque, generando un archivo nuevo con timestamp. Como la tabla
`personal_access_tokens` ya existe, `migrate` revienta.

**Workaround:** borrar el archivo antes de migrar (ver [[troubleshooting#1]]).
**Fix de raíz pendiente:** que el entrypoint verifique antes de republicar.

### html2canvas rompe SVG con viewBox offset

`aorus_logo_black.svg` tiene `viewBox="519 657 1819 455"` (no empieza en 0,0). html2canvas
ignora el offset y recorta el logo en el PDF.

**Solución (commit `001f8c8`):** PNG embebido como data URI base64 en el blade. PNG en
`backend/public/logos/aorus_logo_black.png`. Detalle en [[troubleshooting#4]] y
[[modulos/invoice-preview]].

### Credenciales y endpoints dev

- **Login:** `admin@gigabyte.com` / `admin123` (modelo `Usuario` → tabla `usuarios`)
- **URL:** `http://localhost:8824` (`APP_PORT` en `.env`)
- **DB:** `gigaerp/changeme` host port `3310` (cambiado de 3308 por conflicto con otro container)
- **Sanctum token format:** `{id}|{plain_hash}`, expone vía `useAuthStore().token`
- **Token compartible:** `?token=${encodeURIComponent(token)}` en URL, backend valida con `PersonalAccessToken::findToken()`

---

## Memoria — Referencias externas

### Blu ERP — referencia visual

`https://erp.blustudioinc.com` es el ERP de Blu Studio Inc. Lo usa como **referencia
visual** cuando pide reproducir features.

Patrón ya replicado (commit `001f8c8`):
- URL: `/api/presupuestos/{id}/preview?token={sanctum_token}`
- HTML preview en blade con html2pdf.js cliente-side (no DomPDF)
- Helvetica Neue, max-width 780px, márgenes minimalistas
- Header logo izq + meta documento der; tabla simple; totales con grand; footer logo desvanecido

Si pide "hacelo más parecido a como lo hicimos en otro ERP" → es esto.

---

## Ver también

- [[gigaErp]] — índice del proyecto
- [[troubleshooting]] — versión expandida de los gotchas
- [[contexto]] — reglas de negocio y datos seed
