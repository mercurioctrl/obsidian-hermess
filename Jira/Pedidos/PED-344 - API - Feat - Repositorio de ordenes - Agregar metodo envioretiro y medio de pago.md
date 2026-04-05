---
jira_key: "PED-344"
aliases: ["PED-344"]
summary: "API - Feat - Repositorio de ordenes -> Agregar metodo envio/retiro y medio de pago"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2023-12-18 08:32"
updated: "2024-07-17 18:12"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-344"
---

# PED-344: API - Feat - Repositorio de ordenes -> Agregar metodo envio/retiro y medio de pago

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2023-12-18 08:32 |
| Actualizado | 2024-07-17 18:12 |
| Etiquetas | ninguna |
| Jira | [PED-344](https://bluinc.atlassian.net/browse/PED-344) |

## Relaciones

- **Padre:** [[PED-8]] Listar ordenes de compra
- **blocks:** [[PED-345]] APP - Feat - Repositorio de ordenes -> Agregar 2 columnas con metodo envio/retiro y medio de pago

## Descripcion

Agregaremos la descripción del metodo de envío/retiro y pago

```
{API_URL}/v1/orders
```

Basandonos en 

`MS_VENTAS_REMITOS.TRANSPORTE_FP` y `MS_VENTAS_REMITOS.ID_FORMA`

Y teniendo en cuenta las descripciones de 

`NEW_BYTES.dbo.MS_FORMASPAGO_REMITOS_VENDEDORES ON MS_FORMASPAGO_REMITOS_VENDEDORES.ID_FORMA = MS_VENTAS_REMITOS.ID_FORMA`

y `NewBytes_DBF.dbo.transpor ON transpor.ID_TRANSPORTISTA = MS_VENTAS_REMITOS.TRANSPORTE_FP`

Usaremos como nombre de parametro

- shippingMethod


- paymentMethod
