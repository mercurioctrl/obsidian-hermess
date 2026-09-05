# Contexto y decisiones

Parte de [[portal]].

## De dónde salió

El punto de partida fue un **relevamiento de la extranet de Elibet** (`extranet.elibet.com`),
hecho navegando el sitio con una sesión real de cliente: `SPEC-portal-b2b.md` en el repo. No es
un requerimiento formal sino el análisis de un portal que ya funciona en el mismo rubro.

La consigna: replicar esa funcionalidad **sobre la API que el grupo ya tiene**.

## Decisiones

### El backend no se toca

`sitio-api-rest-v3` es productivo y sirve también al sitio de NB. Todo se resolvió del lado del
frontend; lo que no se pudo quedó documentado como pendiente en [[estado]], no se parcheó.

### Dos instancias de API, una por empresa

El alcance por empresa no es un parámetro de request: la API lo lee de su `.env` y lo interpola
en el SQL. Por eso NBE tiene `api.nbe.com.ar` y el portal solo apunta ahí.
Ver [[configuracion#Empresa NB vs NBE]].

### Donde la API no da el dato, se dice en pantalla

Decisión explícita de producto: **no mostrar columnas vacías ni números inventados**.

- `/comprobantes` aclara que el saldo pendiente y el vencimiento no los expone la API
- `/postventa` aclara que es de consulta y que el alta va por el canal habitual
- `/frecuentes` aclara que el precio es el de la última compra, no el vigente
- El panel solo muestra métricas que la API puede sostener

El razonamiento: un portal que miente sobre un saldo genera más llamados que uno que dice
"esto todavía no está".

### Configuración por deploy, no por panel

Las secciones activas se definen con variables de entorno. Se evaluó un panel de administración
persistido en la API, pero **no hay dónde guardarlo**: `defaultParameters` del CMS mapea a
columnas fijas de `PV_PARAMETROS_VARIOS` del ERP, no es un key-value genérico. Ver
[[configuracion#Secciones activables]].

### El backend queda fuera del repo

`sitio-api-rest-v3/` está clonado adentro de la carpeta del proyecto, pero el `.gitignore` de la
raíz lo excluye. Dos razones:

1. **Es un repo aparte** (`New-Bytes/sitio-api-rest-v3`) con su propio remote. Versionarlo acá
   lo duplicaría.
2. **Su `app/.env-example` trae credenciales reales** — contraseña de la base, de los dos
   mailers y token de static — y el secreto JWT está hardcodeado en `TokenManager.php:10`.
   Publicarlas en un repo nuevo sería una filtración.

Antes del primer commit se escaneó el contenido staged buscando esos patrones.

### Marca tomada del sitio real

Logo, paleta y tipografía se extrajeron del CSS y el DOM de `nbe.com.ar`, no se inventaron.
Ver [[marca]].

## Cómo se trabajó

Por fases sobre el spec, priorizando el camino del pedido:

1. Layout, login, catálogo, carrito, checkout, mis pedidos
2. Lo que la API ya soportaba: precios, comprobantes, frecuentes, recuperación, usuarios,
   direcciones, postventa
3. Marca
4. Configuración de secciones

Lo que quedó afuera no fue por tiempo sino porque la API no tiene el dato.

## Verificación

Todo lo afirmado sobre la API se comprobó **contra la API real**, no contra la lectura del
código: rutas, formas de respuesta, CORS y preflight. Lo que **no** se verificó es cualquier
operación que escriba en el ERP, por no disponer de credenciales de prueba.

## Ver también

- [[api-nbe]] · [[estado]] · [[configuracion]] · [[marca]]
