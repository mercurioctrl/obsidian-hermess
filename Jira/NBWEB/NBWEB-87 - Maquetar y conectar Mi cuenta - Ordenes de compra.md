---
jira_key: "NBWEB-87"
aliases: ["NBWEB-87"]
summary: "Maquetar y conectar Mi cuenta - Ordenes de compra"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Marbe Moreno"
reporter: "Catriel Mercurio"
created: "2022-04-05 10:13"
updated: "2022-06-26 20:17"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/NBWEB-87"
---

# NBWEB-87: Maquetar y conectar Mi cuenta - Ordenes de compra

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Marbe Moreno |
| Reportado por | Catriel Mercurio |
| Creado | 2022-04-05 10:13 |
| Actualizado | 2022-06-26 20:17 |
| Etiquetas | ninguna |
| Jira | [NBWEB-87](https://bluinc.atlassian.net/browse/NBWEB-87) |

## Relaciones

- **Padre:** [[NBWEB-59]] APP -Maquetado y Desarrollo - Mi cuenta
- **relates to:** [[NBWEB-18]] Listar Ordenes de compra

## Descripcion

Se trata de la vista dentro de mi cuenta, para visualizar el listado de ordenes de compra

Para esto se utilizara

```
GET {{API_URL}}/v1/miCuenta/OrdenesDeCompra
```

```

{
  status: 2,
  branch: '0002',
  orderNumber: '25632323',
  clientName: 'Marbe Moreno',
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
