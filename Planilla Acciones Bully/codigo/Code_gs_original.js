/**
 * Configuración
 */
const CONFIG = {
  MAX_RETRIES: 3,
  RETRY_DELAY_MS: 1000, // 1 segundo entre reintentos (para bloques)
  MARK_COLUMN: 27, // Columna de marca/última actualización
  STATUS: 14,      // Columna de estado
  FAIRVALUE_COLUMN: 16, // Fair Value
  NEXTREPORT_COLUMN: 15, // Próximo reporte
  PARALLEL_BATCH_SIZE: 50, // Tamaño de lote para fetchAll (paralelo controlado)
  DEBUG: 1, // 1 = activar logs en pestaña Debug, 0 = no loguear nada
};

/**
 * Función para registrar mensajes de debug en la hoja "Debug"
 */
function logDebugMessage(message) {
  try {
    if (CONFIG.DEBUG !== 1) return; // si DEBUG = 0, no loguea nada
    const hojaDebug = SpreadsheetApp.getActiveSpreadsheet().getSheetByName("Debug");
    const fechaHora = new Date();
    hojaDebug.appendRow([Utilities.formatDate(fechaHora, Session.getScriptTimeZone(), "HH:mm:ss dd/MM/yyyy"), message]);
  } catch (err) {
    // Evitar que falle toda la ejecución por problemas de logging
    if (CONFIG.DEBUG === 1) {
      console && console.log && console.log('Log error:', err);
    }
  }
}

/**
 * Formatea la fecha al formato requerido por la API (dd-mm-yyyy).
 */
function formatDateToAPI(fecha) {
  const fechaObj = new Date(fecha);
  if (isNaN(fechaObj.getTime())) return "Invalid Date";
  const dia = ('0' + fechaObj.getDate()).slice(-2);
  const mes = ('0' + (fechaObj.getMonth() + 1)).slice(-2);
  const año = fechaObj.getFullYear();
  return `${dia}-${mes}-${año}`;
}

/**
 * Construye la request para una fila (y valida datos mínimos).
 * Devuelve un objeto con:
 *  - ok: boolean
 *  - fila: number
 *  - request: {url, muteHttpExceptions}
 *  - errorMark / errorStatus si falla validación
 */
function buildRequestForRow_(hoja, filaNumero) {
  // Obtener los datos de las columnas B, C, D, E
  const data = hoja.getRange(filaNumero, 2, 1, 4).getValues()[0];
  const [expiration_date, symbol, type, strike] = data;

  // Validar fila vacía
  if (!expiration_date && !symbol && !type && !strike) {
    return { ok: false, fila: filaNumero, errorMark: "Fila vacía", errorStatus: "Error" };
  }

  // Validar campos completos
  if (!symbol || !type || !expiration_date || !strike) {
    return { ok: false, fila: filaNumero, errorMark: "Datos incompletos", errorStatus: "Error" };
  }

  // Validar tipo
  const tipo = String(type).toLowerCase();
  if (tipo !== 'c' && tipo !== 'p') {
    return { ok: false, fila: filaNumero, errorMark: "Tipo inválido", errorStatus: "Error" };
  }

  // Formatear fecha
  const fechaFormateada = formatDateToAPI(expiration_date);
  if (fechaFormateada === "Invalid Date") {
    return { ok: false, fila: filaNumero, errorMark: "Fecha inválida", errorStatus: "Error" };
  }

  // Validar y formatear strike
  const strikeNumber = parseFloat(strike);
  if (isNaN(strikeNumber)) {
    return { ok: false, fila: filaNumero, errorMark: "Strike inválido", errorStatus: "Error" };
  }
  const strikeFormateado = strikeNumber.toFixed(2);

  // Armar URL
  const url = `https://api.bully.lio.red/options?symbol=${encodeURIComponent(symbol)}&type=${encodeURIComponent(type)}&expiration_date=${encodeURIComponent(fechaFormateada)}&strike=${encodeURIComponent(strikeFormateado)}`;

  return {
    ok: true,
    fila: filaNumero,
    request: {
      url,
      muteHttpExceptions: true,
    }
  };
}

