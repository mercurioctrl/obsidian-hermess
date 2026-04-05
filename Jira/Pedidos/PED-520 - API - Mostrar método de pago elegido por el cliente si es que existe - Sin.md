---
jira_key: "PED-520"
aliases: ["PED-520"]
summary: "API - Mostrar método de pago elegido por el cliente si es que existe - Sin descripción del método de pago"
status: "Finalizada"
type: "Error"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Guillermo Avila"
created: "2024-01-31 00:28"
updated: "2024-02-06 19:38"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-520"
---

# PED-520: API - Mostrar método de pago elegido por el cliente si es que existe - Sin descripción del método de pago

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Error |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Guillermo Avila |
| Creado | 2024-01-31 00:28 |
| Actualizado | 2024-02-06 19:38 |
| Etiquetas | ninguna |
| Jira | [PED-520](https://bluinc.atlassian.net/browse/PED-520) |

## Relaciones

- **Padre:** [[PED-3]] Ordenes de compra
- **blocks:** [[PED-513]] API - Refactor - Mostrar metodo de pago elegido por el cliente si es que existe

## Descripcion

No aparece la descripción del método de pago seleccionado al realizar la compra en NB.

[adjunto]
Dato extra:
El remito no aparece en la tabla `NEW_BYTES.dbo.MS_VENTAS_REMITOS` que es la que utiliza como unión para mostrar `MS_FORMASPAGO_REMITOS_VENDEDORES.DESCRIPCION as paymentMethodDescription`

```
LEFT JOIN NEW_BYTES.dbo.MS_FORMASPAGO_REMITOS_VENDEDORES ON MS_FORMASPAGO_REMITOS_VENDEDORES.ID_FORMA = MS_VENTAS_REMITOS.ID_FORMA
```
