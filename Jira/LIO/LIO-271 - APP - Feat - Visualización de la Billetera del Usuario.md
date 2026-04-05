---
jira_key: "LIO-271"
aliases: ["LIO-271"]
summary: "APP - Feat - Visualización de la Billetera del Usuario"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Marbe Moreno"
reporter: "Catriel Mercurio"
created: "2025-03-12 10:06"
updated: "2025-03-19 12:45"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/LIO-271"
---

# LIO-271: APP - Feat - Visualización de la Billetera del Usuario

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Marbe Moreno |
| Reportado por | Catriel Mercurio |
| Creado | 2025-03-12 10:06 |
| Actualizado | 2025-03-19 12:45 |
| Etiquetas | ninguna |
| Jira | [LIO-271](https://bluinc.atlassian.net/browse/LIO-271) |

## Relaciones

- **Padre:** [[LIO-231]] Billetera
- **action item from:** [[LIO-248]] API - Feat -  Recurso para Solicitar un Retiro de Dinero en la Billetera
- **action item from:** [[LIO-241]] API - Feat - Gestion de informacion de cuentas bancarias para el cliente y su billetera
- **action item from:** [[LIO-240]] API - Feat - Obtener balance de billetera
- **action item from:** [[LIO-232]] API - Feat - Listar movimientos en billetera
- **action item from:** [[LIO-273]] API - Feat - Editar campos de  cuentas bancarias

## Descripcion

Se debe visualizar la billetera del usuario con su balance total y el listado con todos los movimientos de mi billetera dentro de la plataforma, para conocer el detalle de ingresos y egresos asociados a mis transacciones.

**Criterios de Aceptación:**

Se debe mostrar un apartado de balance, con accionables para hacer retiros de dinero según los recursos (tambien en el contexto de retirar dinero se puede ofrecer agregar una cuenta de retiro)

```
GET {API_V4}/wallet/balance?type={available|pending}
```

```
POST {API_V4}/wallet/cash-out
```

**Se debe mostrar una lista de movimientos con la siguiente información:**

- ID de transacción.


- Monto.


- Moneda.


- Concepto.


- Fecha.


- Tipo de transacción (Ingreso o Gasto)




**Los datos deben obtenerse desde el endpoint**

```
GET {API_V4}/wallet/transactions
```

- Debe aplicarse paginación en la visualización de los movimientos, respetando los valores de `limit`, `offset` y `total`.


- Se deben diferenciar los ingresos y gastos mediante colores o íconos distintivos.


- El listado debe estar ordenado por fecha, mostrando primero los movimientos más recientes.


- En caso de error en la obtención de los datos, debe mostrarse un mensaje de error claro.



**Notas Adicionales:**

- Se podrá considerar una futura implementación de filtros por fecha, tipo de transacción o monto.



Hay atajos con respecto a la interface que se pueden tomar replicando ubicaciones y formas de mercadopago, porque la gente ya hizo esa curva de aprendizaje
