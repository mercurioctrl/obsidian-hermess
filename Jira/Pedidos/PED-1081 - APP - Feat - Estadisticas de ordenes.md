---
jira_key: "PED-1081"
aliases: ["PED-1081"]
summary: "APP - Feat - Estadisticas de ordenes"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Marbe Moreno"
reporter: "Catriel Mercurio"
created: "2025-08-11 07:55"
updated: "2025-08-20 10:45"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-1081"
---

# PED-1081: APP - Feat - Estadisticas de ordenes

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Marbe Moreno |
| Reportado por | Catriel Mercurio |
| Creado | 2025-08-11 07:55 |
| Actualizado | 2025-08-20 10:45 |
| Etiquetas | ninguna |
| Jira | [PED-1081](https://bluinc.atlassian.net/browse/PED-1081) |

## Relaciones

- **Padre:** [[PED-1068]] Periodos logisticos
- **action item from:** [[PED-1069]] API - Refactor - Crearemos un repositorio para ver las ordenes en función de sus estadísticas de periodos logísticos

## Descripcion

Agregaremos una **nueva pestaña** del sistema de pedidos un **listado detallado** de los tiempos por etapa (desde la conversión hasta la entrega) con **filtros** por fecha y atributos del pedido, para **identificar cuellos de botella** y **tomar decisiones operativas**.

Para esto usaremos el recurso [link](https://bluinc.atlassian.net/browse/PED-1069) 

## Alcance

- Nueva pestaña en Pedidos: **“Tiempos”**.


- **Filtros**: `between` (obligatorio, DD-MM-YYYY_DD-MM-YYYY) y opcionales `sellerId`, `shippingMethod`, `companyCode`, `paymentMethod`, `orderStatus`, `orderTypeId`, `provinceId`.


- **Tabla** con todas las columnas del endpoint (no recalcular en front, sólo mostrar).


- **Paginación**, **ordenamiento** por columnas, **búsqueda** por `orderNumber` y `clientDescription`.




```
GET {API_URL}/v1/statistics/logisticPerformance?between=DD-MM-YYYY_DD-MM-YYYY&sellerId={id}&shippingMethod={id}&companyCode={code}&paymentMethod={id}&orderStatus={id}&orderTypeId={id}&provinceId={id}
```

- `between` es **obligatorio**; si falta, mostrar error 400 de la API con mensaje claro.


- Los demás filtros son **opcionales**.



### Filtros

- **Rango de fechas** (`between`)


- **Opcionales** (selects con búsqueda):

- Vendedor (`sellerId`)


- Método de envío (`shippingMethod`)


- Empresa (`companyCode`)


- Medio de pago (`paymentMethod`)


- Estado (`orderStatus`)


- Tipo de pedido (`orderTypeId`)


- Provincia (`provinceId`)
