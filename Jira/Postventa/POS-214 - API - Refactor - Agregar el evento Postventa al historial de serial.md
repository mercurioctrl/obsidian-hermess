---
jira_key: "POS-214"
aliases: ["POS-214"]
summary: "API - Refactor - Agregar el evento \"Postventa\" al historial de serial"
status: "Finalizada"
type: "Tarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2022-10-28 09:27"
updated: "2023-03-07 09:08"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/POS-214"
---

# POS-214: API - Refactor - Agregar el evento "Postventa" al historial de serial

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Tarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2022-10-28 09:27 |
| Actualizado | 2023-03-07 09:08 |
| Etiquetas | ninguna |
| Jira | [POS-214](https://bluinc.atlassian.net/browse/POS-214) |

## Relaciones

- **Padre:** [[POS-12 - Bases del proyecto y formularios|POS-12]] Bases del proyecto y formularios
- **blocks:** [[POS-217 - APP - Refactor - Agregar el evento Postventa al historial de serial|POS-217]] APP - Refactor - Agregar el evento "Postventa" al historial de serial

## Descripcion

Se modifica el recurso

```
GET {API_URL}/V1/aboutSerial
```

Esta historia habla sobre agregar un apartado extra, asi como existe el de venta y compra para el producto, para los cosos donde el serial se ingreso a una o mas postventa con anterioridad.

En ese caso se confeccionara un array de objetos, con cada ingreso que cuente con la siguiente informacion.

- clientId


- ClientName


- afterSaleId


- Solucion 


- Reporte



[adjunto]
Se debe mostrar informacion del pase, del numero de ingreso de postventa y solucion (En este caso sabemos que fue un cambio).
