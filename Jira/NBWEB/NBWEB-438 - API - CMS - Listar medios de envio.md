---
jira_key: "NBWEB-438"
aliases: ["NBWEB-438"]
summary: "API - CMS - Listar medios de envio"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2022-08-04 16:13"
updated: "2022-11-09 11:31"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/NBWEB-438"
---

# NBWEB-438: API - CMS - Listar medios de envio

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2022-08-04 16:13 |
| Actualizado | 2022-11-09 11:31 |
| Etiquetas | ninguna |
| Jira | [NBWEB-438](https://bluinc.atlassian.net/browse/NBWEB-438) |

## Relaciones

- **Padre:** [[NBWEB-73]] API - CMS - ABMS
- **blocks:** [[NBWEB-441]] APP - CMS - Listar medios de envio

## Descripcion

```
GET {{API_URL}}/v1/cms/shippingMethods
```

Retorna:

```
[
  {
    "id": 3030,
    "name": "Moto",
    "description": "Moto (Capital Federal)",
    "active": 1,
    "extraDayMin": 0,
    "extraDayMax": 0,
    "kmPrice": null,
    "minFee": 550,
    "maxDistance": null,
    "insuredLimit": null
  },
  {
    "id": 4041,
    "name": "OCA",
    "description": "OCA a domicilio",
    "active": 1,
    "extraDayMin": 1,
    "extraDayMax": 3,
    "kmPrice": null,
    "minFee": null,
    "maxDistance": null,
    "insuredLimit": null
  },
]
```



```
SELECT *
  FROM [LO].[dbo].[mediosEnvio]
  WHERE activo = 1 and eliminado = 0 and tipo =2
```
