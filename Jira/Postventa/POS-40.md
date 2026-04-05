---
jira_key: "POS-40"
summary: "API - Feat - Definir solucion tecnica"
status: "Finalizada"
type: "Historia"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2022-07-28 17:07"
updated: "2022-10-27 17:36"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/POS-40"
---

# POS-40: API - Feat - Definir solucion tecnica

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Historia |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2022-07-28 17:07 |
| Actualizado | 2022-10-27 17:36 |
| Etiquetas | ninguna |
| Jira | [POS-40](https://bluinc.atlassian.net/browse/POS-40) |

## Descripción

Define la acción que se va a tomar para darle solución al caso de post venta

```
PATCH {API_URL}/v1/aftersales/{afterSaleId}/{detailId}
```

```
{
"testProductStatusId":3,
}

```
