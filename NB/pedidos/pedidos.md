# Pedidos

Sistema de gestiÃÂ³n de pedidos de **NB** (New Bytes). AplicaciÃÂ³n web interna para vendedores y administradores. Multi-empresa: soporta las **11 empresas activas** del grupo (NB, NBElectric, LibreopciÃÂ³n, **Laset**, Mugello, Oxxen, etc.) filtrando por `companyCode`.

## Stack

- **Frontend:** Nuxt.js 2.15 (Vue 2) + Ant Design Vue 1.7
- **Backend:** Laravel 9 (PHP 8.1) + SQL Server
- **Deploy:** Docker (backend, puerto 8093) + PM2 (frontend, puerto 3702)

Ver detalles completos en [[stack|Stack e infraestructura]].

## Notas del proyecto

- [[arquitectura|Arquitectura]] Ã¢ÂÂ Estructura, patrones, controllers, modelos, servicios, modelo canÃÂ³nico ERP
- [[stack|Stack]] Ã¢ÂÂ TecnologÃÂ­as, versiones y dependencias
- [[changelog|Changelog]] Ã¢ÂÂ Registro de cambios por fecha
- [[contexto|Contexto]] Ã¢ÂÂ Reglas de negocio, gotchas, empresas, regla cero ERP
- [[memoria|Memoria]] Ã¢ÂÂ Contexto acumulado de sesiones con Claude
- [[modulo-makesale|MakeSale]] Ã¢ÂÂ Flujo de ejecuciÃÂ³n de pedidos (pedido Ã¢ÂÂ remito)
- [[modulo-removesale|RemoveSale]] Ã¢ÂÂ Flujo de reversiÃÂ³n de remitos
- [[modulo-dashboard-lo|Dashboard Libre OpciÃÂ³n]] Ã¢ÂÂ EstadÃÂ­sticas exclusivas del marketplace LO
- [[feature-asignacion-oc|Feature: AsignaciÃÂ³n OC Ã¢ÂÂ Venta]] Ã¢ÂÂ Trazabilidad pedclil Ã¢ÂÂ pedprol antes de serializar
- [[feature-asignacion-oc-cookbook|Cookbook AsignaciÃÂ³n OC]] Ã¢ÂÂ Recetas, SQL de debug, curl examples y mapa de archivos
- [[feature-laset-import|Feature: Laset Import Framework]] Ã¢ÂÂ ImportaciÃÂ³n de operaciÃÂ³n FOB de Laset (CODEMP=11) desde planilla histÃÂ³rica al ERP existente
- [[feature-laset-cuenta-corriente|Feature: Import Cuenta Corriente Laset]] Ã¢ÂÂ cuenta corriente histÃÂ³rica USD (comp=11) a MC_CCORRIENTES_MOVIMIENTOS; parser Python + reemplazo por cuenta + NB Inc
- [[nota-catalogo-laset|Nota a CatÃÂ¡logo Ã¢ÂÂ alta 39 SKUs Laset]] Ã¢ÂÂ pedido de alta de artÃÂ­culos comp=11 que destraban Fase D
- [[feature-laset-snapshot-restore|Snapshot/Restore Laset]] Ã¢ÂÂ punto de restauraciÃÂ³n comp=11
- [[feature-laset-fix-pedprot-stockonly|Fix bugs histÃÂ³ricos Fase C Laset]] Ã¢ÂÂ pedprot/pedprol duplicados + stock-only descartado
- [[feature-laset-stockonly-completa|Compra completa stock-only + Reservas]] Ã¢ÂÂ la compra se carga completa aunque el ÃÂ­tem no se venda; auto-create de catÃÂ¡logo + reservas (pedclit cestado=P sin remito)
- [[feature-laset-fix-marcas-comp11|Fix marcas comp=11]] Ã¢ÂÂ refactor Fase C marcas + backfill articulo.Id_Marca + cleanup FP_Marcas dups
- [[feature-laset-wipe-reimport|Borrar todo comp=11 + reimport limpio]] Ã¢ÂÂ wipe transaccional con barrido de huÃÂ©rfanos + validaciÃÂ³n de stocks; flujo Borrar todo Ã¢ÂÂ Importar todo
- [[feature-laset-fix-albprol-faltante|Remito de compra faltante (albprol)]] Ã¢ÂÂ cierra el gap de artÃÂ­culos comp=11 con stock pero sin ingreso (albprot/albprol)
- [[feature-laset-cuenta-corriente-proveedores|Feature: Cuenta corriente de PROVEEDORES Laset]] Ã¢ÂÂ cta cte de proveedores comp=11 a MS_MOV_CTACTE_PROVEEDORES; clave CCODPRO, saldo bruto, EUR al TC de cierre, alta automÃÂ¡tica de faltantes; **LST GLOBAL** intercompaÃÂ±ÃÂ­a incluido (111 cuentas, ÃÂ£ 12.914.427,59 USD)
- [[feature-laset-stock-almacen|Feature: Stock por almacÃÂ©n Laset]] Ã¢ÂÂ depÃÂ³sito por lÃÂ­nea en pedclil (no del encabezado); fix en Fase C + comando retroactivo laset:fix-stock-almacen-comp11 (re-apunta + transfiere inter-depÃÂ³sito)
- [[feature-sync-laset-botones|PatrÃÂ³n Sync Laset Ã¢ÂÂ botones de mantenimiento]] Ã¢ÂÂ service+command+controller+UI para fixes Laset
- [[feature-integrar-eccn|Feature: integrarECCN]] Ã¢ÂÂ clasificaciÃÂ³n ECCN por familia ÃÂ proveedor para comp=11
- [[feature-pedidos-olvidados|Feature: Pedidos Olvidados]] Ã¢ÂÂ filtro oculto de ÃÂ³rdenes pendientes/remitidas >2 meses hasta 3 aÃÂ±os; fix de timeout acotando la ventana de fecha
- [[feature-descarga-listado-xlsx|Feature: Descarga xlsx de listados]] Ã¢ÂÂ botÃÂ³n solo-icono que exporta el listado filtrado de pedidos/clientes a xlsx; endpoint `orders/download` reutilizando `OrderListRepository` sin paginar
- [[feature-ranking-vendedores|Feature: Ranking de vendedores]] Ã¢ÂÂ pestaÃÂ±a que rankea vendedores por la suma de puntos (travel miles) de sus clientes en el juego NB Travel Mundial de resellers; modal de desglose por cumplimiento
- [[feature-incentivo-netac|Feature: Incentivo Netac]] Ã¢ÂÂ incentivo por unidades vendidas de Netac (Memorias + SSD): cada 12 u = USD 4; reemplaza al Incentivo Gigabyte; detalle por pedido/producto/fecha
- [[decision-listas-precios-nombradas|DecisiÃÂ³n: Listas de precios nombradas y extensibles por companyCode]] Ã¢ÂÂ diseÃÂ±o acordado (2026-08-18), aÃÂºn sin implementar
- [[feature-estadisticas-lista-precio|Feature: EstadÃÂ­sticas por lista de precio]] Ã¢ÂÂ secciÃÂ³n del dashboard: facturaciÃÂ³n/costo/ganancia/rentabilidad % y **retorno sobre costo** por lista; endpoint `priceListStatistics`
- [[feature-ficha-producto|Feature: Ficha de producto]] Ã¢ÂÂ endpoint `items/{id}/sheet` con la ficha del producto (fotos, descripciÃÂ³n, videos, garantÃÂ­a, logÃÂ­stica, stock) para modal in-app en vez de nb.com.ar
- [[feature-modulo-presupuestos|Feature: MÃÂ³dulo de Presupuestos]] Ã¢ÂÂ armar/guardar/editar/PDF presupuestos con ÃÂ­tems de inventario por empresa + ÃÂ­tems libres; pestaÃÂ±a junto a "Ordenes"; tablas `presupuestos`/`presupuestos_items`
- [[feature-pdf-fiscal-por-empresa|Feature: PDF y links por empresa]] Ã¢ÂÂ datos fiscales del emisor por `companyCode` desde `FP_Empresas` (CompanyDto extendido) + `config/companySites.php`; encabezado/logo del PDF segÃÂºn empresa
- [[feature-cuentas-bancarias-empresa|Feature: Cuentas bancarias por empresa]] Ã¢ÂÂ muestra en Pedido + Info las cuentas de la empresa de facturaciÃÂ³n del cliente (`voucherCompanyCode`) para saber a dÃÂ³nde transferir; tabla `empresas_cuentas_bancarias` (1:N contra `FP_Empresas`)
- [[feature-reportes-intel-dgp|Feature: Reportes Intel DGP-S]] â genera los CSV de inventario y sell-out de procesadores Intel que exige el programa DGP-S; mapeo de part numbers BXânombre de CPU (constante PHP) con warnings de faltantes
- [[feature-comprobantes-emisor|Feature: Emisor (RazÃ³n Social) en Comprobantes]] — el emisor se resuelve por `FP_Empresas.SUCFacturaPlus = CNUMSUC` (NB factura vÃ­a DIGITO BINARIO SRL para suc 0005); fix OUTER APPLY + guard del null que corrÃ­a la grilla
- [[feature-nota-credito-debito|Feature: Nota de CrÃ©dito/DÃ©bito (eze)]] — permiso `creditDebitNote`, endpoint POST /voucher/creditDebitNote (suc 0010, no fiscal) a MC_CCORRIENTES_MOVIMIENTOS; incidente: se probÃ³ sobre la base beta productiva
- [[decision-permiso-nuevo-agente|Checklist: agregar un permiso nuevo]] Ã¢ÂÂ los 4 lugares (tabla, AuthRepository x2, UserDto, middleware); el gotcha del UserDto que oculta el flag al front

