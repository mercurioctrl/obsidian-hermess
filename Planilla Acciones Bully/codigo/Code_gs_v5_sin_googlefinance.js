/**
 * Configuracion - v5 SIN GOOGLEFINANCE
 * Los datos de stock (price, changePct, low52, high52, beta) ahora vienen de la API.
 * Las columnas A, G, R, S, T ya no necesitan formulas GOOGLEFINANCE.
 */
const CONFIG = {
  MAX_RETRIES: 2,
  RETRY_DELAY_MS: 1000,
  MARK_COLUMN: 27,
  STATUS: 14,
  FAIRVALUE_COLUMN: 16,
  NEXTREPORT_COLUMN: 15,
  DISPLAY_BATCH_SIZE: 10,
  DEBUG: 0,
  STOCK_PRICE_COL: 1,
  CHANGE_PCT_COL: 7,
  LOW52_COL: 18,
  HIGH52_COL: 19,
  BETA_COL: 20,
};

const FRASES_COLA = [
  "\u23F3 Casi lo tengo...",
  "\u23F3 Ya casi esta...",
  "\u23F3 Un momentito...",
  "\u23F3 Buscando datos...",
  "\u23F3 Consultando API...",
  "\u23F3 Dame un segundo...",
  "\u23F3 En camino...",
  "\u23F3 Preparando info...",
  "\u23F3 Ya llega...",
  "\u23F3 Procesando...",
];

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
 * - Bloque contiguo columnas 10..16 (7 columnas): lastPrice, IV, bid, OI, status, nextReport, fairValue
 * - Agrega circulo de color emoji al estado
 * - Formato de colores/fuente segun estado
 * - Alineacion: "Listo" centrado, el resto a la izquierda
 * - Marca en columna CONFIG.MARK_COLUMN
 * - Datos de stock en columnas A, G, R, S, T (reemplazan GOOGLEFINANCE)
 */
function writeRowResults_(hoja, fila, rowBlockValues, markText, stockData) {
  // Agregar circulo de color al estado
  var statusText = rowBlockValues[4];
  if (statusText === 'Listo') {
    rowBlockValues[4] = '\u2705 Listo';
  } else if (String(statusText).indexOf('Error') !== -1) {
    rowBlockValues[4] = '\u274C ' + statusText;
  } else if (statusText === 'Sin datos') {
    rowBlockValues[4] = '\u26A0\uFE0F Sin datos';
  } else if (statusText) {
    rowBlockValues[4] = '\u23F3 ' + statusText;
  }

  // Bloque principal de opciones: columnas J(10) a P(16)
  hoja.getRange(fila, 10, 1, 7).setValues([rowBlockValues]);

  // Formato de la celda de estado
  var statusCell = hoja.getRange(fila, CONFIG.STATUS);
  if (statusText === 'Listo') {
    statusCell.setFontColor('#006400').setFontWeight('bold').setFontStyle('normal').setHorizontalAlignment('center');
  } else if (String(statusText).indexOf('Error') !== -1) {
    statusCell.setFontColor('#cc0000').setFontWeight('bold').setFontStyle('normal').setHorizontalAlignment('left');
  } else {
    statusCell.setFontColor('#000000').setFontWeight('normal').setFontStyle('normal').setHorizontalAlignment('left');
  }

  // Marca de ultima actualizacion: columna AA(27)
  hoja.getRange(fila, CONFIG.MARK_COLUMN).setValue(markText);

  // Datos de stock (si vienen de la API)
  // NOTA: stockPrice (columna A) NO se escribe desde la API - se mantiene tal cual
  if (stockData) {
    if (stockData.changePct != null) {
      hoja.getRange(fila, CONFIG.CHANGE_PCT_COL).setValue(stockData.changePct);
    }
    // R, S, T en bloque contiguo (1 call en vez de 3)
    var low52Val = (stockData.low52 != null) ? stockData.low52 : '';
    var high52Val = (stockData.high52 != null) ? stockData.high52 : '';
    var betaVal = (stockData.beta != null) ? stockData.beta : '';
    if (low52Val !== '' || high52Val !== '' || betaVal !== '') {
      hoja.getRange(fila, CONFIG.LOW52_COL, 1, 3).setValues([[low52Val, high52Val, betaVal]]);
    }
  }
}

