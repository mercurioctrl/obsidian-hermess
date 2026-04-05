# Changelog

Registro de cambios del proyecto, agrupado por fecha.

## 2026-03-31

- feat: **Billing Kit Report** — nuevo reporte Excel de kits facturados (controller, service, repository, export)
- fix: nombre de cliente en reporte de kits
- feat: checks post-deploy en Gamma (GitHub Actions workflow)

Archivos: `BillingKitReportController.php`, `BillingKitReportService.php`, `BillingKitReportRepository.php`, `ExcelExportBillingKitReport.php`, `deploy-gamma.yml`

## 2026-03-25 — 2026-03-26

- fix: **ID_ARTICULO null en [[modulo-makesale|MakeSale]]/[[modulo-removesale|RemoveSale]]** — proteger queries con ISNULL para evitar SQL malformado cuando LEFT JOIN no matchea
- fix: usar `ID_Articulo` (de pedclil) en registerStock en vez de `ID_ARTICULO` (de stocks, puede ser null)
- fix: espacio en búsqueda (search)

Archivos: `MakeSaleService.php`, `RemoveSaleService.php`, `MakeSaleRepository.php`

## 2026-03-20

- feat: **Objetivos Gigabyte** — incentivo reutilizable para marca Gigabyte
- feat: objetivos de ventas (backend + frontend)
- fix: respuesta XLSX en reporte

Archivos: `incentivoGigabyte.vue`, `TabMenuDashboard.vue`

## 2026-03-18 — 2026-03-19

- feat: **Kit Report** — reporte de billing de kits
- fix: IVA en kits para sucursal 10
- fix: decompose bundle (descomposición de kits)
- fix: stock en [[modulo-removesale|RemoveSale]]
- fix: listado de productos

## 2026-03-17

- fix: **companyCode en login** — corregir query de auth con ISNULL para includeNull
- fix: **download order warehouse** — respetar `ID_ALMACEN` original del item al descargar pedido
- feat: validación básica post-deploy en Gamma
- refactor: filtro companyCode en ShippingMethods, PaymentMethods y Sellers
- feat: proforma en pedidos (PED-1325)

Archivos: `AuthRepository.php`, filtros de Sellers/Shipping/Payment en frontend

## 2026-03-16

- perf: **optimización de búsqueda de productos** — CONTAINS full-text en vez de LIKE
- perf: eliminar JOINs inutilizados en GetProducts/GetProductById
- perf: reemplazar subconsultas correlacionadas de stockInMyOrder por JOINs
- fix: restaurar LIKE en CDETALLE para substrings
- fix: urldecode en search para compatibilidad

## 2026-03-13

- hotfix: **MercadoLibre sync** — usar `unit_price` como fallback cuando `full_unit_price` no existe
- fix: restaurar JOINs de fotos y prefixar FOT.checksum

## 2026-03-12

- feat: eliminar impuesto interno al agregar a la orden
- fix: **moveItem con kits** — descomponer kits en componentes al mover, preservar precio del origen
- fix: eliminación del origen para items normales en moveItem
