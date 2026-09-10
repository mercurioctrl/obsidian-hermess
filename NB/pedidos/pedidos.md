# Pedidos

Sistema de gestiÃ³n de pedidos de **NB** (New Bytes). AplicaciÃ³n web interna para vendedores y administradores. Multi-empresa: soporta las **11 empresas activas** del grupo (NB, NBElectric, LibreopciÃ³n, **Laset**, Mugello, Oxxen, etc.) filtrando por `companyCode`.

## Stack

- **Frontend:** Nuxt.js 2.15 (Vue 2) + Ant Design Vue 1.7
- **Backend:** Laravel 9 (PHP 8.1) + SQL Server
- **Deploy:** Docker (backend, puerto 8093) + PM2 (frontend, puerto 3702)

Ver detalles completos en [[stack|Stack e infraestructura]].

## Notas del proyecto

- [[arquitectura|Arquitectura]] â Estructura, patrones, controllers, modelos, servicios, modelo canÃ³nico ERP
- [[stack|Stack]] â TecnologÃ­as, versiones y dependencias
- [[changelog|Changelog]] â Registro de cambios por fecha
- [[contexto|Contexto]] â Reglas de negocio, gotchas, empresas, regla cero ERP
- [[memoria|Memoria]] â Contexto acumulado de sesiones con Claude
- [[modulo-makesale|MakeSale]] â Flujo de ejecuciÃ³n de pedidos (pedido â remito)
- [[modulo-removesale|RemoveSale]] â Flujo de reversiÃ³n de remitos
- [[modulo-dashboard-lo|Dashboard Libre OpciÃ³n]] â EstadÃ­sticas exclusivas del marketplace LO
- [[feature-asignacion-oc|Feature: AsignaciÃ³n OC â Venta]] â Trazabilidad pedclil â pedprol antes de serializar
- [[feature-asignacion-oc-cookbook|Cookbook AsignaciÃ³n OC]] â Recetas, SQL de debug, curl examples y mapa de archivos
- [[feature-laset-import|Feature: Laset Import Framework]] â ImportaciÃ³n de operaciÃ³n FOB de Laset (CODEMP=11) desde planilla histÃ³rica al ERP existente
- [[feature-laset-cuenta-corriente|Feature: Import Cuenta Corriente Laset]] â cuenta corriente histÃ³rica USD (comp=11) a MC_CCORRIENTES_MOVIMIENTOS; parser Python + reemplazo por cuenta + NB Inc
- [[nota-catalogo-laset|Nota a CatÃ¡logo â alta 39 SKUs Laset]] â pedido de alta de artÃ­culos comp=11 que destraban Fase D
- [[feature-laset-snapshot-restore|Snapshot/Restore Laset]] â punto de restauraciÃ³n comp=11
- [[feature-laset-fix-pedprot-stockonly|Fix bugs histÃ³ricos Fase C Laset]] â pedprot/pedprol duplicados + stock-only descartado
- [[feature-laset-stockonly-completa|Compra completa stock-only + Reservas]] â la compra se carga completa aunque el Ã­tem no se venda; auto-create de catÃ¡logo + reservas (pedclit cestado=P sin remito)
- [[feature-laset-fix-marcas-comp11|Fix marcas comp=11]] â refactor Fase C marcas + backfill articulo.Id_Marca + cleanup FP_Marcas dups
- [[feature-laset-wipe-reimport|Borrar todo comp=11 + reimport limpio]] â wipe transaccional con barrido de huÃ©rfanos + validaciÃ³n de stocks; flujo Borrar todo â Importar todo
- [[feature-laset-fix-albprol-faltante|Remito de compra faltante (albprol)]] â cierra el gap de artÃ­culos comp=11 con stock pero sin ingreso (albprot/albprol)
- [[feature-laset-cuenta-corriente-proveedores|Feature: Cuenta corriente de PROVEEDORES Laset]] â cta cte de proveedores comp=11 a MS_MOV_CTACTE_PROVEEDORES; clave CCODPRO, saldo bruto, EUR al TC de cierre, alta automÃ¡tica de faltantes; **LST GLOBAL** intercompaÃ±Ã­a incluido (111 cuentas, Î£ 12.914.427,59 USD)
- [[feature-laset-stock-almacen|Feature: Stock por almacÃ©n Laset]] â depÃ³sito por lÃ­nea en pedclil (no del encabezado); fix en Fase C + comando retroactivo laset:fix-stock-almacen-comp11 (re-apunta + transfiere inter-depÃ³sito)
- [[feature-sync-laset-botones|PatrÃ³n Sync Laset â botones de mantenimiento]] â service+command+controller+UI para fixes Laset
- [[feature-integrar-eccn|Feature: integrarECCN]] â clasificaciÃ³n ECCN por familia Ã proveedor para comp=11
- [[feature-pedidos-olvidados|Feature: Pedidos Olvidados]] â filtro oculto de Ã³rdenes pendientes/remitidas >2 meses hasta 3 aÃ±os; fix de timeout acotando la ventana de fecha
- [[feature-descarga-listado-xlsx|Feature: Descarga xlsx de listados]] â botÃ³n solo-icono que exporta el listado filtrado de pedidos/clientes a xlsx; endpoint `orders/download` reutilizando `OrderListRepository` sin paginar
- [[feature-ranking-vendedores|Feature: Ranking de vendedores]] â pestaÃ±a que rankea vendedores por la suma de puntos (travel miles) de sus clientes en el juego NB Travel Mundial de resellers; modal de desglose por cumplimiento
- [[feature-incentivo-netac|Feature: Incentivo Netac]] â incentivo por unidades vendidas de Netac (Memorias + SSD): cada 12 u = USD 4; reemplaza al Incentivo Gigabyte; detalle por pedido/producto/fecha
- [[decision-listas-precios-nombradas|DecisiÃ³n: Listas de precios nombradas y extensibles por companyCode]] â diseÃ±o acordado (2026-08-18), aÃºn sin implementar
- [[feature-estadisticas-lista-precio|Feature: EstadÃ­sticas por lista de precio]] â secciÃ³n del dashboard: facturaciÃ³n/costo/ganancia/rentabilidad % y **retorno sobre costo** por lista; endpoint `priceListStatistics`
- [[feature-ficha-producto|Feature: Ficha de producto]] â endpoint `items/{id}/sheet` con la ficha del producto (fotos, descripciÃ³n, videos, garantÃ­a, logÃ­stica, stock) para modal in-app en vez de nb.com.ar
- [[feature-modulo-presupuestos|Feature: MÃ³dulo de Presupuestos]] â armar/guardar/editar/PDF presupuestos con Ã­tems de inventario por empresa + Ã­tems libres; pestaÃ±a junto a "Ordenes"; tablas `presupuestos`/`presupuestos_items`
- [[feature-pdf-fiscal-por-empresa|Feature: PDF y links por empresa]] â datos fiscales del emisor por `companyCode` desde `FP_Empresas` (CompanyDto extendido) + `config/companySites.php`; encabezado/logo del PDF segÃºn empresa
- [[feature-cuentas-bancarias-empresa|Feature: Cuentas bancarias por empresa]] â muestra en Pedido + Info las cuentas de la empresa de facturaciÃ³n del cliente (`voucherCompanyCode`) para saber a dÃ³nde transferir; tabla `empresas_cuentas_bancarias` (1:N contra `FP_Empresas`)
- [[feature-reportes-intel-dgp|Feature: Reportes Intel DGP-S]] — genera los CSV de inventario y sell-out de procesadores Intel que exige el programa DGP-S; mapeo de part numbers BX→nombre de CPU (constante PHP) con warnings de faltantes
- [[decision-permiso-nuevo-agente|Checklist: agregar un permiso nuevo]] â los 4 lugares (tabla, AuthRepository x2, UserDto, middleware); el gotcha del UserDto que oculta el flag al front

