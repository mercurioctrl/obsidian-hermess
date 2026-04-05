---
jira_key: "EXP-458"
aliases: ["EXP-458"]
summary: "API - Refactor - Ajustar Recurso de Creación de Bultos para Incluir y Guardar Información de Cotización y Diferencia"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Emanuel Jesus Ferreyra"
created: "2024-11-01 15:15"
updated: "2025-03-14 14:57"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/EXP-458"
---

# EXP-458: API - Refactor - Ajustar Recurso de Creación de Bultos para Incluir y Guardar Información de Cotización y Diferencia

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Emanuel Jesus Ferreyra |
| Creado | 2024-11-01 15:15 |
| Actualizado | 2025-03-14 14:57 |
| Etiquetas | ninguna |
| Jira | [EXP-458](https://bluinc.atlassian.net/browse/EXP-458) |

## Relaciones

- **Padre:** [[EXP-13 - Feat - Etiquetas y seguimiento|EXP-13]] Feat - Etiquetas y seguimiento
- **has action item:** [[SNB-2463 - MS -Envios - Refactor - Implementar cambiar el parametro 'items' por|SNB-2463]] MS -Envios - Refactor - Implementar cambiar el parametro 'items' por 'package_dimensions' par Entregar
- **relates to:** [[EXP-481 - API - Añadir etiqueta de seguimiento - Respuesta nula al intentar generar|EXP-481]] API - Añadir etiqueta de seguimiento - Respuesta nula al intentar generar

## Descripcion

Se deberá agregar al recurso de EXP. 

El cual se utiliza para conectarse a ms-envios y generar las etiquetas según  la cantidad de bultos asignadas por el area de Depósito.

**POST /v1/shipments/addTrackingOrder  **

En caso de ser modificada la cantidad de bultos. Se le agregará el atributo: finalDispatchDetails

El cual puede ser enviado en como **finalDispatchDetails = null** ,dando a entender que no existen alteraciones con la cantidad de bultos actual.

esta información se debe guardar en la tabla ** NewBytes_DBF.dbo.quotedPackagesDispatch**



Ejemplo:

```
{
   "branch": "0002",
   "order": "10356120",
   "packageGroup": 1,
   "assignValue": false,
   "finalDispatchDetails": {
      "finalCost": 22446,
      "adjustedPackage": {
         "amount": 1,
         "weight": 11.35,
         "dimensions": "37.31x37.31x37.31"
      },
      "costVariance": {
         "differenceAmount": 14530.39,
         "percentageDifference": 39.3,
         "allowedPercentageDifference": 30,
         "isAllowed": true
      },
      "dispatchTimestamp": "2024-11-06 10:09:27"
   }
}
```
