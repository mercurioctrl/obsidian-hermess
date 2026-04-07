# Planilla Acciones Bully - Apps Script

## Descripcion General

Script de Google Apps Script para la planilla **"Opciones con API Bully"** que consulta precios de opciones financieras desde la API `https://api.bully.lio.red/options`.

**Version actual deployada: v5 (sin GOOGLEFINANCE)**

### Funcionalidades principales

El menu **Opciones API** en la planilla tiene dos acciones: **Actualizar Precios de Opciones** (procesa todas las filas con datos) y **Actualizar Filas Seleccionadas** (procesa solo las filas que tengas seleccionadas). Tambien hay un trigger automatico (`onEditTrigger`) que procesa una fila individual cuando editas las columnas B-E (expiration_date, symbol, type, strike).

### Proyecto Apps Script

- URL del editor: `https://script.google.com/u/0/home/projects/1GQ32BC3XcLudtVARbvMyT1lgJ0WOpCynYUlff8zd2KXhZaB3K7ygRlVO/edit`
- Archivo: `Code.gs` (unico archivo del proyecto)

---

## Configuracion (CONFIG)

```javascript
const CONFIG = {
  MAX_RETRIES: 2,           // Reintentos en caso de error HTTP
  RETRY_DELAY_MS: 1000,     // Delay base entre reintentos (backoff exponencial)
  MARK_COLUMN: 27,          // Columna AA - ultima actualizacion
  STATUS: 14,               // Columna N - estado de la fila
  FAIRVALUE_COLUMN: 16,     // Columna P - Fair Value
  NEXTREPORT_COLUMN: 15,    // Columna O - Proximo reporte
  DISPLAY_BATCH_SIZE: 10,   // Cada cuantas filas hacer flush() para refrescar pantalla
  DEBUG: 0,                 // 0 = sin logs, 1 = escribe en hoja "Debug"
  STOCK_PRICE_COL: 1,       // Columna A - stockPrice (v5)
  CHANGE_PCT_COL: 7,        // Columna G - changePct (v5)
  LOW52_COL: 18,            // Columna R - low52 (v5)
  HIGH52_COL: 19,           // Columna S - high52 (v5)
  BETA_COL: 20,             // Columna T - beta (v5)
};
```

Para activar el modo debug, cambiar `DEBUG: 0` a `DEBUG: 1`. Esto escribe logs detallados en la pestana "Debug" de la planilla, pero ralentiza significativamente la ejecucion.

---

## Estructura de Columnas

| Columna | Letra | Contenido |
|---------|-------|-----------|
| 1 | A | stockPrice (desde v5, antes GOOGLEFINANCE) |
| 2 | B | expiration_date |
| 3 | C | symbol |
| 4 | D | type (C o P) |
| 5 | E | strike |
| 7 | G | changePct (desde v5, antes GOOGLEFINANCE) |
| 10 | J | lastPrice |
| 11 | K | impliedVolatility |
| 12 | L | bid |
| 13 | M | openInterest |
| 14 | N | STATUS (En cola / Listo / Error / etc.) |
| 15 | O | nextReport |
| 16 | P | fairValue |
| 18 | R | low52 (desde v5, antes GOOGLEFINANCE) |
| 19 | S | high52 (desde v5, antes GOOGLEFINANCE) |
| 20 | T | beta (desde v5, antes GOOGLEFINANCE) |
| 27 | AA | Marca de ultima actualizacion |

---

## Flujo de Ejecucion (Actualizar Filas Seleccionadas)

1. Se leen todas las filas seleccionadas y se filtran las que estan en fila >= 2
2. **Pre-lectura batch**: se leen los datos de todas las filas (columnas B-E) en un solo `getRange().getValues()`
3. **Semaforo**: se marcan TODAS las filas como "En cola" de una sola vez usando `getRangeList().setValue()` + `flush()`
4. Se procesan una por una:
   - Se construye la URL de la API con `buildRequestFromData_()`
   - Se hace `UrlFetchApp.fetch()` individual
   - Si HTTP 200: se parsea el JSON, se escribe el resultado inmediatamente con `writeRowResults_()`
   - Si falla: se reintenta hasta MAX_RETRIES veces con backoff exponencial
5. Cada DISPLAY_BATCH_SIZE filas procesadas se hace `SpreadsheetApp.flush()` para refrescar la pantalla
6. Flush final al terminar

### Estados posibles de una fila (columna N)

| Estado | Significado |
|--------|-------------|
| En cola | Esperando ser procesada |
| Procesando... | En proceso (solo en onEditTrigger) |
| Listo | Actualizada exitosamente |
| Error | Error de validacion de datos |
| Error API | La API respondio con error HTTP |
| Error JSON | No se pudo parsear la respuesta |
| Sin datos | La API respondio OK pero sin datos |

---

## API Bully

