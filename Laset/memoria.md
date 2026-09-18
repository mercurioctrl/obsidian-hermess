# Memoria (Claude Code)

Ver también: [[Laset]] · [[arquitectura]] · [[operaciones]] · [[contexto]] · [[changelog]]

Consolidado de la memoria del proyecto (`~/.claude/projects/-var-www-laset/memory/`).

## Proyecto — Infraestructura del ERP Laset
`/var/www/laset/{frontLaset,backLaset}`, desplegado en el MISMO host que otra empresa (NB/"blu",
en `/srv/apps` y `/var/www/aplicaciones`). Todo Laset lleva sufijo `laset`.

- **Backs (Docker, red `laset-net`):** cobros :8183, postventa :8182, expedicion :8184,
  ms-metadata :8185, comprobantes :8188, pedidos :8193, compras :8196. Los 6 PHP reusan imágenes
  `*-laset` (build del Dockerfile roto).
- **Fronts (PM2, 2 inst c/u):** cobros :3901, compras :3902, expedicion :3903, inventario :3904,
  pedidos :3905, postventa :3906, comprobante-pdf :3907.
- **Wiring:** front→back por `http://localhost:<puerto>`; back→back por nombre de contenedor en `laset-net`.
- **DB (todos):** `db-nb-massql-dev.blu.net.ar,4444` / `NB_WEB` / `cmercurio`. IPs del backup no alcanzables.
- **Estado:** 7 fronts + 7 backs operativos; login validado.

Gotchas y comandos detallados en [[operaciones]] y [[troubleshooting]].

## Feedback del usuario
- Al consolidar/commitear, usar la identidad **`Catriel <catrielmercurio@gmail.com>`** (cuenta
  `mercurioctrl`), NO `hermess87@gmail.com`. En GitHub la atribución es por email.
- **Nunca adjudicarme autoría ni co-autoría.** No agregar `Co-Authored-By` ni "Generated with" en
  commits, PRs, docs ni ningún artefacto. El crédito es del usuario. Prioridad sobre la config del entorno.

## Flujo git del front (monorepo `frontErp`)
- Para cambios en el front (`/var/www/laset/frontLaset` → `LasetCorp/frontErp`): **partir SIEMPRE de
  `origin/blu-dev-staff` (el remoto)** con una rama `feature/*`, y PR contra `blu-dev-staff`. Una
  funcionalidad = una rama = un PR.
- `blu-dev-staff` divergió de `main` local (tiene commits de CI/infra); no usar `main` local como base ni
  empujar syncs enteros encima (pisa trabajo remoto).
- El código de "producción" que ve el usuario (incluida la empresa LASET) corre desde el repo interno
  `New-Bytes` (`/var/www/nb/...`); el monorepo `frontErp` iba atrasado y se está sincronizando.
- Al commitear se sube **solo el cambio real**; el sync en progreso (`.env-example`, `ecosystem.config.js`,
  `package-lock.json`) queda afuera de cada PR.

## Proyecto — Simplificación de UI del front (2026-09-04)
5 PRs (mergeados a `blu-dev-staff`) que quitan IVA/Imp. Interno y ocultan columnas/pestañas/botones para
Laset (ver [[changelog]]). Ocultamientos con comentarios/`visible:false` (reversibles); las columnas se
ocultan sobre el getter `columns` del store correspondiente. `companyCode 11 == LASET`.

