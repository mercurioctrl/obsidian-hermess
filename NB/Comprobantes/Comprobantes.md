# Comprobantes

Sistema de comprobantes (facturación, remitos, recibos, certificados) para [[NB]].

Compuesto por **dos repositorios independientes** que trabajan juntos:

- **`microservicio-comprobantes-v2`** — API REST en PHP 8 / Slim 4 que lee datos de SQL Server y los expone como JSON.
- **`servicio-compobante-pdf-web-app`** — Web app Nuxt 2 (SSR) que consume la API y renderiza vouchers como HTML imprimible y PDF descargable.

La app Nuxt es el **cliente** de la API PHP. Cada ruta de voucher en Nuxt tiene un endpoint espejo en la API.

## Ubicación local

`/Users/hermess/www/comprobantes/`

- Repo API: `git@github.com:LibreOpcion/microservicio-comprobantes-v2.git` — branch activa: `Development`
- Repo Web: `git@github.com:LibreOpcion/servicio-compobante-pdf-web-app.git` — branch activa: `development`

## Tipos de comprobante

- **F / FUy** — Facturas (Argentina y Uruguay vía Facturu)
- **I** — After-sale (entrega / recepción)
- **C** — Cobros / movimientos de caja
- **dispatchVoucher / remito** — Remitos
- **operationalOrder / volanta** — Órdenes operativas
- **electricalCertificate** — Certificados eléctricos (con QR)

## Notas del proyecto

- [[NB/Comprobantes/arquitectura|Arquitectura]]
- [[NB/Comprobantes/stack|Stack]]
- [[NB/Comprobantes/changelog|Changelog]]
- [[NB/Comprobantes/contexto|Contexto]]

## Ver también

- [[NB/NB|NB — New Bytes]] (proyecto padre)
- [[NB/pedidos/pedidos|Pedidos]] y [[NB/expedicion/expedicion|Expedición]] (sistemas hermanos en NB)

---

_Última sincronización: 2026-04-22_