## Esquema ERP Ã¢ÂÂ Tablas y relaciones

- [[relacion-tablas-ped-alb|Ventas: pedclit / pedclil / albclit / albclil]] Ã¢ÂÂ pedido Ã¢ÂÂ remito, encabezado Ã¢ÂÂ lÃÂ­neas
- [[relacion-tablas-pedprot-pedprol-pedproi|Compras: pedprot / pedprol / pedproi]] Ã¢ÂÂ OC encabezado, lÃÂ­neas y cargos extra
- [[relacion-tablas-albprot-albprol|Remitos de compra: albprot / albprol]] Ã¢ÂÂ vÃÂ­nculo con pedprot
- [[relacion-tablas-articulo-stocks|ArtÃÂ­culo y stocks]] Ã¢ÂÂ maestro de productos, balance por almacÃÂ©n, reglas de FK
- [[relacion-tablas-stocks-almacen|Stocks y depÃÂ³sitos (FP_Almacen)]] Ã¢ÂÂ columnas de depÃÂ³sito por tabla, depÃÂ³sitos compartidos
- [[relacion-companycode|companyCode Ã¢ÂÂ mapa por tabla]] Ã¢ÂÂ quÃÂ© tablas tienen companyCode propio y cuÃÂ¡les lo heredan

## Runbooks y referencias