/**
 * Convierte numero de columna a letra(s) para notacion A1.
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
 * Extrae los datos de stock de la respuesta de la API.
 * Devuelve null si no hay datos de stock.
 */
function extractStockData_(op) {
  if (!op) return null;
  var hasAny = (op.stockPrice != null) || (op.changePct != null) ||
               (op.low52 != null) || (op.high52 != null) || (op.beta != null);
  if (!hasAny) return null;
  return {
    stockPrice: (op.stockPrice != null) ? op.stockPrice : null,
    changePct: (op.changePct != null) ? op.changePct : null,
    low52: (op.low52 != null) ? op.low52 : null,
    high52: (op.high52 != null) ? op.high52 : null,
    beta: (op.beta != null) ? op.beta : null
  };
}

/**
 * Procesa filas UNA POR UNA con optimizaciones:
 * 1. Pre-lectura de datos en un solo getValues()
 * 2. Semaforo: frases rotativas con formato naranja/italica
 * 3. Fetch individual con escritura inmediata
 * 4. Flush cada DISPLAY_BATCH_SIZE filas
 * 5. Escribe datos de stock de la API (reemplaza GOOGLEFINANCE)
 */
function processRowsOneByOne_(hoja, filasArray) {
  var nowStr = Utilities.formatDate(new Date(), Session.getScriptTimeZone(), "HH:mm:ss dd/MM/yyyy");

  // --- Pre-leer todos los datos en una sola llamada ---
  var minFila = filasArray[0];
  var maxFila = filasArray[filasArray.length - 1];
  var allData = hoja.getRange(minFila, 2, maxFila - minFila + 1, 4).getValues();

  // --- Semaforo: frases rotativas con formato naranja/italica ---
  var statusRanges = [];
  for (var sf = 0; sf < filasArray.length; sf++) {
    var frase = FRASES_COLA[sf % FRASES_COLA.length];
    var ref = columnToLetter_(CONFIG.STATUS) + filasArray[sf];
    hoja.getRange(ref).setValue(frase);
    statusRanges.push(ref);
  }
  var rangeList = hoja.getRangeList(statusRanges);
  rangeList.setFontColor('#CC6600');
  rangeList.setFontWeight('normal');
  rangeList.setFontStyle('italic');
  rangeList.setHorizontalAlignment('left');
  SpreadsheetApp.flush();

  // --- PROCESO UNO POR UNO ---
  var writtenCount = 0;

  for (var f = 0; f < filasArray.length; f++) {
    var fila = filasArray[f];
    var dataIndex = fila - minFila;
    var rowData = allData[dataIndex];

    var built = buildRequestFromData_(fila, rowData);
    if (!built.ok) {
      writeRowResults_(hoja, fila, ["", "", "", "", "Error", "", ""], built.errorMark || "Error", null);
      writtenCount++;
      if (writtenCount % CONFIG.DISPLAY_BATCH_SIZE === 0) {
        SpreadsheetApp.flush();
      }
      continue;
    }

    logDebugMessage("Fila " + fila + ": fetch -> " + built.url);

    var success = false;
    for (var attempt = 0; attempt < CONFIG.MAX_RETRIES; attempt++) {
      try {
        var res = UrlFetchApp.fetch(built.url, { muteHttpExceptions: true });
        var code = res.getResponseCode();
        var responseText = res.getContentText();

        if (code === 200) {
          var block = ["", "", "", "", "", "", ""];
          var mark = "";
          var stockData = null;
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

              // Extraer datos de stock si la API los provee
              stockData = extractStockData_(op);
            } else {
              block = ["", "", "", "", "Sin datos", "", ""];
              mark = "Sin datos";
            }
          } catch (e) {
            block = ["", "", "", "", "Error JSON", "", ""];
            mark = "Error en JSON";
          }

          writeRowResults_(hoja, fila, block, mark, stockData);
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
      writeRowResults_(hoja, fila, ["", "", "", "", "Error API", "", ""], "Error API", null);
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
 * Muestra frase rotativa aleatoria mientras procesa.
 */
function procesarFila(filaNumero) {
  var hoja = SpreadsheetApp.getActiveSpreadsheet().getActiveSheet();

  // Frase rotativa aleatoria con formato naranja/italica
  var randomFrase = FRASES_COLA[Math.floor(Math.random() * FRASES_COLA.length)];
  var statusCell = hoja.getRange(filaNumero, CONFIG.STATUS);
  statusCell.setValue(randomFrase).setFontColor('#CC6600').setFontWeight('normal').setFontStyle('italic').setHorizontalAlignment('left');
  SpreadsheetApp.flush();

  var rowData = hoja.getRange(filaNumero, 2, 1, 4).getValues()[0];
  var built = buildRequestFromData_(filaNumero, rowData);

  if (!built.ok) {
    writeRowResults_(hoja, filaNumero, ["", "", "", "", "Error", "", ""], built.errorMark || "Error", null);
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
        writeRowResults_(hoja, filaNumero, ["", "", "", "", "Error API", "", ""], "Error API", null);
        return;
      }

      var datos;
      try {
        datos = JSON.parse(contenido);
      } catch (jsonError) {
        writeRowResults_(hoja, filaNumero, ["", "", "", "", "Error JSON", "", ""], "Error en JSON", null);
        return;
      }

      if (!datos || datos.length === 0) {
        writeRowResults_(hoja, filaNumero, ["", "", "", "", "Sin datos", "", ""], "Sin datos", null);
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
      var stockData = extractStockData_(opcion);
      writeRowResults_(hoja, filaNumero, block, "Actualizado: " + fechaHoraFormateada, stockData);
      logDebugMessage("Fila " + filaNumero + ": Actualizacion exitosa.");
      return;
    } catch (error) {
      logDebugMessage("Fila " + filaNumero + ": Error en intento " + (intento + 1) + ": " + error);
      if (intento < CONFIG.MAX_RETRIES - 1) {
        Utilities.sleep(CONFIG.RETRY_DELAY_MS * Math.pow(2, intento));
      } else {
        writeRowResults_(hoja, filaNumero, ["", "", "", "", "Error", "", ""], "Error Script", null);
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

  if (filas.length === 0) {
    SpreadsheetApp.getUi().alert("No se encontraron filas con datos.");
    return;
  }

  logDebugMessage("Iniciando actualizacion de " + filas.length + " filas.");
  processRowsOneByOne_(hoja, filas);
  logDebugMessage("Actualizacion completada.");
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
      if (fNum >= 2) {
        filasSet[fNum] = true;
      }
    }
  }

  var filas = Object.keys(filasSet).map(Number).sort(function(a, b) { return a - b; });

  if (filas.length === 0) {
    SpreadsheetApp.getUi().alert("Seleccione al menos una fila con datos (fila 2 en adelante).");
    return;
  }

  logDebugMessage("Actualizando " + filas.length + " filas seleccionadas.");
  processRowsOneByOne_(hoja, filas);
}

/**
 * Crea un menu personalizado al abrir la hoja de calculo.
 */
function onOpen() {
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
    var columnasObjetivo = [2, 3, 4, 5, 25];

    if (columnasObjetivo.indexOf(rangoEditado.getColumn()) !== -1) {
      var filaEditada = rangoEditado.getRow();
      if (filaEditada < 2) return;
      procesarFila(filaEditada);
    }
  } catch (error) {
    logDebugMessage("Error en onEditTrigger: " + error);
  }
}
