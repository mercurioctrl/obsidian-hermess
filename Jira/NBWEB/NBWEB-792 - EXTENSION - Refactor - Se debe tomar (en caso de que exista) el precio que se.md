---
jira_key: "NBWEB-792"
aliases: ["NBWEB-792"]
summary: "EXTENSION - Refactor - Se debe tomar (en caso de que exista) el precio que se encuentra en finalPriceWithUtility, sino el precio conencional en la extension de woocomerce"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Catriel Mercurio"
created: "2024-07-30 09:08"
updated: "2024-07-30 22:24"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/NBWEB-792"
---

# NBWEB-792: EXTENSION - Refactor - Se debe tomar (en caso de que exista) el precio que se encuentra en finalPriceWithUtility, sino el precio conencional en la extension de woocomerce

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Catriel Mercurio |
| Creado | 2024-07-30 09:08 |
| Actualizado | 2024-07-30 22:24 |
| Etiquetas | ninguna |
| Jira | [NBWEB-792](https://bluinc.atlassian.net/browse/NBWEB-792) |

## Relaciones

- **Padre:** [[NBWEB-682]] Productos

## Descripcion

Basándonos en el metodo que existe para agregar utilidad según cada categoría obtenemos que a veces al obtener el catalogo  `finalPriceWithUtility` es diferente a `finalPrice`

En caso de que `finalPriceWithUtility` este disponible tomamos ese precio para sincronizar en la extensión de woordpress 

Fijate que ahora el código tiene algunas modificaciones bájate la ultima versión!