/**
 * Aplica en hoja los resultados de una fila con 2 escrituras:
 * - Bloque contiguo columnas 10..16 (7 columnas)
 * - Marca en columna CONFIG.MARK_COLUMN
 *
 * Orden de 10..16:
 * 10 lastPrice, 11 impliedVolatility, 12 bid, 13 openInterest,
 * 14 STATUS, 15 NEXTREPORT, 16 FAIRVALUE
 */
function writeRowResults_(hoja, fila, rowBlockValues, markText) {
  // Escribir bloque contiguo 10..16
  hoja.getRange(fila, 10, 1, 7).setValues([rowBlockValues]);
  // Escribir marca (columna 27)
  hoja.getRange(fila, CONFIG.MARK_COLUMN).setValue(markText);
}

/**
 * Procesa en paralelo (fetchAll) un conjunto de filas:
 * - Valida datos y arma requests
 * - Dispara fetchAll por lotes (PARALLEL_BATCH_SIZE)
 * - Reintenta por lotes las que fallen (hasta MAX_RETRIES)
 * - Escribe resultados por fila en 2 llamadas
 */
function processRowsInParallel_(hoja, filasArray) {
  const nowStr = Utilities.formatDate(new Date(), Session.getScriptTimeZone(), "HH:mm:ss dd/MM/yyyy");

  // Prevalidación/requests
  const requests = [];
  const meta = []; // {fila}
  const toWriteImmediate = []; // para errores de validación (sin request)
  for (const fila of filasArray) {
    // Estado visual de inicio
    hoja.getRange(fila, CONFIG.STATUS).setValue("Conectando a bully.lio.red");

    const built = buildRequestForRow_(hoja, fila);
    if (!built.ok) {
      // Armar bloque de 7 columnas con estado de error centrado en col 14
      const block = ["", "", "", "", "Error", "", ""];
      toWriteImmediate.push({ fila, block, mark: built.errorMark || "Error", status: built.errorStatus || "Error" });
      continue;
    }
    logDebugMessage(`Fila ${fila}: request paralelo -> ${built.request.url}`);
    requests.push(built.request);
    meta.push({ fila });
  }

  // Escribir de inmediato errores de validación (2 llamadas/fila)
  toWriteImmediate.forEach(({ fila, block, mark }) => {
    writeRowResults_(hoja, fila, block, mark);
  });

  // Si no hay requests válidas, terminar
  if (requests.length === 0) {
    logDebugMessage(`processRowsInParallel_: sin requests válidas. Errores locales escritos. (${nowStr})`);
    return;
  }

  // Función que procesa un bloque de requests (con reintentos por bloque)
  const processBatch = (batchRequests, batchMeta) => {
    let attempts = 0;
    let pendingReqs = batchRequests;
    let pendingMeta = batchMeta;

    while (attempts < CONFIG.MAX_RETRIES && pendingReqs.length > 0) {
      const responses = UrlFetchApp.fetchAll(pendingReqs);
      const nextPendingReqs = [];
      const nextPendingMeta = [];

      responses.forEach((res, idx) => {
        const { fila } = pendingMeta[idx];
        const code = res.getResponseCode();
        const responseText = res.getContentText();
        logDebugMessage(`Fila ${fila}: respuesta paralelo HTTP ${code} | URL=${pendingReqs[idx].url} | Body=${responseText}`);

        if (code === 200) {
          // Parsear y escribir
          let block = ["", "", "", "", "", "", ""];
          let mark = "", status = "Listo";
          try {
            const data = JSON.parse(responseText);
            if (data && data.length) {
              const op = data[0] || {};
              const lastPrice = (op.lastPrice != null) ? op.lastPrice : "N/A";
              const impliedVolatility = (op.impliedVolatility != null) ? op.impliedVolatility : "N/A";
              const bid = (op.bid != null) ? op.bid : "N/A";
              const openInterest = (op.openInterest != null) ? op.openInterest : "N/A";
              const fairValue = (op.fairValue != null) ? op.fairValue : "N/A";
              const nextReport = (op.nextReport != null) ? op.nextReport : "N/A";

              // Bloque 10..16
              block = [
                lastPrice,
                impliedVolatility,
                bid,
                openInterest,
                status,      // col 14
                nextReport,  // col 15
                fairValue    // col 16
              ];
              mark = `${nowStr}`;
            } else {
              // Sin datos
              block = ["", "", "", "", "Error", "", ""];
              mark = "Sin datos";
            }
          } catch (e) {
            block = ["", "", "", "", "Error", "", ""];
            mark = "Error en JSON";
          }
          writeRowResults_(hoja, fila, block, mark);
        } else {
          // Error HTTP: reintentar más tarde si hay intentos restantes
          nextPendingReqs.push(pendingReqs[idx]);
          nextPendingMeta.push(pendingMeta[idx]);
        }
      });

      if (nextPendingReqs.length === 0) {
        break; // todos resueltos
      }

      attempts++;
      if (attempts < CONFIG.MAX_RETRIES) {
        // Espera con backoff por bloque
        const delay = CONFIG.RETRY_DELAY_MS * Math.pow(2, attempts - 1);
        logDebugMessage(`Bloque con ${nextPendingReqs.length} pendientes. Reintento #${attempts + 1} en ${delay} ms`);
        Utilities.sleep(delay);
      } else {
        // Marcar los que quedaron con error API
        nextPendingMeta.forEach(({ fila }) => {
          const block = ["", "", "", "", "Error", "", ""];
          const mark = "Error API";
          writeRowResults_(hoja, fila, block, mark);
        });
      }

      pendingReqs = nextPendingReqs;
      pendingMeta = nextPendingMeta;
    }
  };

  // Procesar en lotes paralelos controlados
  for (let i = 0; i < requests.length; i += CONFIG.PARALLEL_BATCH_SIZE) {
    const batchRequests = requests.slice(i, i + CONFIG.PARALLEL_BATCH_SIZE);
    const batchMeta = meta.slice(i, i + CONFIG.PARALLEL_BATCH_SIZE);
    processBatch(batchRequests, batchMeta);
  }

  logDebugMessage(`processRowsInParallel_: procesadas ${requests.length} requests válidas (${nowStr}).`);
}

