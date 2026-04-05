# Fullstack Docker App Skill

Genera toda la infraestructura de deploy para una app fullstack Nuxt 3 + Laravel 11,
lista para producción con un solo comando: `bash start.sh`.

> Ver [[architecture]] para decisiones de diseño y [[conventions]] para patrones obligatorios.

## Stack Generado

| Capa | Tecnología | Puerto interno |
|------|-----------|----------------|
| Frontend | Nuxt 3 + Vue 3 + Tailwind + Pinia (SSR) | 3000 |
| Backend | Laravel 11 + PHP 8.3 (Sanctum auth) | 8000 |
| Database | MySQL 8 (healthcheck, init SQL) | 3306 |
| Cache | Redis 7 Alpine (cache + sessions) | 6379 |
| Proxy | Nginx Alpine (single port) | 80 → host |
| Scheduler | Mismo backend, distinto CMD | - |

## Proceso de Generación

### 1. Recopilar Inputs

Preguntar o inferir del contexto:

- **nombre_proyecto**: Nombre corto sin espacios (ej: `mi-erp`, `tienda-online`).
- **puerto**: Puerto externo del host (default: `8080`).
- **dominio**: Qué gestiona la app (ecommerce, CRM, ERP, CMS, blog, etc.).
- **modulos**: Lista de módulos de dominio iniciales (ej: clientes, productos, pedidos).

### 2. Leer Templates

Antes de generar CUALQUIER archivo, leer los templates base:

- [[docker-compose.yml]] — Orquestación de servicios
- [[nginx.conf]] — Reverse proxy
- [[backend.Dockerfile]] — Imagen PHP/Laravel
- [[frontend.Dockerfile]] — Imagen Node/Nuxt (multi-stage)
- [[docker-entrypoint.sh]] — Entrypoint resiliente del backend
- [[start.sh]] — Script de arranque con generación de secretos
- [[stop.sh]] — Script de parada
- [[backup.sh]] — Backup de DB + archivos
- [[restore.sh]] — Restore interactivo
- [[00-init.sql]] — Inicialización de la base de datos
- [[env.example]] — Variables de entorno raíz
- [[backend-env.example]] — Variables de entorno del backend

### 3. Leer Referencias

- [[architecture]] — Decisiones de arquitectura y por qué
- [[conventions]] — Convenciones y patrones obligatorios

### 4. Generar Estructura

Reemplazar todos los placeholders y generar:

```
{{nombre_proyecto}}/
├── docker-compose.yml
├── .env.example
├── start.sh
├── stop.sh
├── backup.sh
├── restore.sh
├── backups/
├── nginx/
│   └── default.conf
├── db/
│   └── init/
│       └── 00-init.sql
├── backend/
│   ├── Dockerfile
│   ├── docker-entrypoint.sh
│   ├── .env.example
│   └── (Laravel 11 app)
└── frontend/
    ├── Dockerfile
    └── (Nuxt 3 app)
```

### 5. Generar Código Base

Si el usuario lo pide, generar también:

**Backend (Laravel):**
- Modelos + migraciones para cada módulo
- Controllers API Resource
- Routes en `routes/api.php`
- Seeders con datos de prueba

**Frontend (Nuxt):**
- Páginas para cada módulo
- `composables/useApi.ts`
- `stores/auth.ts` (Pinia)
- `middleware/auth.global.ts`
- Layouts y componentes UI base

### 6. Verificar

- [ ] Todos los placeholders reemplazados
- [ ] Healthcheck en MySQL y depends_on correctos
- [ ] Nginx rutea correctamente
- [ ] Secretos auto-generados, nunca hardcodeados
- [ ] Entrypoint recrea dirs de storage
- [ ] Frontend multi-stage build
- [ ] Backend usa DNS Docker (`db`, `redis`)

## Placeholders

| Placeholder | Descripción | Ejemplo |
|------------|-------------|---------|
| `{{NOMBRE_PROYECTO}}` | Nombre del proyecto | `mi-erp` |
| `{{NOMBRE_PROYECTO_UPPER}}` | Nombre para display | `Mi ERP` |
| `{{CONTAINER_PREFIX}}` | Prefijo de containers | `mi-erp` |
| `{{DB_NAME}}` | Nombre de la base de datos | `mi_erp` |
| `{{PUERTO}}` | Puerto externo | `8080` |
| `{{ADMIN_EMAIL}}` | Email admin | `admin@empresa.com` |
| `{{ADMIN_PASSWORD}}` | Password admin | `admin123` |

## Convenciones Obligatorias

Ver [[conventions]] para el listado completo. Resumen:

- **Single port**: Solo Nginx expuesto al host
- **Secretos auto-generados**: `openssl rand` en [[start.sh]]
- **Entrypoint resiliente**: mkdir + chmod en [[docker-entrypoint.sh]]
- **env() prohibido en controllers**: Siempre `config()`
- **Volumes nombrados**: Para persistencia
- **Retry en migraciones**: Loop 3 intentos
- **Deploy rápido backend**: `docker cp` + `optimize:clear`
- **Deploy frontend**: Siempre rebuild
