/**
 * Configuracion - OPTIMIZADA
 * DEBUG: 0 para maxima velocidad (no escribe en hoja Debug)
 * MAX_RETRIES: 2 para reducir esperas en errores
 * DISPLAY_BATCH_SIZE: 5 para menos flush()
 */
const CONFIG = {
  MAX_RETRIES: 2,
  RETRY_DELAY_MS: 1000,
  MARK_COLUMN: 27,
  STATUS: 14,
  FAIRVALUE_COLUMN: 16,
  NEXTREPORT_COLUMN: 15,
  DISPLAY_BATCH_SIZE: 5,
  DEBUG: 0,
};

/**
 * Funcion para registrar mensajes de debug en la hoja "Debug"
 */
function logDebugMessage(message) {
  try {
    if (CONFIG.DEBUG !== 1) return;
    var hojaDebug = SpreadsheetApp.getActiveSpreadsheet().getSheetByName("Debug");
    var fechaHora = new Date();
    hojaDebug.appendRow([Utilities.formatDate(fechaHora, Session.getScriptTimeZone(), "HH:mm:ss dd/MM/yyyy"), message]);
  } catch (err) {
    if (CONFIG.DEBUG === 1) {
      console && console.log && console.log('Log error:', err);
    }
  }
}

/**
 * Formatea la fecha al formato requerido por la API (dd-mm-yyyy).
 */
function formatDateToAPI(fecha) {
  var fechaObj = new Date(fecha);
  if (isNaN(fechaObj.getTime())) return "Invalid Date";
  var dia = ('0' + fechaObj.getDate()).slice(-2);
  var mes = ('0' + (fechaObj.getMonth() + 1)).slice(-2);
  var anio = fechaObj.getFullYear();
  return dia + '-' + mes + '-' + anio;
}

/**
 * Construye la URL de la API a partir de datos ya leidos (sin leer de la hoja).
 * Recibe el array [expiration_date, symbol, type, strike].
 */
function buildRequestFromData_(filaNumero, rowData) {
  var expiration_date = rowData[0];
  var symbol = rowData[1];
  var type = rowData[2];
  var strike = rowData[3];

  if (!expiration_date && !symbol && !type && !strike) {
    return { ok: false, fila: filaNumero, errorMark: "Fila vacia" };
  }

  if (!symbol || !type || !expiration_date || !strike) {
    return { ok: false, fila: filaNumero, errorMark: "Datos incompletos" };
  }

  var tipo = String(type).toLowerCase();
  if (tipo !== 'c' && tipo !== 'p') {
    return { ok: false, fila: filaNumero, errorMark: "Tipo invalido" };
  }

  var fechaFormateada = formatDateToAPI(expiration_date);
  if (fechaFormateada === "Invalid Date") {
    return { ok: false, fila: filaNumero, errorMark: "Fecha invalida" };
  }

  var strikeNumber = parseFloat(strike);
  if (isNaN(strikeNumber)) {
    return { ok: false, fila: filaNumero, errorMark: "Strike invalido" };
  }
  var strikeFormateado = strikeNumber.toFixed(2);

  var url = 'https://api.bully.lio.red/options?symbol=' + encodeURIComponent(symbol) + '&type=' + encodeURIComponent(type) + '&expiration_date=' + encodeURIComponent(fechaFormateada) + '&strike=' + encodeURIComponent(strikeFormateado);

  return { ok: true, fila: filaNumero, url: url };
}

/**
 * Aplica en hoja los resultados de una fila:
 * - Bloque contiguo columnas 10..16 (7 columnas)
 * - Marca en columna CONFIG.MARK_COLUMN
 */
function writeRowResults_(hoja, fila, rowBlockValues, markText) {
  hoja.getRange(fila, 10, 1, 7).setValues([rowBlockValues]);
  hoja.getRange(fila, CONFIG.MARK_COLUMN).setValue(markText);
}

/**
 * Convierte numero de columna a letra(s) para notacion A1.
 * Ej: 1 -> A, 14 -> N, 27 -> AA
 */
