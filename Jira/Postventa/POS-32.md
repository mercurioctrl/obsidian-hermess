---
jira_key: "POS-32"
summary: "API - Feat - Listar postventas para credito"
status: "Finalizada"
type: "Historia"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2022-07-25 07:38"
updated: "2022-10-11 10:20"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/POS-32"
---

# POS-32: API - Feat - Listar postventas para credito

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Historia |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2022-07-25 07:38 |
| Actualizado | 2022-10-11 10:20 |
| Etiquetas | ninguna |
| Jira | [POS-32](https://bluinc.atlassian.net/browse/POS-32) |

## Descripción

En este recurso se muestran los casos de postventa que quedan pendientes para hacer un crédito, o bien a lo que ya se les realizo uno. Posteriormente conectaremos esa función con el ms de AFI

```
GET {API_URL}/v1/aftersalesCredits
```

```
[{

aftersaleId : 3244,
clientId: 23423,
clientName: 'Nombre del cliente',
admissionDate: '12-10-2021 00:00',
status: 'Sin Revisar',
dispatched: true,
dispatchedDate: '12-10-2021 00:00',
agentName: 'Marcelo',
agentId: 'Nombre agente soporte tecnico',
'elapsedTimeTesting': '24m',
'elapsedTime': '25h'

},
{

aftersaleId : 3244,
clientId: 23423,
clientName: 'Nombre del cliente',
admissionDate: '12-10-2021 00:00',
status: 'Sin Revisar',
dispatched: true,
dispatchedDate: '12-10-2021 00:00',
agentName: 'Pablo'
agentId: 'Nombre agente soporte tecnico',
'elapsedTimeTesting': '24m',
'elapsedTime': '25h'

}]
```

Se puede usar una query similar a esta 

```

        SELECT
        TOP(300)
        A.ID_RMACLIENTE,
        A.ID_CLIENTE,
        A.FECHA_INGRESO,
        A.FECHA_ENTREGA,
        A.ESTADO,
        A.REVISADO,
        A.ENTREGADO,
        B.cnomcli,
        B.cnomcom
        --TOP(50) ID_RMACLIENTE, CONVERT(datetime, FECHA_INGRESO, 103) AS FECHA_INGRESO, ESTADO, AUTORIZO, ID_USUARIO
        FROM  NEW_BYTES.dbo.ST_RMACABECERA A
        LEFT JOIN NewBytes_DBF.dbo.clientes B ON A.ID_CLIENTE = B.ID_CLIENTE
        LEFT JOIN NEW_BYTES.dbo.ST_RMADETALLE C ON A.ID_RMACLIENTE = C.ID_RMACLIENTE

        WHERE A.ID_CLIENTE IS NOT NULL
        --AND FECHA_INGRESO > dateadd(m, -6, getdate() - datepart(d, getdate()) + 1)
        
        --AND (C.ACCION = 'Espera' OR C.ACCION = 'Acreditar')
        AND (ESTADO = 'REVISADO' or ESTADO = 'PARCIALMENTE REVISADO' or (A.REVISADO = 'SI' AND A.ENTREGADO ='SIN ENTREGAR')) AND ACREDITADO = 'NO'
        AND ( C.ACCION = 'Acreditar')

        AND ACREDITADO = 'NO'
        AND  (A.ENTREGADO = 'SIN ENTREGAR' OR A.ENTREGADO = 'PARCIALMENTE ENTREGADO' or (A.REVISADO = 'SI' AND A.ENTREGADO ='SIN ENTREGAR'))
        GROUP BY
        A.ID_RMACLIENTE,
        A.ID_CLIENTE,
        A.FECHA_INGRESO,
        A.FECHA_ENTREGA,
        A.ESTADO,
        A.REVISADO,
        A.ENTREGADO,
        B.cnomcli,
        B.cnomcom
        ORDER BY FECHA_INGRESO DESC
```
