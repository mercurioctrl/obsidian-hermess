# Feature: PDF y links por empresa (datos fiscales del emisor)

Hace que el **presupuesto en PDF del detalle del pedido** (`pages/orders.vue::downloadPDF`) y la [[feature-ficha-producto|ficha de producto]] salgan según la **empresa** (`companyCode`) en vez de hardcodeados a NB. Rama `feature/presupuesto-pdf-por-empresa`. Base reusada por [[feature-modulo-presupuestos]].

## companyCode = FP_Empresas.CODEMP

Empresas emisoras: **4=NB Distribuidora, 9=NBElectric, 10=Pisos y Revest., 11=Laset**. Datos fiscales en `NewBytes_DBF.dbo.FP_Empresas`: `CNOMBRE` (razón social), `CDOMICILIO`, `CPOBLACION`, `CCODPOS`, `CNIF` (CUIT/RUT), `invoiceLogo` (checksum PNG en static). Ver [[relacion-companycode]].

**Ojo:** NBE comparte CUIT con NB (30-70924663-8, misma sociedad; "NBElectric" es marca); Laset tiene CNIF tipo RUT (217502910019). La condición fiscal se imprime como constante "IVA Responsable Inscripto" (FP_Empresas no tiene ese campo como texto).

## Backend

`Dto/Company/CompanyDto.php` extendido: además de id+description ahora expone `businessName, address, city, postalCode, taxId, taxCondition` (desde FP_Empresas). `GET /companies` lo devuelve; el front lo consume con `$api.company.getCompanies({show:1})` y busca por `id === companyCode`. `success()` devuelve el array directo (sin envelope).

`app/config/companySites.php` (nuevo): mapea `companyCode → URL base` del sitio (4=www.nb.com.ar, 9=nbe.com.ar, 11=laset.com.ar; default nb; overridable por env `SITE_URL_NB/NBE/LASET`). Usado en `ProductSheetService::buildWebUrl`.

## Frontend

`pages/orders.vue`: botón .PDF y textarea de observación ahora `v-if="canDownloadPresupuesto"` (companyCode ∈ [4,9,11]); `selectedOrderCompanyCode` se setea en `modalInfoOrderShow`. `getPresupuestoEmisor(companyCode)` trae businessName/address/taxCondition de `/companies` + logo local por empresa; fallback a NB.

**Logos** (jsPDF necesita PNG): en `static/images/logos/` — `logoNB.png` (52.91×11.84), `logoNBE.png` (45.42×11.84), `logoLaset.png` (61.21×11.84, bajados de FP_Empresas.invoiceLogo). Alto fijo 11.84mm, ancho = 11.84 × ratio para no deformar.

## Pendiente

Confirmar si NBE/Laset usan el mismo path del webUrl (`/fromPedidos_-_{id}`). `getPresupuestoEmisor` también vive en `mixins/presupuestoPdf.js` (duplicado; unificar).

## Ver también

- [[feature-modulo-presupuestos]] — reusa este encabezado
- [[feature-ficha-producto]] — usa `config/companySites.php` para el webUrl
- [[relacion-companycode]] — mapeo companyCode ↔ empresas
- [[changelog]]
