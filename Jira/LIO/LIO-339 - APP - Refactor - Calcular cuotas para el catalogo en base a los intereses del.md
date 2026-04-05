---
jira_key: "LIO-339"
aliases: ["LIO-339"]
summary: "APP - Refactor - Calcular cuotas para el catalogo en base a los intereses del repositorio nuevo de medios de pago"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Marbe Moreno"
reporter: "Catriel Mercurio"
created: "2025-05-07 08:45"
updated: "2025-05-20 01:32"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/LIO-339"
---

# LIO-339: APP - Refactor - Calcular cuotas para el catalogo en base a los intereses del repositorio nuevo de medios de pago

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Marbe Moreno |
| Reportado por | Catriel Mercurio |
| Creado | 2025-05-07 08:45 |
| Actualizado | 2025-05-20 01:32 |
| Etiquetas | ninguna |
| Jira | [LIO-339](https://bluinc.atlassian.net/browse/LIO-339) |

## Relaciones

- **Padre:** [[LIO-119]] Inventario
- **action item from:** [[LIO-338]] API - Feat - Agregar repositorio de medios de pago disponibles en el sitio



## Descripcion

Basándonos en la respuesta de [link](https://bluinc.atlassian.net/browse/LIO-338)  modificaremos los items del catalogo, para reflejar de manera correcta los intereses y totales

[adjunto]
Para la base, tomaremos las 6 cuotas (aunque tal vez tambien peude explorarse la posiblidad de extender para ver el resto de la informacion).

**Criterios de aceptación:**

- Las cuotas deben cargar rapidamente y no posteriormente a la carga del catalogo, ya que l informacion pude haberla obtenido en la home o previamente.


- Los montos de cuota y todos los valores deben verse igual para un mismo producto, tanto en el catalogo, como en la ficha y el check out finalmente para ese medio de pago.
