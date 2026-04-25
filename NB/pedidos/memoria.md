# Memoria

Contexto acumulado de sesiones de trabajo con Claude en este proyecto.

## Usuario

- Desarrollador fullstack senior argentino
- Idioma: español rioplatense
- Prefiere iterar rápido y soluciones simples
- No agregar features no solicitadas

## Feedback

- Siempre verificar cambios con pruebas reales (curl, dev server) antes de reportar como terminado
- MakeSale/RemoveSale usan SQL concatenado — verificar nulls con ISNULL antes de interpolar en queries
- **Cancelaciones LO vs carritos abandonados:** pedidos sin pedclit no son cancelaciones sino carritos abandonados. `motivoCancelacion` tiene prioridad sobre `mp_payment_status`. Total cancelados = created - active (no sumar flags que se solapan)
- **No tocar MakeSale/RemoveSale** desde features nuevos — usar triggers SQL o capa nueva. Decisión explícita en [[feature-asignacion-oc|asignación OC]].
- **Antes de tirar SQL contra dev compartida**, mostrar al usuario host/db/user para que confirme.

## Proyecto

- Frontend necesita `NODE_OPTIONS=--openssl-legacy-provider` con Node v17+
- Firebase no configurado en local, plugin usa stub vacío
- Tablas clave: pedclit (pedidos), albclit/albclil (remitos), clientes, agentes, articulo
- Gotcha: columnas duplicadas en SELECT por JOINs, case sensitivity en nombres de columna PHP
- Backend usa varias DBs: NB_WEB (default), NewBytes_DBF, LO, NEW_BYTES, CS
- Rutas syncUp usan TOKEN_SYNCUP del .env, no JWT
- Branching: Development como base, hotfix/*, deploy frontend via gamma
- **Dashboard LO** en branch `feature/dashboard-lo` — ver [[modulo-dashboard-lo]]
  - Entregados = `MS_VENTAS_REMITOS.ID_STATUS > 1` (no `pedclit.delivered`)
  - Carritos cuenta desde pedidosCabecera sin requerir pedclit
  - navList[1] = Libre Opción, navList[2] = Pedidos (desplazado)
  - opcache PHP: ejecutar `docker exec api-rest-pedidos-apirest-laravel php -r "opcache_reset();"` después de modificar PHP
  - Filtros OrderList agregados: `loOnly`, `loCancelled`, `motivoCancelacion`, `mpPaymentStatus`, `mpPaymentStatusDetail`, `sinMotivo`
- **[[feature-asignacion-oc|Asignación OC ↔ Venta]]** en branch `feature/asignacion-oc-pedclil` (ambos repos)
  - Tabla `pedclil_oc_asignacion` (NewBytes_DBF). FK lógica `pedclil_id` (pedclil.id IDENTITY).
  - Vistas `vw_saldo_oc` y `vw_pedclil_estado_asignacion`. Trigger `tg_pedclit_cestado_asignacion`.
  - 5 endpoints HTTP en `Asignacion/AsignacionController` + command `asignaciones:fifo`.
  - Env vars: `ASSIGNMENT_FEATURE_ENABLED`, `ASSIGNMENT_COMPANIES`, `ASSIGNMENT_ALLOW_PARTIAL` (deben coincidir backend↔frontend).
  - **Driver dblib no soporta índices filtrados** → todos los índices del feature van sin `WHERE`.
  - **pedprol no tiene IDENTITY** → identificación por tupla `(nNumPed, nLinea, cRef)`.
  - Decisiones cerradas con el usuario:
    - FIFO por fecha de OC (sin otras políticas en v1)
    - Asignación parcial permitida; no bloquea MakeSale
    - Sin migración retroactiva (Opción A)
    - Cross-warehouse permitido a nivel asignación
    - Toda OC con saldo es candidata sin filtrar por cEstado (Opción C)
  - Cambios colaterales en backend: `OrderDetailDto.companyCode`, `OrderItemDto.pedclilId`. Eran necesarios para que el frontend del feature funcione (item.id estaba mapeado a articulo.ID_ARTICULO, no a la línea de venta).
  - Documentación canónica: `/Users/hermess/www/pedidos/docs/asignacion-oc-pedclil.md` y `database/sql/README.md`.

## Referencias

- Bugs trackeados en Jira (integrado via apiJira.client.js)
- Docker container backend: `api-rest-pedidos-apirest-laravel` (puerto 8093)
- DB dev: SAFDB2 (host 190.210.23.108:1433), user `eferreyra_devweb01` — autorizada para uso por el usuario
- Documentación de features grandes vive en `docs/` del monorepo + nota dedicada en bóveda

## Ver también

- [[pedidos]] — Índice del proyecto
- [[contexto]] — Gotchas técnicos
- [[arquitectura]] — Estructura
- [[feature-asignacion-oc]] — Feature actual
- [[modulo-dashboard-lo]] — Feature reciente
- [[modulo-makesale]] / [[modulo-removesale]]
