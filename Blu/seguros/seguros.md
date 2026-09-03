# Seguros

Restilizado de **certificados de cobertura de seguros** (emitidos por Barbuss Risk) al **look & feel de BLU**, sacando el logo de la aseguradora y aplicando el formato de documento del ERP.

> Fuentes en disco: `/var/www/blu/seguros/`
> Última sincronización: 2026-09-03

## Objetivo
El personal de BLU trabaja como *expositor de stand / venta* en eventos y queda cubierto por pólizas de Accidentes Personales Colectivos que toma **DIGITO BINARIO SRL**. Los certificados originales de Barbuss se rearman con identidad BLU para presentarlos a los organizadores/beneficiarios, sin el logo de la aseguradora.

## Formato usado (decisión clave)
Se replica **exactamente** el formato del documento que saca el ERP en `/api/presupuestos/{id}/preview` — el blade `pdf/presupuesto-preview.blade.php` del [[bluMiniErp]]. Estética **monocroma**:
- Logo BLU (wordmark `blu.`) en **negro**, no azul
- Labels gris en mayúsculas con tracking (`letter-spacing`)
- Tabla con `thead` de borde negro 2px, montos alineados a la derecha
- Cláusula legal en caja `obs-box` gris (mismo patrón que "Observaciones")
- Footer con datos del emisor + firmante y logo BLU desvaído (opacity 0.12)
- Botón "Descargar PDF" (html2pdf.js), idéntico al preview del ERP

Un **primer intento** con estética azul/celeste (cards, acentos `#0474F4`) fue descartado: el usuario prefirió el formato sobrio del ERP.

## Documentos generados
| Póliza | Asegurados | Particularidad | Archivos |
|--------|-----------|----------------|----------|
| **254194** | 4 (De Luca, Easdale, Oliveira, Crespo) | Cláusula NR contra NUEVAS FRONTERAS S.A | `constancia-cobertura-blu.html` / `.pdf` |
| **254339** | 2 (Cipollone, Sanchez Montiel) | Cláusula NR con **9 beneficiarios** (fideicomisos, municipio, etc.) listados con CUIT | `constancia-cobertura-254339-blu.html` / `.pdf` |

Cada uno es un HTML autónomo (SVG del logo inline, sin assets externos salvo el CDN de html2pdf) renderizado a PDF con `google-chrome-stable --headless --print-to-pdf`.

## Contenido legal (auditado contra el original)
Se conservó **todo el texto legal**; solo se quitó el **logo gráfico** de Barbuss (no las menciones de texto, que son datos legales del emisor real):
- Certificación + datos de póliza (rama, N°, productor, tomador, domicilio, vigencia)
- Asegurados con documento, actividad, coberturas y sumas aseguradas
- Cláusula de No Repetición completa
- Cláusula condicional de cobertura ("SE DEJA CONSTANCIA…")
- Advertencia al asegurado / instrumento provisorio (30 días)
- Emisor + firmante (Carolina Albornoz, Subgerente Técnico)
- Código de cláusula `W. CON CAPCNR1T` (agregado en revisión posterior)

## Pendiente / criterio
- **Firma manuscrita:** NO se reproduce la rúbrica escaneada (solo nombre + cargo en texto). Trasladar una firma ajena a un documento rediseñado es sensible; queda a decisión del usuario.
- **Validez legal:** el documento BLU es una **presentación con otro formato**; el instrumento con valor legal sigue siendo el PDF original firmado de Barbuss. Para presentaciones formales, acompañar con el original o pedir reemisión a Barbuss.

## Ver también
- [[bluMiniErp]] — origen del formato de documento (blade `presupuesto-preview`, módulo Documentos con formato BLU)
