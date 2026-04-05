---
jira_key: "COM-216"
aliases: ["COM-216"]
summary: "API - MVP - Refactor  - Cada que se haga un ingreso revisar para cambiar el estado de la orden en caso que sean iguales la cantidad ingresadas que las totales para todos los items"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Marbe Moreno"
created: "2025-10-13 16:48"
updated: "2025-11-17 22:19"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/COM-216"
---

# COM-216: API - MVP - Refactor  - Cada que se haga un ingreso revisar para cambiar el estado de la orden en caso que sean iguales la cantidad ingresadas que las totales para todos los items

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Marbe Moreno |
| Creado | 2025-10-13 16:48 |
| Actualizado | 2025-11-17 22:19 |
| Etiquetas | ninguna |
| Jira | [COM-216](https://bluinc.atlassian.net/browse/COM-216) |

## Relaciones

- **Padre:** [[COM-109 - Generar INGRESO o pedido (a partir de una orden de compra)|COM-109]] Generar INGRESO o pedido (a partir de una orden de compra)
- **action item from:** [[COM-217 - APP - MVP - refactor - agregar botón para cerrar la orden que ejecuta|COM-217]] APP - MVP - refactor - agregar botón para cerrar la orden que ejecuta checkComplete y usarlo cada vez que se cambian las cantidades de “total” y también cuando se hace un ingreso (esto permite cambiar de estado pendiente a remitido)
- **relates to:** [[COM-251 - API - MVP - Review - Generar ingreso - Diferencia de IVA al finalizar la orden|COM-251]] API - MVP - Review - Generar ingreso -> Diferencia de IVA al finalizar la orden

## Descripcion

Este recurso permite cerrar una orden de compra de proveedor cuando todos los ítems asociados ya fueron ingresados al stock. Si se cumplen las condiciones, el estado de la orden se actualiza automáticamente a *cerrada*.

```
PATCH {API_URL}/v1/closeProviderOrderInbound
```

```
  {
    "orderNumber": 11082
  }
```

### **Lógica del proceso**

- **Validación inicial:**
Antes de realizar cualquier operación, se verifica que la orden se encuentre abierta:

```
[NewBytes_DBF].[dbo].[PedProT].cEstado = 'P'
```


- **Condición de cierre:**
Una orden se considera *completada* cuando no quedan ítems pendientes de ingreso a stock.
Esto puede comprobarse de dos formas:

- Mediante la ejecución del flujo correspondiente al ingreso de mercadería (ver [[[COM-110]]](https://bluinc.atlassian.net/browse/COM-110)).


- O directamente mediante el cálculo:

```
SUM(amount) - SUM(amountEntered) = 0
```

Es decir, si la suma total de los montos de los ítems (`amount`) coincide con la suma total de los montos efectivamente ingresados (`amountEntered`), la orden está completamente recibida.




- **Actualización de estado:**
Si se cumple la condición anterior, la orden se marca como cerrada:

```
[NewBytes_DBF].[dbo].[PedProT].cEstado = 'S'
```



[adjunto]
```
{
  "success": true,
  "message": "Operación exitosa",
  "data": {}
}
```


Notas:

- `success` indica si la operación se realizó correctamente.


- `message` puede incluir detalles adicionales (por ejemplo, “La orden ya estaba cerrada”).


- `data` puede contener información complementaria o `null` si no aplica.
