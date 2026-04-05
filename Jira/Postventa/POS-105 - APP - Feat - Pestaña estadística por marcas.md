---
jira_key: "POS-105"
aliases: ["POS-105"]
summary: "APP - Feat - Pestaña estadística por marcas"
status: "Finalizada"
type: "Historia"
priority: "Medium"
assignee: "Marbe Moreno"
reporter: "Catriel Mercurio"
created: "2022-09-08 14:51"
updated: "2023-03-07 09:08"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/POS-105"
---

# POS-105: APP - Feat - Pestaña estadística por marcas

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Historia |
| Prioridad | Medium |
| Asignado | Marbe Moreno |
| Reportado por | Catriel Mercurio |
| Creado | 2022-09-08 14:51 |
| Actualizado | 2023-03-07 09:08 |
| Etiquetas | ninguna |
| Jira | [POS-105](https://bluinc.atlassian.net/browse/POS-105) |

## Relaciones

- **Padre:** [[POS-22]] Dashboard y estadisticas
- **Subtarea:** [[POS-106]] APP - Feat - Mas costosas: Muestra informacion sobre las marcas que tienen mayor costo de postventa
- **Subtarea:** [[POS-107]] APP - Feat - Mas falibles: Se trada de mostrar aquellas marcas que presentaron mas fallas
- **Subtarea:** [[POS-108]] APP - Feat - Falsos positivos: Que categorias ingresan mas a posventa pero no fallan.
- **Subtarea:** [[POS-109]] APP - Feat - Ingresos es un grafico de barras...
- **Subtarea:** [[POS-110]] APP - Feat - Demoras: Las marcas que mas tiempo permanecen dentro del departamenteo de postventa
- **Subtarea:** [[POS-114]] APP - Feat - Soluciones de posventa: Muestra la comparativa de si se reparo, se se cambio o se acredito
- **Subtarea:** [[POS-152]] APP - Feat - Descargar informacion completa de los graficos de marcas
- **is blocked by:** [[POS-67]] API - Feat - Filtros estadisticas marcas

## Descripcion

Tener en cuenta: Se debe mostrar por cada gráfico la mayor informacion posible, dentro de lo que el gráfico permite. Elegir el gráfico mas adecuado para cada caso (Cualquier duda la vemos).

Los distintos gráficos que se deben lograr están descritos en la tareas dentro de esta historia.

La informacion se puede obtener del recurso

```
GET {API_URL}/v1/metrics/brands/
```

 

**Filtros:**

Deben aplicarse filtros que te permitan aplicar cruces por marca.

Y de ser posible matchear por string en el nombre de la marca
