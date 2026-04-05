---
jira_key: "COM-10"
aliases: ["COM-10"]
summary: "API - Feat - Listar ordenes de compra"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Catriel Mercurio"
created: "2024-01-09 15:54"
updated: "2024-02-13 16:51"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/COM-10"
---

# COM-10: API - Feat - Listar ordenes de compra

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Catriel Mercurio |
| Creado | 2024-01-09 15:54 |
| Actualizado | 2024-02-13 16:51 |
| Etiquetas | ninguna |
| Jira | [COM-10](https://bluinc.atlassian.net/browse/COM-10) |

## Relaciones

- **Padre:** [[COM-9 - Listar ordenes de compra|COM-9]] Listar ordenes de compra
- **blocks:** [[COM-21 - APP - Feat - Listar ordenes de compra|COM-21]] APP - Feat - Listar ordenes de compra

## Descripcion

```
GET {API_URL}/v1/providerOrder?status={status}&search={orderNumber o providerid, providername}
```

```
  {
    "status": "s",
    "date": "2016-05-30 10:24:35",
    "orderNumber": 7881,
    "providerId": "000046",
    "providerName": "",
    "currencyId": "PSO",
    "label": null
  },
  {
    "status": "s",
    "date": "2016-05-31 15:12:01",
    "orderNumber": 7885,
    "providerId": "000088",
    "providerName": "",
    "currencyId": "DOL",
    "label": null
  },
  {
    "status": "s",
    "date": "2016-06-02 14:25:30",
    "orderNumber": 7886,
    "providerId": "000098",
    "providerName": "",
    "currencyId": "PSO",
    "label": null
  },
```

```
SELECT cestado
    , CONVERT(VARCHAR, dfecped, 20) AS fecha
    , nnumped
    , pedprot.ccodpro
    , pedprot.ccoddiv
    , pedprot.label
FROM NewBytes_DBF.dbo.pedprot
LEFT OUTER JOIN NewBytes_DBF.dbo.fp_proveedores
    ON NewBytes_DBF.dbo.fp_proveedores.ccodpro = NewBytes_DBF.dbo.pedprot.ccodpro
        
```
