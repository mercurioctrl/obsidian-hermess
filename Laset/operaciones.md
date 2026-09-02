# Operaciones (runbook)

Ver también: [[Laset]] · [[arquitectura]] · [[troubleshooting]]
Runbook completo en el repo: `/var/www/laset/docs/operaciones.md`.

## Backs (Docker)
```bash
cd /var/www/laset/backLaset/<app>
docker compose -p <proj>-laset up -d      # usa imagen *-laset, NO buildea
docker compose -p <proj>-laset down
docker logs -f <container>-laset
```

| carpeta | project (-p) | contenedor | puerto |
|---|---|---|---|
| api-rest-cobros | cobros-laset | cobros-api-rest-laset | 8183 |
| api-rest-compras-laravel | compras-laset | api-rest-compras-apirest-laravel-laset | 8196 |
| api-rest-expedicion | expedicion-laset | expedition-api-rest-laset | 8184 |
| api-rest-pedidos-laravel | pedidos-laset | api-rest-pedidos-apirest-laravel-laset | 8193 |
| api-rest-postventa | postventa-laset | postventa-api-rest-laset | 8182 |
| microservicio-comprobantes-v2 | comprobantes-laset | microservicio-comprobantes-laset | 8188 |
| ms-metadata | msmetadata-laset | ms-metadata-laset | 8185 |

> Red `laset-net` es `external`: si falta, `docker network create laset-net`.
> **NO** `docker network prune` (borra redes de la otra empresa; pool casi lleno).

### Dependencias de un back PHP (no vienen en el repo)
```bash
docker exec <container> sh -c 'cd /var/www/app && composer install --no-interaction --no-security-blocking'
# cobros además: --ignore-platform-reqs
```
### Laravel (compras, pedidos)
```bash
cd <app>/app
mkdir -p storage/app/public storage/framework/{cache/data,sessions,testing,views} storage/logs bootstrap/cache
chmod -R 777 storage bootstrap/cache
# tras cambiar .env:
docker exec <container> sh -c 'cd /var/www/app && php artisan config:clear'
```
### ms-metadata
Lee `.env.docker` al arrancar → tras cambios: `docker compose -p msmetadata-laset restart`. Swagger en `/docs`.
### Permisos
`.env` de back en `chmod 644` (Apache=www-data no lee 600).

## Fronts (PM2)
```bash
cd /var/www/laset/frontLaset/<app>/app
npm install --legacy-peer-deps --no-audit --no-fund
NODE_OPTIONS=--openssl-legacy-provider npm run build
pm2 start ecosystem.config.js && pm2 save
```
- `comprobante-pdf`: install con `--ignore-scripts` (módulo nativo `canvas`).
- Mantener `instances: 2` (no `'max'` = 24 por core → agota RAM).

## Verificación end-to-end
```bash
curl -s http://localhost:8193/v1/auth/login -H 'Content-Type: application/json' \
  --data-raw '{"username":"<user>","password":"<pass>","ip":"0.0.0.0"}'   # → {"token":...}
```

## Pendientes opcionales
- `pm2 startup` (sudo) para arranque tras reboot.
- `DEBUG=0` en back Phinx (evita notices PHP8 en el JSON).
- Confirmar back real de `inventario` (hoy ms-metadata, tentativo).
- Versionar `docker-compose.yml` / `ecosystem.config.js` (los `.env` quedan fuera por secretos).