/**
 * Función para procesar una fila (modo secuencial, se mantiene por compatibilidad)
 */
function procesarFila(filaNumero) {
  const hoja = SpreadsheetApp.getActiveSpreadsheet().getActiveSheet();
  hoja.getRange(filaNumero, CONFIG.STATUS).setValue("Conectando a bully.lio.red");
  logDebugMessage(`Fila ${filaNumero}: Conectando a bully.lio.red`);

  // Obtener los datos de las columnas B, C, D, E
  const data = hoja.getRange(filaNumero, 2, 1, 4).getValues()[0];
  const [expiration_date, symbol, type, strike] = data;

  logDebugMessage(`Fila ${filaNumero}: expiration_date=${expiration_date}, symbol=${symbol}, type=${type}, strike=${strike}`);

  // Validar si la fila está completamente vacía
  if (!expiration_date && !symbol && !type && !strike) {
    logDebugMessage(`Fila ${filaNumero}: Fila vacía, deteniendo...`);
    return;
  }

  // Validar que todos los campos estén completos
  if (!symbol || !type || !expiration_date || !strike) {
    const block = ["", "", "", "", "Error", "", ""];
    writeRowResults_(hoja, filaNumero, block, "Datos incompletos");
    logDebugMessage(`Fila ${filaNumero}: Datos incompletos.`);
    return;
  }

  // Validar el tipo de opción
  const tipo = String(type).toLowerCase();
  if (tipo !== 'c' && tipo !== 'p') {
    const block = ["", "", "", "", "Error", "", ""];
    writeRowResults_(hoja, filaNumero, block, "Tipo inválido");
    logDebugMessage(`Fila ${filaNumero}: Tipo inválido.`);
    return;
  }

  // Formatear la fecha para la API
  const fechaFormateada = formatDateToAPI(expiration_date);
  logDebugMessage(`Fila ${filaNumero}: fechaFormateada=${fechaFormateada}`);
  if (fechaFormateada === "Invalid Date") {
    const block = ["", "", "", "", "Error", "", ""];
    writeRowResults_(hoja, filaNumero, block, "Fecha inválida");
    logDebugMessage(`Fila ${filaNumero}: Fecha inválida.`);
    return;
  }

  // Validar y formatear el strike
  const strikeNumber = parseFloat(strike);
  logDebugMessage(`Fila ${filaNumero}: strikeNumber=${strikeNumber}`);
  if (isNaN(strikeNumber)) {
    const block = ["", "", "", "", "Error", "", ""];
    writeRowResults_(hoja, filaNumero, block, "Strike inválido");
    logDebugMessage(`Fila ${filaNumero}: Strike inválido.`);
    return;
  }

  const strikeFormateado = strikeNumber.toFixed(2);
  const url = `https://api.bully.lio.red/options?symbol=${encodeURIComponent(symbol)}&type=${encodeURIComponent(type)}&expiration_date=${encodeURIComponent(fechaFormateada)}&strike=${encodeURIComponent(strikeFormateado)}`;

  logDebugMessage(`Fila ${filaNumero}: URL=${url}`);

  // Intentar obtener datos de la API con reintentos
  for (let intento = 0; intento < CONFIG.MAX_RETRIES; intento++) {
    try {
      const respuesta = UrlFetchApp.fetch(url, { muteHttpExceptions: true });
      const codigoRespuesta = respuesta.getResponseCode();
      const contenido = respuesta.getContentText();

      logDebugMessage(`Fila ${filaNumero}: Código de respuesta API=${codigoRespuesta}`);
      logDebugMessage(`Fila ${filaNumero}: Contenido de respuesta API=${contenido}`);

      if (codigoRespuesta !== 200) {
        const block = ["", "", "", "", "Error", "", ""];
        writeRowResults_(hoja, filaNumero, block, "Error API");
        logDebugMessage(`Fila ${filaNumero}: Error en la API.`);
        return;
      }

      let datos;
      try {
        datos = JSON.parse(contenido);
      } catch (jsonError) {
        const block = ["", "", "", "", "Error", "", ""];
        writeRowResults_(hoja, filaNumero, block, "Error en JSON");
        logDebugMessage(`Fila ${filaNumero}: Error al parsear JSON: ${jsonError}`);
        return;
      }

      if (!datos || datos.length === 0) {
        const block = ["", "", "", "", "Error", "", ""];
        writeRowResults_(hoja, filaNumero, block, "Sin datos");
        logDebugMessage(`Fila ${filaNumero}: Sin datos en la respuesta de la API.`);
        return;
      }

      const opcion = datos[0];
      const lastPrice = (opcion.lastPrice != null) ? opcion.lastPrice : "N/A";
      const impliedVolatility = (opcion.impliedVolatility != null) ? opcion.impliedVolatility : "N/A";
      const bid = (opcion.bid != null) ? opcion.bid : "N/A";
      const openInterest = (opcion.openInterest != null) ? opcion.openInterest : "N/A";
      const fairValue = (opcion.fairValue != null) ? opcion.fairValue : "N/A";
      const nextReport = (opcion.nextReport != null) ? opcion.nextReport : "N/A";

      const fechaHoraActual = new Date();
      const fechaHoraFormateada = Utilities.formatDate(fechaHoraActual, Session.getScriptTimeZone(), "HH:mm:ss dd/MM/yyyy");

      // Bloque 10..16
      const block = [
        lastPrice,
        impliedVolatility,
        bid,
        openInterest,
        "Listo",      // STATUS en col 14
        nextReport,   // col 15
        fairValue     // col 16
      ];

      writeRowResults_(hoja, filaNumero, block, `Actualizado: ${fechaHoraFormateada}`);
      logDebugMessage(`Fila ${filaNumero}: Actualización exitosa.`);
      return;
    } catch (error) {
      logDebugMessage(`Fila ${filaNumero}: Error en intento ${intento + 1}: ${error}`);
      if (intento < CONFIG.MAX_RETRIES - 1) {
        const delay = CONFIG.RETRY_DELAY_MS * Math.pow(2, intento);
        logDebugMessage(`Fila ${filaNumero}: Reintentando en ${delay} ms`);
        Utilities.sleep(delay);
      } else {
        const block = ["", "", "", "", "Error", "", ""];
        writeRowResults_(hoja, filaNumero, block, "Error Script");
        logDebugMessage(`Fila ${filaNumero}: Error final después de ${CONFIG.MAX_RETRIES} intentos.`);
      }
    }
  }
}

