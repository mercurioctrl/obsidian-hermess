---
jira_key: "POS-261"
aliases: ["POS-261"]
summary: "APP - Feat - Mostrar listado de \"envios a proveedores\""
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Marbe Moreno"
reporter: "Catriel Mercurio"
created: "2023-06-16 13:47"
updated: "2023-07-06 07:03"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/POS-261"
---

# POS-261: APP - Feat - Mostrar listado de "envios a proveedores"

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Marbe Moreno |
| Reportado por | Catriel Mercurio |
| Creado | 2023-06-16 13:47 |
| Actualizado | 2023-07-06 07:03 |
| Etiquetas | ninguna |
| Jira | [POS-261](https://bluinc.atlassian.net/browse/POS-261) |

## Relaciones

- **Padre:** [[POS-235 - Postventa Proveedores Recepcion|POS-235]] Postventa Proveedores Recepcion

## Descripcion

Utilizaremos el siguiente recurso [link](https://lioteam.atlassian.net/browse/POS-260) para crear una pestaña nueva llamada “Envíos a Proveedores”.

Donde mostremos todo los envíos  que fueron realizados en el paso anterior. En principio mostraremos solo los datos que entrega el objeto, pero seguro luego nos pidan alguna cosa mas.

Pare ver el contenido del mismo, podemos usar el recurso que esta en postman

```
GET {{API_URL}}/v1/sendToProvider/13792
```
