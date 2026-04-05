---
jira_key: "PED-346"
aliases: ["PED-346"]
summary: "API - Feat - Mostrar facturacion Totales"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Catriel Mercurio"
created: "2023-12-18 08:51"
updated: "2023-12-20 11:53"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-346"
---

# PED-346: API - Feat - Mostrar facturacion Totales

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Catriel Mercurio |
| Creado | 2023-12-18 08:51 |
| Actualizado | 2023-12-20 11:53 |
| Etiquetas | ninguna |
| Jira | [PED-346](https://bluinc.atlassian.net/browse/PED-346) |

## Relaciones

- **Padre:** [[PED-242]] Pestaña Estadisticas
- **blocks:** [[PED-315]] APP - Feat - Mostrar facturacion Totales

## Descripcion

Mostraremos el total vendido o facturado teniendo en cuenta la suma de 

`[NewBytes_DBF].[dbo].[albclil].npreunit`y `[NewBytes_DBF].[dbo].[albclil].ncanent`

Solo se hace para cuando `[NewBytes_DBF].[dbo].[albclil].ntipoalb > 1`

**Endpoint de la API**:

```
GET {API_URL}/statistics/totalBilled?clientId={clientId}&sellerId={sellerId}&dateInterval={intervalo de fechas}&brandId={marca}&categoryId={categoria}
```

**Filtrado**:

- Intervalo de fechas


- Marca


- Categoría


- Cliente


- vendedor
