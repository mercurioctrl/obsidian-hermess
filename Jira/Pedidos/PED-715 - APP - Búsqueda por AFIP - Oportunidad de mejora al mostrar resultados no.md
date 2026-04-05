---
jira_key: "PED-715"
aliases: ["PED-715"]
summary: "APP - Búsqueda por AFIP - Oportunidad de mejora al mostrar resultados no encontrados"
status: "Finalizada"
type: "Tarea"
priority: "Lowest"
assignee: "Marbe Moreno"
reporter: "Guillermo Avila"
created: "2024-05-13 14:14"
updated: "2024-05-15 14:19"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-715"
---

# PED-715: APP - Búsqueda por AFIP - Oportunidad de mejora al mostrar resultados no encontrados

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Tarea |
| Prioridad | Lowest |
| Asignado | Marbe Moreno |
| Reportado por | Guillermo Avila |
| Creado | 2024-05-13 14:14 |
| Actualizado | 2024-05-15 14:19 |
| Etiquetas | ninguna |
| Jira | [PED-715](https://bluinc.atlassian.net/browse/PED-715) |

## Relaciones

- **Padre:** [[PED-3]] Ordenes de compra
- **relates to:** [[PED-709]] APP - Refactor: ajuste para facturar a terceros que marque la ciudad y el tipo de documento correcto al hacer busqueda por AFIP
- **relates to:** [[PED-716]] API - Búsqueda por AFIP - Oportunidad de mejora en el código de estado al mandar formato incorrecto

## Descripcion

Se sugiere una mejora para que cuando no se encuentre la clave de identificación se muestre el mensaje de respuesta. Esto sucede en el modal de Facturación a terceros así como en el de Agregar nuevo cliente.

[adjunto]
[adjunto]
---

Al buscar accidentalmente por DNI ocurre un error en el back debido a que se está enviando la clave de identificación con puntos.

[adjunto]
