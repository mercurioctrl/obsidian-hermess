---
jira_key: "EXP-26"
aliases: ["EXP-26"]
summary: "API - Feat - Listar pases de mercaderia"
status: "CodeReview"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2022-11-01 09:22"
updated: "2022-11-02 16:08"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/EXP-26"
---

# EXP-26: API - Feat - Listar pases de mercaderia

| Campo | Valor |
|-------|-------|
| Estado | CodeReview (En curso) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2022-11-01 09:22 |
| Actualizado | 2022-11-02 16:08 |
| Etiquetas | ninguna |
| Jira | [EXP-26](https://bluinc.atlassian.net/browse/EXP-26) |

## Relaciones

- **Padre:** [[EXP-18 - Feat - Listar pases|EXP-18]] Feat - Listar pases
- **blocks:** [[EXP-27 - APP - Feat - Listar pases|EXP-27]] APP - Feat - Listar pases

## Descripcion

Basándonos en el recurso que utilizamos en [link](https://lioteam.atlassian.net/browse/POS-27) se debe generar la lista pero desde la PERSPECTIVA DE EXPEDICIÓN.

Es decir que listaremos los pases que en principio están pendientes para ser tomados por expedición.

```
GET {API_URL}/v1/passes
```

```json
[
  {
    "id": 55632,
    "date": "11-04-2019 00:00",
    "agentId": 3,
    "agentDescription" : "Maxi Grillo",
    "description": "Pase entre depósitos por pedido de Depósito: RMA Clientes",
    "changeAccepted": "SI",
    "itemId": "104653",
    "itemDescription": "MEMORIA PATRIOT SIGNATURE LINE DDR4 16 GB 3200 MHZ PS001558",
    "warehouseIdOrigin" : 2,
    "warehouseDescriptionOrigin": "Servicio Técnico",
    "warehouseIdDestiny" : 5,
    "warehouseDescriptionDestiny": "Uso Interno"
  },
  {
    "id": 55631,
    "date": "11-04-2019 00:00",
    "agentId": 3,
    "agentDescription" : "Maxi Grillo",
    "description": "Pase entre depósitos por pedido de Depósito: RMA Clientes",
    "changeAccepted": "SI",
    "itemId": "108586",
    "itemDescription": "FUENTE GAMER EVGA 600W 80+ WHITE W2",
    "warehouseIdOrigin" : 2,
    "warehouseDescriptionOrigin": "Servicio Técnico",
    "warehouseIdDestiny" : 5,
    "warehouseDescriptionDestiny": "Uso Interno"
  },
  {
    "id": 55630,
    "date": "11-04-2019 00:00",
    "agentId": 3,
    "agentDescription" : "Maxi Grillo",
    "description": "Pase entre depósitos por pedido de Depósito: RMA Clientes",
    "changeAccepted": "SI",
    "itemId": "102691",
    "itemDescription": "DISCO SSD GIGABYTE 480 GB",
    "warehouseIdOrigin" : 2,
    "warehouseDescriptionOrigin": "Servicio Técnico",
    "warehouseIdDestiny" : 5,
    "warehouseDescriptionDestiny": "Uso Interno"
  },
  {
    "id": 55629,
    "date": "11-04-2019 00:00",
    "agentId": 3,
    "agentDescription" : "Maxi Grillo",
    "description": "Pase entre depósitos por pedido de Depósito: RMA Clientes",
    "changeAccepted": "SI",
    "itemId": "104918",
    "itemDescription": "MONITOR BENQ LED 24 GW2480 24W BLACK",
    "warehouseIdOrigin" : 2,
    "warehouseDescriptionOrigin": "Servicio Técnico",
    "warehouseIdDestiny" : 5,
    "warehouseDescriptionDestiny": "Uso Interno"
  },
  {
    "id": 55628,
    "date": "11-04-2019 00:00",
    "agentId": 3,
    "agentDescription" : "Maxi Grillo",
    "description": "Pase entre depósitos de RMA Clientes a RMA Proveedores ",
    "changeAccepted": null,
    "itemId": "104918",
    "itemDescription": "MONITOR BENQ LED 24 GW2480 24W BLACK",
    "warehouseIdOrigin" : 2,
    "warehouseDescriptionOrigin": "Servicio Técnico",
    "warehouseIdDestiny" : 5,
    "warehouseDescriptionDestiny": "Uso Interno"
  }
]
```

```
SELECT TOP(100) *
FROM [NEW_BYTES].[dbo].[ST_PASES_DEPOSITOS_CABECERA] A
LEFT JOIN NEW_BYTES.dbo.ST_PASES_DEPOSITOS_DETALLE B ON A.ID_PASE = B.ID_PASE
LEFT JOIN NEW_BYTES.dbo.ST_PASES_DEPOSITOS_MERCADERIA C ON A.ID_PASE = C.ID_PASE
LEFT JOIN NewBytes_DBF.dbo.articulo D ON D.cref = B.CREF
order by 1 desc



```



**Filtros necesarios**

- Origen


- Destino


- Estado
