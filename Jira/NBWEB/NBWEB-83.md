---
jira_key: "NBWEB-83"
summary: "Obtener tracking"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Catriel Mercurio"
created: "2022-04-04 07:53"
updated: "2022-07-03 09:47"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/NBWEB-83"
---

# NBWEB-83: Obtener tracking

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Catriel Mercurio |
| Creado | 2022-04-04 07:53 |
| Actualizado | 2022-07-03 09:47 |
| Etiquetas | ninguna |
| Jira | [NBWEB-83](https://bluinc.atlassian.net/browse/NBWEB-83) |

## Descripción

Se trata del recurso que sirve para obtener el seguimiento del un paquete determinado.



```
GET {{API_URL}}/TrackingOrder/nb/{branch}-{order}
```



Retorna

```json
[
  {
    "status": "Compra confirmada - New Bytes",
    "branch": "New Bytes - CABA, CABA",
    "addres": "Jujuy 1039, CABA, CABA",
    "date": "2022-03-31 13:33:48.463"
  },
  {
    "status": "Pendientes a Autorizar - New Bytes",
    "branch": "New Bytes - CABA, CABA",
    "addres": "Jujuy 1039, CABA, CABA",
    "date": "2022-03-31 16:34:34.953"
  },
  {
    "status": "Parcialmente Serializado - New Bytes",
    "branch": "New Bytes - CABA, CABA",
    "addres": "Jujuy 1039, CABA, CABA",
    "date": "2022-03-31 16:37:00.893"
  },
  {
    "status": "Preparando paquete para envio - New Bytes",
    "branch": "New Bytes - CABA, CABA",
    "addres": "Jujuy 1039, CABA, CABA",
    "date": "2022-03-31 16:37:00.893"
  },
  {
    "status": "En Proceso De Admision - San Telmo",
    "branch": "OCA - San Telmo",
    "addres": "Rivadavia 3868, CABA, CABA",
    "date": "2022-03-31T16:38:51.247-03:00"
  },
  {
    "status": "Admitido En Oca - San Telmo",
    "branch": "OCA - San Telmo",
    "addres": "Rivadavia 3868, CABA, CABA",
    "date": "2022-04-01T15:59:28.207-03:00"
  },
  {
    "status": "Admitido En Oca - San Telmo",
    "branch": "OCA - San Telmo",
    "addres": "Rivadavia 3868, CABA, CABA",
    "date": "2022-04-01T18:04:05-03:00"
  },
  {
    "status": "En Proceso En Oca - Centro De Operaciones Bs As",
    "branch": "OCA - Centro De Operaciones Bs As",
    "addres": "Mariano Ferreyra 302, CABA, CABA",
    "date": "2022-04-01T21:01:25.2-03:00"
  },
  {
    "status": "Procesado En Oca - Centro De Operaciones Bs As",
    "branch": "OCA - Centro De Operaciones Bs As",
    "addres": "Mariano Ferreyra 302, CABA, CABA",
    "date": "2022-04-01T21:01:27.707-03:00"
  },
  {
    "status": "Arribado A branch De Destino - San Juan",
    "branch": "OCA - San Juan",
    "addres": "Mendoza 2778, Va.krausse, San Juan",
    "date": "2022-04-04T18:37:50.087-03:00"
  },
  {
    "status": "Programado Para Visita A Domicilio - San Juan",
    "branch": "OCA - San Juan",
    "addres": "Mendoza 2778, Va.krausse, San Juan",
    "date": "2022-04-06T09:21:25.32-03:00"
  },
  {
    "status": "Visita A Domicilio En Curso - San Juan",
    "branch": "OCA - San Juan",
    "addres": "Mendoza 2778, Va.krausse, San Juan",
    "date": "2022-04-06T09:23:30.947-03:00"
  },
  {
    "status": "Entregado - San Juan",
    "branch": "OCA - San Juan",
    "addres": "Mendoza 2778, Va.krausse, San Juan",
    "date": "2022-04-06T20:45:59-03:00"
  }
]
```

Para obtener los primero estados, antes de mostrar los que son propios de los webservices de los distintos correos se utilizara una query similar a la siguiente

```sql
SELECT  
[DESCRIPCION]
FROM [NEW_BYTES].[dbo].[MS_STATUS_REMITO]
LEFT JOIN [NEW_BYTES].[dbo].[MS_VENTAS_REMITOS] ON MS_VENTAS_REMITOS.ID_STATUS = MS_STATUS_REMITO.ID_STATUS
LEFT JOIN NewBytes_DBF.dbo.albclit ON [MS_VENTAS_REMITOS].REMITO_FP = albclit.cnumalb AND MS_VENTAS_REMITOS.SUCURSAL_REMITO = albclit.cnumsuc
LEFT JOIN NewBytes_DBF.dbo.pedclit ON pedclit.cnumped = albclit.cnumped and pedclit.cnumsuc = albclit.cnumsuc
WHERE pedclit.cnumped = {order} AND pedclit.cnumsuc = {branch}
```
