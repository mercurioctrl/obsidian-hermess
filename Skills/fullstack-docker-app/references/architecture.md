# Decisiones de Arquitectura

> Parte del skill [[SKILL|fullstack-docker-app]]. Ver también [[conventions]].

## Single Port Exposure

Solo Nginx escucha en el puerto del host. Backend (8000) y frontend (3000) son internos.
- Evita conflictos de puertos
- Simplifica CORS (mismo origen)
- En producción, solo un puerto que proteger

Ver configuración en [[nginx.conf]] y [[docker-compose.yml]].

## Nginx como Reverse Proxy

- `/api/*` → backend:8000 (Laravel)
- `/sanctum/*` → backend:8000 (CSRF cookie)
- `/storage/*` → backend:8000 (archivos subidos, PDFs)
- `/*` → frontend:3000 (Nuxt SSR)

Configuración completa en [[nginx.conf]].

## Scheduler como servicio separado

Misma imagen Docker que el backend, pero con `CMD ["php", "artisan", "schedule:work"]`.
- No requiere cron dentro del container
- Se reinicia con `restart: unless-stopped`
- Comparte volúmenes y env con backend

Definido en [[docker-compose.yml]].

## Entrypoint vs CMD

- **Entrypoint** ([[docker-entrypoint.sh]]): Se ejecuta en CADA arranque. Recrea dirs de storage, fix permisos, limpia cache.
- **CMD**: El comando real (`php artisan serve` o `node .output/server/index.mjs`).
- **Por qué**: `COPY . .` en el [[backend.Dockerfile]] sobreescribe dirs creados por `RUN mkdir`. Sin el entrypoint, Laravel falla con "Please provide a valid cache path".

## Multi-stage Frontend Build

- **Stage 1 (builder)**: Instala deps, compila Nuxt → `.output/`
- **Stage 2 (runtime)**: Solo copia `.output/`, imagen final mínima
- `NUXT_PUBLIC_API_BASE` se inyecta como build arg

Ver [[frontend.Dockerfile]].

## Secretos auto-generados

[[start.sh]] genera passwords y APP_KEY con `openssl rand` en el primer arranque.
- Nunca hay secretos hardcodeados
- Cada deploy tiene secretos únicos
- Se persisten en `.env` (en `.gitignore`)

Template en [[env.example]].

## Healthcheck en MySQL

```yaml
healthcheck:
  test: ["CMD", "mysqladmin", "ping", "-h", "localhost"]
  interval: 5s
  retries: 20
```

- Backend tiene `depends_on: db: condition: service_healthy` en [[docker-compose.yml]]
- [[start.sh]] hace poll adicional antes de migrar
- Migraciones con retry loop (3 intentos)

## Volúmenes nombrados

```yaml
volumes:
  mysql_data:       # Datos de MySQL
  redis_data:       # Cache de Redis
  pdf_storage:      # PDFs generados
  uploads_storage:  # Archivos subidos
```

Sobreviven a `docker compose down`. Definidos en [[docker-compose.yml]].

## Backup/Restore

- [[backup.sh]]: mysqldump + docker cp de PDFs y uploads + copia .env → tar.gz
- [[restore.sh]]: Interactivo, lista backups, pide password, restaura DB + archivos

## Deploy rápido (sin rebuild)

### Backend
```bash
docker cp backend/app/Http/Controllers/X.php container:/var/www/html/...
docker exec container php artisan optimize:clear
```

### Frontend
```bash
docker compose build --no-cache frontend && docker compose up -d frontend
docker restart container-nginx
```

Frontend SIEMPRE requiere rebuild. Ver [[conventions]] para más detalles.
