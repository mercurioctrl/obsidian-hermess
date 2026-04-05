---
jira_key: "NBWEB-663"
aliases: ["NBWEB-663"]
summary: "API - Refactor - Agregar parametros para comprobantes de pago al repositorio de ordenes"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2024-03-20 14:07"
updated: "2024-03-25 13:22"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/NBWEB-663"
---

# NBWEB-663: API - Refactor - Agregar parametros para comprobantes de pago al repositorio de ordenes

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2024-03-20 14:07 |
| Actualizado | 2024-03-25 13:22 |
| Etiquetas | ninguna |
| Jira | [NBWEB-663](https://bluinc.atlassian.net/browse/NBWEB-663) |

## Relaciones

- **Padre:** [[NBWEB-610]] API - Refactor - Agregar internalTax a los montos finales de las ordenes dentro de Mi Cuenta
- **relates to:** [[NBWEB-672]] API - Agregar parámetros de pago al repositorio de ordenes - Discrepancia en el tipo de pago

## Descripcion

Agregar los parámetros

`paymentMethodId`: 3 (id medio de pago seleccionado)

`paymentVoucher`: true/false 

En el repositorio

```
GET {API_URL}/v1/miCuenta/ordenesDeCompra
```
