---
jira_key: "NBWEB-187"
aliases: ["NBWEB-187"]
summary: "API - Mi cuenta - Subtotales ordenes de compra"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2022-05-16 14:39"
updated: "2022-06-26 20:13"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/NBWEB-187"
---

# NBWEB-187: API - Mi cuenta - Subtotales ordenes de compra

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2022-05-16 14:39 |
| Actualizado | 2022-06-26 20:13 |
| Etiquetas | ninguna |
| Jira | [NBWEB-187](https://bluinc.atlassian.net/browse/NBWEB-187) |

## Relaciones

- **Padre:** [[NBWEB-2]] API - Mi cuenta

## Descripcion

```
GET {{API_URL}}/v1/miCuenta/OrdenesDeCompra/{branch}/{orderNumber}/total
```



```
{
  "Cotizacion":104.5,
  "SubtotalDollar":4324.56,
  "SubtotalDollarFinal":5232.72,
  "SubtotalPesosAr":454078.8,
  "SubtotalPesosArFinal":549434.38
}
```