- **Endpoint**: `https://api.bully.lio.red/options`
- **Parametros**: `symbol`, `type`, `expiration_date` (dd-mm-yyyy), `strike` (con 2 decimales)
- **Respuesta**: Array JSON con objetos que contienen `lastPrice`, `impliedVolatility`, `bid`, `openInterest`, `fairValue`, `nextReport`, `stockPrice`, `changePct`, `low52`, `high52`, `beta`

Ejemplo de URL: `https://api.bully.lio.red/options?symbol=AAPL&type=C&expiration_date=15-03-2026&strike=150.00`

---

## Archivos de Codigo

- `codigo/Code_gs_original.js` - Codigo original (antes de las optimizaciones)
- `codigo/Code_gs_v4_optimizado.js` - Version intermedia con optimizaciones de cache y batch
- `codigo/Code_gs_v5_sin_googlefinance.js` - **Version actual deployada** (elimina GOOGLEFINANCE)

---

## Historial de Cambios

### v5 - Sin GOOGLEFINANCE (version actual, abril 2026)

Cambios respecto a v4:

1. **Datos de stock via API**: Las columnas A (stockPrice), G (changePct), R (low52), S (high52), T (beta) ahora se llenan desde la respuesta de la API en vez de usar formulas `GOOGLEFINANCE`. Esto elimina la dependencia de GOOGLEFINANCE que era lenta e inestable.

2. **Nueva funcion `extractStockData_()`**: Extrae los campos de stock del objeto de respuesta de la API y los pasa a `writeRowResults_()`.

3. **`writeRowResults_()` ampliada**: Ahora recibe un parametro `stockData` y escribe las 5 columnas nuevas de stock. Las columnas R, S, T se escriben en un solo `getRange().setValues()` (1 call en vez de 3).

4. **Frases rotativas de cola**: En vez del texto fijo "En cola", ahora muestra frases aleatorias (array `FRASES_COLA`) con formato naranja/italica mientras espera. Cada fila de la seleccion recibe una frase diferente de forma rotativa.

5. **`DISPLAY_BATCH_SIZE` subido a 10** (antes 5): Menos llamadas a `flush()` para mayor velocidad.

6. **Nueva funcion `columnToLetter_()`**: Convierte numero de columna a letra para notacion A1, usada internamente.

---

### v4 - Optimizada (abril 2026)

Cambios respecto al original:

1. **DEBUG desactivado** (`DEBUG: 0`): Cada llamada a `logDebugMessage()` hacia un `appendRow()` en la hoja Debug, lo cual era el mayor cuello de botella. Con DEBUG en 0, esas escrituras se saltean completamente.

2. **Pre-lectura de datos en batch**: En vez de leer los datos de cada fila individualmente con `getRange().getValues()` dentro del loop, ahora se lee todo el rango de una sola vez al inicio. Esto ahorra N-1 llamadas al spreadsheet.

3. **Semaforo visual con "En cola"**: Al iniciar el proceso, todas las filas seleccionadas se marcan como "En cola" usando `getRangeList().setValue()` (una sola llamada para todas). Esto reemplaza el antiguo "Conectando a bully.lio.red" que se escribia individualmente antes de cada fetch.

4. **MAX_RETRIES reducido a 2** (antes 3): Reduce la espera maxima en caso de errores de 1+2+4=7s a 1+2=3s.

5. **DISPLAY_BATCH_SIZE subido a 5** (antes 3): Menos llamadas a `flush()`, cada una tiene overhead.

6. **Funcion procesarFila simplificada**: Ahora usa `buildRequestFromData_()` en vez de tener toda la logica de validacion inline.

7. **Se elimino `buildRequestForRow_()`** (leia de la hoja) y se reemplazo por **`buildRequestFromData_()`** (recibe datos ya leidos como parametro).

8. **Se elimino `PARALLEL_BATCH_SIZE`** y `fetchAll()`: El script original usaba `UrlFetchApp.fetchAll()` que bloqueaba hasta que TODAS las respuestas llegaban. Ahora usa `UrlFetchApp.fetch()` individual por fila, lo cual permite escribir resultados progresivamente.

### Notas tecnicas sobre Apps Script

- Apps Script es single-threaded: no se pueden hacer operaciones async/paralelas reales
- `fetchAll()` envia todas las requests pero bloquea hasta recibir TODAS las respuestas
- `SpreadsheetApp.flush()` fuerza el refresco visual de la hoja mid-ejecucion
- `getRangeList()` permite escribir el mismo valor a multiples celdas no contiguas en una sola llamada
- Para inyectar codigo en el editor, se usa la API de Monaco: `monaco.editor.getModels()[0].setValue(decoded)`
- Los caracteres especiales (tildes, enie) causan problemas con `atob()` en el navegador, asi que el codigo usa solo ASCII

---

## Ver tambien

- [[Planilla Acciones Bully/Planilla Acciones Bully|Planilla Acciones Bully]] — Indice del proyecto
- [[Planilla Acciones Bully/prompt-optimizar-api|Prompt - Optimizar API]] — Prompt para optimizar la API Python
- [[Planilla Acciones Bully/prompt-agregar-stock-data-api|Prompt - Agregar stock data API]] — Prompt que origino los cambios de v5
