---
jira_key: "PED-920"
aliases: ["PED-920"]
summary: "APP - Feat - Debe figurar en rojo  en el detalle de una orden si esta en rentabilidad negativa"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Marbe Moreno"
reporter: "Catriel Mercurio"
created: "2024-12-30 07:26"
updated: "2025-01-03 11:22"
labels: ["MVPLaset"]
jira_url: "https://bluinc.atlassian.net/browse/PED-920"
---

# PED-920: APP - Feat - Debe figurar en rojo  en el detalle de una orden si esta en rentabilidad negativa

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Marbe Moreno |
| Reportado por | Catriel Mercurio |
| Creado | 2024-12-30 07:26 |
| Actualizado | 2025-01-03 11:22 |
| Etiquetas | MVPLaset |
| Jira | [PED-920](https://bluinc.atlassian.net/browse/PED-920) |

## Relaciones

- **Padre:** [[PED-497]] Ver orden de compra

## Descripcion

Cuando el parámetro `effectiveness`  del recurso 

```
GET {API_URL}/v1/orders/{order}-{branch}
```

Es menor a cero, entonces destacaremos la fila del producto, o el producto en algun tipo de rojo para dar a entender que el producto sea intencionalmente o no, se vendió con margen negativo.



[adjunto]
Adicionalmente, agregaremos el simbolo de porcentaje para que quede claro que es nominal y que es un porcentaje.