- [[runbook-alta-usuario-interno|Runbook Ã¢ÂÂ Alta de usuario interno]] Ã¢ÂÂ pasos para dar de alta un agente interno en el sistema
- [[runbook-descarga-comprobantes-venta|Runbook Ã¢ÂÂ Descarga masiva de comprobantes (PDF)]] Ã¢ÂÂ bajar en lote los PDF de facturas/NC vÃÂ­a Chrome headless (el link es un SPA con jsPDF, no un PDF server-side)

## Repos

- Backend: `New-Bytes/api-rest-pedidos-laravel` (branch principal: `Development`)
- Frontend: `New-Bytes/pedidos-web-app-v1` (branch principal: `development`)

## Multi-empresa

El sistema soporta **11 empresas activas** (`LACTIVA=1` en `NewBytes_DBF.dbo.FP_Empresas`). Ver [[contexto#Empresas activas (FP_Empresas)]] para la tabla completa.

## Regla cero Ã¢ÂÂ tablas ERP read-only

Las tablas legacy del ERP nunca se modifican desde features nuevos. Toda metadata vive en tablas nuevas con prefijo del feature. Ver [[contexto#Regla cero: tablas ERP son read-only]].

## Tareas

- [[API - Fix - Corregir doble-descuento de stock por race en MakeSale|API - Fix - Doble-descuento de stock (race MakeSale/RemoveSale)]]
- [[API - Fix - Script de regularizaciÃ³n stock doble-descuento|API - Fix - Script de regularizaciÃ³n stock doble-descuento]]
- [[API - Research - Causas del stockDelta distinto de cero|API - Research - Causas del stockDelta != 0 (auditorÃÂ­a global)]]
- [[API - Research - Stock en estanteria no reflejado en el sistema|API - Research - Stock en estanterÃÂ­a no reflejado en el sistema]]
- [[API - Fix - Correccion albclil faltante en ventas cobradas (caso DIAMOND)|API - Fix - CorrecciÃÂ³n: albclil faltante en ventas cobradas (DIAMOND)]]

---
*Última sincronización: 2026-09-16 — **Comprobantes: emisor + Nota de Crédito/Débito**: fix del emisor (Razón Social por SUCFacturaPlus=CNUMSUC) y la feature de créditos de eze; se descubrió que el backend local escribe en la base **beta productiva**. Ver [[feature-comprobantes-emisor]], [[feature-nota-credito-debito]], [[contexto#⚠️ El backend local escribe en BETA (red productiva)]] y [[changelog]].*