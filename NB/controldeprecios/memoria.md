# Memoria Claude — Control de Precios

Sincronizado desde `~/.claude/projects/-var-www-nb-controldeprecios/memory/`

---

## Feedback

### JS: siempre regenerar el minificado
`recursos.php` carga `javaScript/controlDePrecios.min.js` (no el fuente).
Después de editar `controlDePrecios.js`, siempre correr:
```bash
npx terser /var/www/nb/controldeprecios/javaScript/controlDePrecios.js \
  -o /var/www/nb/controldeprecios/javaScript/controlDePrecios.min.js \
  --compress --mangle
```

### Patrón de errores PHP → JS
El backend devuelve `json_encode(["error" => "mensaje"])`.
El JS en `callback_fn` parsea: si tiene `.error`, hace `alert()` y `return` sin tocar el DOM.

---

## Proyecto

### Límite máximo de LO2 — dinámico desde BD
No es hardcodeado. Se lee desde `[NEW_BYTES].[dbo].[PV_PARAMETROS_VARIOS].UMaxLo2`.
Validación en `procesar/cambiarUtilidad.php`. Fallback: `10` si devuelve null.

### Feature: una fila por almacén (en progreso)
`api/data/basic.php` modificado:
- Quitado `AND stocks.ID_ALMACEN = 2` del LEFT JOIN
- Agregado `stocks.ID_ALMACEN` al SELECT
- Orden: `ORDER BY cdetalle ASC, stocks.ID_ALMACEN ASC`

Fix JS para IDs duplicados: cambiar `$('#PL-123')` por `$('[id="PL-123"]')` en:
- `callback_fn` (~línea 1099 y ~1105)
- `cambiarFinal` (~línea 1065)

Columna `rem` (REMITOS_PRO) pendiente — muestra total global, no por almacén.

---

## Referencia / Infraestructura

- **Servidor:** `10.10.10.7` (Ubuntu), Apache 2.4 en host
- **DB:** SQL Server 2012 en `190.210.23.97,4444` (cert autofirmado, TLS 1.0)
- **Contenedor:** `controldeprecios-web-1` (puerto 8084:80)
- **VHost:** `controldeprecios.local` → proxy `localhost:8084`
- Usar `docker compose` v2 (NO `docker-compose` v1)
- `conexion_nb.php`: `sqlsrv_connect()` con `TrustServerCertificate => true`
- `database.class.php`: PDO DSN con `;TrustServerCertificate=1`
- Dockerfile: `msodbcsql17` + `sqlsrv-5.9.0`

---

## Ver también
- [[NB/controldeprecios/controldeprecios|Control de Precios]]
- [[NB/controldeprecios/contexto|Contexto]]
- [[NB/controldeprecios/arquitectura|Arquitectura]]
