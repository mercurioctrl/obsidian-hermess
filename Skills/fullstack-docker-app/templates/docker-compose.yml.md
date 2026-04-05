# docker-compose.yml

> Orquestación de todos los servicios. Parte del skill [[SKILL|fullstack-docker-app]].
> Ver [[architecture]] para decisiones de diseño.

## Servicios

| Servicio | Imagen | Depende de |
|----------|--------|------------|
| `db` | MySQL 8 | — |
| `redis` | Redis 7 Alpine | — |
| `backend` | [[backend.Dockerfile]] | db (healthy), redis |
| `scheduler` | [[backend.Dockerfile]] | db (healthy), redis |
| `frontend` | [[frontend.Dockerfile]] | backend |
| `nginx` | Nginx Alpine + [[nginx.conf]] | frontend, backend |

## Variables

Cargadas desde [[env.example]] (raíz). Backend usa [[backend-env.example]].
Secretos generados por [[start.sh]].

## Base de datos

Init script: [[00-init.sql]]. Healthcheck integrado (ver [[architecture#Healthcheck en MySQL]]).

## Template

```yaml
services:
  db:
    image: mysql:8
    container_name: {{CONTAINER_PREFIX}}-db
    restart: unless-stopped
    environment:
      MYSQL_ROOT_PASSWORD: ${DB_ROOT_PASSWORD}
      MYSQL_DATABASE: ${DB_NAME}
      MYSQL_USER: ${DB_USER}
      MYSQL_PASSWORD: ${DB_PASSWORD}
    ports:
      - "${DB_PORT:-3306}:3306"
    volumes:
      - mysql_data:/var/lib/mysql
      - ./db/init:/docker-entrypoint-initdb.d
    healthcheck:
      test: ["CMD", "mysqladmin", "ping", "-h", "localhost", "-u", "root", "-p${DB_ROOT_PASSWORD}"]
      interval: 5s
      timeout: 5s
      retries: 20
    networks:
      - app-network

  redis:
    image: redis:7-alpine
    container_name: {{CONTAINER_PREFIX}}-redis
    restart: unless-stopped
    ports:
      - "${REDIS_PORT:-6379}:6379"
    volumes:
      - redis_data:/data
    networks:
      - app-network

  backend:
    build:
      context: ./backend
      dockerfile: Dockerfile
    container_name: {{CONTAINER_PREFIX}}-backend
    restart: unless-stopped
    depends_on:
      db:
        condition: service_healthy
      redis:
        condition: service_started
    environment:
      APP_NAME: "${APP_NAME:-{{NOMBRE_PROYECTO_UPPER}}}"
      APP_ENV: "${APP_ENV:-production}"
      APP_KEY: "${APP_KEY}"
      APP_DEBUG: "${APP_DEBUG:-false}"
      APP_URL: "http://localhost"
      DB_CONNECTION: mysql
      DB_HOST: db
      DB_PORT: 3306
      DB_DATABASE: "${DB_NAME}"
      DB_USERNAME: "${DB_USER}"
      DB_PASSWORD: "${DB_PASSWORD}"
      REDIS_HOST: "${REDIS_HOST:-redis}"
      REDIS_PORT: "${REDIS_PORT:-6379}"
      CACHE_STORE: redis
      SESSION_DRIVER: redis
      SANCTUM_STATEFUL_DOMAINS: "localhost"
    volumes:
      - uploads_storage:/var/www/html/storage/app/public
      - pdf_storage:/var/www/html/storage/app/pdfs
      - ../backups:/var/www/html/storage/app/backups
    networks:
      - app-network

  scheduler:
    build:
      context: ./backend
      dockerfile: Dockerfile
    container_name: {{CONTAINER_PREFIX}}-scheduler
    restart: unless-stopped
    depends_on:
      db:
        condition: service_healthy
      redis:
        condition: service_started
    environment:
      APP_NAME: "${APP_NAME:-{{NOMBRE_PROYECTO_UPPER}}}"
      APP_ENV: "${APP_ENV:-production}"
      APP_KEY: "${APP_KEY}"
      APP_DEBUG: "${APP_DEBUG:-false}"
      APP_URL: "http://localhost"
      DB_CONNECTION: mysql
      DB_HOST: db
      DB_PORT: 3306
      DB_DATABASE: "${DB_NAME}"
      DB_USERNAME: "${DB_USER}"
      DB_PASSWORD: "${DB_PASSWORD}"
      REDIS_HOST: "${REDIS_HOST:-redis}"
      REDIS_PORT: "${REDIS_PORT:-6379}"
      CACHE_STORE: redis
      SESSION_DRIVER: redis
    command: ["php", "artisan", "schedule:work"]
    networks:
      - app-network

  frontend:
    build:
      context: ./frontend
      dockerfile: Dockerfile
      args:
        NUXT_PUBLIC_API_BASE: "${API_BASE_URL:-http://localhost/api}"
    container_name: {{CONTAINER_PREFIX}}-frontend
    restart: unless-stopped
    depends_on:
      - backend
    networks:
      - app-network

  nginx:
    image: nginx:alpine
    container_name: {{CONTAINER_PREFIX}}-nginx
    restart: unless-stopped
    ports:
      - "${APP_PORT:-80}:80"
    volumes:
      - ./nginx/default.conf:/etc/nginx/conf.d/default.conf
    depends_on:
      - frontend
      - backend
    networks:
      - app-network

volumes:
  mysql_data:
  redis_data:
  pdf_storage:
  uploads_storage:

networks:
  app-network:
    driver: bridge
```
