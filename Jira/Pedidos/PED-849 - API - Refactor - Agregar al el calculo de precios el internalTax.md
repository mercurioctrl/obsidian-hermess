---
jira_key: "PED-849"
aliases: ["PED-849"]
summary: "API - Refactor - Agregar al el calculo de precios el internalTax"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2024-10-28 11:10"
updated: "2024-10-30 03:06"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-849"
---

# PED-849: API - Refactor - Agregar al el calculo de precios el internalTax

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2024-10-28 11:10 |
| Actualizado | 2024-10-30 03:06 |
| Etiquetas | ninguna |
| Jira | [PED-849](https://bluinc.atlassian.net/browse/PED-849) |

## Relaciones

- **Padre:** [[PED-237 - Precios|PED-237]] Precios
- **action item from:** [[PED-848 - DATA - Agregar parametros para impuestos internos|PED-848]] DATA - Agregar parametros para impuestos internos

## Descripcion

Según la historia [link](https://lioteam.atlassian.net/browse/PED-848)  consideraremos el nuevo parámetro para calcular los precios.

Esto nos permitirá agregar al objeto

```
"price": {
    "value": 66.27261,
    "iva": 10.5,
    "finalPrice": 93.111, <- ver que ahora el precio final tiene tambien el impuesto interno
    "percepcion": null,
    "letra": "D",
    "internalTax": 30 <--- SE AGREGA
    "priceList": {
        "A": 79.62221,
        "B": 78.10938800999999,
        "C": 77.07429927999999,
        "D": 66.27261
    },
```

EN ESTA OBJETO ES UN PORCENTAJE
