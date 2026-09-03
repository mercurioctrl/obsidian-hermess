# Módulo Novedades

Cada **Cliente** tiene su propio **blog público de novedades**, accesible por un **enlace secreto
rotable** (capability URL, mismo modelo que [[Modulo Reservas Reuniones]] / Calendly). **Sin login:**
quien tiene el link entra. **Multi-tenant con aislamiento total** — un cliente no puede ver a otro
tocando la URL, porque el cliente se resuelve **desde el token** y todo se scopea por `cliente_id`
(nunca un id entra por la URL).

El contenido se **alimenta solo de la data que ya existe en el ERP** (no se carga a mano):
`Cliente → Proyecto (cliente_id) → PruebaEjecucion (activación = período) → HitoEjecucion (avances)`
+ `ProyectoAdjunto` de imagen como **evidencias**.

En desarrollo 2026-09-03 (rama `feat/novedades-cliente`, migración 0110). Es módulo de **seguimiento**:
NO genera gasto ni movimiento de banco/caja (igual que [[Modulo Flota GSM]]). Ver también
[[Backend - API]], [[Base de Datos]] y [[Modulo Personal|activaciones]].

## Modelo de datos (migración 0110)

`clientes` sumó dos columnas (**sin tablas nuevas**):
- `novedades_token` — string(64), **nullable, unique**. Capability URL, `Str::random(48)`, lazy.
- `novedades_publicado` — boolean, default `true`. Despublica todo el blog sin rotar el token.

**Decisión de producto:** se publican **todos los hitos** de las activaciones del cliente. Las
activaciones ya son trabajo curado que se reporta al cliente, y `hito.estado` es texto libre sin
catálogo → no se filtra por estado. `hito.categoria_servicio` (también texto libre) agrupa como
chip "por aplicación/servicio".

## Backend

- **`Cliente`:** `proyectos()` hasMany (nuevo) + `asegurarNovedadesToken()` (idempotente, patrón de
  `ProyectoAdjunto::asegurarPublicToken()`) / `regenerarNovedadesToken()` / `novedadesLink($base)`.
- **`NovedadesPublicController@show($token)`** — **PÚBLICO, sin auth** (`throttle:60,1`):
  - `abort_if(!$cliente, 404)` resolviendo por `novedades_token` + `novedades_publicado`.
  - Activaciones (`PruebaEjecucion`) de los proyectos del cliente, `orderByDesc('periodo_hasta')`,
    `with(['hitos','proyecto.adjuntos'])`.
  - **Evidencias** = adjuntos `tipo=ARCHIVO` con mime `image/*`, servidos por
    `/api/archivos/publico/{public_token}` (genera el token on-demand, misma ruta que compartir por
    [[Modulo WhatsApp Inbox|WhatsApp]]).
  - `periodoLabel` = `ucfirst(periodo_hasta->locale('es')->isoFormat('MMMM YYYY'))` → "Agosto 2026".
  - Headers `X-Robots-Tag: noindex, nofollow` + `Referrer-Policy: no-referrer`.
- **`ClienteController`:** `show()` asegura el token; `novedadesRegenerarToken` +
  `novedadesPublicado` (body `publicado:bool`) devuelven `{novedades:{token,publicado,link}}`.
  `ClienteResource` expone `novedades`. Base del link = `config('app.novedades_url')`
  (env `NOVEDADES_URL`, **subdominio dedicado** de prod) con fallback al host del request.

### Rutas
```
GET  /api/novedades/{token}                            (PÚBLICO, throttle:60,1 — junto a /reservas/{token})
POST /api/clientes/{cliente}/novedades/regenerar-token (rota token, devuelve link)
PUT  /api/clientes/{cliente}/novedades/publicado       (body: publicado:bool)
```

## Frontend

- **`pages/n/[token].vue`** — página pública, `layout:'auth'`, `<meta robots noindex,nofollow>`,
  `/n` agregado a `RUTAS_PUBLICAS` del `middleware/auth.global.ts`. Estética Blu: header eyebrow
  "Novedades" + nombre del cliente, **chips de apps** con contador que filtran client-side por
  `app_slug`, entradas por período (card) con avances (título=`descripcion`, sub=`actividad_especifica`,
  badge app, fecha) y **grid de evidencias** (imágenes con borde fino). Footer "Hecho con cariño…".
- **`pages/clientes/[id].vue`** — card **"Novedades"** en el aside (debajo de Mercury): badge
  Publicado/Despublicado, link secreto con **Copiar**/**Abrir** (↗), **Regenerar enlace** (confirm)
  y toggle **Publicar/Despublicar** (patrón Mercury, `novedadesBusy`).

## Seguridad / aislamiento

- Token largo aleatorio (48 chars), unique, no incremental. Nunca un id en la URL.
- Toda query scoped por `cliente_id` resuelto **desde el token**.
- `X-Robots-Tag: noindex` + `Referrer-Policy: no-referrer` (backend) + `<meta robots>` (front) + throttle.
- Regenerar el token invalida el link anterior al instante; despublicar → 404 sin rotar token.

## Limitaciones / futuro

- **Subdominio de prod** (`novedades.blustudioinc.com`) es ops: `NOVEDADES_URL` en `mini-saas/.env`
  + DNS + nginx que proxee `/api` en ese host. Sin eso, el link usa el host actual (dev `localhost:8823`).
- `categoria_servicio` es texto libre → "Marketing" y "Marketing Digital" cuentan como apps distintas.
- Evidencias a nivel **proyecto** (no por hito): todos los períodos de un proyecto comparten sus imágenes.
- Sin analítica de visitas ni expiración temporal del token (sólo rotación manual).

## Ver también

- [[Modulo Reservas Reuniones]] — mismo patrón de capability URL público (link tipo Calendly)
- [[Modulo Flota GSM]] — otro módulo de seguimiento que no toca finanzas
- [[Modulo WhatsApp Inbox]] — la ruta pública de adjuntos por token que reutilizan las evidencias
- [[Frontend]] · [[Backend - API]] · [[Base de Datos]]
- [[changelog#2026-09-03]]
