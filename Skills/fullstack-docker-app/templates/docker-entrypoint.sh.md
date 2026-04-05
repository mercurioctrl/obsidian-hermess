# docker-entrypoint.sh

> Entrypoint resiliente del backend. Se ejecuta en cada arranque del container.
> Parte del skill [[SKILL|fullstack-docker-app]]. Ver [[architecture#Entrypoint vs CMD]].

## Qué hace

1. Recrea directorios de storage (necesario porque `COPY . .` en [[backend.Dockerfile]] los sobreescribe)
2. Asegura el symlink de storage público
3. Fija permisos (775)
4. Limpia cache stale
5. Ejecuta el CMD (`php artisan serve`)

## Template

```bash
#!/bin/sh
set -e

# Recreate storage directories (COPY . . in Dockerfile overwrites them)
mkdir -p storage/framework/{sessions,views,cache/data} \
         storage/app/public \
         storage/app/pdfs \
         storage/app/templates \
         storage/app/temp \
         storage/logs \
         bootstrap/cache

# Ensure symlink exists
ln -sf /var/www/html/storage/app/public /var/www/html/public/storage

# Fix permissions
chmod -R 775 storage bootstrap/cache

# Clear stale cache
php artisan optimize:clear 2>/dev/null || true

# Execute CMD
exec "$@"
```
