---
jira_key: "PED-978"
aliases: ["PED-978"]
summary: "API - Refactor - Al liquidar un pedido de libreOpcion, marcaremos el debito/credito como un movimiento de billetera"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Catriel Mercurio"
created: "2025-03-26 08:55"
updated: "2025-04-30 10:45"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-978"
---

# PED-978: API - Refactor - Al liquidar un pedido de libreOpcion, marcaremos el debito/credito como un movimiento de billetera

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Catriel Mercurio |
| Creado | 2025-03-26 08:55 |
| Actualizado | 2025-04-30 10:45 |
| Etiquetas | ninguna |
| Jira | [PED-978](https://bluinc.atlassian.net/browse/PED-978) |

## Relaciones

- **Padre:** [[PED-123 - Feat - Liquidar pedido|PED-123]] Feat - Liquidar pedido
- **action item from:** [[LIO-231 - Billetera|LIO-231]] Billetera

## Descripcion

Según lo conversado, debemos marcar los movimientos de libreOpcion para que puedan ser visualizados en la billetera.

```
POST {API_URL}/v1/closeSale
```

Como corresponder a los distintos escenarios de liquidación según medio de pago se genera solo un crédito o en algunas ocasiones débito y crédito en el mismo movimiento (por ejemplo cuando se paga con plata en cuenta).

Para todos esos movimientos agregaremos el `HMAC` en `[NEW_BYTES].[dbo].[MC_CCORRIENTES_MOVIMIENTOS]`  ademas de cualquier parámetro que sea necesario para el funcionamiento de la billetera.

Adicionalmente agregaremos informacion complementaria si es necesario en las observaciones que den cuenta de la transacción solo si nos parece relevante.



- Complemento la tarea con esto, para que QA tenga contexto de los cambios puntales realizados. 





Implementar una funcionalidad que genere un HMAC para movimientos asociados a pedidos de Libre Opción y lo almacene en la tabla [NEW_BYTES].[dbo].[MC_CCORRIENTES_MOVIMIENTOS], integrándola al flujo de liquidación.

**Funcionalidad a Implementar:**

- **Generación de HMAC:**

- Verificar si un movimiento corresponde a un pedido de Libre Opción (comprobar si pedclit.idLo no es nulo).


- Genere un HMAC seguro usando los datos del movimiento y el algoritmo [[SHA-256]]. (usados tambien en v4)


- Actualizar el registro correspondiente en [NEW_BYTES].[dbo].[MC_CCORRIENTES_MOVIMIENTOS] con el HMAC generado.




- **Integración en el Flujo:**

- Asegurar que el HMAC se genere automáticamente tras insertar un registro en la tabla de movimientos, utilizando los datos disponibles en ese momento de la cuenta corriente.




- **Configuración Segura:**

- Agregar HMAC en el archivo .env como HMAC_KEY. (igual que v4)





**Escenarios a Cubrir:**

- Movimientos que generan solo un crédito.


- Movimientos que generan débito y crédito simultáneamente (ej. pagos con saldo en cuenta).


- En ambos casos, aplicar el HMAC solo a movimientos de Libre Opción para su visualización en la billetera.



 Los movimientos de Libre Opción deben quedar marcados con un HMAC en la tabla de movimientos,  esto permite que se vean en la billetera.