## Esquema ERP â Tablas y relaciones

- [[relacion-tablas-ped-alb|Ventas: pedclit / pedclil / albclit / albclil]] â pedido â remito, encabezado â lÃ­neas
- [[relacion-tablas-pedprot-pedprol-pedproi|Compras: pedprot / pedprol / pedproi]] â OC encabezado, lÃ­neas y cargos extra
- [[relacion-tablas-albprot-albprol|Remitos de compra: albprot / albprol]] â vÃ­nculo con pedprot
- [[relacion-tablas-articulo-stocks|ArtÃ­culo y stocks]] â maestro de productos, balance por almacÃ©n, reglas de FK
- [[relacion-tablas-stocks-almacen|Stocks y depÃ³sitos (FP_Almacen)]] â columnas de depÃ³sito por tabla, depÃ³sitos compartidos
- [[relacion-companycode|companyCode â mapa por tabla]] â quÃ© tablas tienen companyCode propio y cuÃ¡les lo heredan

## Runbooks y referencias

- [[runbook-alta-usuario-interno|Runbook â Alta de usuario interno]] â pasos para dar de alta un agente interno en el sistema
- [[runbook-descarga-comprobantes-venta|Runbook â Descarga masiva de comprobantes (PDF)]] â bajar en lote los PDF de facturas/NC vÃ­a Chrome headless (el link es un SPA con jsPDF, no un PDF server-side)

## Repos

- Backend: `New-Bytes/api-rest-pedidos-laravel` (branch principal: `Development`)
- Frontend: `New-Bytes/pedidos-web-app-v1` (branch principal: `development`)

## Multi-empresa

El sistema soporta **11 empresas activas** (`LACTIVA=1` en `NewBytes_DBF.dbo.FP_Empresas`). Ver [[contexto#Empresas activas (FP_Empresas)]] para la tabla completa.

## Regla cero â tablas ERP read-only

Las tablas legacy del ERP nunca se modifican desde features nuevos. Toda metadata vive en tablas nuevas con prefijo del feature. Ver [[contexto#Regla cero: tablas ERP son read-only]].

## Tareas

- [[API - Fix - Corregir doble-descuento de stock por race en MakeSale|API - Fix - Doble-descuento de stock (race MakeSale/RemoveSale)]]
- [[API - Fix - Script de regularizaciÃ³n stock doble-descuento|API - Fix - Script de regularizaciÃ³n stock doble-descuento]]
- [[API - Research - Causas del stockDelta distinto de cero|API - Research - Causas del stockDelta != 0 (auditorÃ­a global)]]
- [[API - Research - Stock en estanteria no reflejado en el sistema|API - Research - Stock en estanterÃ­a no reflejado en el sistema]]
- [[API - Fix - Correccion albclil faltante en ventas cobradas (caso DIAMOND)|API - Fix - CorrecciÃ³n: albclil faltante en ventas cobradas (DIAMOND)]]

---
*Última sincronización: 2026-09-10 — **Reportes Intel DGP-S**: se documentó el feature (inventory + sell-out para el programa de distribución Intel) y se completó el mapeo de part numbers faltantes. Ver [[feature-reportes-intel-dgp]] y [[changelog]].*