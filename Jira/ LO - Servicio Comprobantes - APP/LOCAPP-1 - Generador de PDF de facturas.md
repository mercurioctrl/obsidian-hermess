---
jira_key: "LOCAPP-1"
aliases: ["LOCAPP-1"]
summary: "Generador de PDF de facturas"
status: "Finalizada"
type: "Historia"
priority: "Medium"
assignee: "Marbe Moreno"
reporter: "Catriel Mercurio"
created: "2021-11-24 10:20"
updated: "2022-01-04 13:47"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/LOCAPP-1"
---

# LOCAPP-1: Generador de PDF de facturas

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Historia |
| Prioridad | Medium |
| Asignado | Marbe Moreno |
| Reportado por | Catriel Mercurio |
| Creado | 2021-11-24 10:20 |
| Actualizado | 2022-01-04 13:47 |
| Etiquetas | ninguna |
| Jira | [LOCAPP-1](https://bluinc.atlassian.net/browse/LOCAPP-1) |

## Relaciones

- **Subtarea:** [[LOCAPP-3]] Qr: Se busca la forma de generar el qr, en principio se pueden hacer pruebas con cualquier info.
- **Subtarea:** [[LOCAPP-2]] Planteo inicial: Se debe construir el generador de PDF en si mismo, probar el paginado y la separacion de areas en general. Los rectangulos contenedores de las distintas areas.

## Descripcion

En base a un objeto que contiene toda la informacion del comprobante, debe generarse un PDF con JS del lado del cliente inspirado en ejemplo.

[adjunto]
#### Especificación Técnica:

El código QR deberá codificar el siguiente texto:

**{URL}?p={DATOS_CMP_BASE_64}**

##### Donde:

{URL} = https://www.afip.gob.ar/fe/ qr/

{DATOS_CMP_BASE_64} = JSON con datos del comprobante codificado en Base64

##### La especificación del JSON con los datos del comprobante es la siguiente (versión 1):

| Campo | Tipo | Descripción | Valor ejemplo |
| --- | --- | --- | --- |
| ver | Numérico 1 digito | OBLIGATORIO – versión del formato de los datos del comprobante | 1 |
| fecha | full-date ([RFC3339](https://xml2rfc.ietf.org/public/rfc/html/rfc3339.html#anchor14)) | OBLIGATORIO – Fecha de emisión del comprobante | "2020-10-13" |
| cuit | Numérico 11 dígitos | OBLIGATORIO – Cuit del Emisor del comprobante | 30000000007 |
| ptoVta | Numérico hasta 5 digitos | OBLIGATORIO – Punto de venta utilizado para emitir el comprobante | 10 |
| tipoCmp | Numérico hasta 3 dígitos | OBLIGATORIO – tipo de comprobante (según [Tablas del sistema](https://www.afip.gob.ar/fe/ayuda/tablas.asp) ) | 1 |
| nroCmp | Numérico hasta 8 dígitos | OBLIGATORIO – Número del comprobante | 94 |
| importe | Decimal hasta 13 enteros y 2 decimales | OBLIGATORIO – Importe Total del comprobante (en la moneda en la que fue emitido) | 12100 |
| moneda | 3 caracteres | OBLIGATORIO – Moneda del comprobante (según [Tablas del sistema](https://www.afip.gob.ar/fe/ayuda/tablas.asp) ) | "DOL" |
| ctz | Decimal hasta 13 enteros y 6 decimales | OBLIGATORIO – Cotización en pesos argentinos de la moneda utilizada (1 cuando la moneda sea pesos) | 65 |
| tipoDocRec | Numérico hasta 2 dígitos | DE CORRESPONDER – Código del Tipo de documento del receptor (según [Tablas del sistema](https://www.afip.gob.ar/fe/ayuda/tablas.asp) ) | 80 |
| nroDocRec | Numérico hasta 20 dígitos | DE CORRESPONDER – Número de documento del receptor correspondiente al tipo de documento indicado | 20000000001 |
| tipoCodAut | string | OBLIGATORIO – “A” para comprobante autorizado por CAEA, “E” para comprobante autorizado por CAE | "E" |
| codAut | Numérico 14 dígitos | OBLIGATORIO – Código de autorización otorgado por AFIP para el comprobante | 70417054367476 |

##### La especificación del JSON con los datos del comprobante es la siguiente (versión 1):




**Pie del PDF del comprobante:**

[adjunto]
**Texto codificado en el QR:**

[link](https://www.afip.gob.ar/fe/qr/?p=eyJ2ZXIiOjEsImZlY2hhIjoiMjAyMC0xMC0xMyIsImN1aXQiOjMwMDAwMDAwMDA3LCJwdG9WdGEiOjEwLCJ0aXBvQ21wIjoxLCJucm9DbXAiOjk0LCJpbXBvcnRlIjoxMjEwMCwibW9uZWRhIjoiRE9MIiwiY3R6Ijo2NSwidGlwb0RvY1JlYyI6ODAsIm5yb0RvY1JlYyI6MjAwMDAwMDAwMDEsInRpcG9Db2RBdXQiOiJFIiwiY29kQXV0Ijo3MDQxNzA1NDM2NzQ3Nn0=) 

**JSON con datos del comprobante:**

{"ver":1,"fecha":"2020-10-13","cuit":30000000007,"ptoVta":10,"tipoCmp":1,"nroCmp":94,"importe":12100,"moneda":"DOL","ctz":65,"tipoDocRec":80,"nroDocRec":20000000001,"tipoCodAut":"E","codAut":70417054367476}
