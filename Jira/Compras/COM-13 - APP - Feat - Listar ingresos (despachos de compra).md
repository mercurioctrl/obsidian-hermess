---
jira_key: "COM-13"
aliases: ["COM-13"]
summary: "APP - Feat - Listar ingresos (despachos de compra)"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Marbe Moreno"
reporter: "Catriel Mercurio"
created: "2024-01-12 08:52"
updated: "2024-02-22 15:47"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/COM-13"
---

# COM-13: APP - Feat - Listar ingresos (despachos de compra)

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Marbe Moreno |
| Reportado por | Catriel Mercurio |
| Creado | 2024-01-12 08:52 |
| Actualizado | 2024-02-22 15:47 |
| Etiquetas | ninguna |
| Jira | [COM-13](https://bluinc.atlassian.net/browse/COM-13) |

## Relaciones

- **Padre:** [[COM-12 - Listar ingresos (despachos de compra)|COM-12]] Listar ingresos (despachos de compra)
- **is blocked by:** [[COM-29 - API - Feat - Listar ingresos (despacho de compra)|COM-29]] API - Feat - Listar ingresos (despacho de compra)
- **is blocked by:** [[COM-42 - APP - Listar ingresos (despachos de compra) - Selector de marcas vacío|COM-42]] APP - Listar ingresos (despachos de compra) - Selector de marcas vacío
- **is blocked by:** [[COM-57 - API - Listar ingresos - Referencia a tabla distinta|COM-57]] API - Listar ingresos -> Referencia a tabla distinta
- **is blocked by:** [[COM-41 - API - Feat - Listar ingresos (despacho de compra) - Filtro por serializado no|COM-41]] API - Feat - Listar ingresos (despacho de compra) - Filtro por serializado no coincidente 

## Descripcion

Podremos filtrar desde el buscador general por 

- providerOrder


- fullSerialized


- providerId


- brandId


- sku


- itemId



Crearemos una pestaña llamada “Ingresos” para mostar los siguientes datos de compras

- providerOrder (Código de comprobante)


- voucherNumber (Número de comprobante)


- providerId (ID del proveedor)


- providerName (Nombre del proveedor)


- fullSerialized  


- dispatchDate (Fecha del comprobante)


- iva (Moneda)


- totalFinal (Cotizacion)


- fob (FOB)


- statusId (ID de estado)


- id (ID)
