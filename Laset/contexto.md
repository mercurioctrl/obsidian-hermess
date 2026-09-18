# Contexto

Ver también: [[Laset]] · [[arquitectura]] · [[changelog]] · [[memoria]]

## Origen
El ERP Laset estaba repartido en repos individuales (mayormente `New-Bytes` / `LibreOpcion`).
Se consolidó en dos monorepos (`frontErp`, `backErp` de `LasetCorp`) eliminando los `.git`
anidados. Commits firmados como `Catriel <catrielmercurio@gmail.com>` (la cuenta `mercurioctrl`,
NO `hermess87`).

## Decisiones tomadas (2026-09-02)
- **Convivencia con otra empresa**: el host ya corre el ERP de NB/"blu". Se eligió sufijo `laset`
  + puertos nuevos (backs 81xx, fronts 39xx) para correr ambos en paralelo.
- **DB `NB_WEB` sin renombrar** (es compartida y debe existir). El endpoint correcto y alcanzable
  es `db-nb-massql-dev.blu.net.ar,4444` (user `cmercurio`), no los IPs del backup.
- **`inventario`** no tiene back propio en `backLaset`; se apuntó tentativamente a `ms-metadata`
  (:8185). **Pendiente confirmar** si es el back correcto.
- **Secretos**: los `.env` no se commitean. El `.env` de `ms-metadata` estaba trackeado en el repo
  original; en el monorepo quedó excluido.

## Cosas que no funcionaron (y por qué)
- Build directo de los Dockerfile PHP → `pecl install sqlsrv` incompatible con PHP 7.4.
  Se reutilizaron imágenes ya construidas, re-etiquetadas `*-laset`.
- IPs de DB del backup (172.31.10.208, 192.168.0.42) → sin ruta desde este host (LAN 10.10.10.x).
- Una red Docker por app → pool de subredes del host agotado. Se usó `laset-net` compartida.
- `instances: 'max'` en PM2 → 24 procesos por front, agota la RAM del host compartido. Se bajó a 2.

## Convenciones de trabajo (feedback del usuario)
- Commits/PRs a nombre de **`Catriel <catrielmercurio@gmail.com>`** (cuenta `mercurioctrl`).
- **Nunca** adjudicarse autoría ni co-autoría: sin `Co-Authored-By` ni "Generated with" en commits,
  PRs, docs ni ningún artefacto.

