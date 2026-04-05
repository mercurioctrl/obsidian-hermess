---
jira_key: "LIO-128"
aliases: ["LIO-128"]
summary: "API - Feat - Recurso para obtener los comentarios de las calificaciones para un vendedor determinado"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2024-11-08 13:48"
updated: "2024-11-19 18:45"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/LIO-128"
---

# LIO-128: API - Feat - Recurso para obtener los comentarios de las calificaciones para un vendedor determinado

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2024-11-08 13:48 |
| Actualizado | 2024-11-19 18:45 |
| Etiquetas | ninguna |
| Jira | [LIO-128](https://bluinc.atlassian.net/browse/LIO-128) |

## Relaciones

- **Padre:** [[LIO-124 - Calificaciones|LIO-124]] Calificaciones
- **has action item:** [[LIO-130 - APP - Refactor - Implementar comentarios de calificación en la ficha de los|LIO-130]] APP - Refactor - Implementar comentarios de calificación en la ficha de los vendedores

## Descripcion

```
GET {API4_URL}/v4/seller/{sellerId}/calificationReviews <-- este recurso es sugerencia, si ya tenes otra estrcutura cambialo
```

Crearemos un recurso para traer los comentarios para el vendedor. El mismo debe ser paginable por parte del front (con tope máximo de 20 comentarios por ves)

```
SELECT
       [canceladoUsuario]
      ,[calificacionComentario]
      ,[calificacionFecha]
      ,[calificacionType]
  FROM [LO].[dbo].[pedidosCabeceraVendedor]
```

```
[
  {
    "calification": 3,
    "calificationReview": "Quedé tan conforme con la atención que les terminé comprando más productos que los que iba a comprar jajaja. Buenisimos.",
    "calificationDate": "2020-08-26T16:50:50.357",
    "calificationType": null
  },
  {
    "calification": 2,
    "calificationReview": "Buenisimo. Me lo enviaron rapidamente. Solo que el correo esta colapsado pero es ajeno al vendedor. Muy buena atencion chicos",
    "calificationDate": "2020-06-26T15:32:08.247",
    "calificationType": null
  }
]

```
