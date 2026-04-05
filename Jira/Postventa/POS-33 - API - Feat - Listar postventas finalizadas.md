---
jira_key: "POS-33"
aliases: ["POS-33"]
summary: "API - Feat - Listar postventas finalizadas"
status: "Finalizada"
type: "Historia"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2022-07-25 08:25"
updated: "2022-10-11 10:21"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/POS-33"
---

# POS-33: API - Feat - Listar postventas finalizadas

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Historia |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2022-07-25 08:25 |
| Actualizado | 2022-10-11 10:21 |
| Etiquetas | ninguna |
| Jira | [POS-33](https://bluinc.atlassian.net/browse/POS-33) |

## Relaciones

- **Padre:** [[POS-21 - Solucion de postventa|POS-21]] Solucion de postventa
- **Subtarea:** [[POS-76 - API - Feat - Filtros postventa finalizadas|POS-76]] API - Feat - Filtros postventa finalizadas
- **Subtarea:** [[POS-82 - API - Test - Revisar porque no carga correctamente la grilla (falla hace poco,|POS-82]] API - Test - Revisar porque no carga correctamente la grilla (falla hace poco, antes funcionaba)
- **Subtarea:** [[POS-187 - API - Review - Filtrar acrhivados, donados y entregados del listado general|POS-187]] API - Review - Filtrar acrhivados, donados y entregados del listado general
- **Subtarea:** [[POS-201 - API - Refactor - Agregar token para leer comprobante|POS-201]] API - Refactor - Agregar token para leer comprobante
- **Subtarea:** [[POS-218 - API - Feat - Accion reenviar correo con palabra clave|POS-218]] API - Feat - Accion reenviar correo con palabra clave
- **Subtarea:** [[POS-220 - API - Refactor - Se debe enviar una notificacion a la gerencia|POS-220]] API - Refactor - Se debe enviar una notificacion a la gerencia
- **blocks:** [[POS-69 - APP - Feat - Listar postventas finalizadas|POS-69]] APP - Feat - Listar postventas finalizadas

## Descripcion

```
GET {API_URL}/v1/aftersalesFinalized
```

Este listado muestra todos los casos ya finalizados. Es mas que nada un apartado para consultas sobre como se desarrollaron los distintos casos.

```
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
    "warehouseDescriptionDestiny": "Uso Interno",
    "solution": 'Credito'
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
    "warehouseDescriptionDestiny": "Uso Interno",
    "solution": 'Cambio'
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
    "warehouseDescriptionDestiny": "Uso Interno",
    "solution": 'Credito'
  }
]
```
