## 2026-08-06 — Auditoría de credenciales AWS/IAM del bucket de Contenido

Auditoría (sin cambios de código) del alcance de las claves AWS que usa la app, a raíz de la consulta del usuario sobre si compartir la key con un dev expone otra parte de la infra AWS. **Resultado: la key es de mínimo privilegio, seguro compartir (con salvedades).** Ver [[modulos/contenido#Seguridad — credenciales IAM (auditado 2026-08-06)|modulos/contenido]].

- **Identidad**: `arn:aws:iam::830204833423:user/gigaerp-contenido-dev-svc` (service account dedicado). Bucket `gigaerp-contenido-dev` (sa-east-1, S3 nativo, sin endpoint custom).
- **Scope verificado empíricamente** (`aws sts get-caller-identity` + probes): solo puede operar objetos sobre su bucket. Denegado: `ListAllMyBuckets`, políticas IAM propias, `GetBucketPolicy`/`GetBucketAcl`, EC2, RDS, Secrets Manager.
- **Recomendación al usuario**: rotar la key tras compartirla; permite `PutObject`/`DeleteObject` (el dev puede borrar/sobrescribir dev); el bucket es compartido local↔prod.
- **Tip operativo**: los valores S3 se inyectan por env de docker (NO están en `backend/.env`); leerlos con `docker exec gigaerp-backend sh -c 'env | grep -iE "CONTENIDO|AWS"'`. `aws` CLI vive en el host (`/home/hermess/.local/bin/aws`).

---

## 2026-08-04 — Ajustes de Google/Meta Ads (feedback marketing)

Tanda de ajustes finos sobre las dos secciones de ads, ya mergeadas a `Development` (PRs #8 Meta y #9 fix Google; de acá en más se trabaja **directo sobre `Development`**). Ver [[modulos/google-ads]] y [[modulos/meta-ads]].

- **Meta — clics = salientes (`outbound_clicks`), no `clicks`**: el campo `clicks` cuenta toda interacción y daba de más (AR 904). Leo confirma que la métrica correcta son los **clics salientes** (los que llevan fuera de Meta al sitio del reseller). Constante `A_CLIC=['outbound_click']`, se extrae con `valorAccion()`. Verificado AR (Jul4-Ago2): 674 total, Compufan 335, CompuMar 339. Aplica a resumen/serie/campañas; CPC/CTR de Meta derivan de este clic. Ver [[troubleshooting#Meta Ads]].
- **Meta — se quitó la tarjeta ROAS** y la **columna Objetivo** de la tabla de campañas (a pedido).
- **Google — se quitaron los sublabels CPC (Inversión) y CTR (Impresiones)** de las tarjetas (PR #9). Los valores se siguen calculando en el backend, solo no se muestran.
- **Google — "Agregar al carrito" ahora es entero** (redondeado, sin decimales).
- **Ambos — se quitó el aviso amarillo** "No se registraron eventos de conversión…" cuando no venían conversiones (mostraba 0 sin cartel).
- **Tooltips (i) con textos literales del cliente** en Google (8 métricas) y Meta (10 métricas), reemplazando los textos genéricos. Regla acordada: si una métrica no tiene explicación provista, no lleva "i" (en la práctica todas la tienen).

**Deploy:** cambios de frontend → rebuild completo + `docker restart gigaerp-nginx`. El fix de clics (backend) fue hot-deploy (`docker cp` + `config:cache` + `cache:clear`), sin rebuild de frontend. Todo en `Development`.

---

## 2026-08-03 — Sección Meta Ads (reportes)

Nueva sección **Marketing → Meta Ads**: reportes de Facebook/Instagram Ads embebidos en el ERP, navegables entre fechas. Espejo de [[modulos/google-ads]], nativa Laravel + Nuxt (Graph API / Marketing API, sin Python). **PR #8** contra `Development`, funcionando con datos reales. Ver [[modulos/meta-ads]] y `docs/DEPLOY_META_ADS.md`.

- **Backend**: `MetaAdsService` (Graph API con **System User token**, sin refresh_token; `resumen()` agregado + `serieDiaria()` con `time_increment=1` + `topCampanias()`/`metaCampanias()` + `presupuestoDiario()`; cache 5 min; modo demo con fixture), `MetaAdsController` (`/api/meta-ads/cuentas` y `/reporte`, valida `act_id`). Migración `0060` `meta_ads_cuentas` (+ seed AR/UY/CL, act_id sin prefijo `act_`). Config `services.meta_ads`.
- **Frontend**: `pages/meta-ads/index.vue` (cuentas) + `[cid].vue` (reporte: presets, `SelectorFecha`, flechas ◀▶, StatsCards con ícono (i), gráfico SVG, tabla de campañas). Sección en `secciones.ts` (permiso `VER_SECCION_META_ADS`).
- **Métricas**: Presupuesto/día, Inversión, Impresiones, **Alcance**, **Frecuencia**, Clics, Agregar al carrito, Compras, Monto de compra, **ROAS**, Costo por compra. Alcance/Frecuencia/ROAS son **exclusivas de Meta** (Google no las tenía) y se leen del resumen agregado.
- **Cuentas Gigabyte** (AR 1922499601658152 / UY 2533454380455971 / CL 865101106388536, USD) en el Business Manager de Blu; un solo token accede a todas.
- **⚠️ Gotcha clave (mismo que Google)**: el array `actions` cuenta la misma compra ~5 veces (`purchase`, `omni_purchase`, `offsite_conversion.fb_pixel_purchase`…). Sumar duplicaba ×5. Se toma **un action_type canónico**: `omni_purchase` (compras/monto) + `omni_add_to_cart` (carritos). Verificado AR = 26 compras / USD 15.072,09 (no 130). Además: reach/frequency NO sumables entre días; presupuesto en centavos (/100).
- **Pendiente (marketing/Leo)**: confirmar evento de compra/carrito canónico y ventana de atribución (default 7d clic/1d view).

**Deploy backend (en caliente):** `docker cp` de service/controller/model/migración + `api.php` + `services.php`, credenciales `META_ADS_*` al `.env` del container (`docker exec -i … 'cat >> .env'`), `config:cache`, `route:clear`. **Frontend:** rebuild completo + restart nginx. Credenciales **fuera de git**.

---

## 2026-07-31 — Sección Google Ads (reportes)

Nueva sección **Marketing → Google Ads**: reportes de Google Ads embebidos en el ERP, navegables entre fechas. Nativa Laravel + Nuxt (API REST + GAQL, **sin Python** — la guía proponía FastAPI). Mergeada a `Development` (PRs #4/#5/#6, + #7). Ver [[modulos/google-ads]] y `docs/DEPLOY_GOOGLE_ADS.md`.

- **Backend**: `GoogleAdsService` (OAuth refresh→access token cacheado en Redis, `searchStream` GAQL, cache del reporte, modo demo con fixture), `GoogleAdsController` (`/api/google-ads/cuentas` y `/reporte`, valida `cid`). Migración `0059` `google_ads_cuentas` (+ seed AR/UY/CL) con `login_customer_id` por cuenta. Config `services.google_ads`. Script `obtener_refresh_token_google_ads.py`.
- **Frontend**: `pages/google-ads/index.vue` (cuentas) + `[cid].vue` (reporte: presets, `SelectorFecha`, flechas ◀▶, StatsCards con ícono (i), gráfico SVG, tabla de campañas). Sección en `secciones.ts` (permiso `VER_SECCION_GOOGLE_ADS`). `StatsCard` ganó prop `info` (tooltip reutilizable).
- **Métricas**: Presupuesto/día, Inversión, Impresiones, Clics, Agregar al carrito, Compras, Monto de compra, Costo por compra. Alcance/Frecuencia no aplican (son de Meta).
- **Cuentas Gigabyte** (AR 9373933264 / UY 5837677270 / CL 9370009552, USD) cuelgan del MCC BLU STUDIO (3863921811).
- **Gotchas resueltos**: `api_version=v22` (v18 sunseteada→404); `login-customer-id` por cuenta y opcional (forzarlo sobre cuenta directa → `USER_PERMISSION_DENIED`); default de fechas `LAST_30_DAYS` (mes pasado abría vacío); `docker exec` necesita `-i` para escribir al `.env`; strings con acentos vía tinker (utf8mb4), no `mysql -e` (mojibake).
- **⚠️ Fix clave (feedback marketing / Leo Saran)**: Compras y Monto de compra se toman **a nivel campaña (objetivo custom, goal-aware)**, no sumando categorías de conversión que se solapan y duplicaban el monto (UY: 9.545,27 correcto vs 28.977 duplicado). Se quitaron ROAS y la tabla de Destinos. Pendiente: definir la acción de carrito canónica (ADD_TO_CART también puede duplicar).

**Deploy backend (en caliente):** `docker cp` de service/controller/model/migración + `api.php` + `services.php`, credenciales `GOOGLE_ADS_*` al `.env` del container (`docker exec -i … 'cat >> .env'`), `config:cache`, `route:clear`. **Frontend:** rebuild completo + restart nginx. Credenciales **fuera de git**.

---

## 2026-07-28 — Sección Envíos (campañas de mailing)

Nueva sección **Envíos** de solo lectura que proxea la API de campañas de email `envios.to-aor.us`. Commit `f773a34` (rama `Development`, hot-deploy backend + rebuild frontend). Ver [[modulos/envios]].

- **Backend `EnvioController`** (patrón proxy, mismo que [[modulos/resellers|Resellers]], sin DB): `GET /api/envios/campanias` (listado) y `GET /api/envios/campanias/{id}` (detalle, acepta `?estado=` y `?lista=`; la ruta usa `->where('id','.*')` porque el id puede ser `(sin-campania)`). Token en `config/services.php` → `services.envios.{url,token}` vía env `ENVIOS_API_URL`/`ENVIOS_API_TOKEN`, auth `Http::withToken`.
- **Frontend**: `pages/envios/index.vue` (tarjetas por campaña + totales agregados) y `pages/envios/[id].vue` (5 StatsCards + pills de estado + tabla de destinatarios). Alta en `secciones.ts` (grupo Marketing, permiso `VER_SECCION_ENVIOS`).
- **Filtro Real / Test / Todas** en ambas pantallas, **prefiltrado en Real**. Clasificación: lista *Test* si está vacía o su nombre contiene `prueba`/`test`; campaña *Test* si todas sus listas lo son. Se resuelve **client-side** (la API externa no maneja categorías): el detalle se trae completo una vez y el toggle recalcula StatsCards + tabla. Con datos de solo-prueba, el prefiltro Real deja la pantalla vacía a propósito.
- **Gotcha**: los `destinatarios` no traen `id` y hay emails repetidos → id sintético por índice para el `:key` del DataTable. `useApi.get` devuelve el JSON crudo del proxy (sin `.data`).
- **Imprevisto de deploy**: el container tenía `AddonMarketingController` + modelo `AddonMarketing` **sin desplegar** (referenciados en `api.php`) → al copiar el `api.php` actualizado, el ruteo tiraba 500. Se copiaron ambos archivos al container; la tabla `addons_marketing` ya existía (mig `0044`), no hubo migración. De paso quedó funcional `/api/addons`.

**Deploy backend (en caliente):** `docker cp` de `EnvioController.php` + `services.php` + `api.php`, setear `ENVIOS_API_*` en el `.env` del container, `config:cache` + `route:clear`, `docker restart gigaerp-nginx`. **Frontend:** rebuild completo + `up -d --no-deps frontend` + restart nginx.

---

## 2026-07-27 — Ploteos con mapa + estados de proyecto configurables

Trabajo de otro dev integrado en `Development` y deployeado (hot-deploy backend + rebuild frontend). Commits `46e6dab`, `009b911`, `8e58069`, `815c284`. Migraciones `0051`–`0057`.

### Módulo Ploteos (branding físico de resellers) — nuevo. Ver [[modulos/ploteos]]
- Nueva sección `/ploteos` (grupo Marketing) para gestionar los **ploteos/vinilos de sucursales** de los resellers, con **mapa geolocalizado** (Leaflet + markercluster + tiles OSM).
- Modelo `Ploteo` (migs `0051`–`0055`): `cliente_id`, `sucursal`, `ploteo`, `url`, `medidas_cm`, `ubicacion`, `lat`/`lng`, `fecha`, `estado` (`programado`/`en_proceso`). Historial de migraciones sinuoso: `0054` dropea `sucursal`, `0055` la re-agrega.
- **Geocodificación vía Nominatim** (`PloteoController::geocodificar`): al crear/editar con `ubicacion`, le pega a OpenStreetMap con `User-Agent` de `config('services.nominatim.user_agent')` — **bloque nuevo en `config/services.php`** (requirió `config:cache` re-inyectando MAIL_*/CONTENT_DOMAIN). Falla silenciosa; ⚠️ Nominatim devuelve `lon` mapeado a `lng`.
- **Endpoints**: `GET /ploteos/paises`, `GET /ploteos/mapa` (solo `whereNotNull(lat,lng)`), `apiResource('ploteos')` — estáticas antes del wildcard.
- **Importación masiva** (`ImportacionPloteosController`, `/importaciones-ploteos/parsear` + `store`): Excel País/Reseller/Sucursal/Ploteo/Medidas/Fecha, mapea `sucursal`→`ubicacion` y geocodifica fuera de la transacción (rate-limit ~1 req/seg, tope 80). `pages/ploteos/importar.vue`.
- **Gotcha (2026-07-27)**: los ploteos previos a `0053` no tienen `ubicacion`/coords → no aparecen en el mapa; hay que cargarles dirección o re-importar. No es bug de deploy.

### Estados de proyecto configurables (mig `0057`) + calendario datetime (mig `0056`)
- El enum `App\Enums\EstadoProyecto` **se eliminó**, reemplazado por tabla/modelo **`EstadoProyecto`** (`nombre`, `color`, `orden`, `activo`) con CRUD (`apiResource('estados-proyecto')`) editable desde **Configuración** (`pages/configuracion/index.vue`).
- Migración `0057` crea la tabla, siembra los 4 estados legacy (Activo/En pausa/Pendiente de pago/Archivado), agrega FK `proyectos.estado_proyecto_id` (nullOnDelete), migra los datos por estado legacy y **dropea la columna `estado`** vieja. `StatusBadge` gana soporte de color por estado.
- **Calendario**: `eventos_calendario.fecha_inicio`/`fecha_fin` pasan de `DATE` a `DATETIME` (mig `0056`) → eventos con hora. `EventoCalendarioController`/`EventoCalendario` y `pages/calendario/index.vue` ajustados.

**Deploy:** borrar el enum eliminado del container (`rm app/Enums/EstadoProyecto.php`), copiar controllers/models, migrar (dup Sanctum antes), `config:cache` **con envs re-inyectadas** (por `services.php`), rebuild frontend (`package.json` cambió: Leaflet). Ver [[troubleshooting]].

---

## 2026-07-23 — Clientes: tipos distribuidor/reseller + Contactos (rama `Development`)

Nuevo trabajo de otro dev integrado en la rama **`Development`** (la de deploy activa; `main` quedó atrás). Commits `b3b27aa`, `eae97a3`. Ver [[modulos/clientes]].

- **Tipos de cliente**: `clientes.tipo` con default `distribuidor` (mig `0021`) ahora distingue **`reseller`**. El listado `/clientes` gana pestañas distribuidor/reseller; índices `clientes(tipo,pais)` (mig `0050`).
- **Contactos** (mig `0049`, tabla `contactos`): CRUD (`apiResource('contactos')`) + **sección propia** `/contactos` (`pages/contactos/index.vue`) + entrada en el sidebar.
- **Importación por bloques** (`/clientes/importar-contactos`, `ImportacionContactosController`): Excel con bloques CLIENTE/MAIL por país (hoja "LISTA MAILS CLIENTES"), crea clientes `reseller` + contactos, con **carry-forward** del nombre y bloque especial "Partners NVIDIA". PhpSpreadsheet ya instalado (fallback CSV).
- **SMTP real cableado** para los avisos de Contenido: `box.lio.red:465` (`MAIL_SCHEME=smtps`), remitente `gigabyte@blustudioinc.com`. Vars `MAIL_*` en `.env` (gitignored) + `docker-compose.yml` (default `log`). Envío probado OK. Ver [[modulos/contenido#Config y deploy|contenido]].

**Deploy:** hot-deploy backend (controllers + migraciones `0049`/`0050`, borrar dup Sanctum antes de migrar) + rebuild frontend con `--no-deps`. Ver [[troubleshooting]].

---

## 2026-07-23 — Contenido: suscripción por email, deep-links en el ERP, paridad de vistas y OpenAPI

Cuarta tanda del módulo [[modulos/contenido|Contenido]] + docs de API. Commits `2e64e44`, `4af7a34`, `a54da03`, `78daa74`.

### Paridad de features en la vista ERP + descargar todo + fix preview (`2e64e44`)
- La vista admin (`frontend/pages/contenido/index.vue`) alcanza a la pública: **thumbnails on-demand** (fetch a `/api/contenido/thumb`, lazy IntersectionObserver, resolución del header `X-Res`), **resolución/formato + fecha** por archivo, **orden** por Nombre/Fecha (asc/desc), **filtro por resolución**, **abrir en pestaña** (↗) y **descargar directo** (URL firmada `attachment`).
- Botón **"Descargar todo"** (en ambas vistas): baja secuencialmente los archivos de la carpeta respetando el filtro, con progreso.
- Fix **"imagen rota"**: formatos no previsualizables (tif/psd/etc.) muestran ícono + badge de formato en vez de un `<img>` que el navegador no puede dibujar; preview solo si hay thumbnail (png/jpg/gif) o es tipo nativo (webp/svg…), con `onerror` de respaldo.

### Deep-links en el ERP + link público por carpeta (`4af7a34`)
- La página del ERP pasó a **ruta catch-all** (`pages/contenido/[...ruta].vue`): navegar carpetas cambia la URL (`/contenido/A/B`), es recargable y anda back/forward. La **URL es la fuente de verdad** (watch sobre `route.params` + reconstrucción de la pila).
- **"Copiar link" / "Ver público"** arman la URL pública de la carpeta donde estás parado, usando el dominio externo (`CONTENT_DOMAIN`) o el mismo origen en local.
- Nuevo **`GET /contenido/config`** (auth) expone el dominio público al ERP; `config/contenido.php` (`dominio_publico` ← `CONTENT_DOMAIN`).

### Suscripción por email + avisos (`4af7a34`)
- **Footer de suscripción** en el portal público (email, alta idempotente). Tabla **`contenido_suscriptores`** (mig `0048`) + modelo `ContenidoSuscriptor`.
- `POST /contenido/publico/suscribir` (throttle 10/min) y `GET /contenido/publico/desuscribir?token` (baja con página de confirmación, blade `baja`). Ambas **antes del comodín** para que no las trague.
- **`POST /contenido/notificar`** (auth): un mail-resumen a los suscriptores activos. Lo dispara el ERP **una vez** al terminar de subir un lote (no un mail por archivo), tolerante a fallos (no rompe la subida si el mail falla).
- Mailable `ContenidoNuevoMail` + plantilla HTML branded (barra RGB + link a la carpeta), blade `mail_nuevo`. Vars `MAIL_*` en `docker-compose` (default `log` hasta cargar SMTP).

### Vista de suscriptores en el ERP (`a54da03`)
- `GET /contenido/suscriptores` (total, activos, items) y `DELETE /contenido/suscriptores/{id}` (baja definitiva).
- Header del ERP: botón **"Suscriptores"** con contador de activos → modal con la lista (email, fecha, estado), eliminar por fila y **exportar CSV**.

### Fix tareas — estado null en memoria (`4af7a34`)
- `Tarea::$attributes` ahora espeja los defaults de la DB (`estado=POR_HACER`, `prioridad=MEDIA`). Sin esto, una tarea creada sin estado quedaba con `estado=null` en memoria y `TareaResource` rompía en `$this->estado->value` aunque la fila se creara igual. Ver [[troubleshooting#15. Modelo con enum casteado revienta si la columna tiene default en DB pero no en $attributes|troubleshooting #15]].

### Documentación OpenAPI 3.0 + Swagger UI (`78daa74`)
- `backend/docs/openapi.yaml` — spec OpenAPI 3.0 de la API REST (Laravel 11 + Sanctum).
- `backend/docs/index.html` — Swagger UI (CDN) que lee el yaml. `backend/docs/README.md` — cómo verla.

**Archivos:** `frontend/pages/contenido/[...ruta].vue` (renombrado de `index.vue`), `backend/app/Http/Controllers/ContenidoController.php`, `backend/app/Mail/ContenidoNuevoMail.php`, `backend/app/Models/{ContenidoSuscriptor,Tarea}.php`, `backend/config/contenido.php`, `backend/database/migrations/0048_create_contenido_suscriptores_table.php`, `backend/resources/views/contenido/{publico,baja,mail_nuevo}.blade.php`, `backend/routes/api.php`, `docker-compose.yml`, `backend/docs/`.

---

## 2026-07-22 — Contenido: subdominio, deep-links, descarga, filtro y thumbnails

Segunda tanda sobre el módulo [[modulos/contenido|Contenido]] (mismo día). Commits `1388ba5`, `4ad6b8b`, `da0332e`.

### Subdominio propio + URLs linkeables (`1388ba5`)
- La vista pública se puede servir en un **subdominio** configurable por `.env` (`CONTENT_DOMAIN`, ej. `content.gigabyte.com`). nginx pasó de config estática a **template con envsubst** (`nginx/default.conf.template`, reemplaza `default.conf`): nuevo `server` block que sirve Contenido en la raíz del subdominio y proxya `/api/` al backend. El server principal (ERP) queda igual.
- **Deep-linking (History API)**: al entrar/salir de carpetas la URL cambia (`/Carpeta/Sub`), back/forward funciona y un deep-link abre directo esa carpeta. Detecta el base path (subdominio `''` vs localhost `/api/contenido/publico`). Ruta backend comodín `/contenido/publico/{ruta?}`.

### Descarga directa + abrir en pestaña + filtro por resolución (`4ad6b8b`)
- **Descargar** baja el archivo directo: URL firmada con `Content-Disposition=attachment` (el atributo `download` del navegador se ignora por ser cross-origin a S3). Ícono **↗** para abrir en pestaña nueva (URL inline).
- **Filtro por resolución** (desplegable en el toolbar): junta las resoluciones presentes en la carpeta (leídas del thumbnail) y filtra las imágenes. 100% cliente, se resetea al cambiar de carpeta.

### Thumbnails on-demand cacheados en S3 (`da0332e`)
- Endpoint `/api/contenido/thumb`: genera el thumbnail (GD, máx 480px) la 1ª vez, lo cachea en el prefijo `_thumbs` del bucket (disco `contenido_thumbs`) y lo sirve del cache después. Header `X-Res` con la resolución ORIGINAL.
- Frontend: carga los thumbnails **lazy** (IntersectionObserver) vía `fetch` (blob para la preview + `X-Res` para la resolución/filtro). nginx: `location = /api/contenido/thumb` cacheable (rompe el `no-store` global).
- **Impacto: ~1.7 MB → ~60 KB por preview (~28×)**. Nadie espera la imagen full para ver la vista previa. Abrir/descargar siguen usando la imagen completa.
- Fix de encoding: `X-Res` usa `x` ASCII (el `×` multibyte rompe el header HTTP); el front lo formatea a `×`. Ver [[troubleshooting#13. Carácter no-ASCII en header HTTP se ve mal (Ã)|troubleshooting #13]].

**Archivos:** `nginx/default.conf.template` (nuevo), `docker-compose.yml`, `backend/routes/api.php`, `backend/config/filesystems.php`, `backend/app/Http/Controllers/ContenidoController.php`, `backend/resources/views/contenido/publico.blade.php`.

## 2026-07-20 → 22 — Repositorio de Contenido migrado a S3 + UI de marca

El módulo **Contenido** (repositorio de material de marca) pasó de disco local (filesystem-backed + bind-mount SFTP) a un **bucket S3 privado**. Motivo: +10 GB de material que no debía comer disco EBS de la EC2. El resto de adjuntos siguen en disco local. Detalle en [[modulos/contenido]].

### Backend — Contenido sobre S3 (`186e948`)
- **`config/filesystems.php`** (nuevo; antes se usaba el default de Laravel): disco `contenido` (s3, `root`=prefijo `contenido`, `visibility=private`, **`retain_visibility=false`** para no gestionar ACLs por objeto — ver [[troubleshooting#11. Flysystem S3 rompe copy/move por GetObjectAcl|troubleshooting #11]]).
- **`ContenidoController`** reescrito sobre S3: árbol por listado del bucket (los uploads "por fuera" con `aws s3 cp` aparecen solos, reemplaza SFTP), carpeta vacía = placeholder `.keep`, rename = copy+delete por prefijo, archivos servidos con **URLs firmadas temporales** (`temporaryUrl`, TTL 60 min). Bucket **privado** (Block Public Access ON).
- Dependencia `league/flysystem-aws-s3-v3`: en `composer.json` y en el build del Dockerfile (`b832208`); en caliente se instaló con `composer.phar` (el container no trae composer).
- `docker-compose.yml`: vars `AWS_*`/`CONTENIDO_S3_*` (backend+scheduler); se quitó el bind-mount `./contenido-repo`.

### Frontend — UI de la vista pública (`5926516`)
Página pública `contenido/publico` (blade), estilo basado en la investigación de notebooks (Aldrich + Titillium Web + gradiente RGB):
- **Header de marca**: logo oficial **GIGABYTE** (SVG de Wikimedia) en monocromo (`fill=currentColor`), barra RGB superior, pill "Aorus", naranja AORUS `#FF6400`.
- **Orden por Nombre o Fecha de carga** (toggle asc/desc): el backend agrega `fecha` por archivo (S3 `lastModified` = fecha de subida) y la propaga a las carpetas.
- **Metadatos por card**: resolución de imágenes (`ancho×alto`, leída del thumbnail con `onload`), formato de fuentes ("Fuente TTF/OTF") y de otros archivos (extensión), más la fecha.

### ⚠️ Notas
- **Decisión del usuario**: mismo bucket+prefijo (`gigaerp-contenido-dev`, sa-east-1, prefijo `contenido`) para **local y prod** (todo compartido, sin aislar). Versioning ON como red de seguridad. Ver [[contexto#Repositorio de Contenido — S3|contexto]].
- Validado end-to-end contra el bucket real (put/list/URL firmada/rename/delete). Deploy prod: copiar filesystems + controller + blade al container, `config:cache` + `view:clear`; migración one-time `aws s3 sync ./contenido-repo s3://<bucket>/contenido/`.

**Archivos:** `backend/config/filesystems.php` (nuevo), `backend/app/Http/Controllers/ContenidoController.php`, `backend/resources/views/contenido/publico.blade.php`, `backend/composer.json`, `backend/Dockerfile`, `docker-compose.yml`.

## 2026-07-16 — Addons de marketing (lanzadores externos url + token)

Nueva sección **Addons** dentro del grupo Marketing: un catálogo de accesos rápidos a apps externas. Cada addon guarda **nombre, URL, token y descripción**; al hacer clic se abre en una pestaña nueva la **URL con el token concatenado literalmente al final** (`url + token`, sin separador). Commit `455663e`. Persistencia en backend (compartido entre usuarios). Detalle en [[modulos/addons]].

### Backend — CRUD nuevo
- Migración `0044_create_addons_marketing_table.php` → tabla `addons_marketing` (`nombre`, `url` text, `token` text nullable, `descripcion` text nullable, `usuario_id` FK a `usuarios` nullOnDelete).
- Modelo `AddonMarketing` (`$table = 'addons_marketing'`, relación `creador`).
- `AddonMarketingController` → `index` (orden por `created_at`) / `store` (setea `usuario_id` = usuario actual) / `update` / `destroy`.
- Ruta: `apiResource('addons')->only(['index','store','update','destroy'])->parameters(['addons'=>'addon'])`, bajo `auth:sanctum`, en el grupo Marketing.

### Frontend
- `utils/secciones.ts` — sección nueva `VER_SECCION_ADDONS` (label "Addons", ícono `lucide:puzzle`, grupo Marketing). Ya son 14 secciones.
- `pages/addons/index.vue` (nuevo) — botón **Agregar** → modal (nombre, URL, token, descripción); listado en cards; clic abre `url+token` en pestaña nueva (`noopener,noreferrer`); editar/eliminar al hover.

### ⚠️ Notas
- El token se guarda en **texto plano** en DB y viaja literal en la URL (queda en el historial del navegador y en logs del server destino).
- Como todo el sistema de permisos por sección, el bloqueo es **solo frontend**; el endpoint `/api/addons` está abierto a cualquier usuario autenticado.
- Deploy: migración aplicada en caliente (`docker cp` + `migrate --force` + `config:cache`) + rebuild del frontend. Se pusheó **solo Addons** a `main` (sin arrastrar otras ramas).

**Archivos:** `backend/database/migrations/0044_create_addons_marketing_table.php`, `backend/app/Models/AddonMarketing.php`, `backend/app/Http/Controllers/AddonMarketingController.php`, `backend/routes/api.php`, `frontend/utils/secciones.ts`, `frontend/pages/addons/index.vue`.

## 2026-07-02 — Backup/restore completo en ZIP (datos + archivos)

El backup dejó de ser un JSON de solo-base-de-datos y pasó a ser un **ZIP con el dataset completo**, pensado para que *clonando el repo + restaurando el ZIP* se recupere todo (datos, usuarios, documentos e imágenes) sin pasos extra. Rama `feat/backup-completo-zip` (commit `b12ecee`). Detalle en [[arquitectura#Backup/restore completo (ZIP)|arquitectura]] y [[contexto#Backup/restore — reglas|contexto]].

### Backend — `BackupController`
- **`generate()`** arma un `.zip` con `ZipArchive`: `database.json` (volcado de todas las tablas, mismo orden FK de antes) + `files/…` = todo `storage/app/public` recursivo (adjuntos de marketing e imágenes del editor). Se sirve con `response()->download()->deleteFileAfterSend()`.
- **`restore()`** acepta el ZIP nuevo **o** el JSON viejo (compat): detecta el tipo por extensión y por firma `PK\x03\x04`. Restaura tablas (truncate + insert con `FOREIGN_KEY_CHECKS=0`) y extrae `files/*` a `storage/app/public` (merge/overwrite, con guardia anti path-traversal).
- Sube límites en runtime: `ini_set('memory_limit','512M')` + `set_time_limit(300)`.

### Infra — límites para archivos pesados
- **`backend/Dockerfile`**: `conf.d/uploads.ini` con `upload_max_filesize/post_max_size/memory_limit=512M`, `max_execution_time=300`. Antes eran 2M/8M → cualquier ZIP con imágenes fallaba.
- **`nginx/default.conf`**: `client_max_body_size 20M → 512M` + `proxy_read/send_timeout 600s` en `/api/`.

### Frontend — `pages/configuracion/index.vue`
Tab Backups: acepta `.zip,.json`, ícono `lucide:file-archive`, descarga como `.zip`, textos actualizados (datos + documentos + imágenes).

### ⚠️ Gotcha de deploy detectado
El **rebuild limpio del backend está roto**: `docker compose build backend` falla en `composer create-project laravel/laravel:^11.0`. Los cambios se desplegaron **en caliente** (`docker cp` + ini + `docker restart`). Ver [[troubleshooting#10. Rebuild limpio del backend falla (composer create-project)|troubleshooting #10]].

**Verificado local:** genera ZIP (`database.json` 23 MB + 6 archivos), restaura y quedan 15.962 productos + 6 usuarios + archivos en disco intactos.

## 2026-06-29 — Permisos de visualización por sección (sidebar + bloqueo de ruta)

Cada sección del ERP pasa a tener su permiso `VER_SECCION_*`. **Semántica opt-in**: un no-admin solo ve una sección si tiene su permiso; **el admin ve todo**. Detalle en [[arquitectura#Permisos de visualización por sección|arquitectura]] y [[contexto#Permisos por sección — reglas|contexto]].

### Backend — sin cambios
El array `permisos` (`usuarios.permisos`, cast `array`) ya aceptaba strings arbitrarios y `UsuarioController@{store,update}` lo valida como `nullable|array`. Las keys `VER_SECCION_*` se guardan ahí mismo junto a `aprobaciones`/`VER_MONTOS`. **Sin enum ni migración.**

### Frontend
- **`utils/secciones.ts`** (nuevo) — fuente única de verdad: `SECCIONES[]` (key, label, ruta, ícono, grupo) + `permisoDeRuta(path)`. Las 13 secciones: Dashboard, Distribuidores, Proveedores, Stock Bodega, Stock Distri, APIs Distri, Resellers, Órdenes de Venta, Notas de Crédito, Fondos, Calendario, Proyectos, Tareas.
- **`middleware/secciones.global.ts`** (nuevo) — bloquea el acceso directo por URL; si falta el permiso redirige a la primera sección permitida (o `/sin-acceso`). Blinda también `/configuracion` (solo admin). Corre después de `auth.global.ts`.
- **`pages/sin-acceso.vue`** (nuevo) — landing para usuarios sin ninguna sección.
- **`layouts/default.vue`** — sidebar generado desde `SECCIONES`, agrupado, oculta encabezados de grupo vacíos (reemplaza los `v-if puedeVer()` parciales anteriores).
- **`pages/configuracion/index.vue`** — checkboxes "Secciones visibles" por usuario (reusa `togglePermiso`, las keys viven en el mismo array `permisos`), atajo "Marcar/Desmarcar todas", badges legibles.
- **Seeders** (`UsuarioSeeder`, `DemoSeeder`) — operativos demo con secciones para no romper la demo bajo opt-in; se corrigieron claves viejas (`VER_SECCION_ACCIONES`→`CALENDARIO`, `VER_SECCION_VENTAS`→`ORDENES`).

⚠️ **El bloqueo es solo de frontend** (sidebar + route guard). Los endpoints siguen abiertos a cualquier usuario autenticado — para rechazo real falta agregar policies por endpoint en el backend.

**Archivos:** `frontend/utils/secciones.ts` (nuevo), `frontend/middleware/secciones.global.ts` (nuevo), `frontend/pages/sin-acceso.vue` (nuevo), `frontend/layouts/default.vue`, `frontend/pages/configuracion/index.vue`, `backend/database/seeders/{UsuarioSeeder,DemoSeeder}.php`.

---

## 2026-06-23 — Filtro de stock por origen, onboarding/vaciado, e importaciones con peso

### Filtro `con_stock`/`sin_stock` ahora contempla stock de terceros (commit `72268f7`)
El filtro de stock en `ProductoController@index` solo miraba `stock_deposito`, que únicamente existe para productos propios. Los productos de **terceros** (distribuidores con API / Resellers) guardan su disponibilidad en la columna `productos.stock` (la sincroniza [[modulos/resellers|SincronizarApiController]] desde el mayorista) y **nunca tienen filas en `stock_deposito`** → con el filtro viejo, `con_stock` los excluía a todos y `sin_stock` los incluía a todos.

Ahora el filtro **ramifica por origen** (un `where(fn)` con dos sub-`where` unidos por `orWhere`):
- **Propios** (`distribuidor_id IS NULL`): por `stock_deposito.cantidad > 0` en depósito NO ilimitado (igual que antes; la columna global `productos.stock` no cuenta).
- **Terceros** (`distribuidor_id NOT NULL`): `con_stock` = `stock > 0`; `sin_stock` = `stock <= 0 OR stock IS NULL`.

Matiz importante: la columna `productos.stock` es basura del import **para los propios**, pero es la fuente de verdad **para los terceros**. Ver [[contexto#Reglas de stock|contexto]].

Precursor relacionado (commit `320a645`, 2026-06-16): `precios()` ahora filtra `whereNull(distribuidor_id) + whereHas(stocks)` para listar/exportar **solo internos con inventario real**, excluyendo los ~1800 productos sin distribuidor y sin stock (basura del import).

### Onboarding: vaciado de ERP, asistente inicial y autor de productos (commit `2c45e61`)
Prepara el ERP para entregarlo a un cliente nuevo desde cero.
- **`php artisan erp:vaciar`** (`Console/Commands/VaciarErp.php`): deja la base limpia conservando **admin, depósitos y configuración**; evita el re-seed de boot. Ignora `/backups/` en git (dumps de base).
- **Asistente de configuración inicial** en el dashboard (`components/AsistenteInicial.vue` + `utils/onboarding.ts`): guía el camino **usuarios → mercadería → precios → stock → distribuidores**, con autodetección de cada paso vía `GET /api/onboarding/estado` (`OnboardingController`).
- **Autor de productos** (`created_by`, migración `0044`): alta manual e importación masiva registran el usuario; se muestra en el catálogo. `ProductoResource` expone el campo.

**Archivos:** `Console/Commands/VaciarErp.php` (nuevo), `OnboardingController.php` (nuevo), `frontend/components/AsistenteInicial.vue` (nuevo), `frontend/utils/onboarding.ts` (nuevo), migración `0044`, `Producto.php`, `ProductoResource.php`, `ImportacionCatalogoController.php`, `frontend/pages/{index,mercaderia/catalogo}`, `routes/api.php`.

### Importaciones de mercadería: cartón, qty y kg por ítem (commit `e9ec075`)
Columnas `carton`/`qty`/`kg` por ítem de importación y totales de cabecera (`total_carton`/`total_qty`/`total_kg`), con captura en el wizard de importación y la vista de detalle.

**Archivos:** `ImportacionMercaderiaController.php`, `Models/{ImportacionMercaderia,ItemImportacionMercaderia}.php`, migración `add_carton_qty_kg_to_importaciones_mercaderia`, `frontend/pages/mercaderia/importaciones/{nueva,[id],index}.vue`.

---

## 2026-06-17 — Guía interactiva / tour de onboarding por sección

Sistema de **ayuda paso a paso** que se activa en cada sección del ERP. Sin dependencias externas — motor propio. Detalle en [[arquitectura#Guía interactiva (onboarding tour)|arquitectura]] y [[contexto#Guía interactiva — reglas|contexto]]. *(En working tree, sin commit aún.)*

### Cómo funciona
- **Botón "Ayuda"** (`lucide:circle-help`) en el topbar → arranca la guía de la sección actual. Solo aparece si hay guía para esa ruta.
- **Auto-inicio**: la primera vez que se visita una sección, la guía salta sola. Una vez cerrada queda marcada como vista en `localStorage` (key `gigaerp_guias_vistas`) y no vuelve a saltar.
- Cada paso resalta un elemento real con *spotlight* (`box-shadow: 0 0 0 9999px`) + tooltip, o se muestra centrado si no hay `target`.
- Navegación: Anterior / Siguiente / Finalizar, puntitos de progreso clickeables, contador "X de N", atajos de teclado (→/Enter, ←, Esc).

### Piezas (todo en `frontend/`)
- `utils/guias.ts` (nuevo) — contenido por sección. `guias: GuiaSeccion[]`, cada una `{ clave, titulo, pasos[] }`. `PasoGuia = { titulo, texto, target?, posicion? }`. `target` = selector CSS; sin él, paso centrado.
- `composables/useGuia.ts` (nuevo) — estado global singleton (patrón `useNotification`). Match de ruta por la clave-prefijo más larga. `localStorage` de vistas. Expone `iniciar`, `iniciarSiPrimeraVez`, `siguiente`, `anterior`, `irA`, `cerrar`, `hayGuia`.
- `components/GuiaTour.vue` (nuevo) — overlay con `<Teleport to="body">`, spotlight + tooltip, recálculo en resize/scroll.
- `layouts/default.vue` — botón Ayuda en topbar, auto-inicio (`onMounted` + `watch(route.path)`), `<GuiaTour />` montado.
- `components/NavItem.vue` — `:data-guia="'nav-' + to"` para anclar pasos a los ítems del menú.

### Anclajes `data-guia` disponibles
`nav-<ruta>` (cada ítem del sidebar), `topbar-search`, `topbar-ayuda`.

### Para extender
Editar solo `utils/guias.ts`. Para anclar a un botón de página, agregar `data-guia="..."` al elemento y referenciarlo en el paso. Hoy los pasos de página son centrados (no se tocaron las páginas); solo los de menú están anclados.

**Archivos:** `frontend/utils/guias.ts` (nuevo), `frontend/composables/useGuia.ts` (nuevo), `frontend/components/GuiaTour.vue` (nuevo), `frontend/layouts/default.vue`, `frontend/components/NavItem.vue`

---

## 2026-06-16 — Listas de precio: nombres, default por cliente, permisos por usuario

Tres features sobre las 4 listas de precio (`productos.precio_lista_1..4`). Detalle en [[contexto#Listas de precio — reglas|contexto]].

### Nombres configurables de listas (commit `cfa87c1`)
- Se guardan en la tabla `configuraciones` (claves `nombre_lista_1..4`) vía `/api/config` — sin migración ni tabla nueva.
- Composable `frontend/composables/useListasPrecio.ts`: cachea nombres en `useState` y expone `labelLista(n)` → "Lista N · Nombre" (fallback "Lista N").
- Se editan en Configuración → pestaña "Listas de precio". Se muestran en OrdenItems, stock, precios y edición de productos.

### Lista de precio por defecto del cliente (commit `b1dd6f4`)
- Migración `0042`: `clientes.lista_precio_defecto` (tinyint nullable).
- Al armar orden, los ítems entran con la lista preasignada del cliente (overrideable por ítem). `OrdenItems` recibe prop `cliente`.
- Selector en la edición del cliente (con nombres de lista).

### Permisos de lista por usuario (commit `c33be1e`)
- Migración `0043`: `usuarios.listas_precio` (JSON). **Admin = todas; no-admin = exactamente las asignadas; vacío/null = todas** (no bloquea).
- `Usuario::listasPermitidas()`; `UsuarioResource` expone `listas_precio` (cruda) y `listas_permitidas` (efectiva).
- Checkboxes por lista en Configuración → Usuarios. Los selectores muestran solo las listas permitidas; la lista inicial respeta permisos.
- `OrdenVentaController::validar()` rechaza con 422 si un no-admin manda una lista no permitida.
- ⚠️ Un usuario ya logueado no ve sus nuevas restricciones hasta re-login (front cachea `usuario`); el backend sí las aplica siempre.

### Importación masiva de precios por global_part (commit `554527a`)
- Botón **Importar** en Mercadería → Precios (junto al export existente). Flujo: exportar `.xlsx` → editar → re-importar.
- **El archivo se parsea en el navegador** con SheetJS (misma librería del export) y se mandan las filas como JSON → esquiva que el container NO tenga PhpSpreadsheet. Funciona `.xlsx` y `.csv`.
- Detección tolerante de columnas: `Global Part` + `Lista N` (aunque el header tenga el nombre, ej. "Lista 1 · Mayorista"). Solo actualiza las columnas de lista con valor; las vacías quedan igual.
- Backend `POST /api/precios/importar` (`ProductoController@importarPrecios`): update por `global_part` sobre productos propios. Devuelve `{ actualizados, productos_afectados, omitidos, errores }`. Sin migración.

**Archivos:** `migrations/0042,0043`, `Cliente.php`, `Usuario.php`, `Cliente/UsuarioResource.php`, `Cliente/Usuario/OrdenVentaController.php`, `frontend/composables/useListasPrecio.ts` (nuevo), `frontend/pages/{clientes,configuracion,mercaderia/{stock,precios},productos,ordenes-venta/{nueva,[id]}}`, `components/OrdenItems.vue`

---

## 2026-06-16 — Depósito con stock ilimitado + reglas de catálogo/stock propio

Sesión de trabajo sobre depósitos, stock y qué entra en Catálogo / Stock Bodega. Detalle en [[contexto#Stock y depósitos — reglas|contexto]].

### Depósito "Stock Ilimitado" (migración `0041`)

Nueva columna `depositos.stock_ilimitado` (boolean default false). Al armar una orden o pre-orden con un depósito ilimitado se puede poner **cualquier cantidad**, sin tope de stock.

- Backend: `Deposito` (fillable + cast), `DepositoController` (validación en store/update). El endpoint `/depositos` ya devuelve el flag.
- Frontend Depósitos: checkbox "Stock ilimitado" en el modal + badge ∞ en la card.
- `OrdenItems.vue`: si el depósito es ilimitado libera el tope de cantidad, permite agregar aunque el stock sea 0, lo incluye siempre en el selector y muestra **∞**.
- Stock Bodega: la columna de un depósito ilimitado muestra ícono `lucide:infinity`.
- ⚠️ El backend HOY no descuenta ni valida stock en ningún momento — el tope real solo lo imponía el frontend, que es lo que el flag libera.
- Fix (`8a9eee5`): en Stock Bodega el `+` del pedido estaba deshabilitado para productos sin stock físico. `depositoDe` ahora cae al depósito ilimitado si no hay stock real y `maxStock` devuelve `Infinity`, habilitando el stepper sin tope → se pueden agregar al pedido los productos disponibles por depósito infinito.

### Definición de "producto propio" y filtro de stock por depósito

- **Producto propio = `distribuidor_id IS NULL`** (creado a mano o por carga masiva de catálogo). Los productos con distribuidor van a Stock Distri / APIs Distri / Resellers y NO se mezclan.
- **Catálogo** (`solo_catalogo`) y **Stock Bodega** (`solo_inventario`) ahora filtran `whereNull('distribuidor_id')` — muestran TODOS los propios, tengan o no stock. La disponibilidad la maneja el filtro de stock, no la membresía.
- Se agregaron pestañas **Todos / Con stock / Sin stock** a la pantalla Catálogo.
- **Filtro de stock 100% basado en `stock_deposito`**, NO en la columna global `productos.stock` (basura del import: `StockController@update` solo toca `stock_deposito`, nunca la columna global):
  - `con_stock` = existe `stock_deposito.cantidad > 0` en un depósito **no** ilimitado.
  - `sin_stock` = negación exacta (sin filas, todo en 0, o solo en depósito ilimitado).
  - **Depósito ilimitado NO cuenta como "con stock"** (el infinito no es stock real).

### Quirk de datos detectado

~1819 productos propios pero solo **12 con inventario real** (seedeados GIGABYTE, codigo_distribuidor `GB-*`); los otros ~1807 entraron sin distribuidor pero sin filas de stock. Quedan visibles en Catálogo bajo "Sin stock"/"Todos". Pendiente decidir limpieza. Ver [[contexto#TODOs pendientes]].

**Archivos:** `backend/database/migrations/0041_add_stock_ilimitado_to_depositos_table.php` (nuevo), `app/Models/Deposito.php`, `app/Http/Controllers/DepositoController.php`, `app/Http/Controllers/ProductoController.php`, `frontend/components/OrdenItems.vue`, `frontend/pages/mercaderia/depositos/index.vue`, `frontend/pages/mercaderia/stock/index.vue`, `frontend/pages/mercaderia/catalogo/index.vue`

---

## 2026-06-11 — Carga masiva y edición de catálogo GIGABYTE

Pedido del contacto de GIGABYTE (mail): poder cargar la base de productos con campos propios del catálogo (sin stock) y cruzar el stock después.

### Campos de catálogo en `productos` (migración `0040`)

Nuevas columnas: `bu_code`, `chipset`, `item_no`, `global_part`, `link`, `ean`, `carton_box_qty`, `carton_peso_kg`, `carton_largo_mm`, `carton_ancho_mm`, `carton_alto_mm`. **UPC NO se usa** (explícito en el mail).

**Convención clave:** en el catálogo GIGABYTE `sku` = `codigo_distribuidor` = **ITEM NO**, `nombre`/`modelo` = Global Part, `marca`=GIGABYTE, `distribuidor_id`=null. Así el importador de stock de mercadería existente (matchea por sku/codigo_distribuidor) cruza el stock por ese código sin cambios.

### Importador masivo de catálogo (`ImportacionCatalogoController`)

- `POST /api/importaciones-catalogo/parsear` — sube xlsx/csv, devuelve headers + filas + campos mapeables
- `POST /api/importaciones-catalogo` — **upsert** de productos por `item_no` (crea/actualiza, no duplica); devuelve `{creados, actualizados, omitidos, errores}`
- Parseo **CSV nativo** (`fgetcsv`, detecta delimitador `, ; \t`) + xlsx vía PhpSpreadsheet si está disponible

### Frontend

- `/productos/importar` — wizard subir → mapear (auto-detecta las columnas del mail) → resultado. Botón "Cargar catálogo" en `/productos`.
- Toggle **"Mostrar stock"** en la lista de productos (oculta columna + badge en grid/lista).
- Bloque "Datos de catálogo" en el modal de detalle del producto.
- **Pestaña Catálogo** en Inventario (`/mercaderia/catalogo`), junto a Stock · Depósitos · Subir Masivo — listar / editar / crear productos con todos los parámetros del catálogo. ITEM NO se mantiene sincronizado con SKU al guardar.

### Gotchas resueltos

- `$request->validate()` con reglas anidadas (solo `mapping.item_no`) devuelve **únicamente las claves validadas** del array → se perdían los demás mapeos. Fix: `'mapping.*' => 'nullable|integer|min:0'`.
- `productos.codigo_distribuidor` es NOT NULL sin default → al crear, setear = item_no.
- **PhpSpreadsheet no está instalado en el container** (imagen vieja; `maatwebsite/excel` figura en composer.json pero nunca corrió `composer install`) → rompe el parseo xlsx en AMBOS importadores (catálogo y mercadería). CSV anda; para habilitar xlsx falta `docker compose build backend`. Ver [[troubleshooting#8. PhpSpreadsheet no instalado en el container|troubleshooting]].

**Commit:** `d08b3a4`
**Archivos:** `backend/app/Http/Controllers/ImportacionCatalogoController.php` (nuevo), `Producto.php`, `ProductoController.php`, `ProductoResource.php`, `database/migrations/0040_add_catalogo_campos_to_productos_table.php`, `routes/api.php`, `frontend/pages/productos/importar.vue` (nuevo), `frontend/pages/mercaderia/catalogo/index.vue` (nuevo), `productos/index.vue`, tabs en `mercaderia/{stock,depositos,importaciones}`

---

## 2026-06-04 — Integración partpicker + módulo Resellers

### Integración real con API partpicker (`SincronizarApiController`)

Reemplazó la simulación del botón "Sincronizar APIs" por integración real con `https://partpicker.blustudioinc.com`.

**Fuentes mayoristas disponibles:** Air (8368 items), Ceven (466), Invid (1203), Stylus (908).

Flujo de sincronización desde el modal en `/productos`:
1. `GET /api/sincronizar/fuentes` — lista fuentes mayoristas (sin prefijo `preciosgamer_`)
2. Por cada fuente: `POST /api/sincronizar/{source}` — upsert masivo paginando 500 items
   - Crea el `Cliente` (distribuidor) si no existe
   - Upsert por `(distribuidor_id, codigo_distribuidor)`
   - Mapea: `nro_parte → modelo`, `precio_sin_iva → precio_usd`, `stock → stock`
3. `POST /api/sincronizar/vincular-skus` — asigna `sku = strtoupper(trim(modelo))` a todos los productos sin SKU; habilita agrupación en Stock Distri

**Gotchas resueltos en esta sesión:**
- `stock` puede venir negativo (`-1`) → `max(0, (int)$item["stock"])`
- `precio_sin_iva`, `precio_final`, `pct_iva` pueden ser null → defaults `0, 0, 21`
- Ruta `vincular-skus` debe declararse **antes** del wildcard `{source}` en routes/api.php

**Distribuidores nuevos en DB:** Ceven (id=5), Stylus (id=6) — creados al primer sync.

**Commit:** `b7c7377`
**Archivos:** `backend/app/Http/Controllers/SincronizarApiController.php` (nuevo), `backend/routes/api.php`

---

### Módulo Resellers (`ResellersController` + `/resellers`)

Nueva sección que muestra productos de resellers (37 tiendas vía PreciosGamer) directamente desde la API, sin importar a la DB.

- `GET /api/resellers/fuentes` — lista resellers (fuentes con prefijo `preciosgamer_`)
- `GET /api/resellers/items` — proxy a partpicker con filtros: source, fabricante, isinstock, q, limit/offset

**Frontend `/resellers`:** tabla live con imagen, nombre, link a ficha, nro_parte, marca, categoría, precio ARS (`precio_convertido`, no `precio_ars` que siempre es null), badge de stock. Paginación 50 en 50.

**Sidebar:** "Resellers" agregado debajo de "APIs Distri" en sección Operaciones.

**Archivos:** `backend/app/Http/Controllers/ResellersController.php` (nuevo), `frontend/pages/resellers/index.vue` (nuevo), `frontend/layouts/default.vue`

---

### Filtro de marca con default GIGABYTE

Agregado en tres secciones:
- **APIs Distri** (`/productos`): input marca, `filtroMarca = "GIGABYTE"`, param `?marca=` → `WHERE marca LIKE "%X%"`
- **Stock Distri** (`/existencias`): ídem, param `?marca=` en `ExistenciaController`
- **Resellers** (`/resellers`): input marca, `filtroMarca = "GIGABYTE"`, param `?fabricante=` → exact match case-insensitive en partpicker

El filtro se puede borrar para ver todas las marcas.

**Archivos:** `backend/app/Http/Controllers/ProductoController.php`, `backend/app/Http/Controllers/ExistenciaController.php`, `frontend/pages/productos/index.vue`, `frontend/pages/existencias/index.vue`

---

