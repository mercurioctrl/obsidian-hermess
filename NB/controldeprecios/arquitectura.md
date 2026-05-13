# Arquitectura — Control de Precios

## Estructura general

PHP sin framework. SSR con jQuery en el frontend.

```
index.php              → entrada principal, arma la grilla
columnas.php           → genera <th> dinámicos según permisos del agente
filtros.php            → filtros de la grilla (familias, marcas, almacenes)
recursos.php           → incluye JS/CSS (carga el .min.js, no el fuente)
f_controlPrecios.php   → funciones PHP de precios (cambiarUtilidad, recalcularPrecio, etc.)
f_controlDeStock.php   → funciones de stock

api/data/basic.php     → query principal que alimenta la grilla (DataTables)
api/data/almacenes.php → listado de almacenes
api/data/familias.php  → listado de familias
api/data/marcas.php    → listado de marcas

procesar/
  cambiarUtilidad.php  → modifica utilidad/descuento de un artículo individual
  cambiarTodo.php      → modifica utilidad en masa (por distribuidora)
  guardarStock.php     → guarda control de stock
  regu_global.php      → regularización global de precios

class/
  editarPrecios.class.php  → recalcula precios en Libre Opción (CS DB)
  agentes.class.php        → datos del agente

acces/
  login.php            → formulario de login
  procesar_login.php   → valida usuario/clave, guarda SSID
  functions.php        → validarSeccion(), GETCHMODAG() (leer permisos por agente)

javaScript/
  controlDePrecios.js      → fuente JS principal
  controlDePrecios.min.js  → versión minificada (la que usa recursos.php)
```

## Conexiones a base de datos

Dos archivos de conexión coexisten:
- `conexion_nb.php` — `sqlsrv_connect()` (driver nativo PHP)
- `database.class.php` — PDO con DSN sqlsrv

Ambos apuntan a `190.210.23.97,4444` con `TrustServerCertificate=1` (SQL Server 2012, cert autofirmado, TLS 1.0).

## Permisos por agente

Tabla `[NB_WEB].dbo.permisos_agente`. Función `GETCHMODAG($columna, $agente_id)` en `acces/functions.php`.

| Columna | Efecto |
|---|---|
| `unlockedLoPrice` | Ver columnas LO2 / LOP / LIBRE_OPCION en la grilla |
| `unlockedLoPriceModify` | Modificar LO2 via `cambiarUtilidad.php` y `cambiarTodo.php` |

## Feature en progreso: una fila por almacén

`api/data/basic.php` modificado para mostrar una fila por almacén por artículo.
Columnas de stock (stk, stk0, stklo, ctrl, cola, disp) ya funcionan por depósito.
Pendiente: columna `rem` (REMITOS_PRO) — actualmente muestra total global.

## Deployment

Apache en host (`controldeprecios.local.conf`) → proxy a `localhost:8084` → contenedor Docker `controldeprecios-web-1`.

## Ver también
- [[NB/controldeprecios/controldeprecios|Control de Precios]]
- [[NB/controldeprecios/stack|Stack]]
- [[NB/controldeprecios/contexto|Contexto]]
