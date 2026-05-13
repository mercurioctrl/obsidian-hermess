# Stack — Control de Precios

## Backend
- **PHP** (sin framework) — SSR clásico
- **sqlsrv** (extensión nativa PHP) + **PDO sqlsrv** — dos drivers coexisten
- **SQL Server 2012** en `190.210.23.97,4444`

## Frontend
- **jQuery** 1.12.4
- **Bootstrap**
- **DataTables** — grilla principal con paginado/filtrado
- **Tooltipster** — tooltips

## Infraestructura
- **Docker** — contenedor `controldeprecios-web-1` (puerto 8084:80)
  - Imagen base: Debian Buster
  - Driver ODBC: `msodbcsql17`
  - Extensión PHP: `sqlsrv-5.9.0` (ODBC 18 no compatible con SQL Server 2012 + TLS 1.0)
  - TLS bajado a 1.0 en Dockerfile por incompatibilidad con OpenSSL moderno
- **Apache 2.4** en host → proxy reverso a contenedor
- Arrancar: `docker compose -f /var/www/nb/controldeprecios/docker-compose.yml up -d`

## Build JS
Después de editar `controlDePrecios.js`, regenerar el minificado:
```bash
npx terser /var/www/nb/controldeprecios/javaScript/controlDePrecios.js \
  -o /var/www/nb/controldeprecios/javaScript/controlDePrecios.min.js \
  --compress --mangle
```

## Ver también
- [[NB/controldeprecios/controldeprecios|Control de Precios]]
- [[NB/controldeprecios/arquitectura|Arquitectura]]