/**
 * Función principal para actualizar los precios de las opciones.
 * Procesa todas las filas con datos (ahora en paralelo por lotes).
 */
function updateOptionPrices() {
  const hoja = SpreadsheetApp.getActiveSpreadsheet().getActiveSheet();
  const ultimaFila = hoja.getLastRow();

  if (ultimaFila < 2) {
    SpreadsheetApp.getUi().alert("No hay datos para procesar.");
    return;
  }

  // Recolectar filas con algún dato en B..E para evitar filas totalmente vacías
  const values = hoja.getRange(2, 2, ultimaFila - 1, 4).getValues();
  const filas = [];
  for (let i = 0; i < values.length; i++) {
    const rowIdx = i + 2;
    const [expiration_date, symbol, type, strike] = values[i];
    if (expiration_date || symbol || type || strike) {
      filas.push(rowIdx);
    }
  }

  logDebugMessage(`Iniciando actualización en paralelo de ${filas.length} filas (hasta la ${ultimaFila}).`);

  // Procesar en paralelo por lotes
  for (let i = 0; i < filas.length; i += CONFIG.PARALLEL_BATCH_SIZE) {
    const slice = filas.slice(i, i + CONFIG.PARALLEL_BATCH_SIZE);
    processRowsInParallel_(hoja, slice);
  }

  logDebugMessage("Actualización de todas las filas completada.");
}

