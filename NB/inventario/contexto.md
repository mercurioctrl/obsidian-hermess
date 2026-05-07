# Contexto — inventario

Información de entorno local, variables de entorno y gotchas del proyecto.

## Entorno local

### Backend (ms-metadata)

```bash
cd /var/www/nb/inventario/ms-metadata
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```

- **Swagger UI**: http://localhost:8000/docs
- **ODBC**: Solo está instalado "ODBC Driver 18 for SQL Server" (no el 17) — importante en `DB_DRIVER`

### Frontend (inventario-web-app)

```bash
cd /var/www/nb/inventario/inventario-web-app/app
npm run dev
# URL: http://localhost:3000
```

## Variables de entorno

### ms-metadata/.env

```
DB_DRIVER=ODBC Driver 18 for SQL Server
DB_SERVER=190.210.23.97,4444        # formato host,puerto (no DB_HOST/DB_PORT)
DB_NAME=NB_WEB
DB_USER=emanzando_devweb01
DB_PASS=...                          # la variable es DB_PASS, no DB_PASSWORD
ALLOWED_ORIGINS=http://localhost,http://localhost:3000,...
SYNCUP_TOKEN=123456
TIMEOUT=7
```

### inventario-web-app/app/.env

```
API_HOST=http://localhost:8000
NODE_PORT=3000
NODE_ENV=development
```

## Gotchas conocidos

| Problema | Causa | Solución |
|----------|-------|---------|
| Servidor backend crashea al iniciar | `ALLOWED_ORIGINS` no definido (`.split(",")` sin default) | Asegurarse de que la variable esté en `.env` |
| `.env` original tenía nombres incorrectos | El código espera `DB_SERVER`, `DB_PASS`, `DB_DRIVER` (no `DB_HOST`, `DB_PASSWORD`, `DB_TYPE`) | Copiar `.env_example` y completar con los nombres correctos |
| `FastAPIDeprecationWarning: regex has been deprecated` | `main.py:653` usa parámetro `regex` deprecado en Pydantic | No rompe nada, es un warning |
| `Cannot find module ../build-version.json` al iniciar dev | Lo genera `scripts/update-build-version.js` solo al hacer `npm run build` | No rompe nada en dev |
| 401 al iniciar el frontend | El middleware `auth` redirige todas las rutas a `/login` si no hay token | Comportamiento normal |

## Ver también

- [[inventario]] · [[arquitectura]] · [[stack]]