function columnToLetter_(col) {
  var letra = '';
  while (col > 0) {
    var mod = (col - 1) % 26;
    letra = String.fromCharCode(65 + mod) + letra;
    col = Math.floor((col - 1) / 26);
  }
  return letra;
}

/**
 * Procesa filas UNA POR UNA con optimizaciones:
 * 1. Pre-lectura de datos en un solo getValues()
 * 2. Semaforo: marca todas como "En cola" al inicio (batch)
 * 3. Fetch individual con escritura inmediata
 * 4. Flush cada DISPLAY_BATCH_SIZE filas
 */
function processRowsOneByOne_(hoja, filasArray) {
  var nowStr = Utilities.formatDate(new Date(), Session.getScriptTimeZone(), "HH:mm:ss dd/MM/yyyy");

  // --- OPTIMIZACION 1: Pre-leer todos los datos en una sola llamada ---
  var minFila = filasArray[0];
  var maxFila = filasArray[filasArray.length - 1];
  var allData = hoja.getRange(minFila, 2, maxFila - minFila + 1, 4).getValues();

  // --- OPTIMIZACION 2: Semaforo - marcar todas como "En cola" en un batch ---
  var statusLetter = columnToLetter_(CONFIG.STATUS);
  var statusRanges = [];
  for (var f = 0; f < filasArray.length; f++) {
    statusRanges.push(statusLetter + filasArray[f]);
  }
  hoja.getRangeList(statusRanges).setValue("En cola");
  SpreadsheetApp.flush();

  // --- PROCESO UNO POR UNO ---
  var writtenCount = 0;

  for (var f = 0; f < filasArray.length; f++) {
    var fila = filasArray[f];
    var dataIndex = fila - minFila;
    var rowData = allData[dataIndex];

    var built = buildRequestFromData_(fila, rowData);
    if (!built.ok) {
      writeRowResults_(hoja, fila, ["", "", "", "", "Error", "", ""], built.errorMark || "Error");
      writtenCount++;
      if (writtenCount % CONFIG.DISPLAY_BATCH_SIZE === 0) {
        SpreadsheetApp.flush();
      }
      continue;
    }

    logDebugMessage("Fila " + fila + ": fetch -> " + built.url);

    // Fetch individual con reintentos
    var success = false;
    for (var attempt = 0; attempt < CONFIG.MAX_RETRIES; attempt++) {
      try {
        var res = UrlFetchApp.fetch(built.url, { muteHttpExceptions: true });
        var code = res.getResponseCode();
        var responseText = res.getContentText();

        if (code === 200) {
          var block = ["", "", "", "", "", "", ""];
          var mark = "";
          try {
            var apiData = JSON.parse(responseText);
            if (apiData && apiData.length) {
              var op = apiData[0] || {};
              var lastPrice = (op.lastPrice != null) ? op.lastPrice : "N/A";
              var impliedVolatility = (op.impliedVolatility != null) ? op.impliedVolatility : "N/A";
              var bid = (op.bid != null) ? op.bid : "N/A";
              var openInterest = (op.openInterest != null) ? op.openInterest : "N/A";
              var fairValue = (op.fairValue != null) ? op.fairValue : "N/A";
              var nextReport = (op.nextReport != null) ? op.nextReport : "N/A";

              block = [lastPrice, impliedVolatility, bid, openInterest, "Listo", nextReport, fairValue];
              mark = nowStr;
            } else {
              block = ["", "", "", "", "Sin datos", "", ""];
              mark = "Sin datos";
            }
          } catch (e) {
            block = ["", "", "", "", "Error JSON", "", ""];
            mark = "Error en JSON";
          }

          writeRowResults_(hoja, fila, block, mark);
          writtenCount++;
          if (writtenCount % CONFIG.DISPLAY_BATCH_SIZE === 0) {
            SpreadsheetApp.flush();
            logDebugMessage("flush() visual despues de " + writtenCount + " filas");
          }

          success = true;
          break;
        } else {
          if (attempt < CONFIG.MAX_RETRIES - 1) {
            var delay = CONFIG.RETRY_DELAY_MS * Math.pow(2, attempt);
            logDebugMessage("Fila " + fila + ": HTTP " + code + ", reintento en " + delay + "ms");
            Utilities.sleep(delay);
          }
        }
      } catch (err) {
        logDebugMessage("Fila " + fila + ": Error en intento " + (attempt + 1) + ": " + err);
        if (attempt < CONFIG.MAX_RETRIES - 1) {
          var delayErr = CONFIG.RETRY_DELAY_MS * Math.pow(2, attempt);
          Utilities.sleep(delayErr);
        }
      }
    }

    if (!success) {
      writeRowResults_(hoja, fila, ["", "", "", "", "Error API", "", ""], "Error API");
      writtenCount++;
      if (writtenCount % CONFIG.DISPLAY_BATCH_SIZE === 0) {
        SpreadsheetApp.flush();
      }
    }
  }

  // Flush final
  SpreadsheetApp.flush();
  logDebugMessage("processRowsOneByOne_: procesadas " + filasArray.length + " filas.");
}

