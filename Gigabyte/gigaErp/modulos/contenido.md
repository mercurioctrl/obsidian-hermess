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
- `GET /contenido/publico` → vista blade · `GET /contenido/publico/arbol` → JSON del árbol

## Vista pública — UI (commit `5926516`, 2026-07-22)

Estilo basado en la investigación de notebooks (Aldrich + Titillium Web + gradiente RGB).
- **Header de marca**: logo oficial **GIGABYTE** (SVG de Wikimedia) en **monocromo** (`fill=currentColor`), barra RGB superior, pill "Aorus", naranja AORUS `#FF6400`.
- **Orden por Nombre o Fecha de carga** (toggle asc/desc). El backend agrega `fecha` por archivo (S3 `lastModified` = fecha de subida) y la propaga a las carpetas (la más reciente de su contenido).
- **Metadatos por archivo**: resolución de imágenes (`ancho×alto`, leída del thumbnail con `onload`, sin request extra), formato de **fuentes** ("Fuente TTF/OTF/WOFF") y de otros archivos (extensión), más la fecha.

## Config y deploy

- Vars `.env`: `AWS_ACCESS_KEY_ID`, `AWS_SECRET_ACCESS_KEY`, `AWS_DEFAULT_REGION=sa-east-1`, `CONTENIDO_S3_BUCKET`, `CONTENIDO_S3_PREFIX=contenido` (cableadas en `docker-compose.yml`, backend+scheduler).
- Dependencia `league/flysystem-aws-s3-v3` — en `composer.json` y agregada al build del Dockerfile (`b832208`). En caliente se instaló con `composer.phar` (el container no traía composer, ver [[troubleshooting#10. Rebuild limpio del backend falla (composer create-project)|troubleshooting #10]]).
- **Bucket usado (decisión del usuario)**: `gigaerp-contenido-dev` (sa-east-1), **mismo bucket+prefijo para local y prod** (todo compartido, sin aislar). Versioning ON como red de seguridad. Ver [[contexto#Repositorio de Contenido — S3|contexto]].
- Deploy prod: copiar `config/filesystems.php` + `ContenidoController.php` + la vista blade al container, `config:cache` (config) y `view:clear` (vista). Migración one-time: `aws s3 sync ./contenido-repo s3://<bucket>/contenido/`.

## Ver también

- [[changelog]] · [[contexto]] · [[troubleshooting]] · [[stack]] · [[gigaErp]]
