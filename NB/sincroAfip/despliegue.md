# Despliegue

## Prerrequisitos del server

- Docker 24+ y Compose v2.
- Salida a `auth.afip.gob.ar`, `portalcf.cloud.afip.gob.ar`, `fes.afip.gob.ar`, `serviciosweb.afip.gob.ar`, y al host SQL Server.
- Unos MB/mes por CUIT para el volumen `storage/`.

## Instalación inicial

```bash
git clone <repo> sincroAfip && cd sincroAfip
cp .env.example .env && vim .env          # credenciales AFIP + DB
vim cuits.yaml                            # activar CUITs con activo: true
# ejecutar el DDL en SQL Server → ver [[migracion]]
docker compose build
docker compose run --rm sincro --ultimos-dias 3 --cuit 30-70924663-8
```

## Cron diario (opción recomendada)

```cron
0 7 * * * ops cd /opt/sincroAfip && docker compose run --rm sincro --ultimos-dias 2 >> /var/log/sincroafip.log 2>&1
```

`--ultimos-dias 2` da un día de margen. Idempotencia vía MERGE (ver [[arquitectura]]) evita duplicados.

## Monitoreo

- `storage/logs/sincro.log` rotado (5 MB × 5 = ~25 MB máximo).
- Exit code `sincro.py`: `0` OK, `1` al menos un CUIT falló.
- Wrapper con alerta:

```bash
#!/bin/bash
cd /opt/sincroAfip
docker compose run --rm sincro --ultimos-dias 2 || \
  curl -s -X POST https://hooks.slack.com/... -d '{"text":"sincroAfip fallo"}'
```

## Alta de un nuevo CUIT

1. Habilitar "Mis Comprobantes" en **Administrador de Relaciones de Clave Fiscal** de AFIP para el usuario `AFIP_USER`.
2. Agregar a `cuits.yaml`:
   ```yaml
   - cuit: "30-XXXXXXXX-X"
     nombre: "RAZON SOCIAL"
     activo: true
   ```
3. Primera corrida de prueba: `docker compose run --rm sincro --ultimos-dias 3 --cuit 30-XXXXXXXX-X`.

## Baja (pausar)

`activo: false` en `cuits.yaml`. No borrar la entrada. Datos históricos en DB se mantienen.

## Troubleshooting

### "No encontré el tab 'Recibidos'" u otro selector

AFIP cambió la UI. Correr con debug y revisar screenshots:

```bash
docker compose run --rm sincro --ultimos-dias 3 --cuit 30-70924663-8 --debug --headful
```

Ajustar selector en `afip/scraper.py` (ver sección "Lo que rompe" en [[arquitectura]]).

### Sesión inválida

```bash
rm storage/sessions/<cuit_plano>.json
docker compose run --rm sincro --ultimos-dias 3 --cuit <cuit>
```

### "El ZIP no contiene CSV"

Cambio de formato en AFIP. Inspeccionar el archivo temporal antes del `zipfile.extract` en `scraper._descargar_recibidos`.

### pymssql rompe en mac

`brew install freetds` o directamente usar Docker para el loader.

### AFIP activa 2FA inesperadamente

Este scraper no maneja OTP headless. Primera corrida `--headful` para completar OTP manualmente; la sesión queda cacheada.

## Recuperación ante incidentes

**DB perdida:** recrear schema ([[migracion]]) y re-bajar rango amplio. La idempotencia permite re-cargar sin miedo.

**`storage/` borrado:** `sessions/` y `logs/` se regeneran; `output/` se puede regenerar pegándole a AFIP otra vez.

**AFIP bloquea la cuenta por abuso:** espaciar corridas, no usar `--debug` en prod, verificar que no hay otro cron simultáneo.

## Ver también

- [[sincroAfip]]
- [[arquitectura]] — internals del scraper.
- [[migracion]] — para recrear la tabla.
- [[contexto]] — estado actual y pendientes.