/**
 * Funcion para procesar una sola fila (usada por onEditTrigger).
 */
function procesarFila(filaNumero) {
  var hoja = SpreadsheetApp.getActiveSpreadsheet().getActiveSheet();
  hoja.getRange(filaNumero, CONFIG.STATUS).setValue("Procesando...");

  var rowData = hoja.getRange(filaNumero, 2, 1, 4).getValues()[0];
  var built = buildRequestFromData_(filaNumero, rowData);

  if (!built.ok) {
    writeRowResults_(hoja, filaNumero, ["", "", "", "", "Error", "", ""], built.errorMark || "Error");
    logDebugMessage("Fila " + filaNumero + ": " + (built.errorMark || "Error"));
    return;
  }

  logDebugMessage("Fila " + filaNumero + ": URL=" + built.url);

  for (var intento = 0; intento < CONFIG.MAX_RETRIES; intento++) {
    try {
      var respuesta = UrlFetchApp.fetch(built.url, { muteHttpExceptions: true });
      var codigoRespuesta = respuesta.getResponseCode();
      var contenido = respuesta.getContentText();

      if (codigoRespuesta !== 200) {
        if (intento < CONFIG.MAX_RETRIES - 1) {
          var delayH = CONFIG.RETRY_DELAY_MS * Math.pow(2, intento);
          Utilities.sleep(delayH);
          continue;
        }
        writeRowResults_(hoja, filaNumero, ["", "", "", "", "Error API", "", ""], "Error API");
        logDebugMessage("Fila " + filaNumero + ": Error API HTTP " + codigoRespuesta);
        return;
      }

      var datos;
      try {
        datos = JSON.parse(contenido);
      } catch (jsonError) {
        writeRowResults_(hoja, filaNumero, ["", "", "", "", "Error JSON", "", ""], "Error en JSON");
        logDebugMessage("Fila " + filaNumero + ": Error al parsear JSON: " + jsonError);
        return;
      }

      if (!datos || datos.length === 0) {
        writeRowResults_(hoja, filaNumero, ["", "", "", "", "Sin datos", "", ""], "Sin datos");
        logDebugMessage("Fila " + filaNumero + ": Sin datos.");
        return;
      }

      var opcion = datos[0];
      var lastPrice = (opcion.lastPrice != null) ? opcion.lastPrice : "N/A";
      var impliedVolatility = (opcion.impliedVolatility != null) ? opcion.impliedVolatility : "N/A";
      var bid = (opcion.bid != null) ? opcion.bid : "N/A";
      var openInterest = (opcion.openInterest != null) ? opcion.openInterest : "N/A";
      var fairValue = (opcion.fairValue != null) ? opcion.fairValue : "N/A";
      var nextReport = (opcion.nextReport != null) ? opcion.nextReport : "N/A";

      var fechaHoraActual = new Date();
      var fechaHoraFormateada = Utilities.formatDate(fechaHoraActual, Session.getScriptTimeZone(), "HH:mm:ss dd/MM/yyyy");

      var block = [lastPrice, impliedVolatility, bid, openInterest, "Listo", nextReport, fairValue];
      writeRowResults_(hoja, filaNumero, block, "Actualizado: " + fechaHoraFormateada);
      logDebugMessage("Fila " + filaNumero + ": Actualizacion exitosa.");
      return;
    } catch (error) {
      logDebugMessage("Fila " + filaNumero + ": Error en intento " + (intento + 1) + ": " + error);
      if (intento < CONFIG.MAX_RETRIES - 1) {
        var delayR = CONFIG.RETRY_DELAY_MS * Math.pow(2, intento);
        Utilities.sleep(delayR);
      } else {
        writeRowResults_(hoja, filaNumero, ["", "", "", "", "Error", "", ""], "Error Script");
        logDebugMessage("Fila " + filaNumero + ": Error final despues de " + CONFIG.MAX_RETRIES + " intentos.");
      }
    }
  }
}

