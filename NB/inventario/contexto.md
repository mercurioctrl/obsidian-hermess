# Contexto — inventario

Información de entorno local, variables de entorno y gotchas del proyecto.

## Entorno local

### Mac (hermess) — `/Users/hermess/www/inventario/`

```bash
# Backend — OPENSSL_CONF es OBLIGATORIO (ver gotchas: TLS 1.0)
cd ms-metadata
OPENSSL_CONF=$PWD/openssl_legacy.cnf .venv/bin/uvicorn main:app --reload --port 8081 --host 0.0.0.0

# Frontend
cd inventario-web-app/app
npm run dev   # http://localhost:3000 — API_HOST=http://0.0.0.0:8081
```

- Venv del backend: `.venv` (Python 3.9), todas las deps instaladas
- Ambos repos en rama `catri-fine-tuning` (2026-06-11)

### Linux (/var/www/nb/inventario) — setup anterior

```bash
cd ms-metadata && uvicorn main:app --host 0.0.0.0 --port 8000 --reload
cd inventario-web-app/app && npm run dev
```

- **Swagger UI**: http://localhost:{puerto}/docs

## Variables de entorno

### ms-metadata/.env

```
DB_DRIVER=ODBC Driver 18 for SQL Server
DB_SERVER=190.210.23.97,4444        # formato host,puerto (no DB_HOST/DB_PORT)
DB_NAME=NB_WEB
DB_USER=web                          # (antes emanzando_devweb01)
DB_PASS=...                          # la variable es DB_PASS, no DB_PASSWORD
ALLOWED_ORIGINS=http://localhost:3000,...
OPENAI_API_KEY=...                   # placeholder alcanza para levantar; real para IA
STATIC_URL=https://static.nb.com.ar/ # sin esto revienta models.py con productos con foto
```

### inventario-web-app/app/.env

```
API_HOST=http://0.0.0.0:8081   # (en linux era :8000)
NODE_PORT=3000
NODE_ENV=development
```

## Gotchas conocidos

| Problema | Causa | Solución |
|----------|-------|---------|
| **pyodbc 08001 "TCP Provider: 10054"** en todo endpoint con DB, aunque TCP y ping al server andan (parece firewall/VPN, NO lo es) | El SQL Server de prod solo habla **TLS 1.0** y OpenSSL 3.x lo rechaza por defecto (ambos drivers ODBC 17/18, con o sin `Encrypt`) | Levantar uvicorn con `OPENSSL_CONF=openssl_legacy.cnf` (commiteado en el repo: `MinProtocol=TLSv1`, `SECLEVEL=0`) |
| **Filas desalineadas** con columna fija en tablas antd 1.x | `fixed:'left'` clona la tabla en un overlay y sincroniza alturas por JS — siempre se desfasa | CSS `position:sticky` + fondos opacos por estado (misma tabla ⇒ alineación perfecta). Ver `pages/itemsPrices.vue` |
| **Cabeceras corridas** con header fijo (`scroll.y`) | Header y body son tablas separadas; con `scroll.x:'max-content'` cada una calcula anchos distintos | `scroll.x` numérico (suma de anchos visibles) + `table-layout:fixed; min-width:100%` en ambas |
| Item no aparece al deep-linkear a Productos | La query default de la pestaña lleva `noImage=1` y `stock=1`, que FILTRAN | Omitir ambos en deep-links; buscar por ID numérico (`ID_ARTICULO` via LIKE) |
| `fetchCompetition` crashea en SSR (`Not authenticated` / token sync) | Dispatch fire-and-forget durante SSR pierde el contexto req/res de auth | Guardar con `process.client` antes de despachar |
| Servidor backend crashea al iniciar | `ALLOWED_ORIGINS` no definido (`.split(",")` sin default) | Asegurarse de que la variable esté en `.env` |
| `.env` original tenía nombres incorrectos | El código espera `DB_SERVER`, `DB_PASS`, `DB_DRIVER` (no `DB_HOST`, `DB_PASSWORD`, `DB_TYPE`) | Copiar `.env_example` y completar con los nombres correctos |
| `FastAPIDeprecationWarning: regex has been deprecated` | `main.py` usa parámetro `regex` deprecado | No rompe nada, es un warning |
| `Cannot find module ../build-version.json` al iniciar dev | Lo genera `scripts/update-build-version.js` solo al hacer `npm run build` | No rompe nada en dev |
| 401 al iniciar el frontend | El middleware `auth` redirige todas las rutas a `/login` si no hay token | Comportamiento normal |

## Reglas de negocio relevantes

- **Precios**: al fijar un precio a mano, la utilidad derivada se aplica SIEMPRE
  a la primera del par (PL1/MAY1/LO1/PML); la segunda queda fija. Ver [[modulo-precios]].
- **Mayoristas se comparan sin IVA** (campo `precio_sin_iva` de partpicker) contra
  los precios USD propios; resellers en ARS final como referencia de clientes.
- `scrap_hg.search_keys` es compartida entre la sección Precios y el scraper de
  hardgamers — editar keywords afecta a ambos.
- Pendiente de decisión: si `libre-opcion` (canal propio) debe excluirse del
  bloque de resellers en competencia.

## Ver también

- [[inventario]] · [[arquitectura]] · [[stack]] · [[modulo-precios]]