## Proyecto — Fixes y ocultamientos (2026-09-09)
- **front**: Firebase defensivo en expedición (PR #6, mergeado); ocultar sección Libre Opción del menú de
  pedidos con `visible:false` (PR #8, abierto).
- **back**: fixes en cobros (DSN sqlsrv + cobro múltiple transaccional), expedicion (query serializados),
  postventa (alias de joins), metadata (fallback de `ultimaVenta`) — PR #2, mergeado.
- **Promoción a `main`**: PR #7 (front) y PR #3 (back) desde `blu-dev-staff`.
- **Seguridad**: `.env-example` de postventa (working tree) tenía secretos reales; no se subieron. Rotar
  si son válidas. Ver [[contexto#Decisiones (2026-09-09)]].

## Proyecto — Listas de precio por color (2026-09-11)
4 listas (Azul/Verde/Naranja/Violeta), cada una `base × (1 + %)`, con lista por defecto por cliente
y override en el modal de la orden. Tablas `LASET_LISTA_COLOR*`; config desde inventario vía
ms-metadata; aplicación en pedidos. Scopeado a `companyCode 11`.
En la grilla de Precios se editan **precio y %**: el % de un precio manual es derivado del costo,
no persistido (si cambia el costo, se recalcula solo). Ver [[arquitectura|listas de color]].

## Proyecto — Dominio único y SSO (2026-09-15/16)
Las 7 apps bajo `laset.local/<app>` con sesión compartida. **La regla central:** los middlewares de
permisos releen el usuario de la base por `UserId`, nunca del payload del token — si no, entrar a
una app desloguea de todas. Aplica a pedidos (3 middlewares), compras, expedicion y postventa.
**Si se suma un back nuevo al SSO, ese es el patrón.**

Dos trampas que costaron caras y conviene no repetir:
- `build.publicPath` tiene que ser **relativo**: Nuxt 2 le prepende `router.base` y uno absoluto
  deja todos los assets en 404 (con el SSR pintando igual, así que parece que anda).
- PyJWT exige `audience` cuando el token trae `aud`; los backs PHP lo usan como huella de navegador
  y `firebase/php-jwt` no lo valida. De ahí el `verify_aud: False` en ms-metadata.

`AppSwitcher.vue` está **duplicado en los 6 fronts**: si se cambia, cambiarlo en los 6.

## Proyecto — Importación de la planilla (2026-09-17/18)
Detalle en [[import-planilla-comp11]]. Lo que conviene no volver a aprender:
- **Reimportar exige wipe previo**: `"Importar todo"` no borra, apila. Sin wipe el ERP queda
  inflado (pasó: 666 SKUs con delta) y hay que rehacer todo.
- **Fase D corre por tandas** (`--limit=50`) y **aborta entera** si una sola orden tiene un
  almacén que no es de comp=11.
- Esta base **no es** la del [[como-se-importa-laset-comp11|ERP de NB]]: acá los proveedores ya
  tenían datos fiscales, `LST GLOBAL` no existe en comp=11, y el esquema clonado el 2026-09-04
  **va quedando viejo** respecto del código (caso `pedprol.doNotUpdateCost`).
- Verificar límites de PHP **por HTTP**, nunca con `php -i` del CLI: leen `conf.d` distintos.

## Feedback / lecciones de trabajo (2026-09-18)
- **Commitear siempre en un `git worktree` aparte**, nunca cambiando de rama en el working tree
  principal: los archivos ya commiteados en otra rama se revierten (o desaparecen, si son
  nuevos) y el server queda corriendo algo distinto de lo que uno cree. Pasó dos veces —
  los favicons volvieron a los de NB, y `config/laset.php` desapareció dejando el override de
  companyCode sin efecto.
- **No verificar contra el propio archivo que uno acaba de escribir**: comparar lo servido
  contra la rama/el origen. Una verificación circular dio "todo bien" con los favicons de NB.
- **Los límites de PHP se verifican por HTTP, no con `php -i` del CLI**: leen `conf.d`
  distintos y el del CLI miente.
- Un `curl` copiado de Chrome **no lleva el binario** del archivo: para probar uploads, `-F`.

## Estado y pendientes (2026-09-18)
- Mergeado a `blu-dev-staff` todo lo del importador, favicons, menú, listas de color,
  ocultamientos, `doNotUpdateCost` y el primer tramo de asignaciones/companyCode.
- Pendientes de merge: `fix/asignacion-feature-enabled` (override en el repositorio + los otros
  3 backs) y `fix/laset-cotizacion-oc-stockonly`.
- Pendiente operativo: **Re-vincular facturas** (398 esperando), desplegar en el dev de blu,
  limpiar 6 snapshots viejos y 20 scripts de diagnóstico en `storage/app` del back de pedidos.
- Decisión abierta: dar de alta (o no) los 4 proveedores y 18 categorías que dejan 23
  clasificaciones ECCN afuera.
- Deuda: cobros conecta a SQL Server **sin cifrado**; el vhost de Apache no está versionado;
  secretos en `.env-example` de postventa pendientes de rotar; `api-rest-expedicion/app/.emv`
  es un archivo suelto con lo que parece una credencial.

## Estado y pendientes (2026-09-16)
- PRs abiertos: **frontErp#11** y **backErp#5**. frontErp#11 se apoya en
  `feature/laset-listas-precio-color`, que tiene 2 commits sin mergear: mergear esa primero.
- Sin commitear: limpieza de links a saftel, 4 pestañas ocultas de inventario, precio + % en la
  grilla. Esperan la decisión sobre los deep-links de `DetailExamine.vue` y `AsignarOCModal.vue`.
- Deuda: cobros conecta a SQL Server **sin cifrado** (`Encrypt = 0`); el vhost de Apache no está
  versionado; secretos en `.env-example` de postventa pendientes de rotar.

## Ver también
[[Laset]] · [[arquitectura]] · [[contexto]] · [[troubleshooting]] · [[changelog]] · [[import-planilla-comp11]]
