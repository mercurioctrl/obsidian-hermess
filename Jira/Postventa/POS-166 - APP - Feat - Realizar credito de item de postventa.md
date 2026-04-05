---
jira_key: "POS-166"
aliases: ["POS-166"]
summary: "APP - Feat - Realizar credito de item de postventa"
status: "Finalizada"
type: "Historia"
priority: "Medium"
assignee: "Marbe Moreno"
reporter: "Catriel Mercurio"
created: "2022-09-30 09:16"
updated: "2022-10-18 14:21"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/POS-166"
---

# POS-166: APP - Feat - Realizar credito de item de postventa

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Historia |
| Prioridad | Medium |
| Asignado | Marbe Moreno |
| Reportado por | Catriel Mercurio |
| Creado | 2022-09-30 09:16 |
| Actualizado | 2022-10-18 14:21 |
| Etiquetas | ninguna |
| Jira | [POS-166](https://bluinc.atlassian.net/browse/POS-166) |

## Relaciones

- **Padre:** [[POS-24]] Creditos
- **is blocked by:** [[POS-132]] MS - Feat - Emitir comprobante
- **is blocked by:** [[POS-164]] API - Refactor - Agregar precios posibles del producto

## Descripcion

Agregaremos un enlace o boton en el modal 

[adjunto]
Mostraremos un modal con un mensaje “Esta seguro que desea realizar un credito fiscal y en la cuenta del cliente?” o algo similar.

Ademas mostraremos un formularios con los precios precargados que se obtienen de [link](https://lioteam.atlassian.net/browse/POS-164) para que finalmente, luego de elegir que precio voy a usar para hacer el credito (o cargarlo en caso de ser uno solo), al hacer submit (“generar credito”) ejecutaremos el siguiente recurso

[link](https://lioteam.atlassian.net/browse/POS-132)

Una vez que el credito fue realizado, es muy importante que en lugar de mostrar la accion “Acreditar” muestre el estado como ya acreditado. Y mejor aun si tiene adjunto el credito fiscal, propiamente dicho.
