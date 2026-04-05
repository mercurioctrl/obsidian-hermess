---
jira_key: "PED-617"
aliases: ["PED-617"]
summary: "API - Refactor - Control de \"pedidos pendientes\" al liquidar"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Catriel Mercurio"
created: "2024-03-18 18:06"
updated: "2024-03-21 16:16"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-617"
---

# PED-617: API - Refactor - Control de "pedidos pendientes" al liquidar

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Catriel Mercurio |
| Creado | 2024-03-18 18:06 |
| Actualizado | 2024-03-21 16:16 |
| Etiquetas | ninguna |
| Jira | [PED-617](https://bluinc.atlassian.net/browse/PED-617) |

## Relaciones

- **Padre:** [[PED-123 - Feat - Liquidar pedido|PED-123]] Feat - Liquidar pedido
- **is caused by:** [[PED-619 - APP - Mostrar las ordenes pendientes al liquidar en caso de error|PED-619]] APP - Mostrar las ordenes pendientes al liquidar en caso de error
- **is blocked by:** [[PED-622 - API - Control de pedidos pendientes al liquidar - No es posible liquidar orden|PED-622]] API - Control de pedidos pendientes al liquidar - No es posible liquidar orden pendiente

## Descripcion

Para evitar la proliferación de pedidos “viejos” pendientes que quedan en el sistema sin que nadie recuerde, al momento de liquidar realizaremos un control para evitar que se pueda continuar liquidando si tenemos un pedido “pendiente” con mas de X días de antigüedad.

Para esto utilizaremos el parametro 

`[NewBytes_DBF].[dbo].[agentes].xRemitoVto`

que es un parámetro diferente para cada agente y indica la cantidad de días de antigüedad máxima que puede tener un pedido hasta “trabar” la liquidación de cualquier otro.

para poder hacer esto, haremos una verificación del siguiente tipo

```
SELECT count(cnumped) as cantidad
        FROM [NewBytes_DBF].[dbo].[pedclit]
        LEFT JOIN NewBytes_DBF.DBO.agentes ON agentes.ccodage = pedclit.ccodage
        WHERE DATEDIFF(DAY,dfecped, getdate()) > agentes.xRemitoVto 
        AND (cobserv = 'INTERNO' OR  cobserv = 'DESCARGADO') 
        AND cestado ='P' 
        AND pedclit.ccodage = ?
```

Devolveremos un succes false y ademas un mensaje del tipo:
”Tenes un pedido que es mayor a X dias. El pedido es el 0002-0003243”