/**
 * Actualiza los precios de opciones para las filas seleccionadas.
 * (Ahora paraleliza requests y escribe por lotes por fila)
 */
function updateSelectedRows() {
  const hoja = SpreadsheetApp.getActiveSpreadsheet().getActiveSheet();
  const rangoLista = hoja.getActiveRangeList();

  if (!rangoLista) {
    SpreadsheetApp.getUi().alert("Seleccione al menos una celda.");
    return;
  }

  const rangos = rangoLista.getRanges();
  const filasSeleccionadas = new Set();

  rangos.forEach(rango => {
    const filaInicio = rango.getRow();
    const numFilas = rango.getNumRows();
    for (let i = 0; i < numFilas; i++) {
      const f = filaInicio + i;
      if (f >= 2) filasSeleccionadas.add(f);
    }
  });

  if (filasSeleccionadas.size === 0) {
    SpreadsheetApp.getUi().alert("Seleccione al menos una fila con datos.");
    return;
  }

  const filas = Array.from(filasSeleccionadas).sort((a, b) => a - b);

  logDebugMessage(`Iniciando actualización paralela de ${filas.length} filas seleccionadas.`);

  for (let i = 0; i < filas.length; i += CONFIG.PARALLEL_BATCH_SIZE) {
    const slice = filas.slice(i, i + CONFIG.PARALLEL_BATCH_SIZE);
    processRowsInParallel_(hoja, slice);
  }

  logDebugMessage("Actualización de filas seleccionadas completada.");
}

/**
 * Crea un menú personalizado al abrir la hoja de cálculo.
 */
function onOpen() {
  logDebugMessage("onOpen: Cargando el menú de Opciones API.");
  SpreadsheetApp.getUi().createMenu('Opciones API')
    .addItem('Actualizar Precios de Opciones', 'updateOptionPrices')
    .addItem('Actualizar Filas Seleccionadas', 'updateSelectedRows')
    .addToUi();
}

/**
 * Trigger que se ejecuta automáticamente cuando se edita la hoja de cálculo.
 * Si la edición se realiza en las columnas B, C, D o E, actualiza la fila correspondiente.
 */
function onEditTrigger(e) {
  try {
    const rangoEditado = e.range;
    const hoja = rangoEditado.getSheet();
    const columnasObjetivo = [2, 3, 4, 5]; // Columnas B, C, D, E

    // Verificar si la edición ocurrió en una de las columnas objetivo
    if (columnasObjetivo.includes(rangoEditado.getColumn())) {
      const filaEditada = rangoEditado.getRow();

      // Evitar procesar filas de encabezado o filas inválidas
      if (filaEditada < 2) return;

      logDebugMessage(`onEditTrigger: Editando la fila ${filaEditada}, columna ${rangoEditado.getColumn()}`);
      // Para ediciones puntuales mantenemos el modo secuencial clásico
      procesarFila(filaEditada);
    }
  } catch (error) {
    logDebugMessage(`Error en onEditTrigger: ${error}`);
  }
}
