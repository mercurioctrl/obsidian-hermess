---
jira_key: "NBWEB-304"
summary: "API - Feat - Agregar usuario al detalle de la cabecera del carrito"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2022-06-28 09:37"
updated: "2022-07-01 18:00"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/NBWEB-304"
---

# NBWEB-304: API - Feat - Agregar usuario al detalle de la cabecera del carrito

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2022-06-28 09:37 |
| Actualizado | 2022-07-01 18:00 |
| Etiquetas | ninguna |
| Jira | [NBWEB-304](https://bluinc.atlassian.net/browse/NBWEB-304) |

## Descripción

En el recurso 

```
GET {{API_URL}}/v1/miCuenta/ordenesDeCompra
```



se debe agregar el parámetro `userName` para designar el usuario que creo el pedido.

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

La informacion puede obtenerse de la cabecera del carrito, en combinación con el pedido. O bien puede guardarse al momento de procesar el mismo. El string que se debe mostrar es el nombre de usuario propiamente dicho.
