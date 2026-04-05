# env.example

> Variables de entorno raíz del proyecto. Los secretos se auto-generan con [[start.sh]].
> Parte del skill [[SKILL|fullstack-docker-app]].

Usado por [[docker-compose.yml]] para configurar todos los servicios.
Ver también [[backend-env.example]] para variables específicas de Laravel.
Convención: `.env` nunca se commitea — ver [[conventions#General]].

## Template

```env
# Database
DB_NAME={{DB_NAME}}
DB_USER={{DB_NAME}}
DB_PASSWORD=
DB_ROOT_PASSWORD=
DB_PORT=3306

# Laravel
APP_KEY=
APP_NAME={{NOMBRE_PROYECTO_UPPER}}

# Redis
REDIS_HOST=redis
REDIS_PORT=6379

# App
APP_PORT={{PUERTO}}
API_BASE_URL=http://localhost:{{PUERTO}}/api
```
