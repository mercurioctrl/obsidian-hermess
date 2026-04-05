# backend.Dockerfile

> Imagen PHP 8.3 para Laravel 11. Parte del skill [[SKILL|fullstack-docker-app]].
> Ver [[architecture#Entrypoint vs CMD]] para la lógica de arranque.

## Componentes

- PHP 8.3-cli + extensiones (pdo_mysql, redis, gd, zip, etc.)
- Composer (multi-stage copy)
- [[docker-entrypoint.sh]] como entrypoint (recrea dirs en cada arranque)
- Variables de entorno definidas en [[backend-env.example]]

Usado por los servicios `backend` y `scheduler` en [[docker-compose.yml]].
Convenciones de código en [[conventions#Backend (Laravel)]].

## Template

```dockerfile
FROM php:8.3-cli

# Install system dependencies
RUN apt-get update && apt-get install -y \
    git curl libpng-dev libonig-dev libxml2-dev libzip-dev zip unzip \
    && docker-php-ext-install pdo_mysql mbstring exif pcntl bcmath gd zip \
    && pecl install redis && docker-php-ext-enable redis \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

# Install Composer
COPY --from=composer:latest /usr/bin/composer /usr/bin/composer

WORKDIR /var/www/html

# Install dependencies first (layer caching)
COPY composer.json composer.lock* ./
RUN composer install --no-dev --no-scripts --no-autoloader || \
    composer update --no-dev --no-scripts --no-autoloader

# Copy application
COPY . .

# Generate autoload
RUN composer dump-autoload --optimize

# Create storage structure + symlink
RUN mkdir -p storage/app/public storage/app/pdfs storage/app/templates \
    storage/app/temp storage/framework/sessions storage/framework/views \
    storage/framework/cache/data storage/logs bootstrap/cache \
    && ln -sf /var/www/html/storage/app/public /var/www/html/public/storage \
    && chmod -R 775 storage bootstrap/cache \
    && chown -R www-data:www-data storage bootstrap/cache

# Entrypoint (runs every start)
COPY docker-entrypoint.sh /usr/local/bin/
RUN chmod +x /usr/local/bin/docker-entrypoint.sh

EXPOSE 8000

ENTRYPOINT ["docker-entrypoint.sh"]
CMD ["php", "artisan", "serve", "--host=0.0.0.0", "--port=8000"]
```