/**
 * Funcion principal para actualizar los precios de las opciones.
 */
function updateOptionPrices() {
  var hoja = SpreadsheetApp.getActiveSpreadsheet().getActiveSheet();
  var ultimaFila = hoja.getLastRow();

  if (ultimaFila < 2) {
    SpreadsheetApp.getUi().alert("No hay datos para procesar.");
    return;
  }

  var values = hoja.getRange(2, 2, ultimaFila - 1, 4).getValues();
  var filas = [];
  for (var i = 0; i < values.length; i++) {
    var rowIdx = i + 2;
    if (values[i][0] || values[i][1] || values[i][2] || values[i][3]) {
      filas.push(rowIdx);
    }
  }

  logDebugMessage("Iniciando actualizacion de " + filas.length + " filas.");

  processRowsOneByOne_(hoja, filas);

  logDebugMessage("Actualizacion de todas las filas completada.");
}

/**
 * Actualiza los precios de opciones para las filas seleccionadas.
 */
function updateSelectedRows() {
  var hoja = SpreadsheetApp.getActiveSpreadsheet().getActiveSheet();
  var rangoLista = hoja.getActiveRangeList();

  if (!rangoLista) {
    SpreadsheetApp.getUi().alert("Seleccione al menos una celda.");
    return;
  }

  var rangos = rangoLista.getRanges();
  var filasSet = {};

  for (var r = 0; r < rangos.length; r++) {
    var filaInicio = rangos[r].getRow();
    var numFilas = rangos[r].getNumRows();
    for (var i = 0; i < numFilas; i++) {
      var fNum = filaInicio + i;
      if (fNum >= 2) filasSet[fNum] = true;
    }
  }

  var filas = Object.keys(filasSet).map(Number).sort(function(a, b) { return a - b; });

  if (filas.length === 0) {
    SpreadsheetApp.getUi().alert("Seleccione al menos una fila con datos.");
    return;
  }

  logDebugMessage("Iniciando actualizacion de " + filas.length + " filas seleccionadas.");

  processRowsOneByOne_(hoja, filas);

  logDebugMessage("Actualizacion de filas seleccionadas completada.");
}

/**
 * Crea un menu personalizado al abrir la hoja de calculo.
 */
function onOpen() {
  logDebugMessage("onOpen: Cargando el menu de Opciones API.");
  SpreadsheetApp.getUi().createMenu('Opciones API')
    .addItem('Actualizar Precios de Opciones', 'updateOptionPrices')
    .addItem('Actualizar Filas Seleccionadas', 'updateSelectedRows')
    .addToUi();
}

/**
 * Trigger que se ejecuta automaticamente cuando se edita la hoja de calculo.
 */
function onEditTrigger(e) {
  try {
    var rangoEditado = e.range;
    var hoja = rangoEditado.getSheet();
    var columnasObjetivo = [2, 3, 4, 5];

    if (columnasObjetivo.indexOf(rangoEditado.getColumn()) !== -1) {
      var filaEditada = rangoEditado.getRow();
      if (filaEditada < 2) return;

      logDebugMessage("onEditTrigger: Editando la fila " + filaEditada + ", columna " + rangoEditado.getColumn());
      procesarFila(filaEditada);
    }
  } catch (error) {
    logDebugMessage("Error en onEditTrigger: " + error);
  }
}
