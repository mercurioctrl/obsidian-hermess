---
jira_key: "PED-282"
aliases: ["PED-282"]
summary: "API - Feat - Ventas totales"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Catriel Mercurio"
created: "2023-11-24 08:31"
updated: "2023-12-18 08:51"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-282"
---

# PED-282: API - Feat - Ventas totales

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Catriel Mercurio |
| Creado | 2023-11-24 08:31 |
| Actualizado | 2023-12-18 08:51 |
| Etiquetas | ninguna |
| Jira | [PED-282](https://bluinc.atlassian.net/browse/PED-282) |

## Relaciones

- **Padre:** [[PED-242]] Pestaña Estadisticas
- **is blocked by:** [[PED-296]]   API - Ventas totales - Incidencias varias

## Descripcion

Se trata simplemente del numero total de ventas (o pedidos) en un periodo determinado de tiempo

Se debe poder filtrar por

- Intervalo de fechas


- Marca


- Categoría


- Cliente



```
GET {API_URL}/statistics/totalSales?clientId={clientId}&sellerId{sellerId}&dateInterval={intervalo de fechas}&brandId={marca}&categoryId={categoria}
```
