# Contexto

Reglas de negocio, gotchas y contexto de [[Comprobantes]] que no es inferible del código.

## Gotchas del proyecto

### El typo en el nombre es intencional

El repo de la web app se llama `servicio-compobante-pdf-web-app` (falta la "r" en "comprobante"). **No "corregir"**, es el identificador real en GitHub y en el deploy.

### Dos DBs, dos propósitos

- **SQL Server** → datos de negocio de NB (facturas, clientes, stock, etc.). La API lee de acá.
- **MySQL** → solo estado local de la app PHP (lo que mueva Phinx). Migraciones de Phinx **no** afectan al sistema de negocio.

Cambiar schema de SQL Server requiere coordinación con DBA; no se hace desde este repo.

### Dos paths de PDF que duplican lógica

Ver [[arquitectura#Dos paths de renderizado de PDF|arquitectura]]. Al cambiar layout de un comprobante hay que revisar **los dos**:
- `app/pages/voucher/<tipo>/_id.vue` (client-side)
- `app/serverMiddleware/api/generar-pdf.js` (server-side, Express + jsPDF)

Comparten helpers (`header`, `subHeader`, `productos`, `detalleFinal`, `footer`) pero son archivos separados que pueden divergir silenciosamente.

### Rutas con token dual

Cada tipo de comprobante suele tener dos rutas paralelas:
- `/F/{id}` — protegida por JWT en header (uso interno desde apps autenticadas).
- `/F/{id}/{token}` — pública, valida token one-shot en URL (uso en links enviados al cliente).

El middleware `PermissionMiddleware` va **solo** en la primera. Al agregar un tipo nuevo hay que replicar ambas.

### Certificados eléctricos hardcodeados

IDs de certificados con comportamiento especial (QR hardcodeado / link fijo) en la web app:
- `102069`, `103319`, `2936` — tratamiento custom hardcodeado en el código.

Esto se agregó como quick-fix incremental en varios PRs (**LOCAPP-96**, **LOCAPP-98**). No es un patrón limpio — si aparece un caso nuevo, evaluar si corresponde refactor a una lookup table antes de seguir agregando ifs.

## Dominio (AFIP / facturación AR + UY)

Terminología no negociable — son conceptos fiscales reales, no placeholders:

- **CUIT** — Clave Única de Identificación Tributaria (AR).
- **CAE** — Código de Autorización Electrónico que emite AFIP; va impreso con su vencimiento.
- **Punto de venta** + **Nro de comprobante** — identifican unívocamente una factura.
- **Letra A / B / C / E** — determina IVA discriminado vs. incluido y el tipo de receptor.
- **Ingresos Brutos** (ARBA / CABA / otras jurisdicciones) — percepciones/retenciones que se suman al total.
- **Padrón ARBA / AGIP** — registros fiscales provinciales consultados en `/padron`.
- **Responsable Inscripto / Monotributo / Exento** — condiciones frente al IVA que afectan el layout.
- **Facturu** — proveedor externo de facturación electrónica para Uruguay (`FUy`, `/facturu`).

## Organización y contacto

- Owner: **LibreOpcion** (team@libreopcion.com).
- Sistema de tickets: Jira con prefijos **LOCAPP-** (web app) y **COMP-** (API, aparece en branches tipo `COMP-api-feat-...`).
- Rama de trabajo: `Development` (API) / `development` (web app). PRs se mergean desde features individuales.

## Ver también

- [[Comprobantes]]
- [[arquitectura]]
- [[stack]]
- [[changelog]]
