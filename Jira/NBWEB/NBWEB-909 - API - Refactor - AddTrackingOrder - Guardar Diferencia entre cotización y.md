---
jira_key: "NBWEB-909"
aliases: ["NBWEB-909"]
summary: "API - Refactor - AddTrackingOrder  - Guardar Diferencia entre cotización y creación de Bultos con validación % definida"
status: "Finalizada"
type: "Tarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Emanuel Jesus Ferreyra"
created: "2024-11-01 14:55"
updated: "2024-11-20 22:36"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/NBWEB-909"
---

# NBWEB-909: API - Refactor - AddTrackingOrder  - Guardar Diferencia entre cotización y creación de Bultos con validación % definida

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Tarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Emanuel Jesus Ferreyra |
| Creado | 2024-11-01 14:55 |
| Actualizado | 2024-11-20 22:36 |
| Etiquetas | ninguna |
| Jira | [NBWEB-909](https://bluinc.atlassian.net/browse/NBWEB-909) |

## Relaciones

- **Padre:** [[NBWEB-423]] Logistica Envios
- **has action item:** [[SNB-2463]] MS -Envios - Refactor - Implementar cambiar el parametro 'items' por 'package_dimensions' par Entregar

## Descripcion

Tabla que guardara la nueva cotizacion con sus alteraciones en caso de existir.

EL recurso POST /v1/shipments/addTrackingOrder

al pasarle debe ser capaz re gistrar todo lo que esta en `finalDispatchDetails` en la tabla `quotedPackagesDispatch`

el campo `finalDispatchDetails` puede ser enviado en **null**, el recurso es capas de entender que no existen modicaciones.

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
         "differenceAmount": -14530.39,
         "percentageDifference": -39.3,
         "allowedPercentageDifference": 30,
         "isAllowed": true
      },
      "dispatchTimestamp": "2024-11-06 10:09:27"
   }
}
```



```
CREATE TABLE NewBytes_DBF.dbo.quotedPackagesDispatch (
    id INT IDENTITY(1,1) PRIMARY KEY,
    branch NVARCHAR(10) NOT NULL,
    order_number NVARCHAR(20) NOT NULL,
    final_cost DECIMAL(18, 2) NOT NULL,
    package_amount INT NOT NULL,
    package_weight DECIMAL(10, 2) NOT NULL,
    package_dimensions NVARCHAR(50) NOT NULL,
    difference_amount DECIMAL(18, 2) NOT NULL,
    percentage_difference DECIMAL(5, 2) NOT NULL,
    allowed_percentage_difference DECIMAL(5, 2) NOT NULL,
    dispatch_timestamp DATETIME NOT NULL DEFAULT GETDATE() -- Se establece el valor por defecto
);

```
