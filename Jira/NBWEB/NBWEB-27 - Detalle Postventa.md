---
jira_key: "NBWEB-27"
aliases: ["NBWEB-27"]
summary: "Detalle Postventa"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2022-03-25 10:35"
updated: "2022-06-26 10:00"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/NBWEB-27"
---

# NBWEB-27: Detalle Postventa

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2022-03-25 10:35 |
| Actualizado | 2022-06-26 10:00 |
| Etiquetas | ninguna |
| Jira | [NBWEB-27](https://bluinc.atlassian.net/browse/NBWEB-27) |

## Relaciones

- **Padre:** [[NBWEB-2 - API - Mi cuenta|NBWEB-2]] API - Mi cuenta
- **relates to:** [[NBWEB-170 - APP - Mi cuenta - Postventa|NBWEB-170]] APP - Mi cuenta - Postventa

## Descripcion

```
GET {{API_URL}}/v1/miCuenta/postventa/{id_ticket}
```

SQL query ejemplo:



```sql
SELECT *
FROM [NEW_BYTES].[dbo].[ST_RMACABECERA] A
LEFT JOIN NEW_BYTES.dbo.ST_RMADETALLE B ON A.ID_RMACLIENTE = B.ID_RMACLIENTE
WHERE A.ID_RMACLIENTE = 31372
```



Debe retornar



```json
[
  {
    "ticketNumber": 31372,
    "status": "PARCIALMENTE REVISADO    ",
    "userId": "LMENA   ",
    "finalized": "SIN ENTREGAR             ",
    "itemFinalized": "  ",
    "itemTicketNumber": 55329,
    "serial": "sn2017630475",
    "productId": "102396",
    "warranty": "SI",
    "failDescription": "NO ENCIENDE/SOLO C/TRAFO Y20160012615",
    "testStatus": "NO                   ",
    "technicalReport": "",
    "deliveryDate": null
  },
  {
    "ticketNumber": 31372,
    "status": "PARCIALMENTE REVISADO    ",
    "userId": "LMENA   ",
    "finalized": "SIN ENTREGAR             ",
    "itemFinalized": "  ",
    "itemTicketNumber": 55330,
    "serial": "2014121312810218",
    "productId": "VID_EVGA_210_1024",
    "warranty": "SI",
    "failDescription": "BAJA LA RESOLUCION. SE ACHICA LA PANTALLA",
    "testStatus": "NO                   ",
    "technicalReport": "",
    "deliveryDate": null
  },
  {
    "ticketNumber": 31372,
    "status": "PARCIALMENTE REVISADO    ",
    "userId": "LMENA   ",
    "finalized": "SIN ENTREGAR             ",
    "itemFinalized": "NO",
    "itemTicketNumber": 55331,
    "serial": "2003530584801646",
    "productId": "7386",
    "warranty": "SI",
    "failDescription": "NO ENCIENDE // SE VERIFICARA GARANTIA POR ESTADO DE ETIQUETA EN FUENTE Y POSIBLE FALTANTE DE FAJA DE GARANTIA (A VERIFICAR)",
    "testStatus": "REVISADO             ",
    "technicalReport": "no enciende con l mother instalado",
    "deliveryDate": "04/04/2022"
  }
]
```
