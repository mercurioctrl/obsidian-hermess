# 00-init.sql

> Script de inicialización de MySQL. Se ejecuta solo en el primer arranque (cuando el volumen está vacío).
> Parte del skill [[SKILL|fullstack-docker-app]].

Montado en `db` via `docker-entrypoint-initdb.d` en [[docker-compose.yml]].
Nombre de DB definido en [[env.example]] como `DB_NAME`.

## Template

```sql
CREATE DATABASE IF NOT EXISTS {{DB_NAME}} CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
```
