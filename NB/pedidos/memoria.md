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

## Referencias

- Bugs trackeados en Jira (integrado via apiJira.client.js)
- Docker container backend: `api-rest-pedidos-apirest-laravel` (puerto 8093)

## Ver también

- [[contexto]] — Reglas de negocio detalladas
- [[arquitectura]] — Estructura del proyecto
- [[modulo-dashboard-lo]] — Dashboard Libre Opción
