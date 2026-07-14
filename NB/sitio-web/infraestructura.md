# Infraestructura (setup local)

Ver índice: [[sitio-web]]

## API REST

- **Contenedor Docker:** `nb-api-rest` (imagen `sitio-api-rest-v3_apirest:latest`)
- **Puerto host:** `8085` → `http://localhost:8085/v1`
- `docker-compose.yml` en `sitio-api-rest-v3/` (usa la imagen existente, no rebuild)
- **Redis:** vía `172.18.0.1:6379` (gateway del bridge `nb-api-rest-network` → host → contenedor `sitio-api-rest-redis`)
- El código se sirve desde `/var/www/app` en el contenedor (volumen montado: editar el archivo host impacta en vivo).

### Comandos

```bash
sudo docker-compose up -d / down / logs -f
sudo docker exec nb-api-rest composer install --working-dir=/var/www/app
sudo docker exec nb-api-rest vendor/bin/phinx migrate --working-dir=/var/www/app
```

`docker exec` falla si el CWD es un mountpoint de Docker → ejecutar desde `/tmp`.

## Frontend

- **PM2:** proceso `WebAppNB`, modo cluster, puerto `3001`
- `ecosystem.config.js` en `sitio-wep-app-v2/app/` — incluye `NODE_OPTIONS=--openssl-legacy-provider`, `cwd`, `NODE_PORT=3001`, `NODE_HOST=0.0.0.0`, `NODE_ENV=production` (cambio local, no commiteado)
- **Apache vhost:** `sitionb.local` → ProxyPass `http://localhost:3001/`
- **/etc/hosts:** `127.0.0.1 sitionb.local`

### Build / deploy

```bash
NODE_OPTIONS=--openssl-legacy-provider npm run build
pm2 start ecosystem.config.js && pm2 save
pm2 restart WebAppNB
```

## Consultar la BD de producción (debug)

Script PHP dentro del contenedor sourceando `.env` (SQL Server remoto):

```bash
sudo docker exec nb-api-rest sh -c 'set -a; . /var/www/app/.env; php /tmp/script.php'
```

`DB_HOST=190.210.23.97 DB_PORT=4444 DB_NAME=NB_WEB`. Requiere autorización explícita del usuario (es prod).

## Ver también

- [[stack]] · [[arquitectura]] · [[contexto]]
