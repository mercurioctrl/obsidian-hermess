# Stack

## Runtime

- **Python 3.11** — la única versión donde pymssql + playwright instalan sin dolor en local.
- **Docker** con imagen base `mcr.microsoft.com/playwright/python:v1.48.0-jammy` (trae Chromium + deps de sistema pre-instalados).

## Dependencias (`requirements.txt`)

| Paquete           | Versión | Para qué                                                |
|-------------------|---------|---------------------------------------------------------|
| `playwright`      | 1.48.0  | Automatización de Chromium para scraping AFIP.          |
| `python-dotenv`   | 1.0.1   | Carga de credenciales desde `.env`.                     |
| `PyYAML`          | 6.0.2   | Lectura de `cuits.yaml`.                                |
| `pymssql`         | 2.3.1   | Driver SQL Server (TDS 7.4 para SQL 2012+).             |

## Base de datos

- **SQL Server 2012** (compatible con versiones posteriores).
- Tabla: `NewBytes_DBF.dbo.AfipComprobantesRecibidos` — ver [[migracion]] y [[tabla-referencia]].
- Patrón de carga: staging temp table + `MERGE` → idempotencia vía índice único.

## Sistema externo

- Portal AFIP / ARCA: login en `auth.afip.gob.ar`, servicio Mis Comprobantes en `fes.afip.gob.ar/mcmp/`.
- Sin 2FA (cuenta de Sebastián Fontán con relaciones de clave fiscal sobre los CUITs del grupo).

## Ver también

- [[arquitectura]] — por qué cada pieza.
- [[despliegue]] — cómo corre en el server.
