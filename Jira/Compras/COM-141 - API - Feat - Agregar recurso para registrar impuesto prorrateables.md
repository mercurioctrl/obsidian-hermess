---
jira_key: "COM-141"
aliases: ["COM-141"]
summary: "API - Feat  - Agregar recurso para registrar impuesto prorrateables "
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Emanuel Jesus Ferreyra"
created: "2024-09-03 17:37"
updated: "2024-11-19 14:56"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/COM-141"
---

# COM-141: API - Feat  - Agregar recurso para registrar impuesto prorrateables 

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Emanuel Jesus Ferreyra |
| Creado | 2024-09-03 17:37 |
| Actualizado | 2024-11-19 14:56 |
| Etiquetas | ninguna |
| Jira | [COM-141](https://bluinc.atlassian.net/browse/COM-141) |

## Relaciones

- **Padre:** [[COM-38]] Ver orden de compra

## Descripcion

PATCH {URL}/v1/distributeTaxes/{numero-de-orden}

payload:

```
[{
  "id": 1,
  "taxBase": "12",
  "amount": 12
},{
  "id": 2,
  "taxBase": "12",
  "amount": 12
}]
```
