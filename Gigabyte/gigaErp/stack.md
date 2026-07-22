# Stack — gigaErp

## Backend

| Tecnología | Versión | Uso |
|-----------|---------|-----|
| PHP | 8.4 | Runtime (forzado por composer:2 en build stage) |
| Laravel | ^11.0 | Framework principal |
| Laravel Sanctum | ^4.0 | Autenticación Bearer token |
| barryvdh/laravel-dompdf | ^2.2 | Generación de PDF (stubs 501 por ahora) |
| predis/predis | ^2.2 | Cliente Redis |
| maatwebsite/excel | latest | Export Excel (stubs 501 por ahora) |
| league/flysystem-aws-s3-v3 | ^3.0 | Driver S3 del módulo [[modulos/contenido\|Contenido]] (bucket privado) |

## Almacenamiento de archivos

- **Disco local** (`storage/app/public`, volumen `uploads_storage`): adjuntos de marketing, imágenes del editor, importaciones. Es el default (`FILESYSTEM_DISK=public`).
- **S3** (discos `contenido` y `contenido_thumbs`): solo el módulo [[modulos/contenido|Contenido]]. Bucket privado en **sa-east-1** (São Paulo), archivos servidos con URLs firmadas; los thumbnails se generan on-demand (extensión **GD**) y se cachean en el prefijo `_thumbs`. Vars: `AWS_*`, `CONTENIDO_S3_BUCKET`, `CONTENIDO_S3_PREFIX`, `CONTENT_DOMAIN` (subdominio).
- **nginx**: config por template envsubst (`nginx/default.conf.template`) — subdominio de Contenido + cache de thumbnails.

## Frontend

| Tecnología | Versión | Uso |
|-----------|---------|-----|
| Nuxt | ^3.13 | Framework SPA (ssr: false) |
| Vue | 3 | UI framework |
| Pinia + @pinia/nuxt | ^0.7 | Estado global |
| Tailwind CSS | via @nuxtjs/tailwindcss | Estilos |
| nuxt-icon | ^0.6 | Íconos Lucide |
| @vueuse/nuxt | ^11 | Composables utilitarios |

## Infraestructura

| Servicio | Imagen | Puerto interno | Puerto host |
|---------|--------|----------------|-------------|
| gigaerp-db | mysql:8 | 3306 | 3310 |
| gigaerp-redis | redis:7-alpine | 6379 | — |
| gigaerp-backend | php:8.4-cli | 8000 | — |
| gigaerp-scheduler | php:8.4-cli | — | — |
| gigaerp-frontend | node:20 | 3000 | — |
| gigaerp-nginx | nginx:alpine | 80 | **8824** |

## Fuentes de tipografía

- **Inter** — cuerpo y UI
- **JetBrains Mono** — números, badges, tablas

## Comandos de deploy

```bash
# Primera vez
docker compose up -d --build

# Solo frontend (requiere rebuild)
docker compose build --no-cache frontend && docker compose up -d frontend && docker restart gigaerp-nginx

# Solo backend (sin rebuild)
docker cp backend/app/Http/Controllers/X.php gigaerp-backend:/var/www/html/app/Http/Controllers/
docker exec gigaerp-backend php artisan optimize:clear

# Migraciones
docker exec gigaerp-backend php artisan migrate --force

# Seeders
docker exec gigaerp-backend php artisan db:seed --force

# DB directa
docker exec -it gigaerp-db mysql -u gigaerp -p gigaerp
```

## Ver también

- [[gigaErp]] — índice del proyecto
- [[arquitectura]] — decisiones de diseño
