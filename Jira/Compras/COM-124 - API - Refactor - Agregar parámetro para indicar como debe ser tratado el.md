---
jira_key: "COM-124"
aliases: ["COM-124"]
summary: "API - Refactor - Agregar parámetro para indicar como debe ser tratado el impuesto a la hora de calcular el pedido"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Catriel Mercurio"
created: "2024-06-30 17:32"
updated: "2024-07-05 09:33"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/COM-124"
---

# COM-124: API - Refactor - Agregar parámetro para indicar como debe ser tratado el impuesto a la hora de calcular el pedido

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Catriel Mercurio |
| Creado | 2024-06-30 17:32 |
| Actualizado | 2024-07-05 09:33 |
| Etiquetas | ninguna |
| Jira | [COM-124](https://bluinc.atlassian.net/browse/COM-124) |

## Relaciones

- **Padre:** [[COM-98 - Repositorio de impuestos por posicionar arancelaria|COM-98]] Repositorio de impuestos por posicionar arancelaria

## Descripcion

Agregaremos un parámetro para saber si debo incluir en el costo del producto el impuesto tax-inclusive (impuesto absorbido), o si por el contrario es un concepto extra y debo tratarlo como un extra y no como parte del costo del ítem tax-exclusive (impuesto trasladable)

Para esto agregaremos la columna `NewBytes_DBF.[dbo].[FP_IMPUESTOS].tax-exclusive`

```
GET {API_URL}/v1/tariffTax?acronym=true
```

```
[
    {
        "id": "1",
        "acronym": "SI",
        "description": "SIN IMPUESTO",
        "tax-exclusive":true
    },
    {
        "id": "2",
        "acronym": "PP",
        "description": "POR PORCENTAJE"
        "tax-exclusive":false 
    },
...
]
```
