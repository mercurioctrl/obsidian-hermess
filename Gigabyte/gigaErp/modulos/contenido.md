# Módulo Contenido — repositorio de material de marca (S3)

Repositorio de archivos de marca (imágenes, fuentes, PDFs, PSDs, videos) navegable por carpetas. Tiene una **vista pública sin login** (`/api/contenido/publico`, blade `resources/views/contenido/publico.blade.php`) y endpoints **admin** para gestionarlo. Es la única parte del ERP que vive en **S3** (el resto de adjuntos siguen en disco local). Controller: `ContenidoController`.

## Evolución

1. `daf5053` (2026) — repositorio de material con admin + vista pública sin login.
2. `d612b94` — **filesystem-backed**: fuente de verdad = árbol real bajo `storage/app/public/contenido`, bind-mount `./contenido-repo` al host; convivía con uploads por **SFTP/SSH**.
3. `186e948` (2026-07-20) — **migrado a S3 privado**. Motivo: +10 GB de material que no debía comer disco EBS de la EC2. Ver [[changelog#2026-07-20 — Repositorio de Contenido migrado a S3 + UI de marca|changelog]].

## Cómo funciona sobre S3

- Disco **`contenido`** en `config/filesystems.php` (nuevo archivo; antes usaba el default de Laravel): driver `s3`, `root` = prefijo `contenido` dentro del bucket, `visibility=private`, **`retain_visibility=false`** (clave, ver [[troubleshooting#11. Flysystem S3 rompe copy/move por GetObjectAcl|troubleshooting #11]]).
- **Bucket privado** (Block Public Access ON): los archivos se sirven con **URLs firmadas temporales** (`temporaryUrl`, TTL 60 min). Nunca quedan públicos en S3.
- **Fuente de verdad = listado del bucket** (`getDriver()->listContents(rel, true)`), así los uploads que caen "por fuera" (`aws s3 cp`, consola AWS) **aparecen solos en el árbol** — reemplaza la coexistencia SFTP de antes.
- S3 no tiene carpetas reales: **carpeta vacía = objeto placeholder `.keep`**; **rename = copiar+borrar** cada objeto bajo el prefijo (no atómico); delete = `deleteDirectory` por prefijo.
- **Misma API/shape que antes** → el frontend no cambió al migrar (solo se suma `fecha` al árbol después).

## Endpoints

Admin (auth:sanctum, en `routes/api.php`):
- `GET /contenido/arbol` · `POST/PUT/DELETE /contenido/carpetas` · `POST/DELETE /contenido/archivos`

Público (sin login):
- `GET /contenido/publico` + comodín `/contenido/publico/{ruta?}` → vista blade (deep-links a carpetas)
- `GET /contenido/publico/arbol` → JSON del árbol (cada archivo trae `url`, `descarga`, `thumb`, `mime`, `tamano`, `fecha`)
- `GET /contenido/thumb?path=...` → thumbnail on-demand cacheado en S3 (+ header `X-Res`)

## Vista pública — UI

Estilo basado en la investigación de notebooks (Aldrich + Titillium Web + gradiente RGB). Servida en la raíz de un **subdominio propio** (`CONTENT_DOMAIN`, ej. `content.gigabyte.com`) o en `/api/contenido/publico` en localhost.

- **Header de marca** (`5926516`): logo oficial **GIGABYTE** (SVG de Wikimedia) en **monocromo** (`fill=currentColor`), barra RGB superior, pill "Aorus", naranja AORUS `#FF6400`.
- **Orden por Nombre o Fecha de carga** (toggle asc/desc). El backend agrega `fecha` por archivo (S3 `lastModified`) y la propaga a las carpetas.
- **Deep-linking** (`1388ba5`): History API — entrar/salir de carpetas cambia la URL (`/Carpeta/Sub`), back/forward funciona, un deep-link abre directo esa carpeta. Detecta el base path (subdominio `''` vs localhost).
- **Descargar directo** (`4ad6b8b`): URL firmada con `Content-Disposition=attachment` (el `download` del navegador se ignora por cross-origin a S3). Ícono **↗** para abrir en pestaña nueva.
- **Filtro por resolución** (`4ad6b8b`): desplegable con las resoluciones presentes en la carpeta; 100% cliente, se resetea al cambiar de carpeta.
- **Thumbnails on-demand** (`da0332e`): las previews son thumbnails (GD, máx 480px) generados la 1ª vez y **cacheados en S3** (`~1.7 MB → ~60 KB`). Se cargan lazy (IntersectionObserver) vía `fetch`; la **resolución original** viene del header `X-Res` (ASCII `x`, formateado a `×` en el cliente — ver [[troubleshooting#13. Carácter no-ASCII en header HTTP se ve mal (Ã)|troubleshooting #13]]).

## Config y deploy

- Vars `.env`: `AWS_ACCESS_KEY_ID`, `AWS_SECRET_ACCESS_KEY`, `AWS_DEFAULT_REGION=sa-east-1`, `CONTENIDO_S3_BUCKET`, `CONTENIDO_S3_PREFIX=contenido`, `CONTENT_DOMAIN` (subdominio), opcional `CONTENIDO_S3_THUMBS_PREFIX=_thumbs`. Cableadas en `docker-compose.yml` (backend, scheduler, nginx).
- Discos S3 (`config/filesystems.php`): `contenido` (prefijo `contenido`) y `contenido_thumbs` (prefijo `_thumbs`, mismo bucket). Requiere extensión **GD** para thumbnails (ya presente).
- nginx: config por **template envsubst** (`nginx/default.conf.template`, reemplaza `default.conf`); server block del subdominio + `location = /api/contenido/thumb` cacheable. ⚠️ Editar el template no se refleja en caliente por el bind-mount de un solo archivo — ver [[troubleshooting#14. Editar un archivo bind-mounteado (un solo archivo) no se refleja en el container|troubleshooting #14]].
- Dependencia `league/flysystem-aws-s3-v3` — en `composer.json` y en el build del Dockerfile (`b832208`). En caliente se instala con `composer.phar` (ver [[troubleshooting#10. Rebuild limpio del backend falla (composer create-project)|troubleshooting #10]]).
- **Bucket usado (decisión del usuario)**: `gigaerp-contenido-dev` (sa-east-1), **mismo bucket+prefijo para local y prod** (todo compartido, sin aislar). Versioning ON como red de seguridad. Ver [[contexto#Repositorio de Contenido — S3|contexto]].
- **Deploy prod** (deploy en caliente): `docker compose up -d nginx` (toma el template) recrea también el backend → rehacer el hot-deploy (reinstalar flysystem + copiar `config/filesystems.php`, `routes/api.php`, `ContenidoController.php`, la blade + `config:cache`/`route:clear`/`view:clear`). Runbook completo en el mensaje de los commits `1388ba5` y `da0332e`. Migración de archivos one-time: `aws s3 sync ./contenido-repo s3://<bucket>/contenido/`.

## Suscripción por email y avisos (`4af7a34`, `a54da03`)

Portal público con **footer de suscripción** (email, alta idempotente) para que los clientes reciban aviso cuando se sube material nuevo.

- Tabla **`contenido_suscriptores`** (mig `0048`) + modelo `ContenidoSuscriptor`.
- `POST /contenido/publico/suscribir` (throttle **10/min**) y `GET /contenido/publico/desuscribir?token` (baja con página de confirmación, blade `baja.blade.php`). Ambas **antes del comodín** `/{ruta?}` para que no las trague.
- **`POST /contenido/notificar`** (auth): el ERP dispara **un** mail-resumen a los suscriptores activos al terminar de subir un lote (no un mail por archivo), tolerante a fallos (no rompe la subida si el mail falla).
- Mailable `ContenidoNuevoMail` + plantilla HTML branded (barra RGB + link a la carpeta), blade `mail_nuevo.blade.php`. Vars `MAIL_*` en `docker-compose` (default `log` hasta cargar SMTP en el `.env`).
- **Vista de suscriptores en el ERP** (`a54da03`): `GET /contenido/suscriptores` (total/activos/items) y `DELETE /contenido/suscriptores/{id}`. Botón "Suscriptores" en el header con contador, modal con lista, eliminar por fila y **exportar CSV**.

## Deep-linking en el ERP y paridad de vistas (`4af7a34`, `2e64e44`)

- La página del ERP pasó a **ruta catch-all** (`frontend/pages/contenido/[...ruta].vue`, renombrada de `index.vue`): navegar carpetas cambia la URL (`/contenido/A/B`), es recargable y anda back/forward. La **URL es la fuente de verdad** (watch sobre `route.params` + reconstrucción de la pila de navegación).
- **"Copiar link" / "Ver público"** arman la URL pública de la carpeta actual, usando `CONTENT_DOMAIN` (vía `GET /contenido/config`, auth) o el mismo origen en local.
- **Paridad admin ↔ pública** (`2e64e44`): la vista ERP ya tiene thumbnails on-demand, resolución/formato + fecha, orden Nombre/Fecha, filtro por resolución, abrir en pestaña (↗), descargar directo y **"Descargar todo"** (secuencial, respeta el filtro, con progreso — también en la blade pública).
- Fix **"imagen rota"**: formatos no previsualizables (tif/psd/etc.) muestran ícono + badge de formato; preview solo si hay thumbnail (png/jpg/gif) o tipo nativo del navegador, con `onerror` de respaldo.

## Endpoints (actualizado)

Admin (`auth:sanctum`): `GET /contenido/arbol` · `GET /contenido/config` · `POST/PUT/DELETE /contenido/carpetas` · `POST/DELETE /contenido/archivos` · `GET /contenido/suscriptores` · `DELETE /contenido/suscriptores/{id}` · `POST /contenido/notificar`.

Público (sin login): `GET /contenido/publico` + comodín `/contenido/publico/{ruta?}` (deep-links) · `GET /contenido/publico/arbol` · `GET /contenido/thumb?path=` · `POST /contenido/publico/suscribir` · `GET /contenido/publico/desuscribir?token`.


## Ver también

- [[changelog]] · [[contexto]] · [[troubleshooting]] · [[stack]] · [[gigaErp]]