## Decisiones (2026-09-04)
- **Flujo de trabajo del front**: toda funcionalidad sale de una rama `feature/*` creada desde
  **`origin/blu-dev-staff` (remoto)** y se abre PR contra `blu-dev-staff`. No usar `main` local (divergió).
  Ver [[memoria#Flujo git del front (monorepo `frontErp`)]].
- **Ocultamientos reversibles**: los pedidos de "sacar/ocultar" columnas, pestañas, botones y checkboxes se
  implementan **comentando** el código (HTML en templates, `/* */` en JS), no borrando, para poder revertir.
- **Módulo presupuestos**: vivía en el repo interno New-Bytes y no estaba en el monorepo; se portó a
  `frontErp` de forma aditiva, ya sin IVA/Imp. Interno.
- **Columna en blanco de Órdenes (compras)**: no existía como columna; era artefacto de columnas
  `fixed: 'left'`. Se resolvió quitando `fixed` de Fecha/Nº Orden/Pedido (dejan de quedar fijas al scrollear).
- Detalle de los 5 PRs en [[changelog]].

## Decisiones (2026-09-09)
- **Firebase opcional en expedición**: si faltan las `FIREBASE_*` en el `.env`, el front no debe romper.
  Se inicializa Firebase solo con config válida (`projectId`/`apiKey`/`appId`) y se protegen las llamadas
  (`getMessaging()` rompía el arranque del cliente con un 500). Patrón defensivo.
- **Cobro múltiple transaccional (cobros)**: el cobro conjunto escribe en dos fases (registro por pedido +
  consolidación en caja `MC_LOG_OPERACIONES`/`MC_SALDOS_CAJA`). Ahora van dentro de una única transacción y
  se valida cta cte **antes** de escribir, para evitar cobros a medias (cliente cobrado / caja sin impactar).
- **`ultimaVenta` con fallback (metadata)**: `A.ULTIMA_VENTA` del ERP no se actualiza para algunos artículos;
  se usa `MAX(albclit.dfecalb)` de ventas reales (`ntipoalb > 1`, excluye reservas) como fallback.
- **`AfterSaleRepository` COUNT sin `$joins`**: decisión explícita del usuario — dejar el método de conteo
  sin concatenar `$joins` (no aplica esos filtros de estado). No es un bug pendiente.
- **Libre Opción fuera del menú (pedidos)**: sección oculta con `visible: false` (no se usa en Laset); no se
  borran rutas/páginas/store de `libreOpcion`.
- **Secretos en `.env-example`**: se detectaron credenciales reales en el `.env-example` de postventa del
  working tree local; se dejaron **sin subir**. `.env-example` está trackeado (a diferencia del `.env`), así
  que no debe contener secretos. **Pendiente**: rotar esas credenciales si son válidas.

## Decisiones (2026-09-11 · listas de precio por color)
- **Modelo de precios propio de Laset**: 4 listas de color (Azul, Verde, Naranja, Violeta), cada una
  `base × (1 + % propio)`. Reemplaza en la práctica el esquema npvp/ntarifapp heredado de NB.
- **Asignación al cliente: las dos**. Lista por defecto por cliente **y** override editable en el modal
  de la orden. El usuario pidió explícitamente ambas, no una u otra.
- **Tablas nuevas y dedicadas** en vez de reusar `priceList` (existía vacía): `LASET_LISTA_COLOR`,
  `LASET_LISTA_COLOR_ARTICULO`, `LASET_CLIENTE_LISTA_COLOR`.
- **Alcance `companyCode 11`**: las otras empresas del clon siguen con npvp/ntarifapp intacto.
- **Pendiente**: cargar a mano los nombres y % reales desde la UI (los actuales son placeholder).

## Decisiones (2026-09-15/16 · dominio único y SSO)
- **Un solo dominio, `laset.local`**, con cada app bajo su path. El usuario venía entrando por puerto
  y tenía que loguearse en cada app; ahora se entra una vez.
- **Menú de aplicaciones en el header de las 6 apps** (no una landing en la raíz): se eligió el
  switcher porque permite saltar sin volver al inicio, que es lo que espera un ERP.
- **Header de inventario igualado a 64px**: tenía 55px y rompía la uniformidad del conjunto
  logo + menú. Decisión del usuario ante la alternativa de dejarlo distinto.
- **Permisos: siempre releídos de la base, nunca del payload del token.** Es la regla que hace que el
  SSO funcione; la alternativa (meter todos los permisos en un token único) se descartó por tocar el
  login de cada back y agrandar el token.
- **Postventa: `Encrypt = 1; TrustServerCertificate = 1`** en vez de copiar el `Encrypt = 0` que usa
  cobros: mantiene la conexión cifrada y solo omite validar el certificado autofirmado.
- **Menú limpio de `*.saftel.com`**: 28 accesos al dominio de la otra empresa, comentados (no borrados).
  "Reportes" queda, porque apunta a Jira, no a saftel.
- **Ocultamientos reversibles**: se mantiene la convención de comentar (HTML en templates, `/* */` en
  JS) en vez de borrar.

## Decisiones (2026-09-17/18 · importación de la planilla)
- **Importar todo ≠ reimportar**: la cadena no borra nada, así que reimportar la planilla sobre
  una empresa ya cargada **exige wipe previo**. La primera pasada quedó inflada y se rehízo.
  Ver [[import-planilla-comp11]].
- **Las 7 OCs de prueba con almacén `SAF` se borraron** (decisión del usuario), en vez de
  asignarles un depósito válido: eran basura de pruebas con proveedores `Proveedor Testing
  Laset` / `nuevo proveedor`, dos sin líneas.
- **No se dan de alta proveedores desde la hoja `Database Proveedores`**: 26 nombres de la
  planilla no existen en comp=11 y se dejaron afuera a propósito — los crea Fase C cuando
  aparecen en una venta. El importador nuevo sólo rellena campos vacíos, nunca pisa.
- **No se regeneró `eccCategorias.csv`** desde la planilla nueva: se comprobó que no aporta un
  solo vínculo (las claves que agrega son de proveedores inexistentes en comp=11) y ensucia con
  una fila `-`.
- **El % de un precio manual es derivado, no persistido**: si cambia el costo, se recalcula.
- **Validación de subida por extensión + firma ZIP**, no por libmagic. Es más específica que
  `mimes`, y el contenido igual se valida después (openpyxl + headers canónicos).

## Decisiones (2026-09-18 · una sola empresa)
- **`companyCode` fijo por configuración, no por datos**: `FORCE_COMPANY_CODE=11` en el `.env`
  de cada back en vez de `UPDATE agentes SET companyCode = 11`. De los 68 agentes de esta base
  sólo 4 son de Laset: cambiarlos todos habría llenado los selectores de Vendedor con los 46 de
  NB y roto el aislamiento comp=11 que respeta el importador. Es reversible quitando la variable
  y no afecta a NB, que no la define.
- **Se encendió `ASSIGNMENT_FEATURE_ENABLED`** (kill switch de asignación OC ↔ venta), también
  como default en el `.env-example`: los datos ya estaban y sin el flag no se veían.
- **Las 29 OCs sin cotización se repararon con UPDATE**, no se re-importaron: el resto del
  import estaba bien y rehacerlo costaba una hora.

## Decisiones (2026-09-18 · barrido del `router.base`)
- **Se barrieron los 7 fronts, no sólo el bug reportado**: el 404 de compras era una de cuatro
  formas de la misma falla. Aparecieron tres más, dos de ellas mudas (el modal de versión vacío y
  el logo roto de la pantalla pública) que nadie habría reportado.
- **Los comprobantes de cobros y expedición se reapuntaron al servicio local de Laset**, que antes
  iban al de NB (`omega.`/`gamma.comprobantes.lio.red`). Es lo correcto —los datos están en la base
  de Laset— pero es el cambio con más superficie de la tanda y **falta probarlo a mano**.
- **No se tocó el `resolve().href` de `itemsPrices.vue`** (`productHref`): ahí alimenta un
  `<a :href>` y sí necesita el base. Tampoco el manifest: lo genera `@nuxtjs/pwa` ya prefijado.

## Decisiones (2026-09-18 · cta cte de proveedores en euros)
- **Cada movimiento a su cotización real**, no todo al TC de cierre. La diferencia de cambio
  queda en una línea explícita en vez de repartida en todas las facturas.
- **Columnas nuevas en el ledger** (`IMPORTE_ORIGEN`, `MONEDA_ORIGEN`) en vez de reutilizar
  `MONEDA`, que en los datos de la otra empresa ya usa 1/2/15 con una semántica que no está
  documentada en esta base. Aditivas y anulables: los lectores hacen `ISNULL(...)`.
- **El cierre se parte en dos líneas** porque son dos cosas distintas: el saldo declarado por
  la planilla y el efecto FX.
- **Se quitó la columna "$"** de la cuenta corriente, en línea con "es todo en dólares".

## Pendiente de decisión (nuevo)
- Los **22.863,50 €** del "Ajuste de cuenta" de Danicoop: la planilla declara un saldo que no
  es la suma de sus propios movimientos (Debe−Haber 61.870,50 vs 39.007,00 declarado) y
  absorbe la diferencia en su columna "Saldo EUR" sin dejar rastro. Si se sabe de dónde
  salen, corresponde cargarlos como lo que son en vez de como ajuste.
- **HENKELMAN** (002613) quedó marcada como cuenta en euros pero su hoja no tiene columna TC,
  así que vale 1:1 con el dólar. Revisar si es realmente una cuenta en euros.

## Deuda técnica anotada
- **Cobros conecta a SQL Server sin cifrado** (`Encrypt = 0` en su DSN). Venía así; el usuario decidió
  anotarlo y seguir.
- **El vhost de Apache no está versionado** en ningún monorepo: vive solo en el host.
- **Secretos en `.env-example`** (ver 2026-09-09): sigue pendiente rotarlos.

## Pendiente de decisión
- Dos deep-links a `saftel.com` **fuera del menú** (`DetailExamine.vue` en inventario,
  `AsignarOCModal.vue` en pedidos): ¿reapuntar a `laset.local/...` o sacar? (los del **menú**
  ya se ocultaron, 2026-09-18)
- **ECCN**: 23 clasificaciones aduaneras no entran porque 4 proveedores (`LST GLOBAL`, `ASUS
  COMPUTER INTERNATIONAL`, `PNY`, `ZOTAC`) y 18 categorías no existen en comp=11. Darlos de
  alta o dejarlas afuera.
- La raíz del dominio hoy redirige a `/inventario/`; se puede cambiar a `/pedidos/`.

## Estado actual (2026-09-18, tarde)
Los 7 fronts (PM2, 2 instancias c/u) y 7 backs (Docker) **operativos** en `laset.local`, con SSO.

**comp=11 recargado desde la planilla del 2026-09-17**: 661 OCs, 623 ventas, 1.062 artículos,
0 stock negativo, staging con 4.458 filas `IMPORTED` linkeadas. Ver [[import-planilla-comp11]].

Mergeado a `blu-dev-staff`: todo lo anterior + fixes del importador, favicons, fix del menú,
grilla de precios por color, los 2 commits de listas de color que habían quedado colgados y
`feature/laset-ocultamientos-ui` (PR #15).

Abierto: **`fix/router-base-doble-prefijo`** (3 commits), con el barrido del `router.base`. Ya
aplicado y verificado en este host. Ojo con el duplicado del href del favicon: el mismo cambio
vive en `fix/favicon-href-router-base`, que nunca se mergeó.

Sin subir (y no se suben): `.env-example` y `package-lock.json` del sync de New-Bytes.

Pendiente operativo: apretar **Re-vincular facturas** (398 facturas esperando), desplegar los
fixes en el dev de blu, y limpiar 6 snapshots viejos (85 tablas `laset_snap_*`).
