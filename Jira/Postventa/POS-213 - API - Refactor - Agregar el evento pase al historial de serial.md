---
jira_key: "POS-213"
aliases: ["POS-213"]
summary: "API - Refactor - Agregar el evento \"pase\" al historial de serial"
status: "Finalizada"
type: "Tarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2022-10-27 17:44"
updated: "2023-03-07 09:08"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/POS-213"
---

# POS-213: API - Refactor - Agregar el evento "pase" al historial de serial

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Tarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2022-10-27 17:44 |
| Actualizado | 2023-03-07 09:08 |
| Etiquetas | ninguna |
| Jira | [POS-213](https://bluinc.atlassian.net/browse/POS-213) |

## Relaciones

- **Padre:** [[POS-12]] Bases del proyecto y formularios
- **relates to:** [[POS-196]] Feat - Obtener informacion completa de un serial
- **blocks:** [[POS-216]] APP - Refactor - Agregar el evento "pase" al historial de serial

## Descripcion

Esta historia habla sobre agregar un apartado extra, asi como existe el de venta y compra para el producto, para los casos donde se realizo un pase del mismo.

Se modifica el recurso

```
GET {API_URL}/V1/aboutSerial
```

[adjunto]
Se debe mostrar informacion del pase, del numero de ingreso de postventa y solucion (En este caso sabemos que fue un cambio).
