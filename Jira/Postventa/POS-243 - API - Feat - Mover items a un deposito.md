---
jira_key: "POS-243"
aliases: ["POS-243"]
summary: "API - Feat - Mover items a un deposito"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Catriel Mercurio"
created: "2023-03-15 13:04"
updated: "2023-04-11 09:34"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/POS-243"
---

# POS-243: API - Feat - Mover items a un deposito

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Catriel Mercurio |
| Creado | 2023-03-15 13:04 |
| Actualizado | 2023-04-11 09:34 |
| Etiquetas | ninguna |
| Jira | [POS-243](https://bluinc.atlassian.net/browse/POS-243) |

## Relaciones

- **Padre:** [[POS-235 - Postventa Proveedores Recepcion|POS-235]] Postventa Proveedores Recepcion

## Descripcion

Esta historia se trata sobre poder enviar **uno o mas** productos a un deposito especifico.

```
PATCH {API_URL}/v1/sendToWarehouse
```

```
{
arrivalWarehouse: 4 // este es el deposito a donde llega la mercaderia
incomeAfterSaleIds: [
 3433,34234,23467,765,3434,6565
]
}
```

Los id que se reciben corresponden a la columna

`[NEW_BYTES].[dbo].[ST_RMADETALLE].id` la cual es unica.

Lo que hacemos simplemente sera cambiar `ID_DEPOSITO` por el deposito elegido.

Esto solo se puede hacer si el producto en si, esta como “Credito” o “Cambio”  (ver ID_ACCION en la misma tabla)
