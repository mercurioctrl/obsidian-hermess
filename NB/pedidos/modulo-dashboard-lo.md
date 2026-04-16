# Dashboard Libre Opción

Sección de estadísticas exclusiva del marketplace **Libre Opción**. Permite visualizar conversiones, cancelaciones, medios de pago/envío, ticket, facturación y performance de resellers.

**Branch:** `feature/dashboard-lo` (ambos repos)
**Visibilidad:** solo Administrador, Gerente General, Product Manager

## Endpoints

Todos bajo `/v1/statistics/lo/`, aceptan filtro `between` (rango de fechas).

| Endpoint | Descripción |
|----------|-------------|
| `GET /summary` | KPIs: pedidos, facturación, ticket promedio, conversión, cancelación, devoluciones |
| `GET /funnel` | Embudo 5 etapas + motivos de cancelación con links clickeables |
| `GET /byPaymentMethod` | Distribución por medio de pago (para gráfico pie) |
| `GET /byShippingMethod` | Distribución por medio de envío (para gráfico pie) |
| `GET /resellers` | Ranking de resellers con paginación server-side |
| `GET /cube` | Cubo OLAP dinámico (`groupBy`, `groupBy2`, `measure`) |

## Embudo de conversión

5 etapas, todos los porcentajes calculados sobre el total de carritos:

| Etapa | Fuente | Condición |
|-------|--------|-----------|
| **Carritos** | `LO.dbo.pedidosCabecera` | Todos los que entraron al marketplace |
| **Pedido generado** | `NewBytes_DBF.dbo.pedclit` | `WHERE idLo IS NOT NULL` |
| **Activos** | pedclit + pedidosCabecera | Ningún flag de cancelación activo |
| **Facturados** | pedclit | `cestado = 'S'` AND `lanula = 0` |
| **Entregados** | MS_VENTAS_REMITOS | `ID_STATUS > 1` |

### Cancelaciones vs Carritos abandonados

**Regla fundamental:** los que no superaron el checkout (sin pedclit) son **carritos abandonados**, NO cancelaciones. Solo los pedidos con pedclit y flags de cancelación activos son cancelaciones reales.

- **Total cancelados** = pedidos generados - activos (NO la suma de flags individuales, porque se solapan)
- Un pedido puede tener múltiples flags simultáneos (ej: `canceladoUsuario=1` Y `lanula=1`)
- Los desgloses por tipo suman más que el total — es esperado

### Motivos de cancelación

Dos reglas de agrupamiento (UNION):
1. **Si hay `motivoCancelacion`:** se agrupa solo por motivo, sin mostrar datos de pago (el motivo real ya explica)
2. **Si no hay motivo:** se agrupa por `mp_payment_status_detail` como contexto, con `mp_payment_status` informativo

### Links clickeables a /orders

Cada fila de motivos es clickeable y navega a `/orders` con filtros exactos:
- `loCancelled=1` — replica la lógica de cancelación del embudo (no usa `orderStatus=cancelled` que solo chequea `lanula`)
- `motivoCancelacion=X` — si tiene motivo real
- `mpPaymentStatusDetail=X` — si tiene detalle de pago
- `sinMotivo=1` — para los sin motivo ni payment detail

## Filtros agregados a OrderList

Sin afectar el comportamiento existente (todos opcionales, solo agregan WHERE si presentes):

| Filtro | Efecto |
|--------|--------|
| `loOnly=1` | `pedclit.idLo IS NOT NULL` |
| `loCancelled=1` | Todos los flags de cancelación LO (quita el default `lanula=0`) |
| `motivoCancelacion=X` | `pedidosCabecera.motivoCancelacion = X` |
| `mpPaymentStatus=X` | `pedidosCabecera.mp_payment_status = X` |
| `mpPaymentStatusDetail=X` | `pedidosCabecera.mp_payment_status_detail = X` |
| `sinMotivo=1` | Sin motivoCancelacion Y sin mp_payment_status_detail |

## Cubo OLAP

Dimensiones: reseller, marca, categoría, producto, medio de pago, medio de envío, mes.
Medidas: pedidos, facturación, cantidad items, ticket promedio.
Soporta 1 o 2 dimensiones simultáneas.

## Tablas y JOINs

```
NewBytes_DBF.dbo.pedclit (WHERE idLo IS NOT NULL)
  ├── INNER JOIN LO.dbo.pedidosCabecera (ON id = idLo)
  │     ├── cancelado*, motivoCancelacion, mp_payment_status*
  │     └── fechaCreacion (filtro de fechas)
  ├── INNER JOIN LO.dbo.pedidosCabeceraVendedor (ON pedidoCabeceraID)
  │     ├── LEFT JOIN LO.dbo.vendedores (resellers)
  │     ├── LEFT JOIN LO.dbo.mediosEnvio
  │     └── LEFT JOIN LO.dbo.mediosPago
  ├── LEFT JOIN LO.dbo.pedidosDetalle (items: precio, cantidad, descuento, devuelto)
  ├── LEFT JOIN NewBytes_DBF.dbo.albclit (remitos)
  │     └── LEFT JOIN NEW_BYTES.dbo.MS_VENTAS_REMITOS (ID_STATUS > 1 = entregado)
  └── Para cubo: CS.DBO.productos → articulo → familias, marcas
```

## Gotchas

- **opcache PHP**: el container Docker cachea PHP. Ejecutar `docker exec api-rest-pedidos-apirest-laravel php -r "opcache_reset();"` después de modificar archivos
- **navList[1]** = Libre Opción, **navList[2]** = Pedidos (desplazado en basic.vue)

## Ver también

- [[arquitectura]] — Estructura general del proyecto
- [[contexto#Base de datos|Contexto: Base de datos]] — Tablas y gotchas
- [[stack]] — Tecnologías
- [[changelog#2026-04-16|Changelog: 2026-04-16]] — Entrada del changelog
