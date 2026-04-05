# backend-env.example

> Variables de entorno de Laravel. Generado automáticamente por [[start.sh]] a partir de [[env.example]].
> Parte del skill [[SKILL|fullstack-docker-app]].

Nota: `DB_HOST=db` y `REDIS_HOST=redis` son DNS internos de Docker — ver [[conventions#DB_HOST es el nombre del servicio]].
Usado por [[backend.Dockerfile]] y [[docker-compose.yml]].

## Template

```env
APP_NAME={{NOMBRE_PROYECTO_UPPER}}
APP_ENV=local
APP_KEY=
APP_DEBUG=true
APP_URL=http://localhost

DB_CONNECTION=mysql
DB_HOST=db
DB_PORT=3306
DB_DATABASE={{DB_NAME}}
DB_USERNAME={{DB_NAME}}
DB_PASSWORD=

REDIS_HOST=redis
REDIS_PORT=6379
CACHE_STORE=redis
SESSION_DRIVER=redis

SANCTUM_STATEFUL_DOMAINS=localhost
```
