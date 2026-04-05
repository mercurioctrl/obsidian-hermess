---
jira_key: "POS-27"
aliases: ["POS-27"]
summary: "API - Feat - Listas de pases"
status: "Finalizada"
type: "Historia"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2022-07-21 08:54"
updated: "2022-10-18 14:20"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/POS-27"
---

# POS-27: API - Feat - Listas de pases

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Historia |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2022-07-21 08:54 |
| Actualizado | 2022-10-18 14:20 |
| Etiquetas | ninguna |
| Jira | [POS-27](https://bluinc.atlassian.net/browse/POS-27) |

## Relaciones

- **Padre:** [[POS-23 - Pases de mercaderia|POS-23]] Pases de mercaderia
- **blocks:** [[POS-54 - API - Refactor - Listas de pases|POS-54]] API - Refactor - Listas de pases
- **blocks:** [[POS-115 - APP - Feat - Lista de pases|POS-115]] APP - Feat - Lista de pases

## Descripcion

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
