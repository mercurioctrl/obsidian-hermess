---
jira_key: "COM-170"
aliases: ["COM-170"]
summary: "API - Refactor - Cambiar de estado la orden, cuando ya se hicieron todos los ingresos posible"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Catriel Mercurio"
created: "2025-02-12 12:21"
updated: "2025-02-19 00:51"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/COM-170"
---

# COM-170: API - Refactor - Cambiar de estado la orden, cuando ya se hicieron todos los ingresos posible

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Catriel Mercurio |
| Creado | 2025-02-12 12:21 |
| Actualizado | 2025-02-19 00:51 |
| Etiquetas | ninguna |
| Jira | [COM-170](https://bluinc.atlassian.net/browse/COM-170) |

## Relaciones

- **Padre:** [[COM-109 - Generar INGRESO o pedido (a partir de una orden de compra)|COM-109]] Generar INGRESO o pedido (a partir de una orden de compra)

## Descripcion

Refactorizaremos el recurso para poder cambiarlo de estado una vez que esta terminado.

```
POST {API_URL}/v1/makeProviderOrderInbound
```

## ¿Como sabemos cuando ya se termino de cargar el pedido?

Se podría decir que cuando todos las filas del pedido `ncanped` es igual a `ncanent`

```
  SELECT 
       [nCanPed]
      ,[nCanEnt]
  FROM [NewBytes_DBF].[dbo].[pedprol]
  WHERE nNumPed = ?
```

## ¿Que hacemos cuando consideramos que esta completo?

El paso final es que deje de estar pendiente, para esto el ultimo paso de cada vez que ejecutamos `POST {API_URL}/v1/makeProviderOrderInbound` sera hacer la comparativa y si todo es cero marcaremos el pedido en su proximo estado

```
[NewBytes_DBF].[dbo].[PedProT].cEstado = 's'
```
