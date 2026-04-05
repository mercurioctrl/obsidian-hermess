---
jira_key: "EXP-54"
aliases: ["EXP-54"]
summary: "APP - Feat - Armar paqueteria"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Marbe Moreno"
reporter: "Catriel Mercurio"
created: "2022-11-09 09:02"
updated: "2023-05-29 06:34"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/EXP-54"
---

# EXP-54: APP - Feat - Armar paqueteria

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Marbe Moreno |
| Reportado por | Catriel Mercurio |
| Creado | 2022-11-09 09:02 |
| Actualizado | 2023-05-29 06:34 |
| Etiquetas | ninguna |
| Jira | [EXP-54](https://bluinc.atlassian.net/browse/EXP-54) |

## Relaciones

- **Padre:** [[EXP-12 - Feat - Listar pedidos para envio|EXP-12]] Feat - Listar pedidos para envio

## Descripcion

Este es un modal que se abre para poder crear el paquete (y generar la etiqueta) para un pedido determinado.

Ejecuta el recurso [link](https://lioteam.atlassian.net/browse/EXP-53)

Que envia la siguiente carga util.

```
{
    "branch": "0002",
    "order": "10286794",
    "packageGroup": 2
}
```

Siendo `packageGroup` la cantidad de bultos para el paquete.

En principio mostraremos solo un modal con la leyenda:

Indique cuantos bultos desea armar para este envío, seguido de un input numérico (Mas adelante refactorizaremos para agregar informacion adicional para el “armador”).

Luego de eso tenemos el botón “Generar paquete y etiqueta” que ejecuta [link](https://lioteam.atlassian.net/browse/EXP-53)
