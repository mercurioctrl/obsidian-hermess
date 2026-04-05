---
jira_key: "INV-225"
aliases: ["INV-225"]
summary: "APP - MVP - Feat - Mostrar log de stock para un item determinado"
status: "Finalizada"
type: "Tarea"
priority: "Medium"
assignee: "Marbe Moreno"
reporter: "Catriel Mercurio"
created: "2025-11-05 08:21"
updated: "2025-12-05 04:31"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/INV-225"
---

# INV-225: APP - MVP - Feat - Mostrar log de stock para un item determinado

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Tarea |
| Prioridad | Medium |
| Asignado | Marbe Moreno |
| Reportado por | Catriel Mercurio |
| Creado | 2025-11-05 08:21 |
| Actualizado | 2025-12-05 04:31 |
| Etiquetas | ninguna |
| Jira | [INV-225](https://bluinc.atlassian.net/browse/INV-225) |

## Relaciones

- **Padre:** [[INV-199]] Control de Stock / Stock en general  / Control de Precios
- **action item from:** [[INV-218]] API - MVP - Feat - Mostrar log de stock para un item determinado

## Descripcion

Al hacer clic en un ítem (o en un botón/ícono de “ver historial de stock”) dentro del listado de stock, el sistema debe abrir un **modal** que muestre el **historial de movimientos de stock** para ese producto y depósito, usando el recurso de backend `GET /v1/stock-history`.

El modal debe listar cronológicamente (más reciente primero) todos los movimientos de stock registrados: ventas, compras, movimientos entre depósitos y movimientos entre stkcs, junto con el detalle de stock previo/posterior y el estado de los distintos stocks.

### Flujo de uso (UX esperado)

- El usuario se encuentra en la pantalla de stock / listado de ítems.


- En cada fila de ítem se muestra una acción tipo “Ver historial” (botón, link o icono).


- Al hacer clic:

- Se abre un **modal** de “Movimientos de stock” sobre el ítem seleccionado.


- El front dispara una llamada a la API `GET /v1/stock-history` pasando al menos:

- `itemId`


- `warehouseId` (el depósito que se está viendo)


- `dateFrom` y `dateTo` (por defecto, por ejemplo, el rango que se muestre en la cabecera del modal, ej: del 01-07-2025 al 05-11-2025, o los últimos X días).






- Mientras la API responde, se muestra un estado de **cargando** dentro del modal (spinner o mensaje “Cargando movimientos…”).


- Cuando la respuesta llega:

- El modal muestra una grilla con columnas similares a:

- Fecha


- Documento


- Agente


- Fichero (origen / servicio que generó el movimiento)


- Cantidad


- Stock previo


- Stock posterior


- STKLO previo (nstock_lo)


- STK previo (nstock)


- COLA previo (nstock_en_cola)


- STK0 previo (nstock_d1)


- PED previo (nstock_reserva_pedidos)


- PEDLO previo (nstock_lo_reserva_pedidos)


- POSTV previo (nstock_postventa)


- Info (IP, navegador, user_agent, etc. si está disponible)




- Las filas se muestran ordenadas por fecha descendente (primero lo más nuevo).




- Si no hay movimientos para el rango/ítem:

- El modal muestra un mensaje del tipo: “No se encontraron movimientos de stock para este período”.




- El usuario puede:

- Cerrar el modal.


- (Opcional / futuro) Cambiar el rango de fechas y volver a consultar.


- (Opcional / futuro) Navegar entre páginas si hay muchos resultados.





El modal del sistema viejo es este, pero debe ser mejorado dentro de lo posible

[adjunto]
