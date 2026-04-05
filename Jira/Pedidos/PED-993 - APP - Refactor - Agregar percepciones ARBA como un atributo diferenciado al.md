---
jira_key: "PED-993"
aliases: ["PED-993"]
summary: "APP - Refactor - Agregar percepciones ARBA como un atributo diferenciado al momento de ver el detalle de la orden"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Marbe Moreno"
reporter: "Catriel Mercurio"
created: "2025-04-25 07:59"
updated: "2025-05-27 10:34"
labels: ["esperandoDependencia"]
jira_url: "https://bluinc.atlassian.net/browse/PED-993"
---

# PED-993: APP - Refactor - Agregar percepciones ARBA como un atributo diferenciado al momento de ver el detalle de la orden

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Marbe Moreno |
| Reportado por | Catriel Mercurio |
| Creado | 2025-04-25 07:59 |
| Actualizado | 2025-05-27 10:34 |
| Etiquetas | esperandoDependencia |
| Jira | [PED-993](https://bluinc.atlassian.net/browse/PED-993) |

## Relaciones

- **Padre:** [[PED-497 - Ver orden de compra|PED-497]] Ver orden de compra
- **action item from:** [[PED-992 - API - Refactor - Agregar percepciones ARBA como un atributo diferenciado al|PED-992]] API - Refactor - Agregar percepciones ARBA como un atributo diferenciado al momento de ver el detalle de una orden
- **relates to:** [[PED-1002 - API - Refactor - Agregarquitar item a una orden - Recalcular percepciones|PED-1002]] API - Refactor - Agregar/quitar item a una orden - Recalcular percepciones

## Descripcion

Utilizaremos el refactor realizado en [link](https://bluinc.atlassian.net/browse/PED-992)  para mostrar la nueva percepcion ARBA en el caso de que esta exista.

La misma la mostraremos como una linea extra si existe (Si no existe, la linea extra no se muestra) `A` .

Ademas, aclararemos en la percepción de siempre la leyenda “percepción AGIP” `B`

[adjunto]
El parámetro `percepcion_arba` proviene del recurso

```
GET {API_URL}/v1/orders/{branch-order}
```

Asi como pasa con `percepcion` el parametro `percepcion_arba` afecta los totales `C` y `D`
