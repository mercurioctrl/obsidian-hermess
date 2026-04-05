---
jira_key: "NBWEB-1004"
aliases: ["NBWEB-1004"]
summary: "API - Refactor - Recurso para leer precios -> Actualizar objeto de respuesta"
status: "Code Review"
type: "Subtarea"
priority: "Medium"
assignee: "Guillermo Avila"
reporter: "Guillermo Avila"
created: "2025-10-08 18:46"
updated: "2025-10-20 10:34"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/NBWEB-1004"
---

# NBWEB-1004: API - Refactor - Recurso para leer precios -> Actualizar objeto de respuesta

| Campo | Valor |
|-------|-------|
| Estado | Code Review (En curso) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Guillermo Avila |
| Reportado por | Guillermo Avila |
| Creado | 2025-10-08 18:46 |
| Actualizado | 2025-10-20 10:34 |
| Etiquetas | ninguna |
| Jira | [NBWEB-1004](https://bluinc.atlassian.net/browse/NBWEB-1004) |

## Relaciones

- **Padre:** [[NBWEB-4]] API - Catalogos de productos
- **relates to:** [[NBWEB-574]] API - Feat - Recurso para leer precios

## Descripcion

Un cliente reportó que el recurso de precios no le está mostrando el valor correcto. Al analizar el caso, detectamos que el recurso que utiliza es una versión antigua, lo que ocasiona discrepancias en la información recibida.

Para resolver esta situación, realizaremos una refactorización al recurso `/v1/prices`, con el objetivo de actualizarlo y mejorar su funcionalidad. Entre los cambios contemplados se encuentran:

- Eliminación de advertencias existentes.


- Inclusión de nuevas claves en el objeto de respuesta, manteniendo la estructura original y asegurando compatibilidad con las implementaciones actuales.





```
{{API_URL}}/v1/prices
```

```
{
    "id": 2062,
    "sku": "SMWVB",
    "currencyQuote": 1310,
    "value": 128.36127,        
    "iva": 21,
    "internalTax": 0, <------------------------------ **SE AGREGA**
    "percepcion": null, <---------------------------- **SE AGREGA**            
    "utility": null, <------------------------------- **SE AGREGA**        
    "finalPrice": 155.3171367,              
    "finalPriceWithUtility": 155.31714, <------------ **SE AGREGA**        
}
```

[adjunto]
