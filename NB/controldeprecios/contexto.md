# Contexto — Control de Precios

## Propósito

Sistema interno de NB para que los vendedores/operadores gestionen precios de artículos.
Permite ajustar utilidades (PL, PLI, MAY1, MAY2, LO1, LO2, CF) y ver stock por depósito.

## Reglas de negocio

### Utilidades disponibles
| Código | Descripción |
|---|---|
| PL | Precio lista |
| PLI | Precio lista incrementado |
| MAY1 / MAY2 | Mayorista 1 y 2 |
| LO1 / LO2 | Libre Opción 1 y 2 |
| CF | Costo final |
| DT2 / DT3 | Descuentos |

### Límites
- **LO2 máximo**: se lee dinámicamente desde `[NEW_BYTES].[dbo].[PV_PARAMETROS_VARIOS].UMaxLo2` (fallback: 10%)
- **Utilidad mínima**: validada por artículo en `ST_GANANCIA_ESTIPULADA_ARTICULOS` + `PV_PARAMETROS_VARIOS.minUtility`
- Artículos de familia 65 y con `minUtilityExclude=1` quedan excluidos de validación mínima

### Permisos por agente (`[NB_WEB].dbo.permisos_agente`)
- `unlockedLoPrice = 1` → puede **ver** columnas LO2/LOP/LIBRE_OPCION
- `unlockedLoPriceModify = 1` → puede **modificar** LO2 (individual y masivo)
- LO1 no tiene restricción de modificación

### Patrón error PHP → JS
El backend devuelve `json_encode(["error" => "mensaje"])` para rechazar operaciones.
El JS parsea: si hay `.error`, hace `alert()` y `return` sin tocar el DOM.

### Cambio de utilidad LO1/LO2 — efecto cascada
Al cambiar LO1 o LO2, se recalcula el costo en la BD de Libre Opción (`CS.dbo.productos`).
Si `PV_PARAMETROS_VARIOS.dtoDelay = 'SI'`, también se ejecuta el SP `ActualizarCostoClienteConDescuento`.

## TODOs / Próximos pasos
- Columna `rem` (REMITOS_PRO) pendiente de filtrar por almacén (actualmente muestra total global)
- Feature "una fila por almacén" en progreso en `api/data/basic.php`

## Ver también
- [[NB/controldeprecios/controldeprecios|Control de Precios]]
- [[NB/controldeprecios/arquitectura|Arquitectura]]
- [[NB/controldeprecios/memoria|Memoria Claude]]
