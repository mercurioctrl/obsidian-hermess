---
jira_key: "NBWEB-670"
aliases: ["NBWEB-670"]
summary: "MS - Feat - Cotizar con la bonificacion desde ms-envios directamente"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Catriel Mercurio"
created: "2024-03-25 10:48"
updated: "2024-04-09 02:43"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/NBWEB-670"
---

# NBWEB-670: MS - Feat - Cotizar con la bonificacion desde ms-envios directamente

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Catriel Mercurio |
| Creado | 2024-03-25 10:48 |
| Actualizado | 2024-04-09 02:43 |
| Etiquetas | ninguna |
| Jira | [NBWEB-670](https://bluinc.atlassian.net/browse/NBWEB-670) |

## Relaciones

- **Padre:** [[NBWEB-668 - Envíos bonificados|NBWEB-668]] Envíos bonificados
- **is blocked by:** [[NBWEB-669 - API - Feat - Dataset para limites de exclusion|NBWEB-669]] API - Feat - Dataset para limites de exclusion
- **blocks:** [[NBWEB-671 - APP - Feat- Mostrar los que tienen precios en cero, como GRATIS y mensaje con|NBWEB-671]] APP - Feat- Mostrar los que tienen precios en cero, como GRATIS y mensaje con condiciones

## Descripcion

Se debe devolver el precio del envío en cero (No así el costo) cuando la compra sea para 

- cualquier código postal que no este en la lista de exclusión de los bonificados ([link](https://lioteam.atlassian.net/browse/NBWEB-669) )


- No posea gabinetes 


- Sea una venta mayor a 600 + IVA (parametros varios)



Siempre debe guardarse el costo cotizado en ncosteextra
