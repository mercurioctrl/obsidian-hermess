---
jira_key: "COM-22"
aliases: ["COM-22"]
summary: "API - Refactor - Listar ordenes de compra ->Agregados"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Catriel Mercurio"
created: "2024-02-13 16:55"
updated: "2024-02-19 17:24"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/COM-22"
---

# COM-22: API - Refactor - Listar ordenes de compra ->Agregados

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Catriel Mercurio |
| Creado | 2024-02-13 16:55 |
| Actualizado | 2024-02-19 17:24 |
| Etiquetas | ninguna |
| Jira | [COM-22](https://bluinc.atlassian.net/browse/COM-22) |

## Relaciones

- **Padre:** [[COM-9]] Listar ordenes de compra
- **blocks:** [[COM-21]] APP - Feat - Listar ordenes de compra
- **is blocked by:** [[COM-35]] API - Listar ordenes de compra - Depósitos no coincidentes

## Descripcion

```
[
 {
    "status": "s",
    "date": "2016-05-30 10:24:35",
    "orderNumber": 7881,
    "providerId": "000046",
    "providerName": "NEW BYTES",
    "currencyId": "PSO",
    "label": null,
    "status": "R",
    "currencyAmount": 1005,5 <-- NUEVO
    "warehouse": "SAF"<-- NUEVO,
    "warehouseDescription": "SAFcom"<-- NUEVO
  },
  ...
```

```
SELECT cestado
    , CONVERT(VARCHAR, dfecped, 20) AS fecha
    , nnumped
    , pedprot.ccodpro
    , pedprot.ccoddiv
    , pedprot.label
    , pedprot.cCodAlm
    , pedprot.cEstado
    , pedprot.nValDiv
FROM NewBytes_DBF.dbo.pedprot
LEFT OUTER JOIN NewBytes_DBF.dbo.fp_proveedores
ON NewBytes_DBF.dbo.fp_proveedores.ccodpro = NewBytes_DBF.dbo.pedprot.ccodpro
```

Adicionalmente agregaremos la posibilidad de filtrar por `warehouse`

```
GET {API_URL}/v1/providerOrder?warehouse=SAF
```
