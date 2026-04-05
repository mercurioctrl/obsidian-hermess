---
jira_key: "POS-99"
aliases: ["POS-99"]
summary: "APP - Feat - Pestaña estadística por categorías "
status: "Finalizada"
type: "Historia"
priority: "Medium"
assignee: "Marbe Moreno"
reporter: "Catriel Mercurio"
created: "2022-09-08 09:04"
updated: "2023-03-07 09:08"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/POS-99"
---

# POS-99: APP - Feat - Pestaña estadística por categorías 

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Historia |
| Prioridad | Medium |
| Asignado | Marbe Moreno |
| Reportado por | Catriel Mercurio |
| Creado | 2022-09-08 09:04 |
| Actualizado | 2023-03-07 09:08 |
| Etiquetas | ninguna |
| Jira | [POS-99](https://bluinc.atlassian.net/browse/POS-99) |

## Relaciones

- **Padre:** [[POS-22]] Dashboard y estadisticas
- **Subtarea:** [[POS-101]] APP - Feat - Mas costosos: Muestra informacion sobre las categorias que tienen mayor costo de postventa
- **Subtarea:** [[POS-100]] APP - Feat - Mas Falibles: Se trata de mostrar aquellas categorías que mas fallan.
- **Subtarea:** [[POS-102]] APP - Feat - Falsos positivos: Que categorías ingresan mas a postventa, pero no fallan.
- **Subtarea:** [[POS-104]] APP - Feat - Ingresos es un grafico de barras...
- **Subtarea:** [[POS-103]] APP - Feat - Demoras: Las cateogiras que mas tiempo permanecen dentro del departamenteo de postventa
- **Subtarea:** [[POS-111]] APP - Feat - Soluciones de posventa: Muestra la comparativa de si se reparo, se se cambio o se acredito
- **Subtarea:** [[POS-153]] APP - Feat - Descargar informacion completa de los graficos de categorias
- **is blocked by:** [[POS-66]] API - Feat - Filtros estadisticas categorias
- **is blocked by:** [[POS-58]] API - Feat - Estadisticas de categorias

## Descripcion

Tener en cuenta: Se debe mostrar por cada gráfico la mayor informacion posible, dentro de lo que el gráfico permite. Elegir el gráfico mas adecuado para cada caso (Cualquier duda la vemos).

Los distintos gráficos que se deben lograr están descritos en la tareas dentro de esta historia.

La informacion se puede obtener del recurso

```
GET {API_URL}/v1/metrics/categories/
```



**Filtros: **

Deben aplicarse filtros que te permitan aplicar cruces por marca. 

Y de ser posible matchear por string en el nombre de producto.
