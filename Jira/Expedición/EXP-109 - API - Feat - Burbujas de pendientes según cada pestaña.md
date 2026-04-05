---
jira_key: "EXP-109"
aliases: ["EXP-109"]
summary: "API - Feat - Burbujas de pendientes según cada pestaña"
status: "CodeReview"
type: "Subtarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Catriel Mercurio"
created: "2022-12-19 12:22"
updated: "2023-02-06 15:43"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/EXP-109"
---

# EXP-109: API - Feat - Burbujas de pendientes según cada pestaña

| Campo | Valor |
|-------|-------|
| Estado | CodeReview (En curso) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Catriel Mercurio |
| Creado | 2022-12-19 12:22 |
| Actualizado | 2023-02-06 15:43 |
| Etiquetas | ninguna |
| Jira | [EXP-109](https://bluinc.atlassian.net/browse/EXP-109) |

## Relaciones

- **Padre:** [[EXP-108 - Feat - Burbujas|EXP-108]] Feat - Burbujas
- **blocks:** [[EXP-110 - APP - Feat - Burbujas de pendientes según cada pestaña|EXP-110]] APP - Feat - Burbujas de pendientes según cada pestaña

## Descripcion

```
GET {API_URL}/v1/pendings
```

```
{
  "passes":3,
  "pickUp":5,
  "shipments":4,
  "items":4,
  "providersOrders":4,
}
```



Se trata del recurso que hacemos para estas aplicaciones que datan de cuantas acciones tenemos pendientes en cada pestaña.

- Ingresos: Mostraremos la cantidad de los que aun figuran como “no serializados”


- Retiros: Mostramos la cantidad de los RETIROS aun no despachados con el boton “despachar”


- Envíos: Mostramos la cantidad de los ENVIOS aun no despachados con el boton “despachar”


- Pases de mercadería: Mostramos la cantidad de paseas que aun no fueron “aceptados” y están pendientes.


- Inventario: Muestro la cantidad de productos que aun están pendientes de conteo.
