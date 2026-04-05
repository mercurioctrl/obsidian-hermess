---
jira_key: "NBWEB-305"
aliases: ["NBWEB-305"]
summary: "APP - Feat - Que se vea que usuario hizo la orden de compra"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Marbe Moreno"
reporter: "Catriel Mercurio"
created: "2022-06-28 10:09"
updated: "2022-07-01 18:00"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/NBWEB-305"
---

# NBWEB-305: APP - Feat - Que se vea que usuario hizo la orden de compra

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Marbe Moreno |
| Reportado por | Catriel Mercurio |
| Creado | 2022-06-28 10:09 |
| Actualizado | 2022-07-01 18:00 |
| Etiquetas | ninguna |
| Jira | [NBWEB-305](https://bluinc.atlassian.net/browse/NBWEB-305) |

## Relaciones

- **Padre:** [[NBWEB-301 - API - APP - Feat - Mostrar nombre de usuario creador para los pedidos|NBWEB-301]] API - APP - Feat - Mostrar nombre de usuario creador para los pedidos

## Descripcion

Se debe agregar el nombre de usuario a la tabla de ordenes de compra.

La imagen a continuación es solo ilustrativa, puede hacerse de otras formas.

[adjunto]
```
GET {{API_URL}}/v1/miCuenta/ordenesDeCompra
```

```
{
  status: 2,
  branch: '0002',
  orderNumber: '25632323',
  clientName: 'Marbe Moreno',
  userName: 'Pepito',
  clientId: 43243,
  subtotal:
    {
    cotizacion:104.5,
    subtotalDollar:4324.56,
    subtotalDollarFinal:5232.72,
    subtotalPesosAr:454078.8,
    subtotalPesosArFinal:549434.38
    }
}
```
