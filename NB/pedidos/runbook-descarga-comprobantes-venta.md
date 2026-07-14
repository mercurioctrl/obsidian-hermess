# Descarga masiva de comprobantes de venta (PDF)

Procedimiento para bajar en lote los PDF de comprobantes de venta (facturas, notas de crédito/débito, etc.) de una empresa, tal como salen del botón "Descargar comprobante" del listado de vouchers.

Caso de referencia: bajar **todos** los comprobantes de los **primeros 4 días hábiles** de enero/febrero 2024, mayo y diciembre 2025 de **NB DISTRIBUIDORA MAYORISTA SRL** (`companyCode = 4`) → 1.461 PDFs, 0 fallos.

## Cómo funciona el link de descarga (cadena completa)

1. **Listado:** `GET /v1/vouchers?companyCode=4` → cada fila trae `voucherId` (`ID_NROFACCLI_ENC`) y `token` (`A.token`). Ver [[modulo-makesale|flujo de venta]] y la tabla `NewBytes_DBF.dbo.FP_FactWebCliEncabezado`.
2. **Front** (`pages/vouchers.vue → downloadVoucher`) arma la URL del SPA de comprobantes:
   - NB (comp ≠ 11): `https://comprobantes.lio.red/voucher/F/{voucherId}/{token}`
   - Laset/UY (comp = 11): `https://comprobantes.lio.red/voucher/laset/factura/{voucherId}/{token}`
   - La ruta **`/F/` es genérica por id**: sirve para facturas, notas de crédito, débito, exportación, etc. (el botón del front usa siempre `F` sin mirar el tipo). Verificado con NC → devuelve `tipoComprobante = NOTA DE CREDITO`.
3. **⚠️ Gotcha clave — no hay PDF server-side.** `comprobantes.lio.red/voucher/F/...` es un **SPA Nuxt** que pide los datos JSON a la API `https://ms-comprobantes.lio.red/v2/F/{id}/{token}` (llamada `$axios.get("F/"...)`) y **arma el PDF en el navegador con jsPDF**. Bajar la URL con `curl` devuelve el HTML del SPA (~3 KB), NO el PDF. Para obtener el PDF real hay que **renderizar con un navegador headless** e interceptar la descarga.

## Selección de comprobantes (SQL directo)

Consultar la DB directamente (container `api-rest-pedidos-apirest-laravel`) replica el filtro base del endpoint:

```sql
FROM NewBytes_DBF.dbo.FP_FactWebCliEncabezado A
LEFT JOIN NewBytes_DBF.dbo.clientes ON A.ccodcli = clientes.ccodcli
WHERE LANULADA = 0 AND A.CAE IS NOT NULL AND A.NCNOTOCASALDONISTOCK IS NULL
  AND clientes.CODEMP = 4        -- companyCode
```

- **Empresa:** `clientes.CODEMP` (= `companyCode`). 4 = NB DISTRIBUIDORA MAYORISTA SRL. Ver [[relacion-companycode]].
- **Fecha:** `DFECFAC`. Para "primeros N días" → `DATEPART(day, DFECFAC) <= 10`. Día hábil ≈ Mon–Fri **con actividad** (usar `COUNT(*)>0` como proxy salta feriados sin listar el calendario; ej. mayo 2025: 1 = feriado, 2–4 finde/puente → primeros hábiles = 5,6,7,8).
- **Moneda:** `A.CCODDIV` (`DOL` / `PSO`). En NB la mayoría son DOL.
- **Token:** filtrar `A.token IS NOT NULL` (sin token no se puede descargar).
- **Tipo:** `A.NTIPODOCU` + `FP_TiposDocumentosCobro.Descripcion` (1=Factura, 2=NC, 3=ND, 4=Fact. Export., 8=FCE MiPyME).

Volcar el resultado a un manifiesto JSON (`voucherId, token, day, total, cur, client, serie, branch, num, ym, docType`) para alimentar el descargador.

## Descarga real — Chrome headless + puppeteer-core

Instalar `puppeteer-core` (usa el `google-chrome` del sistema, `/usr/bin/google-chrome`):

```bash
mkdir -p /tmp/vdl && cd /tmp/vdl && npm init -y && npm install puppeteer-core@21
```

El script recorre el manifiesto y, por cada voucher, hace `page.goto(url)` y **captura la descarga que dispara jsPDF**. Claves aprendidas:

- **Concurrencia (6 en paralelo):** ~1.461 PDFs en ~7 min (vs ~1 h secuencial).
- **`Page.setDownloadBehavior` es efectivamente global** → con varios workers el último pisa el `downloadPath` de los demás y se pierden descargas. **Solución:** un único `Browser.setDownloadBehavior({behavior:'allowAndName', eventsEnabled:true})` a un dir compartido (los archivos se nombran por `guid`), y **correlacionar cada descarga con su worker por `frameId`**:
  - `Browser.downloadWillBegin` → `{guid, frameId}` (frameId estable por page, se obtiene con `Page.getFrameTree`).
  - `Browser.downloadProgress` → `{guid, state}`; al `completed` mover `SHARED/{guid}` → destino.
- **Flags anti-throttling** (por las dudas, aunque el fix real es el de arriba): `--disable-background-timer-throttling --disable-backgrounding-occluded-windows --disable-renderer-backgrounding`.
- **Reintentos:** hasta 3 por voucher; `waitUntil: 'networkidle2'`, timeout 45 s para el inicio de descarga.
- **Idempotente:** si el archivo destino ya existe (>1 KB) se saltea → se puede re-correr para completar fallidos.

Script de referencia usado: `/tmp/vdl/download_days.js` (efímero, en `/tmp`).

## Verificación

```bash
# cantidad por mes
find "<out>" -name '*.pdf' | wc -l           # debe igualar el nº de filas del manifiesto (sin colisiones)
# integridad: todos empiezan con %PDF
find "<out>" -name '*.pdf' -exec sh -c 'h=$(head -c4 "$1"); [ "$h" != "%PDF" ] && echo BAD $1' _ {} \;
# ninguno vacío/trunco
find "<out>" -name '*.pdf' -size -2k
```

Nombre de archivo sugerido (evita colisiones — `serie-sucursal-nº` es único por comprobante):
`{fecha}__{tipo}__{serie}-{sucursal}-{num}__{moneda}__{cliente}.pdf`

## Resultado del caso de referencia (2026-07-14)

| Mes | Días hábiles | Comprobantes |
|---|---|---|
| 2024-01 | 02, 03, 04, 05 | 228 |
| 2024-02 | 01, 02, 05, 06 | 244 |
| 2025-05 | 05, 06, 07, 08 | 579 |
| 2025-12 | 01, 02, 03, 04 | 410 |
| **Total** | | **1.461** |

Por tipo: 1.335 facturas, 116 NC, 4 fact. exportación, 3 ND, 3 FCE. Salida en `/var/www/nb/pedidos/comprobantes de venta/{YYYY-MM}/` + `_manifiesto.json`. 0 fallos, todos PDF válidos, ~112 MB.

## Ver también

- [[relacion-companycode]] — qué es `companyCode`/`CODEMP` y cómo se hereda por tabla
- [[contexto#Empresas activas (FP_Empresas)]] — mapa de las 11 empresas
- [[feature-descarga-listado-xlsx]] — otra descarga en lote (listados a xlsx, esa sí server-side)
